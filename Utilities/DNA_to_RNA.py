def DNA_to_RNA(dna):
    translate = {
        'A': 'A',
        'C': 'C',
        'T': 'U',
        'G': 'G'
    }
    return ''.join(translate[a] for a in dna)


def reverse_complement(dna):
    dna = dna[::-1]
    complement = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }

    return ''.join(complement[a] for a in dna)
