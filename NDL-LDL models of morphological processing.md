HTML header: <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>


# NDL/LDL models of Morphological Processing

Linear algebra is a branch of mathematics concerned with **vectors, matrices, and linear transformations**, and the rules governing how these objects combine and interact. It provides a formal language for representing and manipulating structured numerical data.

At a more technical level, linear algebra studies **vector spaces**—collections of objects (vectors) that can be added together and scaled by numbers—and **linear mappings** between those spaces. A mapping is “linear” if it preserves addition and scalar multiplication. This constraint gives the field its structure and tractability.

A concrete way to understand it is through systems of equations. For example, a set of linear equations like:

* $2x + y = 5$
* $x − y = 1$

can be rewritten compactly as a **matrix equation**:

\\[
A \mathbf{x} = \mathbf{b}
\\]

where $A$ is a matrix of coefficients, $\mathbf{x}$ is a vector of unknowns, and $\mathbf{b}$ is a vector of outcomes. Linear algebra provides the tools to analyze when such systems have solutions, whether those solutions are unique, and how to compute them efficiently.

In applied contexts—such as regression, signal processing, or machine learning—the key objects are:

* **Vectors**: ordered lists of numbers (e.g., a participant’s responses, a word embedding, a time series)
* **Matrices**: rectangular arrays representing datasets or transformations
* **Linear transformations**: operations that map vectors to new vectors via matrix multiplication

Ordinary least squares (OLS) regression, which your quote refers to, is fundamentally a linear algebra problem. You are finding a vector of coefficients $ \boldsymbol{\beta} $ such that:

\\[
X \boldsymbol{\beta} \approx \mathbf{y}
\\]

where $X$ is a matrix of predictors and $\mathbf{y}$ is an outcome vector. The solution is derived using matrix operations (e.g., transposes and inverses), not iterative nonlinear optimization as in most neural networks.

The reason this matters for the claim you quoted is that linear algebra imposes **strict linearity constraints**: outputs are weighted sums of inputs. Neural networks, by contrast, introduce **nonlinear activation functions**, allowing them to represent far more complex mappings. So describing LDL as “closer to multivariate linear regression” is essentially saying it operates within this linear algebraic framework rather than a nonlinear function-approximation regime.

If you want, I can unpack how LDL specifically fits into this framework mathematically.

---

If LDL is being described as “ordinary least squares between vector spaces,” then mathematically it can be made quite explicit. The core idea is that you are learning a **linear map** from one representational space to another.

Start with two spaces:

* an input space $\mathbb{R}^p$ (e.g., form-based features: orthography, phonology, cues)
* an output space $\mathbb{R}^q$ (e.g., semantic features, meanings, distributions)

Each observation is a pair:
\\[
(\mathbf{x}_i, \mathbf{y}_i)
\\]
where $\mathbf{x}_i \in \mathbb{R}^p$ and $\mathbf{y}_i \in \mathbb{R}^q$.

Stack these into matrices:

* $X \in \mathbb{R}^{n \times p}$: rows are input vectors
* $Y \in \mathbb{R}^{n \times q}$: rows are output vectors

The LDL objective is to find a **weight matrix**:
\\[
W \in \mathbb{R}^{p \times q}
\\]
such that:
\\[
X W \approx Y
\\]

This is exactly a **multivariate linear regression** problem. Each column of $Y$ is being predicted from the same predictors $X$, and the solution is obtained in closed form via ordinary least squares:

$W = (X^T X)^{-1} X^T Y$

This equation is doing several things simultaneously:

* $X^T X$: computes the covariance structure of the predictors
* $(X^T X)^{-1}$: rescales to account for correlations among predictors
* $X^T Y$: computes cross-covariance between predictors and outcomes
* The product yields the **best linear mapping** (in the least-squares sense)

Once $W$ is learned, prediction is straightforward:

\\[
\hat{\mathbf{y}} = \mathbf{x} W
\\]

So for any new input vector, you generate an output by a **weighted sum of its features**, where the weights are learned globally across the dataset.

There are a few implications worth making explicit:

First, this is a **single-layer linear transformation**. There are no hidden layers, no nonlinearities, and no compositional depth. The geometry is entirely governed by linear operations.

Second, the model is **deterministic and convex**. The solution above is the global optimum; there is no dependence on initialization or stochastic training dynamics.

Third, all structure comes from the **geometry of the spaces themselves** (how $X$ and $Y$ are encoded) and from their covariance. In that sense, LDL is less about “learning features” and more about **aligning two representational systems** via a linear map.

This is why the comparison to neural networks is limited. A standard feedforward network would instead learn something like:

\\[
\hat{\mathbf{y}} = \sigma(X W_1) W_2
\\]

where $\sigma(\cdot)$ is a nonlinear activation. That nonlinearity fundamentally changes the class of functions that can be represented. LDL never leaves the space of linear mappings.

If you want to push this further, the interesting theoretical question is: what kinds of linguistic or cognitive structure can be captured purely through this linear alignment, and where does it break down?

---

# What does 'the model is deterministic and convex." mean?

Those two terms are making precise claims about the **optimization problem** underlying the model.

**Deterministic** means that, given the same input data $X, Y$, the model will always return the *same* solution $W$. There is no randomness in the procedure—no random initialization, no stochastic gradient descent, no dependence on training order. The weights are computed directly from the data via a fixed algebraic expression. If you rerun the analysis, you recover identical coefficients (up to numerical precision).

In contrast, many neural network training procedures are *stochastic*: they involve random initial weights and randomized minibatches, so different runs can converge to slightly different solutions.

---

**Convex** refers to the *shape of the objective function* being optimized. In LDL / OLS, the goal is to minimize squared error:

$\min_W |XW - Y|^2$

This objective is a **convex function** of $W$. Formally, convexity means:

* The error surface has a single global minimum
* There are no local minima that can trap the solution
* Any optimization method (or the closed-form solution) will reach the same best answer

Geometrically, you can think of it as a smooth “bowl-shaped” surface. There is one lowest point, and everything slopes down toward it.

---

Putting the two together:

* *Deterministic*: the algorithm doesn’t inject randomness
* *Convex*: the problem itself guarantees a unique optimal solution

So LDL/OLS has a very strong property: **there is one best linear mapping, and you can compute it directly and reproducibly**.

This is in sharp contrast to most neural networks, where:

* the loss function is **non-convex** (many local minima and flat regions)
* training is **stochastic** (different runs can yield different parameter settings)

That difference is what underlies the claim that LDL behaves more like classical linear regression than like a neural architecture.

---

# what kinds of linguistic or cognitive structure can be captured purely through this linear alignment, and where does it break down?

The short answer is that linear alignment can capture **graded, distributed, and approximately additive structure** in language, but it breaks when the target relationship depends on **nonlinear interactions, discrete structure, or context-dependent transformations**.

---

### What linear alignment *can* capture well

**1. Graded similarity structure (semantic geometry)**
If meanings are encoded as vectors where similarity is reflected in distance (e.g., distributional semantics), a linear map can preserve and exploit that geometry.

* Words with similar meanings cluster in $Y$
* Similar forms or cues cluster in $X$
* A linear map aligns these spaces so that neighborhoods correspond

This is why LDL often works well for **mapping form → meaning** in a coarse-grained way: it preserves **relative structure**, not just pointwise mappings.

---

**2. Additive compositional effects**
Linear models assume that contributions combine additively. This is a strong but useful assumption.

Examples that fit this well:

* Morphological cues contributing independently (e.g., stem + suffix each shift meaning)
* Frequency, neighborhood density, or familiarity effects in processing
* ERP amplitudes modeled as sums of factor contributions (which is essentially what your LMMs assume)

Formally, this corresponds to:
\\[
\mathbf{y} = \sum_j x_j \mathbf{w}_j
\\]
Each feature contributes a weighted component; the total is just their sum.

---

**3. Cue integration and probabilistic structure**
If linguistic knowledge is approximated by **correlation structure**—which cues co-occur with which meanings—linear regression captures this directly via covariance.

This aligns well with:

* Distributional learning
* Statistical learning paradigms (including your visual SL work)
* Gradual sensitivity effects that do not require categorical decisions

---

**4. Global mappings between representational spaces**
LDL is particularly strong when the task is:

> “Find the best overall alignment between two high-dimensional systems.”

This includes:

* Orthography → semantics
* Form → lexical meaning
* Surface cues → latent representations

The key is that the mapping is **consistent across the space**.

---

### Where linear alignment breaks down

**1. Nonlinear interactions (feature dependencies)**
If the effect of one feature depends on another, linear models fail.

Example:

* The meaning of a suffix depends on the stem it attaches to (true compositional semantics)
* Ambiguity resolution where context *modulates* interpretation

These require terms like:
\\[
x_1 \times x_2
\\]
or more complex nonlinear transformations. Linear models cannot represent this unless you manually engineer interaction terms.

---

**2. Hierarchical and structured representations**
Language is not just a flat feature space—it has **hierarchical syntax and compositional semantics**.

Linear mappings cannot inherently represent:

* Nested structure (e.g., recursive syntax)
* Scope relations
* Binding dependencies (e.g., pronoun resolution in your “they” work)

These require representations where **structure matters**, not just vector position.

---

**3. Context-sensitive interpretation**
Many linguistic phenomena depend on *context-dependent reweighting*:

* “bank” (river vs financial) depends on surrounding words
* Pronoun interpretation depends on discourse context and referential constraints
* Prediction in sentence processing depends on dynamically updated expectations

A single fixed matrix $W$ cannot adapt its mapping based on context unless context is explicitly encoded as additional features—and even then, only linearly.

---

**4. Categorical or rule-like behavior**
Some phenomena are effectively **thresholded or discrete**:

* Grammatical vs ungrammatical judgments
* Agreement violations (often eliciting P600 effects)
* Rule-based transformations (e.g., syntactic movement)

Linear models produce continuous outputs; they do not naturally implement **decision boundaries with sharp transitions** unless you add external thresholding.

---

**5. Representational warping**
Neural networks succeed partly because they **reshape the geometry** of the input space via nonlinear layers. Linear models cannot do this.

They can only:

* rotate
* scale
* shear

They cannot:

* “bend” the space to separate overlapping categories
* create new feature dimensions through nonlinear combinations

---

### Framing it in your domain (ERP / psycholinguistics)

There is a useful alignment here:

* Linear models (LDL, LMMs) are well-suited to capturing **graded sensitivity effects**—exactly the kind you see in N400 amplitude modulations or statistical learning without explicit awareness.

* They struggle with phenomena that elicit **categorical reanalysis or repair**—more in line with P600-type effects or discrete grammatical violations.

So a reasonable interpretation is:

* **N400-like effects**: often compatible with linear, distributional, similarity-based structure
* **P600-like effects**: more likely to reflect processes that require nonlinear, rule-like, or structure-sensitive computations

---

### Bottom line

Linear alignment works when:

* structure is **distributed, continuous, and additive**
* relationships are **stable across the space**
* learning reduces to **capturing covariance**

It breaks when:

* structure is **interactive, hierarchical, or context-dependent**
* interpretation requires **nonlinear transformations or discrete decisions**

This is not a limitation in a trivial sense—it’s a very specific hypothesis about what aspects of cognition are fundamentally **linear vs nonlinear**. In your work, that distinction maps quite naturally onto different ERP components and processing stages.

---

# The State of Morphological Processing Models: Beyond Baayen-Schreuder and Caramazza

The short answer is that those models are foundational but no longer state of the art. The field has moved substantially, and interestingly, Baayen himself has moved furthest from his own earlier framework. Here is a structured overview of where things stand.

---

### What Happened to the Classical Models

**Caramazza's Augmented Addressed Morphology** has largely been absorbed into the broader visual word recognition literature rather than developed as a standalone framework. Its core insight — that whole-form and decomposed routes compete — survives, but the specific architecture has been superseded by more computationally explicit models.

**Baayen & Schreuder's race model** was explicitly a probabilistic competition between a whole-form lookup route and a decompositional route, with stem frequency and family size as diagnostics of each. Baayen himself came to see this as insufficiently mechanistic and has moved dramatically away from it.

---

### Major Subsequent Developments

#### 1. The Early Automatic Decomposition View (Rastle, Davis, and colleagues)

This is arguably the most influential empirical development of the 2000s–2010s. Using **masked morphological priming**, Rastle, Davis, Marslen-Wilson, and others showed that:

- Morphological decomposition occurs **extremely early** in processing — within the first ~150ms — and is **obligatory and form-based**, not contingent on semantic transparency.
- Crucially, *pseudo-morphological* primes like *corner* → *corn* produce early priming just like truly morphological pairs, suggesting the initial parse is **purely structural**, stripping apparent affixes regardless of meaning.
- A **second, semantic stage** then filters out spurious decompositions, so the early form-based effect is modulated by meaning at a later point.

This two-stage account — early blind decomposition followed by semantic evaluation — is importantly different from a race model, because it is **serial and asymmetric** rather than parallel and competitive. It is compatible with neuroimaging work (particularly MEG and EEG) by Marslen-Wilson, Tyler, Devlin and colleagues showing left inferior frontal and posterior temporal contributions at distinct latencies.

#### 2. Naïve Discriminative Learning (NDL) — Baayen, Milin, and colleagues

This represents a genuine paradigm shift. Around 2011–2016, Baayen and collaborators applied **error-driven (Rescorla-Wagner) learning** to the lexicon. NDL abandons the notion of discrete morpheme representations entirely. Instead:

- The input consists of **cues** (letter or phoneme n-grams, or whole-word forms) and the **outcomes** are meanings or lexical concepts.
- Connection weights between cues and outcomes are adjusted through a learning algorithm, without any symbolic decomposition.
- Frequency effects, family size effects, and paradigmatic effects all emerge from the **weight structure** learned over the distribution of the language — they are not built-in architectural features.

This model is significant because it shows that many classical morphological effects can be **epiphenomena of distributional learning** rather than evidence for a dedicated morphological parser. It explicitly challenges the idea that morphemes are stored or accessed as discrete units.

#### 3. The Discriminative Lexicon (Baayen, Chuang, Heitmeier, Blevins — ~2019 onward)

This is the most recent and ambitious development from Baayen's group, and represents a further radicalization of the NDL approach using **linear discriminative learning (LDL)**:

- Form-to-meaning and meaning-to-form mappings are modeled as **linear transformations between vector spaces** — essentially large matrices learned from corpus data.
- There are no morphemes, no rules, no decomposition: the system maps form vectors directly onto semantic vectors and vice versa.
- Inflectional paradigms, derivational families, and phonological form all fall out of the geometry of these learned spaces.
- This connects directly to **Word and Paradigm morphology** (Blevins) and to distributional semantics, treating the lexicon as fundamentally a system of **analogical, implicative relationships** rather than a rule-governed combinatorial system.

The Discriminative Lexicon is computationally explicit and makes quantitative predictions about processing difficulty that have been validated against lexical decision and other behavioral data.

#### 4. Morphological Processing in Visual Word Recognition Models

Computational models of reading have increasingly incorporated morphological structure:

- **CDP++ (Perry, Ziegler, Zorzi)** and related dual-route cascade models have been extended to handle morphological regularity.
- **Grainger and colleagues** have proposed that morphological units are active at an intermediate **morpho-orthographic** level of representation, between sublexical letter clusters and whole-word form representations — a level that is accessed before semantics and that explains early masked priming effects.
- This morpho-orthographic hypothesis is distinct from both classical decomposition models and from NDL: it is a **representational** level in a localist or semi-distributed network.

#### 5. Distributional and Semantic Vector Space Approaches

Researchers have used distributional semantic models (LSA, word2vec, and more recently transformer-based embeddings) to:

- Quantify **semantic transparency** of morphological relationships more precisely than binary judgments allow.
- Show that family size effects are modulated by the **mean semantic similarity** of family members to the base — a richer, more coherent family helps more than a large but semantically scattered one (work by Lazaridou, Marelli, Crepaldi, and others).
- Model the **graded** nature of morphological relatedness rather than treating it as categorical.

#### 6. Paradigm-Based and Whole-Word Approaches

Connecting to theoretical morphology, **Hay and Baayen's** work on **parsing ratios** (the probability that an encountered word will be parsed vs. accessed whole) and **Blevins' implicative structure** of paradigms have pushed processing models toward a more **exemplar-based or analogical** view, where the unit of storage is closer to the inflected word form than to the abstract morpheme.

---

### Where the Field Currently Stands

| Framework | Key Claim | Status |
|---|---|---|
| Caramazza AAM | Whole-form + decomposition routes | Historically influential, largely superseded |
| Baayen-Schreuder Race Model | Parallel competition; stem freq & family size index separate routes | Foundational but replaced even by Baayen himself |
| Rastle-Davis Early Decomposition | Obligatory early form-based parse, then semantic filter | Very influential; widely accepted for visual processing |
| NDL / LDL (Baayen et al.) | No morphemes; distributional cue-outcome learning | Major active framework; growing empirical support |
| Morpho-orthographic (Grainger) | Dedicated intermediate morpho-orthographic level | Strong empirical base; integrated into visual word recognition |
| Distributional/Semantic approaches | Graded semantic transparency modulates family effects | Increasingly mainstream; complements other models |

---

### The Deeper Conceptual Shift

What is most striking about the post-2010 landscape is a move **away from the morpheme as the fundamental processing unit**. Both the discriminative learning tradition and the whole-word/paradigm tradition converge on skepticism toward the classical picture in which morphemes are stored, retrieved, and concatenated. Instead, morphological effects increasingly look like **emergent consequences of statistical regularities** in the form-meaning space of the language, learned incrementally and reflected in graded, probabilistic processing behavior.

This does not mean that decomposition is an illusion — the early masked priming evidence for it is robust — but it does mean that the *interpretation* of what decomposition is (accessing stored morpheme entries vs. propagating activation through a learned weight space) is genuinely contested in a way it was not in the Baayen-Schreuder era.

---

# How NDL and LDL Explain Stem Frequency and Family Size Effects

This is where these models make their most theoretically significant claims, because they reframe both effects as emergent consequences of a single learning mechanism rather than as diagnostics of separate processing routes. The reframing is subtle but has deep implications.

---

### A Quick Recap of the Representational Architecture

In **NDL**, the system learns associations between **cues** (letter or phoneme n-grams, or whole word forms) and **outcomes** (word meanings or lexical identities) via the Rescorla-Wagner update rule — an error-driven algorithm that adjusts connection weights based on prediction error. There are no morpheme nodes, no decomposition procedure, and no stored stems.

In **LDL**, this is extended into a full matrix algebra framework. Two matrices are learned from corpus data:

- **F** (form-to-meaning): maps a word's form vector (a bag of character n-grams) onto a semantic vector
- **G** (meaning-to-form): maps a semantic vector back onto a predicted form vector

Comprehension involves form → F matrix → predicted semantic vector → nearest neighbor retrieval in semantic space. Production runs the reverse through G. Again, no morpheme representations exist anywhere in this architecture.

---

### Stem Frequency Effects in NDL/LDL

**Classical explanation:** Stem frequency reflects how often a stored morpheme entry is accessed; high frequency strengthens that entry, facilitating any form built on it.

**NDL reframing:**

In NDL, a high-frequency stem means that the character or phoneme n-grams that spell out the stem — say, *w-o-r*, *o-r-k*, *r-k* for the stem WORK — have appeared repeatedly across many training trials, distributed across all surface forms (*work*, *works*, *worked*, *working*, *worker*, *overwork*, etc.).

Through Rescorla-Wagner learning, these n-grams develop **strong, well-calibrated weights** pointing toward the semantic outcomes associated with the WORK meaning. High stem frequency means more cumulative learning trials for those n-grams, reducing residual prediction error and sharpening the weights. When a new surface form like *worked* is encountered, the stem n-grams it contains activate the WORK meaning robustly because their weights have been tuned by long exposure history.

So the effect looks like stem frequency — and it *is* stem frequency in a statistical sense — but it is not mediated by accessing a stored stem entry. It is the **accumulated weight history of shared sublexical cues**.

**LDL reframing:**

In LDL, the F matrix is learned so as to minimize the error between predicted and actual semantic vectors across all training words. For a high-frequency stem, the rows of F corresponding to the stem's n-grams receive strong, consistent gradient updates across many words. The learned weights for those n-grams therefore point precisely and reliably toward the stem's semantic region.

When processing a complex form, the accuracy of the predicted semantic vector — and therefore the ease of retrieving the correct lexical neighbor — depends on how well the F matrix has learned to exploit the form's n-grams. High stem frequency means those n-grams are more reliably informative, producing more accurate semantic predictions and faster, more confident lexical access.

Critically, **there is no discrete moment of stem access**. The stem frequency effect is a gradient property of the weight matrix, not a bottleneck at a morpheme node.

---

### Morphological Family Size Effects in NDL/LDL

**Classical explanation:** Family size reflects spreading activation through a semantic network of morphological relatives; a larger family means richer co-activation of the base representation.

**NDL reframing:**

Family size in NDL relates to a more complex property of the learning dynamics. Consider what it means for a stem's n-grams to appear in a large versus small family:

- In a **large family**, the stem n-grams appear across many distinct surface forms, each associated with a semantically related but distinct outcome (WORKER, OVERWORK, WORKLOAD, etc.). The shared semantic core — the WORK component — is repeatedly reinforced across all these learning trials, while the idiosyncratic semantic features of each family member are discriminated away through competitive inhibition between outcomes.

- In a **small family**, the stem n-grams appear in fewer contexts, providing less consistent reinforcement of the shared semantic core.

The result is that a large morphological family produces **stronger, more coherent weights** for the stem n-grams, pointing toward a more robustly represented semantic core. Importantly, this falls out of the competitive dynamics of Rescorla-Wagner learning: outcomes that are consistently predicted across many cue contexts become strongly weighted, while noise is suppressed. Family size therefore indexes **the consistency and breadth of the training signal** for the stem's n-grams — not the size of an activation network.

**LDL reframing:**

In LDL, the family size effect is explained through both the F and G matrices, and through the geometry of the semantic space:

- A large morphological family means that many word forms share overlapping n-gram cues. Learning the F matrix requires finding weights that simultaneously work well for *worked*, *worker*, *working*, *overwork*, and so on. The optimization pressure across all these forms forces the weights for shared stem n-grams to converge on the **semantic dimensions that are common across the family** — the core WORK meaning — because those dimensions are what the shared cues consistently predict.

- This produces a well-structured region in semantic space: family members cluster together, and their centroid corresponds to the robustly learned stem meaning. A larger, more coherent family creates a denser, better-defined semantic neighborhood.

- At the point of lexical retrieval — finding the nearest neighbor in semantic space — a form with a large, semantically coherent family yields a more accurate semantic prediction (because the F matrix weights are well-trained), and the correct neighbor is more easily distinguished from competitors.

**The semantic transparency wrinkle:**

Both NDL and LDL handle the finding that semantically opaque relatives do not contribute to the family size effect **without any additional stipulation**. In these models, an opaque relative simply has a semantic vector that is distant from the base in distributional space. It therefore does not contribute consistent signal during learning — Rescorla-Wagner does not reinforce the stem n-grams toward that semantic region, and in LDL the optimization pressure from that form does not push F weights toward the stem semantic dimensions. Transparency sensitivity is a **natural consequence of distributional learning**, not an additional architectural filter.

---

### The Critical Theoretical Point: One Mechanism, Not Two Routes

This is where NDL and LDL make their most provocative claim. In classical models, stem frequency and family size effects were taken as evidence for **two distinct processing routes** — stem frequency indexing the decompositional route (morpheme access), family size indexing the whole-form route (semantic network). The dissociation between them seemed to require a dual-route architecture.

In NDL and LDL, **both effects emerge from the same mechanism** — error-driven learning over distributional statistics — and both are properties of the same learned weight matrices. They look different because they tap different aspects of the statistical structure:

| Effect | What it reflects in NDL/LDL |
|---|---|
| Stem frequency | Weight strength for shared n-gram cues, accumulated over token frequency |
| Family size | Consistency and coherence of learning signal across distinct form-meaning pairs (type diversity) |

The difference between token frequency accumulation and type diversity is real and explains why the effects are empirically dissociable — but it does not require two routes or two representational levels. Both are facets of a single learned mapping.

---

### What This Does and Does Not Explain

It is worth being honest about where these accounts are less fully worked out:

- **Early masked priming effects** — particularly the finding that purely form-based (pseudo-morphological) priming occurs within ~150ms — sit somewhat uncomfortably with NDL/LDL, because these models do not obviously predict an early purely form-based decomposition stage. Baayen's response has generally been to question whether masked priming taps the same system as lexical decision latencies, or to argue that early priming reflects n-gram overlap rather than morpheme parsing — a position that is contested.

- **Productivity and novel form processing** — how the system handles genuinely novel morphological combinations — is handled differently than in rule-based models, through analogy in the learned weight space, but the predictions are harder to make explicit.

- The **processing time predictions** of LDL are derived from measures like the correlation between predicted and actual semantic vectors (called *semantic support*) and the distance to the nearest neighbor. These are sophisticated but require large corpus and semantic resources to implement, making direct comparison with classical models non-trivial.

Nonetheless, the reframing of both stem frequency and family size as emergent distributional learning effects — requiring no morpheme representations and no architectural routes — represents one of the most substantive theoretical moves in the recent morphological processing literature.

---

# NDL and LDL: One Framework or Two?

This is a genuinely interesting question about the architecture of a research program, and the answer is neither a simple yes nor no. They are best understood as **successive stages of a single evolving theoretical commitment**, sharing deep assumptions but differing enough in formalism and scope that treating them as identical would obscure important developments.

---

### What They Definitively Share: The Core Commitments

Both models are grounded in the same foundational ideas, and these shared commitments are what make them look like a single framework:

**Discriminative learning as the organizing principle.** Both hold that the language system is fundamentally a system of learned associations between cues and outcomes, shaped by prediction error. The Rescorla-Wagner learning rule — or more precisely the equilibrium it converges to — is the theoretical engine of both. This is not a superficial similarity; it is the central claim that distinguishes this approach from all morpheme-based, rule-based, and dual-route models.

**Rejection of morphemes as processing units.** Neither model posits stored morpheme representations, a decomposition procedure, or a dedicated morphological parser. This is a shared ontological commitment, not just a methodological convenience.

**Emergence over stipulation.** Both treat morphological effects — stem frequency, family size, paradigmatic structure, inflectional regularity — as emergent consequences of learning over distributional statistics rather than as architectural features that need to be built in. This is a shared explanatory strategy.

**Distributional semantics as the meaning space.** Both use corpus-derived semantic representations — whether as discrete outcomes in NDL or as continuous vectors in LDL — rather than structured symbolic semantic representations.

**Grounding in the same empirical tradition.** Both emerge from the same group, primarily Baayen and collaborators including Milin, Chuang, Heitmeier, and Blevins, and are motivated by overlapping sets of empirical phenomena. They share a theoretical lineage that is explicit and acknowledged.

These shared commitments are deep enough that it is reasonable to speak of a **discriminative learning framework** that encompasses both.

---

### Where They Differ: Not Just Implementation Details

Despite the shared foundation, the differences are substantial enough to matter theoretically.

#### Representational Architecture

**NDL** operates with **discrete outcomes** — typically individual word forms or lemmas — and discrete cues such as letter bigrams or trigrams. The learning problem is essentially a multi-class classification: given these cues, which outcome (word) does this input correspond to? The Rescorla-Wagner rule is applied iteratively over training events, and the equilibrium weights can be computed analytically via the Danks equations, which gives NDL unusual mathematical tractability.

**LDL** replaces discrete outcomes with **continuous semantic vectors** and continuous form vectors. The learning problem becomes a regression: find a matrix F that maps form vectors to semantic vectors as accurately as possible across the lexicon. This is a fundamentally different mathematical structure. It operates in a geometric space rather than a categorical space, and it produces predictions about the *quality* of semantic approximation rather than just the *probability* of a categorical outcome.

This distinction matters because LDL can represent **graded semantic similarity**, paradigmatic relationships across an entire inflectional system, and the geometry of the form-meaning mapping in ways that NDL's discrete outcome structure cannot easily capture.

#### Scope and Ambition

**NDL** was primarily developed to explain **single-word recognition** — lexical decision latencies, naming times, and related measures. Its scope is the mapping from a form cue to a lexical identity, and it is most naturally applied to comprehension.

**LDL** is explicitly designed as a **bidirectional model of the full lexicon** — it models both comprehension (form to meaning via F) and production (meaning to form via G), and it attempts to account for the structure of the entire morphological system simultaneously rather than one word at a time. This includes predicting paradigmatic structure, morphological typology, and the learnability of different inflectional systems — a scope that goes well beyond what NDL was designed to address.

#### The Role of Analogy and Paradigmatic Structure

LDL incorporates a much more explicit treatment of **paradigmatic implicative structure** — the idea developed by Blevins in Word and Paradigm morphology that words within an inflectional paradigm are related by analogical implication rather than by rule application to a stored stem. LDL's geometry naturally captures these implicative relations through the similarity structure of semantic and form vectors across paradigm cells.

NDL does not have a natural analog to this. It can learn that certain cues predict certain outcomes, but the relational structure *across* paradigm cells is not part of its representational vocabulary in the same way.

#### Mathematical Formalism

NDL uses an **online learning rule** (Rescorla-Wagner) operating over sequences of training events, and much of its theoretical work involves the equilibrium weights that result from learning. The key analytical tool is the Danks equilibrium, which allows the learned weights to be computed from co-occurrence matrices without simulating the learning process itself.

LDL uses **closed-form linear algebra** — the learned matrices F and G are computed via ordinary least squares regression over the full training corpus simultaneously. This is mathematically cleaner and more transparent, but it means LDL is less directly a model of *how learning unfolds over time* and more a model of the *end state* that learning produces.

This matters for questions about acquisition, the time course of learning, and the processing of low-frequency or novel forms — questions where the online dynamics of NDL are potentially more informative.

---

### The Developmental Relationship

Understanding their relationship historically clarifies their theoretical status.

NDL came first, developed roughly between 2007 and 2014, and was explicitly positioned as showing that classical morphological processing effects could be reproduced by a learning system with no morphological architecture. The key papers by Baayen, Milin, Durdevic, Hendrix, and Marelli demonstrated that n-gram cues, weighted by Rescorla-Wagner learning, could predict lexical decision latencies at least as well as classical morphological variables.

LDL emerged from a recognition that NDL, while powerful, had two limitations: its discrete outcome structure could not capture the continuous semantic relationships central to morphological family effects and paradigmatic structure, and it was essentially a comprehension-only model. LDL was developed — with Chuang, Heitmeier, and Blevins as key contributors — to address these limitations while preserving the core discriminative learning commitment.

LDL should therefore be understood as a **generalization and extension** of NDL rather than a replacement. NDL's predictions about cue weights and their relation to processing difficulty are largely preserved in LDL's F matrix structure — the logic is continuous even as the formalism changes. Baayen himself has described LDL as where the research program has arrived, suggesting he views it as superseding rather than coexisting with NDL.

---

### The Case for Treating Them as One Framework

The strongest argument for unity is that they share a **research ontology** — a set of commitments about what kinds of entities exist (cues, outcomes/vectors, weights), what processes operate (discriminative learning, error minimization), and what counts as an explanation (emergent statistical structure rather than stipulated architecture). A researcher working within either model is asking the same questions and treating the same kinds of evidence as relevant.

They also share **the same critical target**: the classical morpheme-based, route-based architecture represented by models like Caramazza's AAM, the race model, or the early decomposition account. The argument against morpheme representations and for discriminative learning is identical in both.

---

### The Case for Treating Them as Distinct

The strongest argument for distinguishing them is that **they are not interchangeable for specific research questions**:

- Questions about paradigmatic structure, morphological typology, and production require LDL's bidirectional matrix architecture — NDL cannot address them.
- Questions about the time course of learning, frequency effects in sparse data, and online adaptation may be more naturally addressed by NDL's online learning dynamics.
- They make somewhat different quantitative predictions — LDL's *semantic support* and *nearest neighbor distance* measures are not straightforwardly equivalent to NDL's activation weights, and they are not always interchangeable as predictors of behavioral data.

---

### A Reasonable Summary Position

NDL and LDL are best described as **two implementations of a single theoretical framework**, where the framework is **discriminative learning applied to the form-meaning mapping of the lexicon**. They share all their foundational commitments and differ in how those commitments are formalized and extended. LDL is the more mature and ambitious implementation, and it is where the research program is currently centered.

The analogy might be to the relationship between early connectionist models of reading and later, more sophisticated implementations like the triangle model: they share a theoretical vision — distributed representations, learned weights, emergent structure — but the later model is not just the earlier one with better parameters. It is a genuine extension that can address a wider range of phenomena. The theoretical framework is one; the specific models within it are two.

---

# Is Morphological Processing Research Firmly in the Neural Network Camp?

The honest answer is: not firmly, not unanimously, and — importantly — the question contains a terminological ambiguity that actually matters quite a lot for how we evaluate the field's current position.

---

### The Terminological Issue: NDL/LDL Are Not Neural Networks

This needs to be said clearly because it is frequently misunderstood. **NDL and LDL are not neural networks** in the sense that term is used in contemporary machine learning or in the earlier connectionist tradition of Rumelhart, McClelland, and the PDP research group.

- NDL is mathematically equivalent to a **single-layer linear model** whose weights are set by the Rescorla-Wagner rule. It has no hidden layers, no nonlinear activation functions, no distributed intermediate representations in the connectionist sense.
- LDL is explicitly a **linear algebra framework** — ordinary least squares regression between vector spaces. It is, in formal terms, closer to multivariate linear regression than to any neural network architecture.

Baayen and colleagues are explicit about this. They deliberately chose linear models because linearity is **interpretable** — you can inspect the weight matrices and understand what the model has learned — and because they wanted to make a theoretical claim about the sufficiency of simple discriminative learning, not about the power of deep nonlinear processing.

So the relevant contrast in the morphological processing literature is better framed as **symbolic/morpheme-based versus discriminative/distributional**, rather than symbolic versus neural network. The connectionist tradition — Rumelhart and McClelland's past-tense model, subsequent multi-layer networks — is actually a somewhat separate strand of the debate, though related.

---

### The Actual State of the Debate

The field is genuinely divided, and it would be inaccurate to say any camp has firmly won. Here is a more precise picture:

#### Where the Discriminative/Distributional Approach is Strong

- It provides the most **parsimonious** account of stem frequency and family size effects, requiring no architectural stipulations about morpheme storage or processing routes.
- It handles **gradient and probabilistic** phenomena — the graded nature of morphological relatedness, the interaction between frequency and transparency — more naturally than categorical symbolic models.
- LDL has shown impressive success in modeling **inflectional paradigm structure** across typologically diverse languages, suggesting it captures something real about the organization of morphological systems.
- The approach connects naturally to the broader movement toward **distributional and usage-based** accounts in linguistics, giving it theoretical allies beyond psycholinguistics.

#### Where the Symbolic/Decompositional Approach Remains Strong

The early masked priming evidence has not gone away, and it remains genuinely difficult for discriminative learning models to accommodate:

- **Morpho-orthographic priming** — the finding that *corner* primes *corn* at ~130ms — seems to require something like a structural parsing procedure that strips apparent affixes regardless of meaning. Explaining this as n-gram overlap is possible, but it requires the n-gram account to do a lot of work that starts to look like decomposition under another name.
- **Across-modality and cross-script priming** — morphological priming that survives changes in modality or script — is difficult to explain purely in terms of shared sublexical form cues, since the cues differ radically across conditions.
- **Neuroimaging evidence** from MEG and EEG studies by Marslen-Wilson, Pylkkänen, and others shows temporally distinct components associated with form-based and semantic morphological processing, which maps more naturally onto a two-stage decompositional architecture than onto a single learned mapping.
- The **left anterior temporal lobe and inferior frontal gyrus** show selective sensitivity to morphological structure in ways that suggest dedicated neural infrastructure, not just general pattern association.

#### The Hybrid and Intermediate Positions

Much of the most careful current work does not sit cleanly in either camp:

**Grainger's morpho-orthographic level** is a hybrid — it accepts early automatic form-based decomposition (sympathetic to the symbolic side) but frames the representations involved as intermediate-level pattern units rather than symbolic morphemes (sympathetic to the distributional side). This is probably the most widely held position among visual word recognition researchers who take both the priming data and the distributional data seriously.

**Hay and Baayen's parsing ratio** work sits in an interesting intermediate position — it preserves the idea that individual words vary in how likely they are to be parsed versus accessed whole, but grounds this in usage-based, frequency-sensitive factors rather than fixed architectural routes.

**Amenta, Marelli, Crepaldi and colleagues** have developed approaches that use distributional semantic similarity to model morphological processing while still allowing for something like a decomposition step — essentially trying to integrate the strengths of both traditions.

---

### The Complication: Large Language Models

There is a separate and increasingly unavoidable issue: **transformer-based large language models** like BERT, GPT, and their successors have become relevant to this debate in ways that are not yet fully worked out.

These models:
- Have no explicit morphological architecture whatsoever
- Are trained on distributional statistics at a scale that dwarfs any psycholinguistic corpus
- Nevertheless handle morphologically complex words, novel formations, and cross-lingual morphological generalization remarkably well
- Show internal representations that, when probed, exhibit something like morphological structure in their intermediate layers

This could be taken as strong evidence that morphological processing can emerge from purely distributional learning without symbolic architecture. But there are complications:
- These models are **not cognitive models** — they are not constrained by processing time, working memory, or biological plausibility, so their success does not straightforwardly support claims about human processing.
- The fact that a nonlinear high-capacity model can do something does not tell us much about how a resource-limited biological system does it.
- There is active debate about whether what these models learn about morphology is genuinely morphological structure or a sophisticated form of surface pattern matching — a debate that mirrors the symbolic versus distributional argument in miniature.

Baayen and colleagues have begun engaging with this, arguing that the success of linear models like LDL — which have far less capacity than transformers — actually makes a stronger theoretical point: if even a linear model can capture the relevant effects, the case for symbolic architecture is weakened further. Critics counter that the phenomena LDL handles well are not the phenomena that motivated decomposition accounts in the first place.

---

### A Candid Assessment

The most accurate characterization of the current state is probably this:

**The symbolic/morpheme-based architecture has lost its status as the default assumption.** It is no longer taken for granted that decomposition into stored morphemes is the primary mechanism, and models that dispense with morpheme representations entirely are now taken seriously by the mainstream of the field.

**But a clear victor has not emerged.** The early masked priming data and the neuroscientific evidence for temporally distinct processing stages remain genuine challenges for purely discriminative accounts. The field currently contains:

- A **discriminative/distributional camp** centered on NDL/LDL, strongest in the corpus-based and computational psycholinguistics communities
- A **decompositional camp** centered on masked priming and neuroscientific methods, strongest in experimental psycholinguistics and cognitive neuroscience
- A **large and probably growing middle** that treats the question as genuinely open and looks for models that can accommodate both sets of findings

What has changed most decisively is not that one side has won, but that the **burden of proof has shifted**. Twenty years ago, the question was whether there was any alternative to a morpheme-based architecture. That question has been answered affirmatively. The current question — whether human morphological processing actually works that way — remains genuinely contested.
