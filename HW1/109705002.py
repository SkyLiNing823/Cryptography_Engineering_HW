C = 'C UYGHARMZ IUWMPRWIR GAIR YVRMP MBHMZWMPUM C VMMXWPE YV PYR VCZ ZMGYQMD VZYG CXCZG YP CPCXKTWPE CPD MBHXYZM RNM VXYYD YV CDQCPUMD OPYSXMDEM SNWUN MCUN KMCZ LZWPEI SWRN WR'
F = {}
for i in range(ord('A'),ord('Z')+1):
    F[chr(i)] = 0
for letter in C:
    if letter != ' ':
        F[letter] += 1
F = dict(sorted(F.items()))
for alphabet in F.keys():
    print(f'{alphabet} : {F[alphabet]}')