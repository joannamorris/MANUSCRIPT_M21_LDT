# N250 Word Data

1. For the N250 word data,  As OS increases the N250 amplitude decreases, and the decrease is steeper for low base frequency words that for high ones.    Ultimately, the high OS participants there is a greater N250 for high base frequency words than for low.  This is difficult to explain if base frequency helps processing and the N250 is a measure of processing difficulty.

	- **High base frequency** means the orthographic form occurs frequently across many surface forms (*walked*, *walking*, *walks*, *walker*), but the form itself is not consistently paired with a single meaning — it abstracts across all of them. Frequency here is a property of the form level, and whatever processing benefit it confers is purely orthographic or sublexical.

	- **High morphological family size** means the base form is consistently paired with a coherent semantic core across many derived words — the meaning of *walk* is preserved and active across the whole family. Repeated co-occurrence of a stable form with a stable meaning produces stronger form-to-meaning mappings, and feedback from semantics to the form level could make the form more readily identified when encountered.

	- Under this account, the N250 direction difference is theoretically interpretable: large family size reduces N250 amplitude because semantic feedback stabilises and facilitates form-level identification, whereas high base frequency increases N250 amplitude because stronger orthographic activation drives more effortful morpho-orthographic parsing without the benefit of semantic reinforcement.

	- This would also connect naturally to the OS × base frequency interaction at N250: high OS readers are more sensitive to sublexical orthographic structure and therefore show the strongest engagement with high-frequency bases, precisely because they are processing at the form level where base frequency has its effect — without semantic feedback to facilitate recognition.

1. "high base frequency increases N250 amplitude because stronger orthographic activation drives more effortful morpho-orthographic parsing"  Why?

	- You are right to challenge that — the claim was poorly reasoned. If high base frequency means the form is frequently encountered and therefore well-represented, one would expect *more fluent* processing, not more effortful. The appeal to "stronger orthographic activation" does not actually explain why N250 amplitude would be *greater*.

	- The honest answer is that the direction of the base frequency effect at the N250 is genuinely puzzling on its own terms, and I do not think there is a clean mechanistic explanation for it in isolation. The stronger theoretical move is the contrastive one — the fact that base frequency and family size pull in *opposite* directions at the N250, which is explained by the presence or absence of semantic reinforcement of the form:

		- Family size reduces N250 amplitude because consistent form-meaning pairing produces semantic feedback that facilitates form-level identification
		- Base frequency does not carry that semantic reinforcement, so whatever form-level activation it produces does not benefit from that feedback

	- The implication would be that the N250 direction difference is the key finding, and the explanation lies in the *absence* of semantic feedback for base frequency rather than in any positive mechanistic account of why high frequency increases amplitude. You would be making a theoretically motivated prediction about direction based on the form/meaning distinction, rather than claiming to know the precise processing mechanism underlying the base frequency direction alone.


# N400 Word Data

1. In the N400 window, as LP increases the N400 decreases for high base frequency words but increases for low base frequency words resulting in a cross-over interaction in which low LP participants have a greater N400 for high base frequency words (although contrasts indicate that this is not significant at LP = -1)  while high LP participants have a higher N400 for low base frequency words (signficant at LP = 1).

	- This pattern is the semantic-integration analogue of what you found at the N250, and the same form/meaning distinction can anchor the explanation — but the direction of dependency is reversed in a theoretically meaningful way.

	- At the N250, base frequency mattered most for **high OS** readers — those most sensitive to orthographic form. At the N400, base frequency's influence depends on **LP**, but here the story is about how readers use a purely form-level statistic during semantic integration, where it has no inherent semantic warrant.

	- One way to frame it: base frequency carries no consistent meaning information, so its relevance at the semantic integration stage is, in principle, ambiguous — a high base frequency form has been encountered often, but not in service of one stable meaning. Low LP readers, with less differentiated lexical-semantic representations, do not show a reliable difference between high and low frequency bases at this stage (consistent with the non-significant contrast at LP = −1) — they integrate form-level frequency information into semantic processing only weakly or inconsistently.

	- High LP readers, by contrast, have more precise and differentiated lexical-semantic representations (in Lexical Quality Hypothesis terms), and this precision extends to *using* base frequency information during integration — but because base frequency is not meaning-consistent, its influence shows up as a cost for low-frequency bases (less entrenched forms create more integration difficulty for these sensitive readers) and a benefit for high-frequency bases (well-entrenched forms integrate more easily). The result is that proficiency increases sensitivity to this form-level statistic rather than uniformly facilitating processing.

	- This framing treats the crossover not as two independently meaningful slopes pulling in opposite directions, but as a single underlying phenomenon: **higher LP confers greater differentiation in how form-level frequency is weighted during semantic integration**, and that differentiation happens to manifest as opposite-signed trends at the two ends of the base frequency continuum. This also gives you a principled reason to lean on the ±1 SD contrasts (where the asymmetry in significance is informative) rather than treating both slopes as independently established effects, which is consistent with what your `emtrends` results already showed.
