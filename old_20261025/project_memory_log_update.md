# Project Memory Log Update: Morphological Processing ERP Paper
## Supplement to prior log — covers this session's developments

---

## 1. MAJOR DECISIONS FROM THIS SESSION

### Word data: KEPT IN THE PAPER
After extensive discussion of whether to drop word data for a cleaner, faster nonword-only paper, Joanna decided explicitly to **keep both word and nonword data**, prioritizing a novel theoretical contribution over speed to publication. This decision was reaffirmed once it became clear the word N250 base-frequency × OS finding is needed to theoretically ground the nonword affix-led/stem-led account (see below).

### Analytic structure: SYMMETRIC MODELS ADOPTED
- **Nonword N250**: `complexity * OS + complexity * LP + family_size` (family_size = covariate). This was already symmetric by original design — not a late addition.
- **Nonword N400**: NEW primary model — single symmetric model: `complexity * family_size * LP + complexity * family_size * OS` (sum coding required — must explicitly set `contrasts()` for complexity and family_size, or treatment coding will corrupt lower-order term interpretation, though 3-way terms are coding-invariant).
- This symmetric N400 model is the primary confirmatory analysis, not exploratory — it directly tests the OS/LP dissociation within one model rather than via separate models.
- Old separate LP-only and OS-only N400 models are superseded by the symmetric model and generally shouldn't be reported in full.

### Item-level variable assignment: THEORETICALLY JUSTIFIED (not post-hoc)
- **Words**: Base Frequency is the primary item-level ERP variable (indexes strength of stored lexical representation / stem-form entrenchment).
- **Nonwords**: Family Size is the primary item-level ERP variable (indexes richness of morphological neighborhood available when no whole-word representation exists).
- Critical: this must NOT be justified by pointing to which variable produced significant results (circular). The justification is theoretical: words study stored-representation access; nonwords study morphological generalization absent whole-word storage. This text has been drafted and integrated into the Methods (ERP Data section).
- Base frequency remains a covariate/secondary variable in nonword models; family size remains secondary for words (may go to supplementary — final call on main-text-vs-supplementary still open, see Outstanding Items).

### Extended contrast ranges: NOW USING OBSERVED DATA LIMITS, NOT ROUND SDs
- Actual observed range: **LP: −2.67 to +3.11**; **OS: −1.98 to +1.93**.
- All follow-up contrasts throughout the paper (N250 and N400, words and nonwords) were rerun/should be reported at these limits (e.g., LP at −2.5 and +3, OS at −1.9 and +1.9) rather than at round ±2 SD, because doing so revealed a genuine reversal at the nonword N250 for OS (significant only at OS = +1.9, not at +1) and a genuine reversal at the nonword N400 family-size-within-complex effect at LP = +3 (not visible at ±2).

---

## 2. KEY NEW EMPIRICAL FINDINGS THIS SESSION

### Nonword N250 — OS reversal mechanism (REVISED)
- OS reversal at N250 IS real but only reaches significance at the extreme of the range (OS = +1.9: Δ = −0.49, t = −4.27, p < .001; at OS = +1 only marginal, p = .053).
- Mechanism: driven primarily by the **complex nonword trajectory** decreasing in negativity faster than simple nonwords (EMM complex: −1.72 → +0.16 across OS range; EMM simple: −0.72 → −0.34). NOT driven by a rising cost for simple nonwords.
- Reframed account: OS does not gate whether a parse is triggered (that account was logically incoherent — see below); rather, the real suffix triggers parsing in ALL readers, but higher-OS readers resolve that parse more efficiently. This is "affix-led parsing" reframed as being about parsing **efficiency**, not parsing **sensitivity/triggering**.
- (Earlier reasoning error, corrected: original phrasing implied low-OS readers don't detect the affix at all, which would predict NO complexity effect at low OS — contradicted by data showing LARGEST complexity cost at low OS.)

### Nonword N250 — LP reversal mechanism (CONFIRMED, verified at new range)
- LP reversal significant at LP = +1 (Δ = −0.141, p = .032) and LP = +3 (Δ = −0.86, t = −6.38, p < .001).
- Mechanism: driven ENTIRELY by the **simple nonword trajectory** becoming increasingly negative with LP (EMM simple: +0.42 at LP=−2.5 → −1.70 at LP=+3). Complex nonwords stay essentially FLAT across LP (EMM: −0.69 → −0.84).
- This is "stem-led parsing": stem recognition triggers a parse attempt regardless of what follows; succeeds (no cost/benefit, flat) for complex nonwords, fails (growing cost) for simple nonwords as LP increases.
- **Key contrast with OS**: OS reversal driven by complex-word trajectory; LP reversal driven by simple-word trajectory. This dissociation of mechanism (not just magnitude) is a centerpiece theoretical contribution.

### Nonword N400 — symmetric model results (VERIFIED, sum-coded)
- 3-way Complexity × FamilySize × LP: β=0.229, t(4851)=2.29, **p=.022** — significant.
- 3-way Complexity × FamilySize × OS: β=0.143, t(4851)=1.04, **p=.300** — NOT significant.
- Complexity × OS 2-way IS significant (β=0.240, t=3.49, p<.001) — OS reduces overall complexity effect at N400 but doesn't touch the family-size interaction. This must be stated accurately (a previous draft mistakenly implied there were OS 3-way follow-ups to report when there weren't — corrected to frame OS follow-ups as descriptive characterization of a null 3-way, not inferential follow-up).
- Family-size-within-complex-nonwords effect reverses significantly at LP=+3 (Δ=−0.58, t=−2.49, p=.013) after being large positive at LP=−2.5 (Δ=+0.72, p<.001) — genuine reversal, not mere attenuation to zero. Does NOT reverse across the OS range (attenuates only, non-sig at OS=+1.9: Δ=−0.11, p=.581).
- Complexity effect (averaged over family size) attenuates with LP but does NOT significantly reverse even at LP=+3 (Δ=−0.30, p=.065) — contrast with N250 where it does reverse significantly. (Interpretive claim about WHY this contrast exists was drafted then retracted for being unsupported post-hoc reasoning — see Section 4.)
- Family Size × LP 2-way also significant (β=0.122, p=.015) — now reported with own sentence (previously omitted despite being listed in intro sentence — fixed).

### Exploratory nonword RT model (Complexity × OS/LP added)
- Formula: `logRT ~ complexity*OS + complexity*LP + zLogBF + zLogFS + (1+complexity|SubjID) + (1|ItemID)`
- Complexity × OS: NOT significant (p=.721).
- Complexity × LP: significant (β=0.009, t=2.108, **p=.039**) — but OPPOSITE direction from N250: complexity cost in RT GROWS monotonically with LP (Δ log-RT: 0.026 at LP=−2.5 → 0.074 at LP=+3, all p<.05, no reversal). ~34ms cost at mean LP growing to ~55ms at LP=+3.
- Interpretation: high-LP readers show more efficient neural parsing (N250) but take LONGER behaviorally for complex nonwords — consistent with stem-led parsing account: they engage in more thorough morphological analysis before the reject decision, which is neurally efficient but behaviorally costly.
- This model is EXPLORATORY (not pre-specified; original RT models deliberately excluded morphological × ID interactions by design) and should be reported/labeled as such, feeding into the Behavioral/ERP dissociation Discussion section, not the main confirmatory Results.

---

## 3. NEW THEORETICAL FRAMEWORK: AFFIX-LED VS STEM-LED PARSING

This is the paper's most novel contribution, refined heavily this session:

- **OS → affix-led parsing**: indexes efficiency of parsing triggered by real-affix recognition. Grounded in existing affix-stripping accounts (Taft & Forster, 1975; Rastle & Davis, 2008) — NOT novel in the "affix triggers parsing" part, but novel in mapping OS specifically onto this mechanism's efficiency.
- **LP → stem-led parsing**: indexes propensity for parsing triggered by stem recognition, independent of affix status. This IS genuinely novel, but is empirically grounded in **Beyersmann, Cavalli, Casalis, & Colé (2016, Scientific Studies of Reading)** — critical citation identified this session. Beyersmann et al. found high-proficiency readers show embedded stem priming even for non-affixed pseudowords (e.g., "cashew"), suggesting stem activation isn't contingent on affix presence for skilled readers, and that affix-stripping alone is insufficient. Their proficiency measure was a single undifferentiated construct — the present study's contribution is decomposing this into OS vs. LP and showing it's specifically LP-linked.
- Citation key confirmed by Joanna: `beyersmannEmbeddedStemPriming2016`
- This citation has now been integrated into: Introduction (new paragraph after the NDL/LDL section, before Individual Differences section), Aims and Predictions (nonword prediction paragraph), N250 Discussion (Nonword Stimiuli subsubsection, twice), and Theoretical Implications section.
- Important nuance repeatedly corrected: Taft & Forster and Rastle & Davis are BOTH affix-stripping/affix-led models (lexical access is stem-based but triggered by affix-stripping) — they are not stem-led alternatives. The real novel/stem-led contrast is with Beyersmann et al.'s embedded stem activation account.

### Word data now needed to ground this theoretical claim
Because OS also modulates base-frequency (a STEM-level variable) at the word N250, simply calling OS "affix-specific" would be inconsistent with the word data. Resolution reached (Option B, chosen over dropping word data or reframing nonword account): OS operates more broadly on orthographic/form-level information in general (as shown in word N250 base-frequency effect), but when a novel form must be parsed with no stored whole-word entry, OS-driven parsing is specifically channeled through affix recognition because that's the primary morphological signal available. This connective paragraph has been added to end of N250 Nonword Discussion subsubsection.

---

## 4. KEY REASONING CORRECTIONS MADE THIS SESSION (im important for avoiding regression)

Joanna caught and corrected numerous logical/theoretical errors in Claude's reasoning. Key ones to not reintroduce:

1. **Family size ≠ "whole word access"**: Larger family size does NOT mean more whole-word access (that's backwards — bigger family could mean MORE decomposition pressure, not less). Correct account: family size → richer/more precise SEMANTIC representation of the stem via repeated form-meaning pairings (citing Bolger et al. 2008; Li et al. 2026), which enables stronger semantic-to-form feedback, not "whole word access."
2. **Base frequency ≠ homograph-driven meaning inconsistency**: Original claim that base frequency involves "different meanings" across inflectional variants was wrong (inflectional variants like walk/walks/walked share meaning). Corrected: the real distinction is that base frequency is driven by INFLECTIONAL variants (same lexical entry, no new form-meaning pairings), while family size is driven by DERIVED words (distinct lexical entries, each reinforcing the stem's semantic core).
3. **"High-OS readers insensitive to affix" is logically incoherent**: If low-OS readers were simply insensitive to affix-status, there should be NO complexity effect for them, not the LARGEST one. Corrected to an efficiency-based account (see Section 2 above) rather than a sensitivity/detection-based account.
4. **Semantic richness activated by a stem does NOT differ by LP** — what differs is representational PRECISION/quality of that same activated content, not its quantity. (Corrected an error where Claude implied low-LP readers activate "more" semantic content.)
5. **Can't claim a crossover interaction reflects "two mechanisms" (familiarity-gating vs. efficient-mapping) without evidence discriminating them** — retracted this account for the word N400 BF×LP crossover in favor of Option C: describe the empirical crossover pattern, remain agnostic about mechanism, note that accuracy data would be needed to adjudicate.
6. **A stated interpretive claim needs an actual reason, not just an assertion** — repeatedly, Joanna asked "why?" after Claude asserted mechanism-flavored claims (e.g., "why would high base frequency increase N250 amplitude via more effortful parsing" — no good answer existed, so the claim was walked back to a purely contrastive/relational one rather than a positive mechanistic claim about BF alone).
7. **Two things can't be "just stated," they need explaining**: e.g., why LP has "nothing to modulate" for simple-nonword family-size effects (because pseudoaffix doesn't trigger family recruitment in the first place) — now explained rather than asserted.
8. Grammatical/stylistic fixes to retain: comparative/comparative parallelism (not "higher...largest"), avoid unexplained jargon ("gates," "bindings," "scaffold," "architecture" as unglossed terms — replaced with plainer language throughout), avoid forward-referencing undefined terms ("these two accounts" before both are introduced), avoid AI-sounding throat-clearing phrases ("it is worth stating plainly," "the finding can be stated plainly before the statistics are unpacked").

---

## 5. WRITING/STYLE DECISIONS THIS SESSION

- LaTeX should be produced WITHOUT line breaks at fixed column width (one-line-per-paragraph) per Joanna's explicit request, EXCEPT Joanna later asked to revert BACK to line-wrapped LaTeX (as in original style) — **current standing instruction: USE LINE BREAKS** (the no-line-break request was temporary/superseded).
- British spelling throughout (organised, behavioural, analysed, etc.) — enforce even in newly drafted Methods/Results text that may have been drafted pre-this-session in American spelling.
- OS and LP always capitalized as named constructs (not "orthographic sensitivity" lowercase) — multiple inconsistencies caught and fixed this session; keep flagging.
- "Double dissociation" language should be used cautiously — replaced with "dissociation of mechanism" in the N250 nonword context since it isn't a classic crossed double dissociation.
- Report t-ratios as "t" not "z" even when emmeans output prints them without clarifying — Joanna caught this error (contrasts were being mislabeled as z when they were t).
- Avoid metaphors that don't cash out concretely for readers (e.g., "scaffold for processing," "resolve semantic content against the novel form") — Joanna pushed back hard on these; replace with mechanistic, concrete language even if longer.

---

## 6. OUTSTANDING ITEMS (carried forward, still unresolved)

1. **Words Family Size ERP results (both N250 and N400 versions)**: Decision leaning toward brief in-text mention (main effects + key stats) with full model output relegated to supplementary materials, since Base Frequency is now the theoretically-justified PRIMARY word variable. Not yet drafted/finalized.
2. **Table 1 (`tab:models`)**: Has been substantially redrafted this session to reflect (a) symmetric nonword N400 model showing both 3-way interactions, (b) covariate notation (†) distinguishing covariates from primary predictors, (c) updated explanatory paragraphs before/after the table. Should be re-verified against final Results text once family-size words decision is finalized.
3. **Citation placeholders**: Several [CITATION] tags remain unfilled throughout (lmerTest, emmeans package citations flagged specifically this session; general sweep still needed).
4. **Sawi (2016) attribution**: Still needs to be placed in Materials section per original instruction (not addressed this session).
5. **Abstract**: Drafted and trimmed to fit Frontiers in Language Sciences requirement of 350 words (single paragraph, no citations) — current draft is 305 words, confirmed. Target journal: **Frontiers in Language Sciences** (newly decided this session), likely Psycholinguistics or Neurobiology of Language section.
6. **OS main effect at word N400 (p=.049) caution sentence**: Previously drafted, still needs to be checked for integration into final words N400 results paragraph.
7. **Results orienting paragraph**: Has been revised this session to reflect symmetric model and updated theoretical framing (morpho-orthographic decomposition + LQH replacing "structured parsing accounts and discriminative learning framework" language). Should be considered finalized pending final read-through.
8. **Methods — ERP Data section**: Substantially revised this session (symmetric N400 model description, item-level variable justification paragraph, contrast-range language updated to "observed range" rather than ±1 SD). Should be considered finalized pending final read-through.
9. **Discussion**: ALL major subsections now drafted and revised this session:
   - Opening ✓ (revised, no mid-sentence jargon, forward-pointing rather than front-loading mechanism detail)
   - N250 Word Stimuli ✓ (revised: comparative/comparative fix, Family Size × OS reframed as parallel marginal trend not "same direction," forward pointer to nonword complexity added)
   - N250 Nonword Stimuli ✓ (fully reworked: efficiency-based OS account, Beyersmann citation integrated twice, connects back to word data at end)
   - N400 opening ✓ (revised to accurately reflect OS 2-way significance, not "OS only a main effect")
   - N400 Word Stimuli ✓ (fully reworked: Option C agnostic mechanism framing, LQH introduced before precision argument not after, accuracy-data paragraph unpacked)
   - N400 Nonword Stimuli ✓ (fully reworked: two-factor explanation of when family size matters — valid morphological signal AND representational precision — LQH-first framing, OS null 3-way properly characterized as descriptive not inferential)
   - Behavioral and Electrophysiological Measures Index Different Aspects of Morphological Processing ✓ (renamed from earlier titles per Joanna's concern about alienating RT-focused reviewers; incorporates exploratory RT model)
   - Theoretical Implications and Limitations ✓ (four subsubsections: form-meaning distinction; affix-led/stem-led mechanisms; LQH and N400; limitations — pre-registration limitation carefully reframed per Joanna's pushback, NOT implying no plan existed, noting pre-registration wasn't standard practice when study began and isn't universal even now at small institutions)
10. **Introduction**: Revised passage integrating Beyersmann et al. citation has been drafted (new paragraph after NDL/LDL section) — needs to be checked against what currently follows it in the actual manuscript for smooth transition into Individual Differences section.
11. **Aims and Predictions**: Revised to incorporate Beyersmann-motivated LP/N250 prediction — completed and integrated this session.

---

## 7. KEY VERIFIED STATISTICS TABLE (this session, for quick reference)

### Nonword N250 (family_size covariate model) — FINAL
- Complexity: β=−0.233, t(4856)=−4.63, p<.001
- Complexity×OS: β=0.392, t(4856)=6.98, p<.001
- Complexity×LP: β=0.358, t(4856)=8.76, p<.001
- R²m=.025, R²c=.575
- OS contrasts: −1.9(Δ=0.99,p<.001), −1(Δ=0.64,p<.001), 0(Δ=0.25,p<.001), +1(Δ=−0.14,p=.053), +1.9(Δ=−0.49,p<.001)
- LP contrasts: −2.5(Δ=1.11,p<.001), −1(Δ=0.57,p<.001), 0(Δ=0.22,p<.001), +1(Δ=−0.14,p=.032), +3(Δ=−0.86,p<.001)

### Nonword N400 (symmetric model) — FINAL, sum-coded
- Complexity: β=−0.469, t(4851)=−7.64, p<.001
- Complexity×FamilySize: β=−0.446, t(4851)=−3.63, p<.001
- Complexity×LP: β=0.254, t(4851)=5.08, p<.001
- FamilySize×LP: β=0.122, t(4851)=2.45, p=.015
- Complexity×OS: β=0.240, t(4851)=3.49, p<.001
- FamilySize×OS: β=0.066, t(4851)=0.955, p=.340
- Complexity×FamilySize×LP: β=0.229, t(4851)=2.29, **p=.022**
- Complexity×FamilySize×OS: β=0.143, t(4851)=1.04, p=.300 (n.s.)
- R²m=.013, R²c=.667

### Exploratory Nonword RT (Complexity×OS/LP added)
- Complexity×OS: β=−0.002, t(59)=−0.358, p=.721 (n.s.)
- Complexity×LP: β=0.009, t(64)=2.108, **p=.039**

---

*This update should be read alongside the original project_memory_log.md. Paste both into a new chat to establish full context.*
