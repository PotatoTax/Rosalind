table = None


def protein_from_rna(rna):
    global table

    if not table:
        with open('../Resources/codonTable', 'r') as file:
            lines = file.readlines()

            table = {}

            for line in lines:
                ls = line.split()
                table[ls[0]] = ls[1]


    return table[rna]
