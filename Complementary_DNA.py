"""
This function, named DNA_strand, takes a DNA sequence and returns its complementary sequence,
where each base is replaced by its complementary base according to a reference dictionary.
"""

def DNA_strand(dna):
    reference = { "A":"T",
                  "T":"A",
                  "C":"G",
                  "G":"C"
                  }

    return "".join([reference[x] for x in dna])