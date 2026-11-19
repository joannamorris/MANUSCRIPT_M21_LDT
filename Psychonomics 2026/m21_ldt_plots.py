"""
m21_ldt -- talk figures

Usage: python3 m21_ldt_plots.py <st folder> <erp folder>
  Reads figures/output/grand_averages.npz (from m21_ldt_grand_averages.py),
  the trial files, the ROI reliability table and the behavioural reliability
  table, and writes PNG figures to figures/output/.
"""
import sys, os, glob
import numpy as np, pandas as pd, scipy.io as sio
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import mne

st, erp_dir = sys.argv[1:3]
out = os.path.join(st, "figures", "output")

# Palette (reference dataviz palette: categorical slots 1-2, diverging pair, text inks)
BLUE, ORANGE = "#2a78d6", "#eb6834"
INK, INK2, GRID, SURF = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
DIV = LinearSegmentedColormap.from_list("div", ["#1c5aa6", BLUE, "#f0efec", "#e34948", "#a92b2b"])
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 13, "axes.edgecolor": INK2,
                     "axes.labelcolor": INK, "xtick.color": INK2, "ytick.color": INK2,
                     "figure.facecolor": "white", "axes.facecolor": "white"})

ROI = ["C3", "CZ", "C4", "CP1", "CP2", "CP5", "CP6", "P3", "Pz", "P4"]
ga = np.load(os.path.join(out, "grand_averages.npz"))
times, labels = ga["times"], list(ga["labels"])
roi_idx = [labels.index(c) for c in ROI]

contrasts = [  # key, levels (first = colour 1), panel title, legend names
    ("complexity", ("complex", "simple"), "Nonwords", ("Complex (gasful)", "Simple (gasfil)")),
    ("word_frequency", ("high", "low"), "Words: word frequency", ("High frequency", "Low frequency")),
    ("family_size", ("large", "small"), "Words: family size", ("Large family", "Small family")),
]

# ---- Figure 1: ROI waveforms ---------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(16, 5.2), sharey=True)
for ax, (key, (a, b), title, names) in zip(axes, contrasts):
    for lvl, col, ls, nm in [(a, BLUE, "-", names[0]), (b, ORANGE, "--", names[1])]:
        subj = ga[f"{key}_{lvl}"]                       # subj x chan x time
        y = subj[:, roi_idx, :].mean(axis=1).mean(axis=0)
        ax.plot(times, y, color=col, lw=2.2, ls=ls, label=nm)
    for lo, hi, nm in [(200, 300, "N250"), (300, 500, "N400")]:
        ax.axvspan(lo, hi, color="#000000", alpha=0.06 if nm == "N250" else 0.11, lw=0)
        ax.text((lo + hi) / 2, 0.03, nm, transform=ax.get_xaxis_transform(), ha="center",
                va="bottom", color=INK2, fontsize=11)
    ax.axhline(0, color=INK2, lw=0.8); ax.axvline(0, color=INK2, lw=0.8)
    ax.set_xlim(-200, 900); ax.set_title(title, color=INK, fontsize=15, loc="left")
    ax.set_xlabel("Time from target onset (ms)")
    ax.grid(axis="y", color=GRID, lw=0.8); ax.set_axisbelow(True)
    for sp in ("top", "right"): ax.spines[sp].set_visible(False)
    ax.legend(frameon=False, loc="lower left", fontsize=11, borderaxespad=0.3)
axes[0].set_ylabel("Amplitude (µV)")
axes[0].invert_yaxis()                                  # negative up (shared y)
fig.text(0.01, 0.01, "Central-parietal ROI (C3, Cz, C4, CP1, CP2, CP5, CP6, P3, Pz, P4); "
         "negative plotted up; correct trials; N = 56. Word frequency is a median split for display only.",
         fontsize=10, color=INK2)
fig.tight_layout(rect=(0, 0.04, 1, 1))
fig.savefig(os.path.join(out, "fig1_roi_waveforms.png"), dpi=200); plt.close(fig)

# ---- Figure 2: scalp maps of the differences (N400 first, then N250) ----------
E = sio.loadmat(glob.glob(os.path.join(erp_dir, "**", "S101_LDT.erp"), recursive=True)[0],
                squeeze_me=True, struct_as_record=False)["ERP"]
scalp = [i for i, c in enumerate(E.chanlocs) if c.labels in labels[:27]]
pos = {}
for i in scalp:   # EEGLAB: X = nose, Y = left ear  ->  MNE head: x = right, y = nose
    c = E.chanlocs[i]
    v = np.array([-c.Y, c.X, c.Z], float); pos[c.labels] = v / np.linalg.norm(v) * 0.095
info = mne.create_info([labels[i] for i in scalp], 200.0, "eeg")
info.set_montage(mne.channels.make_dig_montage(ch_pos=pos, coord_frame="head"))
wins = [("N400", 300, 500), ("N250", 200, 300)]
maps = {}
for key, (a, b), _, _ in contrasts:
    d = (ga[f"{key}_{a}"] - ga[f"{key}_{b}"]).mean(axis=0)   # chan x time
    for wn, lo, hi in wins:
        tw = (times >= lo) & (times <= hi)
        maps[(key, wn)] = d[scalp][:, tw].mean(axis=1)
vmax = np.ceil(max(abs(v).max() for v in maps.values()) * 10) / 10
fig, axes = plt.subplots(len(contrasts), 2, figsize=(7.2, 10))
for r, (key, (a, b), title, names) in enumerate(contrasts):
    for c, (wn, lo, hi) in enumerate(wins):
        ax = axes[r, c]
        im, _ = mne.viz.plot_topomap(maps[(key, wn)], info, axes=ax, show=False, cmap=DIV,
                                     vlim=(-vmax, vmax), contours=0, sensors=True)
        if r == 0: ax.set_title(f"{wn} ({lo}–{hi} ms)", color=INK, fontsize=14)
    lab = {"complexity": "Complex − simple", "word_frequency": "High − low frequency",
           "family_size": "Large − small family"}[key]
    axes[r, 0].text(-0.15, 0.5, lab, transform=axes[r, 0].transAxes, rotation=90,
                    ha="center", va="center", fontsize=13, color=INK)
cb = fig.colorbar(im, ax=axes, orientation="horizontal", fraction=0.035, pad=0.04, shrink=0.8)
cb.set_ticks([-1, -0.5, 0, 0.5, 1]); cb.set_label("Difference (µV)", color=INK)
fig.savefig(os.path.join(out, "fig2_topographies.png"), dpi=200, bbox_inches="tight"); plt.close(fig)

# ---- Figure 3: split-half reliability -------------------------------------------
roi_rel = pd.read_csv(os.path.join(st, "single_trial_roi_output", "split_half_reliability_ROI.csv"))
beh_rel = pd.read_csv(os.path.join(st, "behaviour_output", "split_half_reliability_behaviour.csv"))
rel = {r.measure: (r.median, r.lower, r.upper) for r in roi_rel.itertuples()}
relb = {r.measure: (r.median, r.lower, r.upper) for r in beh_rel.itertuples()}
rows = [  # label, (median, lo, hi), group
    ("Nonwords, N400", rel["Nonwords N400 mean amplitude"], "Mean amplitude"),
    ("Nonwords, N250", rel["Nonwords N250 mean amplitude"], "Mean amplitude"),
    ("Words, N400", rel["Words N400 mean amplitude"], "Mean amplitude"),
    ("Words, N250", rel["Words N250 mean amplitude"], "Mean amplitude"),
    ("Complexity, RT", relb["Nonwords: complexity effect on RT (correct)"], "Behavioural effects"),
    ("Complexity, accuracy", relb["Nonwords: complexity effect on accuracy"], "Behavioural effects"),
    ("Family size, RT", relb["Words: family size effect on RT (correct)"], "Behavioural effects"),
    ("Family size, accuracy", relb["Words: family size effect on accuracy"], "Behavioural effects"),
    ("Complexity, N400", rel["Nonwords N400 complexity effect"], "ERP effects"),
    ("Complexity, N250", rel["Nonwords N250 complexity effect"], "ERP effects"),
    ("Family size, N400", rel["Words N400 family-size effect"], "ERP effects"),
    ("Family size, N250", rel["Words N250 family-size effect"], "ERP effects"),
    ("Base frequency, N400", rel["Words N400 base-frequency effect"], "ERP effects"),
    ("Base frequency, N250", rel["Words N250 base-frequency effect"], "ERP effects"),
]
fig, ax = plt.subplots(figsize=(10, 7.5))
ypos, y, ticks, tlabels, groups = [], 0, [], [], []
for i, (lab, (m, lo, hi), g) in enumerate(rows):
    if i and g != rows[i - 1][2]: y += 0.9
    col = {"Mean amplitude": BLUE, "Behavioural effects": INK2, "ERP effects": ORANGE}[g]
    ax.plot([lo, hi], [y, y], color=col, lw=2.2, solid_capstyle="round")
    ax.plot(m, y, "o", color=col, ms=9, mec="white", mew=2)
    ax.text(1.04, y, f"{m:.2f}", va="center", fontsize=11, color=INK)
    ticks.append(y); tlabels.append(lab)
    if i == 0 or g != rows[i - 1][2]: groups.append((y, g, col))
    y += 1
ax.axvline(0, color=INK2, lw=1)
ax.set_yticks(ticks); ax.set_yticklabels(tlabels); ax.invert_yaxis()
ax.set_xlim(-1.65, 1.15); ax.set_xlabel("Split-half reliability (Spearman–Brown), median and 95% range across 2,000 splits")
for gy, g, col in groups:
    ax.text(-1.62, gy - 0.65, g, fontsize=13, fontweight="bold", color=col, va="bottom")
ax.grid(axis="x", color=GRID, lw=0.8); ax.set_axisbelow(True)
for sp in ("top", "right", "left"): ax.spines[sp].set_visible(False)
ax.tick_params(axis="y", length=0)
fig.tight_layout()
fig.savefig(os.path.join(out, "fig3_reliability.png"), dpi=200); plt.close(fig)

# ---- Figure 4: one random split, N400 nonwords ---------------------------------
mea = pd.read_csv(os.path.join(st, "data", "M21_LDT_mea_300_500_bl_n200_0.csv"))
mea = mea[mea.chlabel.isin(ROI)]
mea["SubjID"] = mea.ERPset.str.replace("_LDT", "", regex=False)
amp = mea.groupby(["SubjID", "binlabel"]).value.mean().reset_index()
nw = pd.read_csv(os.path.join(st, "single_trial_output", "nonword_trials.csv"))
nw = nw[nw.window == "N400"][["SubjID", "binlabel", "complexity"]].merge(amp, on=["SubjID", "binlabel"])
rng = np.random.default_rng(20261101)
half = {"mean": [], "effect": []}
for s, d in nw.groupby("SubjID"):
    hm = {}
    for c in ("complex", "simple"):
        v = d.value[d.complexity == c].to_numpy(); v = v[rng.permutation(len(v))]; k = len(v) // 2
        hm[c] = (v[:k].mean(), v[k:2 * k].mean())
    half["mean"].append(((hm["complex"][0] + hm["simple"][0]) / 2, (hm["complex"][1] + hm["simple"][1]) / 2))
    half["effect"].append((hm["complex"][0] - hm["simple"][0], hm["complex"][1] - hm["simple"][1]))
fig, axes = plt.subplots(1, 2, figsize=(12, 5.6))
for ax, key, title, col in [(axes[0], "mean", "Mean N400 amplitude", BLUE),
                            (axes[1], "effect", "N400 complexity effect (complex − simple)", ORANGE)]:
    h = np.array(half[key]); r = np.corrcoef(h[:, 0], h[:, 1])[0, 1]; sb = 2 * r / (1 + r)
    lim = np.abs(h).max() * 1.1
    ax.plot([-lim, lim], [-lim, lim], color=GRID, lw=1.2, zorder=0)
    ax.scatter(h[:, 0], h[:, 1], s=60, color=col, edgecolor="white", linewidth=1.5, zorder=2)
    ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim); ax.set_aspect("equal")
    ax.set_title(title, color=INK, fontsize=14, loc="left")
    ax.set_xlabel("First half of trials (µV)"); ax.set_ylabel("Second half of trials (µV)")
    ax.text(0.04, 0.96, f"r = {r:.2f}\nSpearman–Brown = {sb:.2f}", transform=ax.transAxes,
            va="top", fontsize=12, color=INK)
    for sp in ("top", "right"): ax.spines[sp].set_visible(False)
fig.text(0.01, 0.01, "One random split of each participant's nonword trials (within condition); "
         "each dot is one participant; N = 56. Central-parietal ROI, 300–500 ms.",
         fontsize=10, color=INK2)
fig.tight_layout(rect=(0, 0.04, 1, 1))
fig.savefig(os.path.join(out, "fig4_split_half_scatter.png"), dpi=200); plt.close(fig)
print("Figures written to", out)
