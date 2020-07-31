# Counting Point Mutations

a = "GACGATGATTTGCCTTGGGTTTGTACGGGTTGCCTTATCGATTGACCTTGACGAAGGTTCGATCAGAGTTGGGTGTCATGAACCCAGAGCGATCGTTGTTAAGGATCATAGGGCTGATGGCGATGTTAGTCTATGGTGGCTTACCGATTCTGCCCGAGTTGCACGTTCACATTTTAGATGTGAACGATTGATCATCCGTAGGCCTCCCATGCCCGAAAAGCTGCGGACTGACAAAGACTAGTAATGGTCCAGTTTTCCACTCCACAGCCTCTTAGTCTAAGGCTCGTGCGTCTCATATCCGTACCTGTACAGATAGACTGGGGGCAGCGCTTTCACCGCGTGTCCTGGTATCTATGGTTGGGAGTGCAGTCGTTCCCGAAGACACCCTTACTGTCTCAGCCTGCAGTTTCGAGGTGCGCTTTTCGTACCGAGTTAATTCTGCTCACTATGTGCTTATGCGTTTACTGTAGAAAAGGAAACGCCAAGTATCCCCCGATATGAAAATGCGGCGCCCCACCTTAGGATTCCTCCAAGTGTACCTTATCATGCGCACAGGTACAAATCATAAGGGTCGGATAAGCAGGAACAACACCACTGACACGAGGGATGGGGGGACCGTGCATGACCTAAAACTGTTGTCTATTGTGCTAACTGTACTCTGGGCAACAAGGTGGAGGGTAAAGGAACTACGAGGTCTATAATGAAGTCTGTGGTGGGTGTGACGCTGGTTTCCCCCGCTATTGAGGTGCGCTGCTCTCATTGACATTGGGGAAGACTGCGGAGGCCGTATCTTAACGCGAATTCAGATTTTTTGTCTTAGCGCTGACTCGTCTGACTATGGAGAGGCCCCTTAAAGGTGCGCGCTTATTGTCATGAACTTTCAAGCTGACGGCCTGGCAAGCCTGGTAACGCCTGACCCACCTATGAGATGTTCTTGAGTACAC"
b = "TGTGTGCGTGTGTCTAGGCTTTTGGAGCGCAACCAAATCTAGGCTACGGAACGAATTTCCGGTCGGGATTAGGTGTGTTGATCCCAGTGCGACCATTGAGAAGTAAGATAGGGATGTTCCGGATCGTCATTTACGGCATCTTGTAAAGTGTGCGCCTGATTCGCCGGGTTTTATGAGAAGTCACCGTCCGTTTAGGAGTGGGATCTCCATGCCACATAACCATCTCAGTACGCCAGCCAAGTCTTATTACGTTTATCCACGGCACGACGCTTTTGTGTCTGGACCTATCGACCCGAATCTGGTCCTATCCTTTGACGGTGGTCGGAAGGGACTGATAACAAGGGCTCGAGCCCAATGCTGGAATAACTTAAGAGCGCGAAACCACCTTTCCTGACCCGACATGGATTCCATAAGTGGGCCTAGCTTATCCAGTTTCCGCCTAACAACATAGGCGTTTGAGTATACGCACGCTAGGACATGGCCATGTTTCGCCCGAGGCTCACCCGCGCCGTTGAACCCTAGGACACCTCCGCATGAACATTAAAATCCGTTGTGAGAATTACCAACACCTGAAGCAACACTCCGTCGGCAGTATAGAACCGTGTGTATTGGGGGATGCTAGTGTCCTACATCCGATTTCTTCAGATCCTACTTGGTGCTTTGCTCCAAAATAGAGGCTGGACTAAGTCAGGATTATTTGCTTTTGTGACTGGTCGGTGTAACCGATGATTCCCGCGTGAGATTTCGTAGTCGCACCGCATAGTATTGTAGAATAATGGAAGAGACCAGTCTCAGCGCAAACTAATGATTTTGATCGACGTGCGGAGGAGTCTAACTTGAGCTGAGTCACCTCAAGGGGAGCCCACTTAGTCCGACGGTCTGAAGAGTACGCCGTCGAAATAGTACGGCCGGCCCATAAAGCCGTAGGGTCATCCTAAGTATAC"

count = 0

for i in range(len(a)):
    if a[i] != b[i]:
        count += 1

print(count)