# Continuity Log: M21 LDT Frontiers Manuscript
*Paste this as the first message in a new chat, along with the two attached .tex files, to resume with no loss of context.*

---

## What just happened (this session)

Two things were discovered and fixed:

1. **A significant secondary finding was missed and then integrated.** Exploratory models (reversing the interaction structure at each ERP component) revealed that **Language Proficiency (LP) significantly modulates the N250 Base Frequency effect for words** (β = 0.180, SE = 0.082, t(1618) = 2.20, p = .028) — running in the *opposite direction* to the primary Orthographic Sensitivity (OS) effect (largest at low LP, attenuating and nearly reversing at high LP). The three parallel exploratory tests (Family Size × LP at N250; Base Frequency × OS and Family Size × OS at N400) were all null, confirming OS has no N400 role at all for words, while LP has a small but real N250 role in addition to its primary N400 role.

2. **This broke the "double dissociation" claim.** A true double dissociation requires mutual exclusivity in both directions. The data show: OS is cleanly N250-specific (excludes N400 entirely, even under exploratory testing) — but LP is *not* cleanly N400-specific, since it also modulates N250 (weaker, opposite-signed). Decision: **retire "double dissociation" language throughout the paper** in favor of "component-specific modulation" / "differentially modulate" / "primarily modulate."

All statistics above were verified against actual R output across three rounds of PDF uploads (two contained copy-paste errors — mismatched `time_window` subsets and duplicated `eta_squared()`/`r2_nakagawa()` calls pointing at the wrong model object — both caught and corrected before use).

---

## Files produced this session (attached)

- **`m21_ldt_frontiers_v2_3.tex`** (main manuscript, edited)
- **`M21_LDT_Supplementary.tex`** (supplementary materials, edited)

Both are brace-balanced and verified. Abstract is exactly 350/350 words (Frontiers limit) — **no room to add anything further without cutting elsewhere.**

### Edits applied to the main manuscript
- **Abstract**: "OS selectively modulated the N250 BF effect" → "OS primarily modulated... with a smaller LP effect too"; dropped "consistent with a form-to-meaning dissociation."
- **Aims and Predictions**: both instances of "double dissociation" → "pattern of component-specific modulation."
- **Statistical Analyses intro** (×2 near-duplicate paragraphs) and **Results intro**: "dissociably/selectively modulate" → "differentially/primarily modulate."
- **Methods, Table 1 explainer paragraph**: "selectively modulated" → "primarily modulated"; **added new paragraph** describing the four exploratory reversed-structure models and their rationale.
- **Results, Words section**: **added two new paragraphs** —
  - After the N250 Base Frequency + Family Size results: reports the significant LP × BF exploratory finding in full (with follow-up contrasts) and the null FS × LP result briefly, pointing to Supplementary Tables S3a–S3b.
  - After the N400 Base Frequency + Family Size results: reports both null OS exploratory findings (BF × OS, FS × OS), pointing to Supplementary Tables S4a–S4b.

### Edits applied to the Supplementary file
- **Overview** paragraph: term-swapped away from "double dissociation," added a sentence introducing the new S3–S4 sections.
- **New Section S3** (Words N250, exploratory LP models): two sub-models (BF×LP significant; FS×LP null), each with full prose + fixed-effects table, matching S1/S2 formatting exactly (η²p reported only for significant terms, per your convention).
- **New Section S4** (Words N400, exploratory OS models): two sub-models (BF×OS null; FS×OS null), same format.
- S1 and S2 themselves were **not** edited (their content didn't need it).

---

## Outstanding / NOT yet done — pick up here

### 1. Finish the terminology sweep (in progress, was going in document order)
We were sweeping every "dissociation"/"selectively modulate" occurrence in the main manuscript, one at a time, deciding case-by-case whether it's (a) an unrelated use to leave alone, (b) a hedged prediction that's fine as-is, or (c) an overclaim needing correction. **Completed through the old line 228** (now shifted ~4 lines later due to insertions). **Still need review** (approximate original line numbers, will have shifted slightly — search for these phrases instead of trusting line numbers):

- **Old line 237** (RT paragraph): "...does not selectively modulate morphological effects on response times" — likely fine (null result), low priority, wasn't flagged before but should get a quick look.
- **Old line 330** (Figure 2 caption): "OS does not selectively modulate..." / "predicted dissociation" — likely fine, describes a correctly-scoped null result, but not yet formally reviewed.
- **Old line 336** (Discussion opening, "Three findings structure the discussion..."): contains **"OS selectively modulated the base frequency effect for word stimuli"** — this is now a confirmed overclaim (LP also modulates it, exploratory) and needs the same fix as the Abstract. Also still contains **"qualitatively distinct mechanisms"** for the nonword N250 finding — this exact phrase was revised away from in an earlier part of this same conversation (changed to "independent routes rather than a single shared mechanism operating at different strengths") but that fix was never propagated to this summary paragraph. **Two fixes needed here.**
- **Old line 363** (N400 Discussion section): "LP selectively modulated N400 amplitude..." — appears correctly scoped (LP does modulate N400 broadly); "OS... did not modulate the joint influence..." — correctly scoped to the three-way specifically. Likely fine, but wasn't formally signed off.
- **Old line 408**: "OS indexes sensitivity... and **selectively modulates** base frequency effects at the N250" — **confirmed overclaim**, same fix needed as Abstract/line 336. "LP indexes... and **selectively drives** the three-way interaction... at the N400" — this one is fine (correctly scoped to the three-way). "**The dissociation between OS and LP** therefore mirrors..." — reconsider in light of retiring "double dissociation," though "dissociation" alone (not "double dissociation") may be fine here since it's describing the asymmetric pattern we're keeping.
- **Old lines 412–414**: nonword mechanism paragraphs — these were extensively revised earlier in this conversation (overclaim fixes: "entirely distinct trajectories" → "driven primarily by," hedging additions like "on this account"/"appears to," etc.). **Need a final check** that those earlier fixes are still intact in the current file version (they should be, since we worked from this same base file, but verify).
- **Old line 436** (Limitations): "the OS/LP dissociation" — generic, low-stakes, probably fine as-is.

**Recommended next step**: search the attached manuscript for `selectively modul` and `dissociat` and go through each remaining hit in document order, same process as this session.

### 2. Table 1 — not yet touched
Needs new rows or footnotes for the four exploratory models (S3a/S3b/S4a/S4b), parallel to the existing †/‡/§ footnote system for the family-size models. Explicitly deferred twice this session pending the terminology decision, which is now settled — this can proceed.

### 3. Final assembly pass (per your standing workflow)
Once the terminology sweep and Table 1 are done, a full read-through is still warranted for:
- Citation placeholders (lmerTest, emmeans)
- Confirming Sawi (2016) attribution is in place in Materials
- Methods ERP Data section vs. finalized model structure

---

## Key verified statistics (for quick reference, no need to re-derive)

**Words N250** (primary): BF × OS: β=−0.455, t(1618)=−4.06, p<.001. FS × OS: β=−0.111, t(1618)=−1.70, p=.089 (marginal).

**Words N250** (exploratory, NEW): BF × LP: β=0.180, SE=0.082, t(1618)=2.20, p=.028, η²p=.003 — opposite sign to OS interaction; largest effect at low LP, attenuating/reversing at high LP (contrasts: LP=−2.5 SD Δ=−0.78, p=.001; LP=+1 SD Δ=−0.15, p=.259; LP=+3 SD Δ=+0.21, p=.433). FS × LP: β=−0.074, p=.119, ns.

**Words N400** (primary): BF × LP: β=0.344, t(1618)=3.98, p<.001. FS × LP: β=−0.071, t(1618)=−1.37, p=.172, ns.

**Words N400** (exploratory, NEW): BF × OS: β=0.195, p=.104, ns. FS × OS: β=0.091, p=.204, ns. → OS has **zero** role at N400 for words, confirmed.

**Nonwords N250**: Complexity × OS: β=0.392, p<.001. Complexity × LP: β=0.358, p<.001. Both interactions show the same reversal pattern (large cost at low skill → attenuates → reverses at high skill) but via different EMM trajectories (OS: driven primarily by complex-nonword trajectory; LP: driven primarily by simple-nonword trajectory) — interpreted via affix-led (OS) vs. stem-led (LP) parsing accounts.

**Nonwords N400**: Complexity × FS × LP three-way: β=0.229, p=.022 (centerpiece finding). Complexity × FS × OS three-way: ns. Complexity × OS two-way: β=0.240, p<.001 (real, but doesn't extend to the three-way).

**The honest summary of the overall pattern**: OS is genuinely N250-specific (never touches N400, words or nonwords' three-way). LP is N400-dominant but not N400-exclusive (also has a real, weaker, oppositely-signed N250 role for words, and a robust N250 role for nonwords). This is why "double dissociation" no longer fits and "component-specific modulation" was adopted instead.

---

## Working style notes (carried over)
- Verify every statistic against actual R output before using it in prose — this session caught three separate copy-paste/mislabeling errors this way.
- Hold edits for approval before applying; work one change at a time; flag overclaims proactively rather than waiting to be asked.
- η²p reported only for significant effects, omitted for null effects (established convention, applied to new S3/S4 tables).
- British spelling; OS/LP capitalised as named constructs; "nonwords" no hyphen; em-dashes retained where parentheses would otherwise appear.
