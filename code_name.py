# codon_name.py
"""
Codon Name Encoder

Convert a name written using amino-acid one-letter codes
(e.g. PRACHI) into a DNA sequence using roughly
human-biased codon usage for standard amino acids.

- Standard amino-acid letters (20 canonical AAs):
  A C D E F G H I K L M N P Q R S T V W Y

- Any other letter (e.g. B, J, O, U, X, Z) is encoded as 'NNN',
  representing an unspecified / wildcard codon.

This is a simple educational/toy tool, not a gene-design pipeline.
"""

# human-preferred codons for each of the 20 standard amino acids
HUMAN_CODON_MAP = {
    "A": "GCC",  # Alanine
    "C": "TGC",  # Cysteine
    "D": "GAC",  # Aspartic acid
    "E": "GAA",  # Glutamic acid
    "F": "TTC",  # Phenylalanine
    "G": "GGC",  # Glycine
    "H": "CAC",  # Histidine
    "I": "ATC",  # Isoleucine
    "K": "AAG",  # Lysine
    "L": "CTG",  # Leucine
    "M": "ATG",  # Methionine
    "N": "AAC",  # Asparagine
    "P": "CCC",  # Proline
    "Q": "CAG",  # Glutamine
    "R": "CGC",  # Arginine
    "S": "AGC",  # Serine
    "T": "ACC",  # Threonine
    "V": "GTG",  # Valine
    "W": "TGG",  # Tryptophan
    "Y": "TAC",  # Tyrosine
}

VALID_AA_LETTERS = "".join(sorted(HUMAN_CODON_MAP.keys()))

def name_to_codons(name: str) -> str:
    """
    Convert a string into a codon sequence.

    For each character:
      - If it is a standard amino-acid one-letter code, use a preferred human codon.
      - Otherwise (including B, J, O, U, X, Z), use 'NNN' as an unspecified codon.

    Parameters
    ----------
    name : str
        Input string (e.g. "PRACHI").

    Returns
    -------
    str
        Codon sequence like 'CCT-CGC-GCC-TGC-CAC-ATC' or with 'NNN' for unknowns.
    """
    name = name.strip().upper()
    codons = []

    for letter in name:
        if letter in HUMAN_CODON_MAP:
            codons.append(HUMAN_CODON_MAP[letter])
        elif letter.isalpha():
            # Letter is alphabetic but not a standard AA code -> unknown amino acid
            codons.append("NNN")
        else:
            # Non-alphabetic characters: skip or treat as unknown
            # Here we choose to skip them.
            continue

    return "-".join(codons)


def main():
    print("Codon Name Encoder")
    print("----------------------")
    print("This tool encodes names as DNA codon sequences.")
    print("Standard amino-acid letters (canonical 20):")
    print(VALID_AA_LETTERS)
    print("\nOther letters (e.g. B, J, O, U, X, Z) will be encoded as 'NNN'.\n")

    name = input("Enter a name (e.g. PRACHI, SACHIN): ").strip()
    if not name:
        print("No input provided. Exiting.")
        return

    codon_seq = name_to_codons(name)
    print(f"\n{name.upper()} -> {codon_seq}")

    if "NNN" in codon_seq:
        print(
            "\nNote: 'NNN' indicates letters that are not standard amino-acid "
            "one-letter codes, encoded as unspecified/wildcard codons."
        )


if __name__ == "__main__":
    main()
