# Structured Conversation Summary
## Morphological Processing ERP Paper — Working Session

---

## Overview

This was an extended working session covering the full arc of a specialist psycholinguistics journal paper, from theoretical framing through analytic strategy, R implementation, results writing, and Discussion planning. The conversation moved through five broad phases: (1) background theory, (2) introduction writing, (3) analytic restructuring, (4) R implementation and results writing, and (5) Discussion planning.

---

## Phase 1: Theoretical Background

### Topics Covered
The session opened with a series of theoretical questions about morphological processing that ultimately shaped the paper's framing:

**Stem frequency vs. morphological family size**
- Stem frequency indexes token-level familiarity — the accumulated frequency of the base morpheme across all its surface forms. It reflects the ease of form-level morpheme access.
- Family size indexes type-level morphological structure — the number of distinct words sharing a base. It reflects the richness of the semantic representation associated with a morpheme.
- The two variables are empirically dissociable and tap different aspects of lexical organisation.

**State of the art in morphological processing models**
- Classical models (Baayen-Schreuder race model; Caramazza's AAM) are no longer state of the art.
- Three current frameworks are most influential: (1) Early automatic decomposition (Rastle & Davis) — obligatory early form-based parse, semantic filter later; (2) Morpho-orthographic account (Grainger) — intermediate learned orthographic pattern level; (3) Discriminative learning (NDL/LDL, Baayen et al.) — no morpheme representations, both effects emerge from learned weight structure.
- NDL and LDL are related but distinct: NDL uses online Rescorla-Wagner learning with discrete outcomes; LDL uses closed-form linear algebra with continuous semantic vectors. They share the same core theoretical commitments and are best understood as two implementations of a single discriminative learning framework.
- The field has not declared a winner: early masked priming data still supports decomposition accounts; distributional approaches are increasingly mainstream.

**Key papers recommended**
- Baayen et al. (2011), *Psychological Review* — foundational NDL paper
- Baayen, Chuang, Shafaei-Bajestan & Blevins (~2019), *Complexity* — LDL paper

---

## Phase 2: Introduction Writing

### What Was Produced
A complete introduction was drafted and refined across multiple iterations, comprising:

1. **Opening paragraphs** — reading as meaning extraction, English morphology challenge
2. **Bridge paragraph** — plants individual differences logic early
3. **Subsection: Stem Frequency and Morphological Family Size** — covers all four model families in sequence, explains how each interprets the two key variables, closes by identifying time course, novel forms, and individual differences as the three dimensions along which the study adjudicates
4. **Subsection: Individual Differences in Morphological Processing** — Lexical Quality Hypothesis; Andrews et al. (2013) dissociable orthographic and semantic profiles; mapping of OS/LP onto theoretical accounts
5. **Subsection: Aims and Predictions** — three-question structure; asymmetric OS/LP predictions; honest treatment of the words/nonwords separation

### Key Writing Decisions
- Words and nonwords framed as doing distinct theoretical work rather than as equivalent stimulus types
- The asymmetric interaction structure — OS foregrounded at N250, LP at N400 — is explicitly justified in the aims
- The words RT analysis is framed as regression-based with a stated caveat about lack of orthogonal matching
- The nonword analysis is framed as a test of generalization to novel morphological structure
- The double dissociation is the paper's central theoretical claim, stated explicitly as such

---

## Phase 3: Analytic Restructuring

### The Core Decision
The original analyses were symmetric — both OS and LP tested against both components equally. This was replaced with an asymmetric three-question structure:

- **Q1 (RT):** Does OS influence overall lexical decision efficiency? Individual differences as main effects only; no morphological × ID interactions.
- **Q2 (N250):** Does OS modulate early morpho-orthographic parsing? OS foregrounded; LP as covariate.
- **Q3 (N400):** Does LP shape semantic integration? LP foregrounded; OS as covariate.

### Handling Base Frequency and Family Size
A key decision was made to assign each variable to its theoretically appropriate analytic home:
- **Base frequency → RT models** as the primary lexical familiarity predictor
- **Family size → ERP models** as the primary morphological structure predictor (in the original symmetric analyses)
- **Later revision:** Base frequency was identified as the variable specified in the original double dissociation prediction, leading to additional analyses with base frequency as the primary ERP predictor for words

### Model Specifications Finalised
All six models were specified and coded:
- Words RT: `logRT ~ zLogBF + zLogFS + OS + LP + (1|SubjID) + (1|Item)`
- Nonwords RT: `logRT ~ complexity + zLogBF + zLogFS + OS + LP + (1+complexity|SubjID) + (1|ItemID)`
- Words N250: `value ~ base_frequency * OS + LP + (1|SubjID) + (1|SubjID:chlabel)`
- Words N400: `value ~ base_frequency * LP + OS + (1|SubjID) + (1|SubjID:chlabel)`
- Nonwords N250: `value ~ complexity * OS + complexity * LP + family_size + (1|SubjID) + (1|SubjID:chlabel)`
- Nonwords N400: `value ~ complexity * family_size * LP + OS + (1|SubjID) + (1|SubjID:chlabel)`

---

## Phase 4: R Implementation and Results Writing

### R Technical Issues Resolved

**Contrast coding**
- Sum coding `c(-0.5, 0.5)` recommended throughout for categorical predictors
- OS and LP confirmed as already mean-centered from PCA — no additional scaling needed
- Global `options(contrasts = c("contr.treatment", "contr.poly"))` rejected in favour of explicit per-variable coding

**Model fitting issues**
- Words RT: dropping random slope for zLogBF resolved singular fit; OS became non-significant — reported as marginal and unstable
- Nonwords RT: model healthy (isSingular = FALSE); Kenward-Roger hanging due to correlated random slope — Satterthwaite used throughout
- `r2()` from performance package returned NA for conditional R² — `r2_nakagawa()` used instead
- emmeans crashing on complex models — resolved by `emm_options(lmer.df = "satterthwaite")` set globally
- patchwork/ggplot2 namespace conflict — resolved by loading ggplot2 before lmerTest
- Back-transformation of log RT: `tran = "log"` in emmeans plus manual exponentiation

**Effect sizes and R²**
- `eta_squared(model, partial = TRUE)` from effectsize package
- `r2_nakagawa()` from performance package (NOT `r2()`)
- Both marginal and conditional R² reported throughout

### Results Section — What Was Written

All eight result paragraphs were drafted, verified against R output, and corrected:

**Words:**
- RT: Base frequency and family size drive responding; OS marginal and unstable; LP null
- N250 (base frequency primary): Base Frequency × OS significant — KEY FINDING; LP not interacted
- N400 (base frequency primary): Base Frequency × LP significant — KEY FINDING; OS main effect only

**Nonwords:**
- RT: Complexity drives responding; base frequency inhibitory; OS predicts overall efficiency; LP null
- N250: Complexity and family size main effects; Complexity × OS and Complexity × LP both significant; reversal at high skill
- N400: Three-way Complexity × Family Size × LP — centerpiece finding; monotonic attenuation (no reversal unlike N250)

### Key Findings Verified Against R Output

**Double dissociation for words (base frequency):**

| | N250 | N400 |
|---|---|---|
| Base Frequency × OS | ✓ Significant | OS main effect only |
| Base Frequency × LP | LP not interacted | ✓ Significant |

**N250 nonwords — reversal pattern:**
Both OS and LP show identical pattern across three SD levels:
- Low skill: large complexity cost
- Mean skill: attenuated cost
- High skill: reversed (complex less negative than simple)

**N400 nonwords — three-way:**
- Low LP: large Complexity × Family Size interaction (Δ = −0.667, p < .001)
- Mean LP: attenuated but significant (Δ = −0.440, p = .0003)
- High LP: absent (Δ = −0.213, p = .188)

### Results Section Structure Finalised
```
Words
  RT
  N250 (base frequency primary)
  N400 (base frequency primary)

Nonwords
  RT
  N250
  N400

Results Summary
```

### Key Writing Decisions
- No claim that RT interactions were absent — they were not tested by design
- ERP models framed as "designed to detect" modulation RT models were not designed for
- OS and LP unpacked by name in the N250 summary — "skill" rejected as ambiguous
- Results summary split: empirical synthesis stays in Results; "three key findings" paragraph moves to open Discussion
- Model summary table (Table 1) added to orient readers to the asymmetric interaction structure
- Explanatory paragraph added after table justifying asymmetric design choices

---

## Phase 5: Discussion Planning

### Structure Agreed
The Discussion is organised around three findings in inferential dependency order:

**Opening paragraph** — frames three findings, signals structure

**Section 1: N250 reversal at high skill** (most unexpected, must be established first)
- Processing cost vs. morphological sensitivity debate
- Why reversal = real suffix facilitates parsing for skilled readers
- Why both OS and LP converge on early processing — broad lexical experience
- Connection to morpho-orthographic and discriminative learning accounts

**Section 2: Behavioral/ERP dissociation**
- Individual differences invisible in RTs but visible in neural dynamics
- Lexical Quality Hypothesis — precision of representation vs. response speed
- Why OS predicts nonword RT efficiency but not morphological modulation

**Section 3: N400 three-way and semantic integration** (culmination)
- What Complexity × Family Size × LP means theoretically
- Attenuation without reversal — contrast with N250
- LP selective at N400; OS not — clearest support for predicted dissociation
- Connection to NDL/LDL and multi-stage accounts
- Null family size × LP for words — why familiar words differ from nonwords
- Base frequency × LP for words — LP enhances semantic integration of high frequency stems

**Closing:** Partial dissociation; limitations; future directions

### Opening of Each Discussion Section Drafted
Draft opening sentences were produced for all three sections, each starting with a concrete empirical observation before moving to interpretation.

---

## Phase 6: Theoretical Clarifications Made During Session

Several theoretical points were clarified during the session that will be important for the Discussion:

1. **N250 direction for base frequency vs. family size:** High base frequency → MORE negative N250; large family size → LESS negative N250. These are in opposite directions. Explanation: base frequency reflects strength of form-level activation (more effortful early processing for high frequency stems); family size reflects efficiency of morphological pattern matching (less effortful for large families).

2. **Why large family size produces less negative N250 for both words and nonwords:** The N250 does not reflect decision direction — it reflects degree of morphological activation. Large families generate more efficient activation regardless of lexical status. The behavioral cost of strong morphological activation for nonwords appears in RTs (via base frequency inhibition), not in the N250.

3. **Why base frequency (not family size) slows nonword rejection behaviorally:** Base frequency is a token-level variable reflecting stem activation strength, which directly competes with the rejection decision. Family size is a type-level variable reflecting network breadth — it shapes early processing but does not persist strongly enough to reliably slow rejection.

4. **The N250 reversal interpretation:** The reversal at high skill (complex less negative than simple for high OS/LP readers) should be interpreted as the real suffix *facilitating* early processing for skilled readers, not as skilled readers being more misled by morphological structure. The N250 reflects processing cost, not morphological sensitivity per se.

5. **NDL/LDL are not neural networks:** They are linear models. NDL is a single-layer model using Rescorla-Wagner learning; LDL is ordinary least squares regression between vector spaces. The relevant theoretical contrast is symbolic/morpheme-based vs. discriminative/distributional, not symbolic vs. neural network.

---

## Outstanding Issues for New Chat

### Must Resolve First
- Integration of base frequency (primary) and family size (secondary) word ERP analyses — whether both reported in full or one supplementary

### Address in New Chat
- Write Discussion sections 1, 2, and 3
- Update Table 1 to reflect base frequency as primary predictor for word ERP analyses
- Minor update to results orienting paragraph
- Formally integrate null Complexity × BF × LP for nonwords as specificity cross-check
- Complete all [CITATION] placeholders

---

*Summary created at end of extended working session. Use alongside project_memory_log.md when opening new chat.*
