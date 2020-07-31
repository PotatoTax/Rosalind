# Inferring mRNA from Protein

sequence = "MACRYCGYKSDTQFMMGVEWAADGTSANLEAICRFNEASQYCHAPPNNVQDLMFVRWEVSWGSNTCLPDWGEHVDMDMILPEYCFLEKAIVVIKQEYEHDYQWKIDQDPFWDWLGNHKVAFSEWAYNILCCIHHWQETSAHILCKTQTDHTDVHDMMNEMGTEIHNMWDRRFYMKDAYCTVYWNSSKDILYLHHWGPLTTECCEMMPWALHYFFSFSKIINHIGEITITGMFKNRWDVDNYRCEEDTDICMQCDDLCMQQAMNYPHVSDFSYIKDDTIVETITEIACCLALYHNDCQADETWQEHKDTEIWEFPAPSNSQEGMFWPKCQAFIIWGFHNRPIWYKLLPIMGMKGPQWKRIQHVKNQEWAWWNCQFYLRILHYIFKFIIYQPINGFAIVDIPIYPRVSDHWGMIHCFGMGMTERWKWNIEGGRNAAEDAMFCSAMCTYCPGIIWHCLETIEEHGCQDDTQAPGIEAPNCTKLNQMLNFCYWAMNQRRHHWRMNAAETPRQLYHRGYHSCICEMHDGVPKYCQREAMGVATNGSNMDMKTVLWWCCQRMWCMWNQNANQIRSNWQLMVSSTTQVEINENGNGGWEGPGTGRGLRWHTQVVVHYHCYQDFGYKRPMRMNNESQVIHGEPEQNEWNMCSEWNTCEKCYGASQCIAMSFDIYTHGEEQTDNQKHKCRMCKRASLYPMACVRYSGFNTQFQRWIWDSGEYGILHMCTHNGWWIQCRPSGQIWVDDDNSWMLFVRLGHDIKPAWASFPNMAVVKDYWKLKTCHWPARLVKKEWQITTSEVHYETHEMEYEVDFYEWEKMRFMGPWGAHGEKRYIGEDTPRFVYQKNEWPIDTMSVDSKSQKIRAHHCDRGCYNSFQWFKWEYCKERILWFGPICRYTAMKKDCQGPVAAIVWTKCDRQYIMEFFDPVSRGTKKNNCTQMFFMYHTVRKLMWERRSTVRMITIPNSICDRTTLRASSLPKASWQAVLKALVHWWASAMISVTFMATDVV"

counter = {}

with open('../Resources/codonTable', 'r') as file:
    lines = file.readlines()

    for l in lines:
        prot = l.split()[1]

        try:
            counter[prot] += 1
        except KeyError:
            counter[prot] = 1

n = counter['Stop']

for s in sequence:
    n *= counter[s]
    n %= 1000000

print(n)