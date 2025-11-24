# codon-name-generator
Fun tool to convert names into codon-optimised DNA sequences

# Codon Name Encoder

Simple tool to encode names as **codon-based DNA sequences**, using roughly
**human-biased codon usage** for the 20 standard amino acids.

Run the interactive notebook here: [![Kaggle Notebook](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/code/prachiabhang/codon-name-generator)


The idea:

- Treat each letter as a **one-letter amino-acid code** where possible.
- For **standard amino acids** (A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y),
  choose a commonly used human codon.
- For **all other letters** (e.g. B, J, O, U, X, Z), use `NNN`, representing an
  unspecified / wildcard codon.

> This is a small educational / toy project, **not** a full codon optimisation
> tool for real gene design.

---

## Standard amino-acid letters

The 20 canonical amino acids and their one-letter codes:

`A C D E F G H I K L M N P Q R S T V W Y`

These are encoded using roughly human-preferred codons, e.g.:

- A → GCC  
- S → AGC  
- M → ATG  

(See `codon_name.py` for the full mapping.)

Any other letter (including `B J O U X Z`) is treated as:

- “unknown / non-standard amino acid” → encoded as **`NNN`**

---

## Examples

Some example encodings:

```text
PRACHI  -> CCT-CGC-GCC-TGC-CAC-ATC

