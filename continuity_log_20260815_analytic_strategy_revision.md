# Continuity Log Addendum: Analytic Strategy Revision
## Session Date: 2026-08-15

*This document supplements `project_memory_log.md` and the userMemories summary. Paste this as the first message in a new chat, alongside the existing continuity log, to resume work on Table 1 / Results restructuring.*

---

## 1. WHY THIS SESSION HAPPENED

Jesse (Harvard psycholinguist, pre-submission reviewer) gave two kinds of feedback on the near-final manuscript:

1. **Introduction restructuring** — funnel-down opening, offload theory comparison to Discussion, remove predictive hedging from Introduction. **COMPLETED THIS SESSION** — new Introduction is in `m21_ldt_frontiers_v2_4.tex`, replacing the old Section 1 (four subsections: Base Frequency/Family Size, OS/LP as Dissociable Dimensions, N250/N400 as Indices, Affix-Led/Stem-Led Parsing; Aims and Predictions trimmed to remove the Beyersmann hedge).

2. **Analytic strategy** — Jesse wanted a simpler set of models than the existing primary/exploratory split, entered hierarchically. This conflicted with Joanna's original principle (include only theoretically-motivated interaction terms) and triggered a full re-analysis.

## 2. THE METHODOLOGICAL RESOLUTION (IMPORTANT — GOVERNS ALL MODELS GOING FORWARD)

**Agreed principle:** OS, LP, and the lexical variable of interest (base frequency or family size) are **fully crossed with each other** in every confirmatory model, because the Introduction treats OS and LP as parallel, equally-weighted, dissociable dimensions — there is no theoretical basis for demoting one to a covariate while the other interacts freely. This was not just a modeling-convenience fix: the original primary/exploratory split (which treated LP as a covariate in the "OS" models and vice versa) was shown empirically to bias the two-way coefficients that were reported, because it omitted a real three-way interaction.

**Complexity** (the nonword structural manipulation) is crossed with each of OS, LP, and the lexical variable individually — this tests the theoretically motivated affix-led/stem-led prediction — but is **not** required to enter a four-way interaction with all three simultaneously. This was tested explicitly (see below) and found unnecessary.

This principle should be stated plainly in the Methods section, e.g.: *"Individual difference terms (OS, LP) were fully crossed with each other and with the lexical variable of interest in every model, since both dimensions are treated as theoretically parallel; higher-order interactions with the structural manipulation (Complexity) were tested as a follow-up specificity/robustness check rather than included in the confirmatory model, given the added parameters relative to sample size."*

## 3. CONFIRMED FINDINGS — WORDS

### N250, Base Frequency (`m_3way_bf`)
- `base_frequency:OS:LP`: β = −0.537, t(1620) = −4.97, p < .0001
- **Robust**: survives removal of S153 (extreme LP outlier, LP = 3.11, ~2.55 SD above mean) — β = −0.534, t = −4.92, p < .0001 with S153 excluded
- **Shape**: continuous grid (20-point LP sequence × OS = −1/0/1) confirms a genuine, smooth **crossover** — not attenuation. At low OS, the BF effect reverses sign as LP increases (low LP: strongly negative/expected direction; high LP: strongly positive/reversed). At high OS, the reverse pattern holds (near-zero at low LP, strongly negative at high LP).
- Joint-extreme corners (e.g., low-OS/high-LP) are populated by only 2–3 participants — the *shape* of the crossover is well-supported by the bulk of the sample, but the most extreme fitted values at the plot edges should be described cautiously.
- Original two-way `base_frequency:OS` term (from the old covariate-only model) is subsumed by this — it was an average across the crossover, which is why it looked "clean" before.

### N250, Family Size (`m_3way_fs`)
- `family_size:OS:LP`: β = −0.282, t(1620) = −4.47, p < .0001
- **Robust**: survives S153 removal — β = −0.284, t = −4.47, p < .0001
- **Shape**: 3×3 grid (Low/Mid/High OS × Low/Mid/High LP) shows a clean crossover — the OS-driven amplification of the family size effect is strong and positive at low LP (0.03 → 0.88 ns→*** as OS increases), and reverses to negative at high LP (0.39 → −0.01 as OS increases). The old mean-LP row is what the original two-way model captured, obscuring the reversal.

### N400, Base Frequency (`m_3way_bf_n400`)
- Three-way `base_frequency:OS:LP`: **NOT significant** — χ²(1) = 2.16, p = .141; β = −0.170, t = −1.47, p = .142
- **What survives**: `base_frequency:LP` two-way is robust and essentially unchanged from the original exploratory model — β = 0.334, t = 3.84, p = .0001 (original was β = 0.344, p < .001)
- OS main effect remains marginal (p = .043; original was p = .049) — still needs the existing caution sentence
- `base_frequency:OS` is now a trend (p = .083) — visible only because OS was allowed to interact; not significant, not a finding

### N400, Family Size (`m_3way_fs_n400`)
- Three-way `family_size:OS:LP`: **NOT significant** — χ²(1) = 0.29, p = .593; β = −0.037, p = .593
- **No individual-difference modulation of family size at N400 at all**: `family_size:OS` p = .212, `family_size:LP` p = .164 (consistent with original model's p = .172), `OS:LP` p = .9995
- What survives: `family_size` main effect (robust, p < .0001), `OS` main effect (p = .033, consistent with original p = .038)
- This is a genuine null, not a power issue — the least individual-difference-sensitive result in the whole set of word models.

### Summary Table — Words
| | N250 | N400 |
|---|---|---|
| **Base Frequency** | OS×LP crossover (robust) | LP two-way only; three-way absent |
| **Family Size** | OS×LP crossover (robust) | No modulation — main effects only |

## 4. CONFIRMED FINDINGS — NONWORDS

### Four-way check (Complexity × OS × LP × FS), both components
- **NOT significant at either N250 or N400** (N250: β = −0.084, p = .439; N400: β = 0.088, p = .510) — Complexity does not need to enter a four-way; this justifies excluding it from the confirmatory model per the resolution in §2.
- Omnibus LRTs comparing the old confirmed models to the full four-way saturated models WERE significant at both components (N250: p = .016; N400: p = .009) — but this was driven by lower-order terms, not the four-way itself (see below).

### N250 nonwords, confirmatory model (`m_confirm_nw_n250`: Complexity crossed individually with OS/LP/FS; OS×LP×FS fully crossed; no Complexity four-way)
- `OS:LP:family_size`: β = 0.139, t(4852) = 2.54, p = .011
- **Robust**: survives S153 removal — β = 0.137, t = 2.49, p = .013
- `complexity:OS` (β = 0.392, p < .0001) and `complexity:LP` (β = 0.358, p < .0001) — **unchanged from the original confirmed nonword N250 model** (this is the existing "processing cost reversal at high skill" centerpiece finding; untouched by the rebuild)
- **Specificity check against base frequency**: `OS:LP:base_frequency` at N250 is null (β = 0.135, p = .343) — confirms the `OS:LP:family_size` effect is family-size-specific, not a stem-frequency effect in disguise. Mirrors the logic of the existing N400 BF specificity check.

### N400 nonwords, confirmatory model (`m_confirm_nw_n400`)
- `OS:LP:family_size`: β = 0.216, t(4852) = 3.23, p = .0013
- **Robust**: survives S153 removal — β = 0.216, t = 3.21, p = .0013
- `complexity:OS` (β = 0.240, p = .0005) and `complexity:LP` (β = 0.254, p < .0001) — consistent with original models
- `complexity:family_size` (β = −0.451, p = .0002) and `family_size:LP` (β = 0.140, p = .0054) also present — part of the existing centerpiece three-way story, now embedded in the larger confirmatory structure
- Original `Complexity × Base Frequency × LP` specificity check (from before this session) was already null — consistent with today's findings.

### Summary Table — Nonwords
| | N250 | N400 |
|---|---|---|
| **Family Size (OS×LP)** | Significant, robust | Significant, robust |
| **Base Frequency (OS×LP), specificity check** | Null (confirms FS-specificity) | Null (confirms FS-specificity, pre-existing) |

### PARKED — not yet investigated, noted for later
From the nonword four-way check (four-way itself was null, but these lower-order terms were significant and are new, untested in isolation):
- `complexity:OS:family_size` at N250, p = .020 (from the four-way check model, not yet re-tested in the trimmed confirmatory model)
From the N250 base-frequency specificity check model:
- `complexity:base_frequency` at N250, β = 0.683, p = .0087 — new, not part of original design
- `OS:base_frequency` at N250, β = −0.357, p = .014 — new, not part of original design

**Decision:** these three terms are parked. Return to them only if the Results write-up reveals a need — do not chase them proactively.

## 5. THE EMERGING STORY (ONE SENTENCE)

OS and LP jointly reshape the base frequency and family size effects at N250 for words, and jointly reshape the family size effect in both words and nonwords at both N250 and N400 — but base frequency's individual-difference sensitivity narrows to LP alone, and only at N400, and only for words.

This replaces the original "OS is early/N250-specific, LP is late/N400-specific" double-dissociation framing, which does not survive the maximal-model treatment. The new framing is more complex but arguably more theoretically interesting: it is not a clean stage-based dissociation between OS and LP, but a **narrowing** — early processing (N250) involves both dimensions jointly and interactively across both lexical variables and both stimulus types; late processing (N400) narrows to LP alone, and even then only for base frequency, with family size showing no late-stage individual-difference sensitivity at all.

## 6. WHAT THIS MEANS FOR THE MANUSCRIPT (NOT YET DONE)

- **Table 1** needs a full rebuild — the old primary/exploratory row structure with ¶‡§¶ footnotes no longer matches the models actually being reported.
- **Results section** needs a substantial rewrite, not an edit — the words N250/N400 paragraphs and the nonword N250/N400 paragraphs all need to reflect the new confirmatory models, the crossover shapes (with the participant-density caveats for the extreme tails), and the specificity checks.
- **Introduction** (already rewritten this session, see §1) currently still assumes something closer to the old OS-early/LP-late framing in a couple of places, particularly the Affix-Led and Stem-Led Parsing subsection and the closing paragraph of Aims and Predictions — these will need a light revision once the Results section's new framing is finalized, so the Introduction's predictions and the Results' actual findings are consistent.
- **Discussion** — the existing Affix-Led/Stem-Led Parsing section and the planned structure around "OS drives N250 reversal, LP drives N400 three-way" both need rethinking around the new "narrowing" framing.
- **OS/LP spell-out pass** (per Jesse's separate note that abbreviations annoy reviewers in Introduction/Discussion prose) is still pending — was deferred earlier in this session and not yet started.

## 7. NEXT SESSION

**Planned starting point:** Table 1 / Results restructuring, building from the confirmed model set in §3–4 above.

**Open decisions to make during that session:**
- How to present the crossover interactions visually/statistically given the participant-density caveats at the distribution tails (restrict reported range to ~±1.5 SD, as discussed, rather than full min–max)
- Whether/how to fold the "narrowing" framing into a revised Results Summary and whether the three-key-findings opening of the Discussion (per the original planned structure) needs to change
- Whether to revisit the parked terms (§4) once the Results section reveals whether the story needs them
