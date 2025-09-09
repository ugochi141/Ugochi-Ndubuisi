from collections import Counter
import re

def analyze_sequence(dna):
    """
    Comprehensive DNA sequence analysis pipeline.
    
    Args:
    dna (str): DNA sequence string
    
    Returns:
    dict: Dictionary containing various sequence analyses
    """
    dna = dna.upper()  # Convert to uppercase
    length = len(dna)
    nucleotide_counts = Counter(dna)
    gc_content = (nucleotide_counts['G'] + nucleotide_counts['C']) / length * 100
    rna = transcribe_dna(dna)
    
    return {
        'length': length,
        'nucleotide_counts': dict(nucleotide_counts),
        'gc_content': gc_content,
        'rna': rna,
        'is_valid': is_valid_dna(dna),
        'complement': complement_dna(dna),
        'reverse_complement': reverse_complement(dna)
    }

def transcribe_dna(dna):
    """Convert DNA to RNA"""
    return dna.replace('T', 'U')

def is_valid_dna(sequence):
    """Check if the sequence is a valid DNA sequence"""
    return set(sequence).issubset({'A', 'T', 'G', 'C'})

def complement_dna(dna):
    """Return the complement of a DNA sequence"""
    complement_dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join(complement_dict[base] for base in dna)

def reverse_complement(dna):
    """Return the reverse complement of a DNA sequence"""
    return complement_dna(dna)[::-1]

def find_motif(dna, motif):
    """Find all occurrences of a motif in a DNA sequence"""
    return [m.start() for m in re.finditer(f'(?={motif})', dna)]

# You can add more functions as needed

# Example usage
if __name__ == "__main__":
    test_dna = "ATGGGCCGCAGTAATTGA"
    result = analyze_sequence(test_dna)
    print(result)
    
    motif = "GGC"
    motif_positions = find_motif(test_dna, motif)
    print(f"Motif '{motif}' found at positions: {motif_positions}")
