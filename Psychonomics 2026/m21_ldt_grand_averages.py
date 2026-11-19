"""
m21_ldt -- grand-average ERPs from the single-trial .erp files

Uses exactly the trials in the statistical analyses: the trial files written by
m21_ldt_single_trial.R (correct, artefact-free trials; faulty items, DESIGN and
the adopt item removed; 56 participants). Within each participant, trials are
averaged per condition; participants are then averaged with equal weight.

Usage: python3 m21_ldt_grand_averages.py <folder with .erp files> <trial-file folder> <output folder>
"""
import sys, glob, os
import numpy as np, pandas as pd, scipy.io as sio

erp_dir, trial_dir, out_dir = sys.argv[1:4]
os.makedirs(out_dir, exist_ok=True)

ROI = ["C3", "CZ", "C4", "CP1", "CP2", "CP5", "CP6", "P3", "Pz", "P4"]

# Trials in the analysis (same trials in both windows; use the N400 rows)
nw = pd.read_csv(os.path.join(trial_dir, "nonword_trials.csv"))
nw = nw[nw.window == "N400"][["SubjID", "binlabel", "complexity"]]
w = pd.read_csv(os.path.join(trial_dir, "word_trials.csv"))
w = w[w.window == "N400"][["SubjID", "binlabel", "cond_trig", "WordID", "logWF"]]
# Word frequency: median split over the 99 words (illustration only; the
# statistics treat word frequency as continuous)
items = w.drop_duplicates("WordID")
wf_median = items.logWF.median()
w["WF"] = np.where(w.logWF > wf_median, "high", "low")
w["FS"] = np.where(w.cond_trig == 202, "large", "small")
print(f"Words: {len(items)} items; WF median split at log10 WF = {wf_median:.3f} "
      f"({(items.logWF > wf_median).sum()} high, {(items.logWF <= wf_median).sum()} low)")

conds = {
    "complexity": (nw, "complexity", ["complex", "simple"]),
    "word_frequency": (w, "WF", ["high", "low"]),
    "family_size": (w, "FS", ["large", "small"]),
}

subjects = sorted(nw.SubjID.unique())
subj_avgs = {k: {lvl: [] for lvl in v[2]} for k, v in conds.items()}
n_trials = []
dropped = []
times = labels = chanlocs = None
for s in subjects:
    f = glob.glob(os.path.join(erp_dir, "**", f"{s}_LDT.erp"), recursive=True)
    assert len(f) == 1, f"{s}: {f}"
    E = sio.loadmat(f[0], squeeze_me=True, struct_as_record=False)["ERP"]
    bins = [b.strip() for b in E.bindescr]
    acc = np.asarray(E.ntrials.accepted)
    if times is None:
        times = np.asarray(E.times); labels = [c.labels for c in E.chanlocs]; chanlocs = E.chanlocs
    for key, (df, col, levels) in conds.items():
        d = df[df.SubjID == s]
        for lvl in levels:
            idx = [bins.index(b.strip()) for b in d.binlabel[d[col] == lvl]]
            assert all(acc[i] >= 1 for i in idx), f"{s}: included bin with no accepted trial"
            # A few bins (S135: 2, S144: 5) hold two epochs although the log
            # shows the item once; they are not single trials, so leave them out.
            dropped += [(s, bins[i]) for i in idx if acc[i] != 1]
            idx = [i for i in idx if acc[i] == 1]
            subj_avgs[key][lvl].append(E.bindata[:, :, idx].mean(axis=2))
            n_trials.append((s, key, lvl, len(idx)))

print("Bins left out (more than one epoch):", sorted(set(dropped)))
counts = pd.DataFrame(n_trials, columns=["SubjID", "contrast", "level", "n"])
print(counts.groupby(["contrast", "level"]).n.agg(["mean", "min", "max"]).round(1))

roi_idx = [labels.index(c) for c in ROI]
scalp = [i for i, c in enumerate(labels) if c not in
         ("Mastoid R", "Mastoid L", "HEOG R", "HEOG L", "VEOG L", "HEOG")]
rows = []
np.savez(os.path.join(out_dir, "grand_averages.npz"), times=times,
         labels=np.array(labels), **{f"{k}_{lvl}": np.stack(v[lvl])
                                     for k, v in subj_avgs.items() for lvl in v})
for key, (_, _, levels) in conds.items():
    for lvl in levels:
        ga = np.stack(subj_avgs[key][lvl]).mean(axis=0)          # chan x time
        for ti, t in enumerate(times):
            rows.append((key, lvl, t, ga[roi_idx, ti].mean()))
pd.DataFrame(rows, columns=["contrast", "level", "time_ms", "roi_uV"]).to_csv(
    os.path.join(out_dir, "grand_average_roi.csv"), index=False)

# Check: ROI mean amplitude in each window, mean over participants of the
# within-participant difference (raw, not model-based)
for key, (_, _, (a, b)) in conds.items():
    for win, (lo, hi) in {"N400": (300, 500), "N250": (200, 300)}.items():
        tw = (times >= lo) & (times <= hi)
        diff = [(x[roi_idx][:, tw].mean() - y[roi_idx][:, tw].mean())
                for x, y in zip(subj_avgs[key][a], subj_avgs[key][b])]
        print(f"{key:15s} {win}: {a} - {b} = {np.mean(diff):6.3f} uV (SE {np.std(diff, ddof=1)/np.sqrt(len(diff)):.3f})")
print("Saved to", out_dir)
