REVISED ANALYTIC STRUCTURE JULY 20267

A paper that makes a genuinely new theoretical claim about the mechanistic distinction between OS and LP in morphological parsing is more valuable and more cited than a cleaner but less ambitious paper. The extra time is worth it.

So the decision is: **keep the word data, pursue Option B.**

This means the paper's theoretical structure becomes:

**The word data establish the baseline:**
- Base frequency × OS at N250 — OS is sensitive to stem-level orthographic frequency information in familiar word recognition
- Family size × LP at N400 — LP modulates semantic integration of morphological family information for familiar words

**The nonword data extend and deepen the story:**
- Complexity × OS and Complexity × LP at N250 — in novel form processing, OS drives affix-led parsing while LP drives stem-led parsing; the contrast with the word data shows that OS operates at the affix level specifically when no whole-word representation is available
- Complexity × Family Size × LP at N400 — LP selectively modulates how family richness is recruited during semantic integration of novel forms

**The dissociation argument then has two levels:**
- Within words: OS at N250, LP at N400
- Within nonwords: OS and LP dissociate mechanistically at N250; LP selectively drives N400 three-way

This is a richer and more precise contribution than either dataset alone could support.

Good. Let me lay out each question clearly and work through them one at a time.

---

**Question 1: Should the word models also be symmetric — testing both OS and LP at both N250 and N400?**

For nonwords, the symmetric design was necessary because the dissociation claim requires showing that OS and LP produce different patterns at both time windows within the same dataset. For words, the situation is different — the word data are not the primary test of the dissociation but rather the theoretical anchor establishing what OS and LP do with familiar forms. The asymmetric word models — base frequency × OS at N250, family size × LP at N400 — are sufficient for that purpose.

However, by the same logic that led us to run symmetric nonword models, a reviewer could ask: did you test OS at the word N400 and LP at the word N250? You have already run these exploratorily and have the output. The question is whether they should be part of the primary analysis or reported as supporting evidence.

My recommendation: **keep the word models asymmetric as primary analyses, but report the symmetric exploratory models as supporting evidence for the dissociation.** This avoids doubling the number of primary word models while still addressing the reviewer concern.



**Question 2: Should base frequency be a primary predictor in the nonword N250 model, tested in interaction with OS and LP?**

If base frequency is an orthographic variable that recruits morpho-orthographic parsing and OS indexes sensitivity to that information, then base frequency should interact with OS at the nonword N250, just as it does for words.

The counterargument is that for nonwords, the primary manipulation is complexity — the presence of a real versus pseudoaffix. Base frequency is a stem property held constant across complexity conditions, so its role at the nonword N250 is fundamentally different from its role in the word N250 model where it is the primary morphological contrast.

There are two options:

**Option 2a — Add base frequency × OS and base frequency × LP to the nonword N250 model:**
```r
m_nw_N250_full <- lmer(
  value ~ complexity * OS + complexity * LP +
          base_frequency * OS + base_frequency * LP +
          family_size +
    (1 | SubjID) + (1 | SubjID:chlabel),
  data = subset(erp_nw, time_window == "N250"),
  control = lmerControl(optimizer = "bobyqa")
)
```
This tests whether base frequency modulates OS and LP effects at the nonword N250, paralleling the word model. The cost is a more complex model.

**Option 2b — Keep base frequency as a nuisance covariate but acknowledge the theoretical tension in the Discussion:**
The nonword N250 model remains as currently specified, and the Discussion notes that the theoretical parallel between word and nonword N250 models suggests base frequency warrants further investigation in novel form processing.

My recommendation: **Option 2b for now.** The nonword N250 model is already producing clean, theoretically interpretable results. Adding base frequency interactions risks complicating the model without clear theoretical payoff — the complexity manipulation is doing the primary theoretical work in the nonword N250, not base frequency. The theoretical tension can be acknowledged as a limitation and future direction.


**Question 3: For the nonword N400, does the symmetric model we just ran replace the separate LP and OS models, or do all three get reported?**

The symmetric model is the cleanest solution — it tests both dimensions in the same model and provides the strongest evidence for the dissociation. The separate models are now superseded.

My recommendation: **report only the symmetric nonword N400 model as the primary analysis.** The separate LP and OS models can be noted as preliminary analyses that motivated the symmetric model, but do not need to be reported in full.

---

**Summary of recommended analytic structure:**

| | Words | Nonwords |
|---|---|---|
| **RT** | BF + FS + OS + LP | Complexity + BF + FS + OS + LP |
| **N250** | BF × OS + LP (primary); FS × OS + LP (secondary) | Complexity × OS + Complexity × LP + FS covariate |
| **N400** | FS × LP + OS (primary); BF × LP + OS (secondary) | Complexity × FS × LP + Complexity × FS × OS (symmetric) |
