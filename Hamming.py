class Hamming:
    def __init__(self):
        self.nucleotides = ["A", "T", "C", "G"]

    def distance(self, strand1, strand2):
        hamming_value = 0
        if len(strand1) != len(strand2):
            raise ValueError("Strands of different lengths")
        for nt, nt2 in zip(strand1, strand2):
            if nt not in self.nucleotides or nt2 not in self.nucleotides:
                raise ValueError("Invalid nucleotide strand")
            if nt != nt2:
                hamming_value += 1
        return hamming_value
