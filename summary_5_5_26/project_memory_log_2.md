# Project Memory Log: Morphological Processing ERP Paper
## Conversation Summary and Continuity Document — Updated after Chat 3

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

---

## 2. CURRENT MANUSCRIPT STATUS

The manuscript is in advanced draft. The current working file is `m21_ldt_frontiers_updated.tex`. All sections are complete in draft form. The manuscript is being refined through targeted edits as citations are added.

### Title
*Reading skill and the time course of morphological processing: electrophysiological evidence for stage-specific modulation*

### Structure
```
\title
\abstract  ← revised this chat (see Section 4)
\section{Introduction}
  [Opening paragraphs]
  \subsection{Base Frequency and Family Size: Theoretical Interpretations}
  \subsection{Individual Differences in Morphological Processing}
  \subsection{Aims and Predictions}
\section{Methods}
\section{Results}
  [Orienting paragraph + Table 2 explanation paragraph]
  \subsection{Words}
    \paragraph*{Words RT}
    \paragraph*{Words N250: Base Frequency}   ← new this chat
    \paragraph*{Words N250: Family Size}
    \paragraph*{Words N400: Base Frequency}   ← new this chat
    \paragraph*{Words N400: Family Size}
  \subsection{Nonwords}
    \paragraph*{Nonwords RT}
    \paragraph*{Nonwords N250}
    \paragraph*{Nonwords N400}
  \subsection{Results Summary}
\section{Discussion}
  \subsection{Individual Differences Dissociate from Behavioral Responses...}
  \subsection{N250 Effects and the Partial Dissociation...}   ← revised this chat
  \subsection{N400 Effects and Language Proficiency...}
  \subsection{Theoretical Implications, Limitations, and Conclusion}  ← consolidated this chat
```

---

## 3. WORK COMPLETED THIS CHAT

### 3.1 New Results Sections Integrated
Two new word ERP sections were written and integrated, completing the words results section:

**Words N250: Base Frequency** (model: `m_w_N250_bf`)
- Main effect of base frequency: β = −0.318, SE = 0.100, t(1618) = −3.18, p = .002 — high-frequency bases → more negative N250
- **Base Frequency × OS interaction: β = −0.455, SE = 0.112, t(1618) = −4.06, p < .001, η²p = .010** ← key finding
- OS and LP main effects: both ns
- R²marginal = .018, R²conditional = .801

**Words N400: Base Frequency** (model: `m_w_N400_bf`)
- Main effect of base frequency: β = 0.214, SE = 0.106, t(1618) = 2.01, p = .044 — high-frequency bases → more positive N400 (facilitation)
- OS main effect: β = 1.290, SE = 0.640, t(57) = 2.02, p = .049 — consistent with FS model
- LP main effect: ns
- **Base Frequency × LP interaction: β = 0.344, SE = 0.087, t(1618) = 3.98, p < .001, η²p = .010** ← key finding
- R²marginal = .026, R²conditional = .825

### 3.2 LaTeX Compilation Errors Fixed
- **Fatal error:** `\bottomrule` undefined — fixed by adding `\usepackage{booktabs}` as a separate line in the preamble (the original booktabs was inside a fully commented-out `\usepackage` line)
- **Overfull/underfull hboxes:** New 6-column Table 2 was overflowing — fixed by adding `\small`, rewriting random effects column in plain text (`Subj, Elec/Subj`), and rebalancing column widths
- **PCA table (Table 1) header overflow:** Fixed using `\shortstack{Dimension~1 \\ (Language Proficiency)}` — no extra package needed

### 3.3 Table Cross-Referencing
- Table 2 (model summary) given label `\label{tab:models}`
- All three hard-coded `Table~1` references in the text replaced with `Table~\ref{tab:models}`
- Table 1 (PCA) already had `\label{tab:pca_loadings}` and `\ref{tab:pca_loadings}` in place

### 3.4 Discussion Revisions
Two structural changes:

**N250 section opening rewritten** with stronger framing that leads with the reversal finding:
> *"The most striking finding at the N250 was not the presence of a complexity effect — which is predicted by all current accounts — but its reversal at high levels of both Orthographic Sensitivity and Language Proficiency..."*
The word-level results (BF×OS, FS×OS) are then introduced as a second paragraph with "For real words, the results additionally provided support…"

**Three closing subsections collapsed into one:** "Theoretical Implications," "Limitations and Future Directions," and "Conclusion" merged into a single `\subsection{Theoretical Implications, Limitations, and Conclusion}`. The reversal discussion was moved to the front of this section as the most theory-constraining finding.

### 3.5 Introduction Revisions

**Motivation added for LP modulating nonword N250.** The nonword prediction paragraph in Aims and Predictions was extended with three sentences arguing that without a stored whole-word entry, the early parse must run entirely on distributional knowledge; and that on discriminative learning accounts, suffix recognisability is learned because it predicts morphological family membership, meaning LP's contribution to morphological vocabulary breadth bleeds into the form-level stage for novel items. This positions the LP×N250 convergence finding as a predicted (if secondary) possibility.

**Methods sentence updated** to reference the introduction rather than asserting the motivation independently: *"reflecting the prediction, developed in the Aims and Predictions section, that Language Proficiency may contribute to early N250 processing of novel forms alongside Orthographic Sensitivity."*

**Paragraph 3 bridging sentence added:**
> *"Characterising how readers differ in their sensitivity to base frequency and family size, however, first requires clarity about what these variables actually measure — a question that has proven theoretically contentious, because the answer depends on the architecture one ascribes to the word recognition system."*

**BF/FS distinction stated immediately** after "different levels of morphological representation" — expanded via colon structure to explain that base frequency indexes form-based access while family size indexes richness of semantic representation, so the dissociation is immediately clear before the next sentence exploits it.

**Statistical learning → representational differences → BF/FS sensitivity chain** expanded from one sentence into two:
> *"If morphological sensitivity reflects the accumulated product of statistical learning, then readers with more extensive print exposure will have acquired both more precise orthographic representations of base morphemes and richer semantic networks connecting them to their morphological relatives. Because base frequency indexes the strength of the form-level mapping and family size indexes the richness of the semantic one, readers who differ in the precision of their orthographic knowledge versus the breadth of their semantic knowledge should differ selectively in their sensitivity to each variable — and, if form-based and semantic processing are temporally dissociable, those differences should emerge at distinct stages in the processing cascade."*

**Semicolon note (pending):** The lead-in sentence before this passage ends with a semicolon introducing what are now two full sentences. User may want to change it to a period or colon.

### 3.6 Abstract Revised
Full rewrite prioritising: (a) naming both OS and LP explicitly in the ERP results; (b) making the double dissociation the headline finding; (c) compressing methods; (d) splitting theoretical and methodological implications into separate final sentences. Also fixed typo "efficienct."

### 3.7 Terminology Standardised
- "stem frequency" → "base frequency" throughout, via global find-and-replace
- One instance of "stem familiarity" in the N400 results paragraph also corrected

### 3.8 Citation Work
- `\citep{CITATION}` for the independence claim replaced with `\citep{fordDerivationalMorphologyBase2010}`
- **Ford et al. (2010) nuance to be aware of:** base frequency facilitation is conditional on suffix productivity; family size effect is productivity-independent. Reviewer may flag this.
- `\citep{schreuderHowComplexSimplex1997}` verified as appropriate for the family size facilitates lexical decision claim (founding family size paper), but **not** appropriate for the independence-of-BF-and-FS claim — Ford et al. is correct for that
- Six citation sets added to opening paragraphs of introduction (see Section 3.9)

### 3.9 Citations Added to Introduction Opening Paragraphs
| Location | Citation keys added |
|---|---|
| "readers vary considerably" | `perfettiReadingAbilityLexical2007, castlesHowDoesOrthographic2006, stanovichExposurePrintOrthographic1989` |
| "central to this goal" | `taftMorphologicalDecompositionReverse2004, taftRecognitionAffixedWords1979, dejongMorphologicalFamilySize2000, bertramEffectsFamilySize2000` |
| "when a morphological base is encountered" | `schreuderHowComplexSimplex1997` |
| "insufficient basis for fluent word recognition" | `zieglerReadingAcquisitionDevelopmental2005, castlesHowDoesOrthographic2006` |
| "deeply and precisely that structure is represented" | `bryantMorphologySpellingWhat2005, arciuliReadingStatisticalLearning2018, treimanStatisticalLearningSpelling2018` |
| Independence of BF and FS | `fordDerivationalMorphologyBase2010` |

---

## 4. PENDING DECISIONS AND OUTSTANDING ISSUES

### Immediate (addressed but not yet integrated)
1. **Collapse early automatic decomposition and morpho-orthographic accounts** — agreed in principle this chat. Draft replacement text ready (see below). Awaiting integration into file.

*Proposed collapsed text:*
> *Early automatic decomposition accounts \citep{CITATION} reconceptualize this dissociation in temporal rather than architectural terms: decomposition is not one route among several but an obligatory initial parsing step that precedes semantic access. On the morpho-orthographic formulation of this view \citep{CITATION}, an intermediate level of representation mediates between sublexical letter clusters and whole-word forms, and base frequency reflects the strength of activation at this level. Family size effects are then attributed to a later, semantically sensitive stage, consistent with the finding that opaque relatives contribute less to the family size effect than transparent ones \citep{CITATION}.*

Citation keys needed: Taft for early decomposition; Rastle/Davis for morpho-orthographic formulation; opacity/family size citation (likely Schreuder & Baayen 1997 or Baayen et al.)

2. **Semicolon → period/colon** in the lead-in to the statistical learning passage (paragraph 3 of introduction). Currently reads: "...differ in their predictions about individual differences; If morphological sensitivity reflects..." — should be a period or colon.

### Ongoing
3. **Remaining \citep{CITATION} placeholders** throughout the manuscript — being filled in progressively as citations are verified
4. **Methods section** — not reviewed this chat; may need checking once citation work is complete
5. **Figures** — not yet created/referenced
6. **Final proofread** — some Frontiers template boilerplate (figures/tables instructions) still present after Discussion; to be removed before submission

---

## 5. KEY RESULTS SUMMARY (unchanged from previous log)

### Double Dissociation — Confirmed

| | N250 (early form-based) | N400 (later semantic) |
|---|---|---|
| **Base Frequency × OS** | ✓ Significant (words) | OS main effect only |
| **Base Frequency × LP** | LP not interacted | ✓ Significant (words) |
| **Nonwords** | Both OS and LP modulate complexity effect (reversal at high skill) | Complexity × FS × LP three-way (LP selective) |

### Key Effect Sizes and Statistics
*(Full statistics in previous log — Section 5; unchanged)*

---

## 6. KEY TERMINOLOGY AND VARIABLE NAMES (unchanged)

| Concept | Variable name in R | Notes |
|---|---|---|
| Language Proficiency | `LP`, `Dim.1` | PCA dimension 1, already centered |
| Orthographic Sensitivity | `OS`, `Dim.2` | PCA dimension 2, already centered |
| Base Frequency | `zLogBF` (RT), `base_frequency` (ERP) | "base frequency" now used exclusively throughout |
| Family Size | `zLogFS` (RT), `family_size` (ERP) | |
| Complexity | `complexity` | Factor: Simple vs Complex |
| ERP amplitude | `value` | |
| Electrode nested in participant | `SubjID:chlabel` | |

---

## 7. WORKING PRINCIPLES (accumulated across chats)

- Claude's manual character counting is unreliable; tool-based verification required for length-constrained drafts
- Theoretical claims in results sections should be restricted to what the data directly support
- Statistical reporting must match R output exactly — sign, rounding, CIs, variable names
- One change at a time is preferred for structural edits; independent changes can be batched
- Paste exact current text when requesting edits to specific passages
- Corrections and pushback from the user should be treated as authoritative
- Before citing a paper, verify it actually supports the specific claim being made

---

*Log updated at end of Chat 3. Open new chat in this project and paste this document to establish context.*
