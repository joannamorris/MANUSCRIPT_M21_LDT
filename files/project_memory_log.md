# Project Memory Log: Morphological Processing ERP Paper
## Conversation Summary and Continuity Document

---

## 1. THE ORIGINAL PROBLEM

The user is writing a specialist psycholinguistics journal paper examining individual differences in morphological processing using ERPs and reaction times. The study involves a lexical decision task (LDT) with:

- **Participants:** 67 adults (60 with ERP data)
- **Stimuli:** 100 words and 100 morphologically complex nonwords
- **Nonword types:** Complex (real stem + real affix, e.g., *gasful*) vs. Simple (real stem + pseudoaffix, e.g., *gasfil*)
- **Measures:** Reaction times (RTs) and ERPs (N250 and N400 components)
- **Individual differences:** Two orthogonal PCA dimensions derived from vocabulary knowledge, spelling ability, and print exposure:
  - **Dim.1 = Language Proficiency (LP)** — depth/breadth of lexical-semantic knowledge
  - **Dim.2 = Orthographic Sensitivity (OS)** — sensitivity to sublexical orthographic structure

The user was struggling with: (a) theoretical framing of the introduction, (b) analytic strategy, (c) R code for mixed effects models, and (d) writing up results.

---

## 2. KEY THEORETICAL DECISIONS

### The Core Prediction: Double Dissociation
The study tests whether OS and LP dissociably modulate morphological processing at distinct temporal stages:
- **OS → early form-based processing (N250):** OS should modulate stem/base frequency effects at the N250, reflecting sensitivity to sublexical orthographic structure
- **LP → later semantic integration (N400):** LP should modulate family size effects at the N400, reflecting depth of lexical-semantic knowledge

This prediction follows from Andrews and colleagues' finding that orthographic and semantic profiles are dissociable axes of individual variation, combined with the theoretical distinction between stem frequency (form-level access) and family size (semantic representation richness).

### The Three-Question Analytic Structure
The analyses are organised around three core questions:
1. **Q1 (RT/Behavioral):** Does OS influence overall lexical decision efficiency?
2. **Q2 (N250/Early neural):** Does OS modulate early morpho-orthographic parsing?
3. **Q3 (N400/Late neural):** Does LP shape semantic integration of morphological information?

### Key Theoretical Models Discussed
- **Baayen-Schreuder race model** (classical dual-route): stem frequency → decomposition route; family size → whole-form route
- **Early automatic decomposition (Rastle & Davis):** obligatory early form-based parse, then semantic filter
- **Morpho-orthographic account (Grainger):** intermediate morpho-orthographic level
- **NDL/LDL (Baayen et al.):** no morpheme representations; discriminative learning from distributional statistics; both effects emergent from learned weight structure

---

## 3. INTRODUCTION — CURRENT STATUS: COMPLETE

### Structure
1. Opening paragraphs on reading and English morphology
2. Bridge paragraph planting individual differences logic
3. **Subsection: Stem Frequency and Morphological Family Size: Theoretical Interpretations Across Current Models** — covers classical, early decomposition, morpho-orthographic, and NDL/LDL accounts
4. **Subsection: Individual Differences in Morphological Processing** — Lexical Quality Hypothesis; Andrews et al. (2013) finding; OS/LP profiles mapped onto theoretical accounts
5. **Subsection: Aims and Predictions** — three analyses, double dissociation as central claim

### Key Framing Decisions
- Words and nonwords framed as doing distinct theoretical work (words = time course of stored representations; nonwords = generalization to novel forms)
- RT models framed as efficiency measures (no morphological × ID interactions by design — stated explicitly in methods)
- ERP models framed as architecture measures
- The asymmetric interaction structure (OS at N250, LP at N400) is justified in both the aims section and the results section

---

## 4. ANALYTIC STRATEGY — FINALISED

### RT Models
No morphological structure × individual difference interactions in RT models by design. Individual differences entered as main effects only.

**Words RT:**
```r
m_rt_words <- lmer(
  logRT ~ zLogBF + zLogFS + OS + LP +
    (1 | SubjID) + (1 | Item),
  data = rt_w,
  control = lmerControl(optimizer = "bobyqa")
)
```

**Nonwords RT:**
```r
m_rt_nw <- lmer(
  logRT ~ complexity + zLogBF + zLogFS + OS + LP +
    (1 + complexity | SubjID) + (1 | ItemID),
  data = rt_nw,
  control = lmerControl(optimizer = "bobyqa")
)
```

### Contrast Coding
- `complexity`: sum coded `c(-0.5, 0.5)` with levels `c("Simple", "Complex")`
- `family_size`: sum coded `c(-0.5, 0.5)` with levels `c("Small", "Large")`
- `base_frequency`: sum coded `c(-0.5, 0.5)` with levels `c("Low", "High")`
- OS and LP: PCA scores, already mean-centered by construction — no additional scaling needed

### ERP Models — Base Frequency Analyses (Primary for Words)

**Words N250 (Base Frequency × OS):**
```r
contrasts(erp_w$base_frequency) <- c(-0.5, 0.5)
m_w_N250_bf <- lmer(
  value ~ base_frequency * OS + LP +
    (1 | SubjID) + (1 | SubjID:chlabel),
  data = subset(erp_w, time_window == "N250"),
  control = lmerControl(optimizer = "bobyqa")
)
```

**Words N400 (Base Frequency × LP):**
```r
m_w_N400_bf <- lmer(
  value ~ base_frequency * LP + OS +
    (1 | SubjID) + (1 | SubjID:chlabel),
  data = subset(erp_w, time_window == "N400"),
  control = lmerControl(optimizer = "bobyqa")
)
```

### ERP Models — Family Size Analyses

**Words N250 (Family Size × OS) — secondary:**
```r
contrasts(erp_w$family_size) <- c(-0.5, 0.5)
m_w_N250_fs <- lmer(
  value ~ family_size * OS + LP +
    (1 | SubjID) + (1 | SubjID:chlabel),
  data = subset(erp_w, time_window == "N250"),
  control = lmerControl(optimizer = "bobyqa")
)
```

**Words N400 (Family Size × LP) — secondary:**
```r
m_w_N400_fs <- lmer(
  value ~ family_size * LP + OS +
    (1 | SubjID) + (1 | SubjID:chlabel),
  data = subset(erp_w, time_window == "N400"),
  control = lmerControl(optimizer = "bobyqa")
)
```

**Nonwords N250 (Complexity × OS and LP; family_size as covariate — CONFIRMED FINAL):**
```r
contrasts(erp_nw$family_size) <- c(-0.5, 0.5)
m_nw_N250 <- lmer(
  value ~ complexity * OS + complexity * LP + family_size +
    (1 | SubjID) + (1 | SubjID:chlabel),
  data = subset(erp_nw, time_window == "N250"),
  control = lmerControl(optimizer = "bobyqa")
)
```

**Nonwords N400 (Complexity × Family Size × LP — centerpiece finding):**
```r
contrasts(erp_nw$complexity)  <- c(-0.5, 0.5)
contrasts(erp_nw$family_size) <- c(-0.5, 0.5)
m_nw_N400 <- lmer(
  value ~ complexity * family_size * LP + OS +
    (1 | SubjID) + (1 | SubjID:chlabel),
  data = subset(erp_nw, time_window == "N400"),
  control = lmerControl(optimizer = "bobyqa")
)
```

### R Packages Used
```r
library(lme4)
library(lmerTest)    # Satterthwaite df — load BEFORE lmerTest, BEFORE fitting models
library(emmeans)     # follow-up contrasts; use emm_options(lmer.df = "kenward-roger")
library(effectsize)  # eta_squared(model, partial = TRUE)
library(performance) # r2_nakagawa(model) — use this, NOT r2()
library(MuMIn)       # r.squaredGLMM() as alternative if performance fails
library(ggplot2)
library(patchwork)   # load after ggplot2, before lmerTest
```

### Important Technical Notes
- Always load `ggplot2` and `patchwork` BEFORE `lmerTest` to avoid namespace conflicts
- Use `r2_nakagawa()` not `r2()` — the latter has a bug with certain model structures
- `emm_options(lmer.df = "kenward-roger")` at start of emmeans session
- For back-transforming log RT: use `tran = "log"` in emmeans or exponentiate manually
- KR df hang with complex random effects — Satterthwaite is acceptable and standard
- Nonword RT: `emmeans` crashed until `emm_options(lmer.df = "satterthwaite")` was set globally

---

## 5. KEY RESULTS — SUMMARY

### RT Results

**Words RT:**
- Base Frequency: β = −0.017, t(100.97) = −3.66, p < .001, η²p = .12
- Family Size: β = −0.013, t(93.59) = −2.64, p = .010, η²p = .07
- OS: marginal trend, β = −0.035, t(63.84) = −1.85, p = .069 — NOT robust to random effects changes
- LP: null, p = .35
- R²marginal = .033, R²conditional = .417

**Nonwords RT:**
- Complexity: β = 0.049, t(62.68) = 9.13, p < .001, η²p = .57; M_complex = 718.9 ms [695.2, 743.4], M_simple = 684.6 ms [661.5, 708.5]; difference ≈ 34 ms
- Base Frequency: inhibitory effect, β = 0.015, t(98.21) = 3.05, p = .003, η²p = .09
- Family Size: ns, p = .22
- OS: significant, β = −0.041, t(62.21) = −2.23, p = .030, η²p = .07
- LP: null, p = .78
- R²marginal = .050, R²conditional = .494

### N250 Results

**Words N250 — BASE FREQUENCY (primary, tests double dissociation):**
- Base Frequency main effect: β = −0.318, t(1618) = −3.18, p = .002; High more negative than Low
- **Base Frequency × OS: β = −0.455, t(1618) = −4.06, p < .001** ← KEY FINDING
- Follow-ups: BF effect absent at low OS (p = .374), significant at mean OS (Δ = 0.318, p = .002), large at high OS (Δ = 0.773, p < .001)
- LP: not interacted, main effect ns (p = .162)
- R²marginal = .018, R²conditional = .801

**Words N250 — FAMILY SIZE (secondary):**
- Family Size: β = −0.324, t(1618) = −5.54, p < .001; M_large = −0.57 µV [−1.03, −0.11], M_small = −0.90 µV [−1.36, −0.44]
- Family Size × OS: marginal trend, β = −0.111, t(1618) = −1.70, p = .089
- LP: ns
- R²marginal = .019, R²conditional = .738

**Nonwords N250:**
- Complexity: β = −0.233, t(4856) = −4.63, p < .001; M_complex = −0.759 µV, M_simple = −0.526 µV
- Family Size (covariate): β = 0.182, t(4856) = 3.63, p < .001
- **Complexity × OS: β = 0.392, t(4856) = 6.98, p < .001** ← KEY FINDING
- **Complexity × LP: β = 0.358, t(4856) = 8.76, p < .001** ← KEY FINDING (parallel to OS)
- Both interactions show same pattern: large complexity cost at low skill → attenuated → REVERSED at high skill
  - OS: Δ = 0.642 (low), 0.250 (mean), −0.142 (high, p = .053)
  - LP: Δ = 0.574 (low), 0.216 (mean), −0.141 (high, p = .032)
- Theoretical interpretation: N250 reflects processing COST not sensitivity; reversal = real suffix facilitates parsing for skilled readers; both dimensions converge on early processing (qualifies predicted OS-specific effect)

**Nonwords N250 (family_size as covariate — CONFIRMED FINAL):**

### N400 Results

**Words N400 — BASE FREQUENCY (primary, tests double dissociation):**
- Base Frequency main effect: β = 0.214, t(1618) = 2.01, p = .044; High more positive than Low (facilitation)
- **Base Frequency × LP: β = 0.344, t(1618) = 3.98, p < .001** ← KEY FINDING
- Follow-ups: BF effect absent at low LP (p = .333), significant at mean LP (Δ = −0.214, p = .044), large at high LP (Δ = −0.558, p < .001)
- OS: main effect significant p = .049 (overall amplitude, no interaction with BF)
- R²marginal = .026, R²conditional = .825

**Words N400 — FAMILY SIZE (secondary):**
- Family Size: β = −0.452, t(1618) = −7.07, p < .001; M_large = 0.518 µV [−0.054, 1.089], M_small = 0.062 µV [−0.509, 0.634]
- Family Size × LP: ns, p = .172
- OS: main effect significant, p = .038

**Nonwords N400:**
- Complexity: β = −0.460, t(4854) = −7.48, p < .001
- **Complexity × Family Size × LP three-way: β = 0.227, t(4854) = 2.27, p = .023** ← CENTERPIECE FINDING
- Complexity × Family Size interaction:
  - Low LP: Δ = −0.667, p < .001 (large, significant)
  - Mean LP: Δ = −0.440, p = .0003 (attenuated, significant)
  - High LP: Δ = −0.213, p = .188 (absent)
- Family size effect within complex nonwords disappears at high LP
- Complexity × Base Frequency × LP three-way: NOT significant (confirms specificity — LP effect is about family richness not stem familiarity)
- Complexity × LP (averaged over FS): monotonic attenuation (unlike N250 reversal), significant at all LP levels

### The Double Dissociation — Confirmed

| | N250 (early form-based) | N400 (later semantic) |
|---|---|---|
| **Base Frequency × OS** | ✓ Significant | OS main effect only |
| **Base Frequency × LP** | LP not interacted | ✓ Significant |

For nonwords: both OS and LP modulate N250 (partial qualification of predicted dissociation); LP selectively drives N400 three-way.

---

## 6. RESULTS SECTION — CURRENT STATUS

### Written and Approved Paragraphs

**Words section:**
- ✓ Words RT — complete, verified against R output
- ✓ Words N250 (family size version) — complete
- ✓ Words N400 (family size version) — complete
- ✓ Words N250 (base frequency version) — drafted in final exchange
- ✓ Words N400 (base frequency version) — drafted in final exchange

**Nonwords section:**
- ✓ Nonwords RT — complete, verified against R output
- ✓ Nonwords N250 — complete with follow-up contrasts
- ✓ Nonwords N400 — complete with three-way follow-up contrasts

**Summary section:**
- ✓ Results Summary — drafted and approved, split so that the "three key findings" paragraph moves to open the Discussion

### Results Section Structure
```
\section{Results}
[Orienting paragraph]
[Table 1: Model summary]
[Asymmetric interaction explanation paragraph]

\subsection{Words}
  \paragraph{Words RT}
  \paragraph{Words N250}   ← base frequency version now primary
  \paragraph{Words N400}   ← base frequency version now primary

\subsection{Nonwords}
  \paragraph{Nonwords RT}
  \paragraph{Nonwords N250}
  \paragraph{Nonwords N400}

\subsection{Results Summary}
```

### Key Writing Decisions
- Words and nonwords reported separately (not by component)
- RT then ERP (N250 then N400) within each stimulus type
- No claim that "interactions were absent in RTs" since they were not tested — instead state models were specified for efficiency only
- ERP measures framed as "designed to detect" modulation that RT models were not designed to detect
- N250 direction for base frequency: high frequency = MORE negative (opposite to family size effect) — to be explained in Discussion
- Conditional R² values for ERP models are very high (0.738–0.825) due to large participant and electrode variance

---

## 7. OUTSTANDING ISSUES TO RESOLVE

### Critical (resolve before opening new chat)

1. ~~**Nonword N250 covariate**~~ — **RESOLVED:** Final model uses `family_size` as covariate.

2. **Integration of base frequency and family size analyses for words:** The words section now has two sets of ERP analyses — base frequency (primary, tests double dissociation) and family size (secondary). Need to decide:
   - Report base frequency as primary, family size as secondary/supplementary?
   - Or report both in full within the words section?
   - Recommended: base frequency primary in main text, family size results noted briefly or in supplementary

3. **N250 direction for base frequency:** High frequency bases → MORE negative N250 (opposite of family size effect). This dissociation between BF and FS at N250 needs a sentence in Discussion. Likely explanation: BF = strength of form-level activation (more effort); FS = efficiency of pattern matching (less effort).

### Important (address in new chat)

4. **Discussion — not yet started.** Structure agreed:
   - Opening: three key findings paragraph (moved from Results Summary)
   - Section 1: N250 reversal at high skill (most unexpected finding)
   - Section 2: Behavioral/ERP dissociation
   - Section 3: N400 three-way and semantic integration (connect to theoretical frameworks)
   - Closing: theoretical implications and limitations

5. **Updated model summary table:** Table 1 needs updating to reflect base frequency as primary predictor for words ERP analyses (currently shows family size)

6. **Results orienting paragraph:** Needs minor update to reflect that base frequency analyses are primary for words

7. **Nonword N400 base frequency analyses:** Null three-way (Complexity × BF × LP) should be reported as a cross-check confirming specificity of the family size finding — currently this is mentioned but not formally integrated into the results write-up

---

## 8. DISCUSSION — PLANNED STRUCTURE (not yet written)

### Opening Paragraph (moved from Results Summary)
The three key findings that structure the Discussion:
1. Individual differences dissociate from behavioral responses but visible in neural dynamics
2. LP selectively drives the N400 three-way (closest support for predicted dissociation)
3. N250 shows reversal at high skill; N400 shows attenuation without reversal — qualitatively different mechanisms

### Section 1: Early Morphological Parsing and the N250 Reversal
- Processing cost vs. morphological sensitivity interpretation
- Why the reversal indicates real suffix facilitates parsing for skilled readers
- Why both OS and LP converge on early processing — broad lexical experience, not just orthographic skill
- Marginal Family Size × OS for words — consistency with nonword pattern
- Connect to morpho-orthographic and discriminative learning accounts

### Section 2: The Behavioral/ERP Dissociation
- Individual differences invisible in RTs but visible in ERPs
- Implications for measuring individual differences in morphological processing
- Lexical Quality Hypothesis — precision of representation vs speed of response
- Why OS predicts nonword RT but not morphological modulation in ERPs

### Section 3: N400 Three-Way and Semantic Integration
- What Complexity × Family Size × LP means
- Attenuation without reversal — contrast with N250
- LP selective at N400; OS not — closest to predicted dissociation
- Connect to NDL/LDL: LP indexes depth of form-to-meaning mapping
- Connect to multi-stage accounts
- Null Family Size × LP for words — why LP does not modulate FS for familiar words
- Base Frequency × LP at N400 for words — LP enhances semantic integration benefit of high frequency stems

### Closing: Theoretical Implications and Limitations
- Partial dissociation — what it means
- Limitations: unmatched words, asymptotic CIs, generalisability
- Future directions

---

## 9. KEY TERMINOLOGY AND VARIABLE NAMES

| Concept | Variable name in R | Notes |
|---|---|---|
| Language Proficiency | `LP`, `Dim.1` | PCA dimension 1, already centered |
| Orthographic Sensitivity | `OS`, `Dim.2` | PCA dimension 2, already centered |
| Base/Stem Frequency | `zLogBF` (RT), `base_frequency` (ERP) | Continuous for RT, binned for ERP |
| Family Size | `zLogFS` (RT), `family_size` (ERP) | Continuous for RT, binned for ERP |
| Complexity | `complexity` | Factor: Simple vs Complex |
| Participant ID | `SubjID` | |
| Item ID | `Item` (words), `ItemID` (nonwords) | Note different names |
| ERP amplitude | `value` | |
| Electrode nested in participant | `SubjID:chlabel` | |
| Log RT | `logRT` | log(response_time) |

---

## 10. CITATIONS NEEDING COMPLETION

The following citations appear as [CITATION] placeholders throughout the manuscript:
- Baayen & Schreuder race model — original dual-route paper
- Rastle, Davis et al. — early automatic decomposition / masked priming papers
- Grainger et al. — morpho-orthographic account
- Baayen et al. NDL paper — 2011 Psychological Review
- Baayen et al. LDL paper — ~2019 Complexity journal
- Family size effects — original Schreuder & Baayen paper
- Stem frequency operationalisation — relevant citations
- Semantic transparency and family size — opacity studies
- N250 and N400 components — relevant ERP citations
- Andrews et al. (2013) — individual differences in morphological priming
- Perfetti — Lexical Quality Hypothesis (2002, 2007, 2017)
- Andrews and colleagues — lexical precision papers
- Marslen-Wilson, Tyler, Devlin — neuroimaging morphology papers

---

*Log created at end of extended working conversation. Open new chat in this project and paste this document as the first message to establish context before posting new R output.*
