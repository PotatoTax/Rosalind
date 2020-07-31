table = None


def mass(isotope):
    global table
    if not table:
        table = {}

        with open('../Resources/monoisotopicMassTable', 'r') as file:
            lines = file.readlines()

            for line in lines:
                ls = line.split()
                table[ls[0]] = float(ls[1])

    return table[isotope]