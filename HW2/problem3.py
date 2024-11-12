from itertools import permutations

tc = 'UONCS VAIHG EPAAH IGIRL BIECS TECSW PNITE TIENO IEEFD OWECX TRSRX STTAR TLODY FSOVN EOECO HENIO DAARQ NAELA FSGNO PTE' # 98 words
vowels = ['A', 'E', 'I', 'O', 'U']
c = tc.replace(' ', '')


# 7 * 14
print('--------------------\n7 * 14: \n--------------------')
L = [ [] for _ in range(14)]
for i in range(7):
    for j in range(14):
        L[j].append(c[i*14+j])
total_Bias = 0
for s in L:
    count = 0
    for w in s:
        if w in vowels:
            count+=1
    bias = round(abs(7*0.4 - count),3)
    print(f"{''.join(s)}   {count}   {bias}")
    total_Bias += bias
print(f'average : {total_Bias/14} ')

# 14 * 7
print('\n--------------------\n14 * 7: \n--------------------')
L = [ [] for _ in range(7)]
for i in range(14):
    for j in range(7):
        L[j].append(c[i*7+j])
total_Bias = 0
for s in L:
    count = 0
    for w in s:
        if w in vowels:
            count+=1
    bias = round(abs(14*0.4 - count),3)
    print(f"{''.join(s)}   {count}   {bias}")
    total_Bias += bias
print(f'average : {total_Bias/7} ')




# 14 * 7



def generate_permutations(input_list):
    return list(permutations(input_list))

# # Example usage
# input_list = [i for i in range(7)]

# permutations_list = generate_permutations(input_list)

# for l in permutations_list:
#     new_L = ''
#     new_L2 = ''
#     new_L3 = ''
#     for n in l:
#         new_L += f'{str1[n]} '
#         new_L2 += f'{str2[n]} '
#         new_L3 += f'{str3[n]} '
#     print(new_L)
#     print(new_L2)
#     print(new_L3)
#     print('-------------')



