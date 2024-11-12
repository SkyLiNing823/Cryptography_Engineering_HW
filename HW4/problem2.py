def LFSR(state, poly):
    fb = 0
    for i in range(len(state)):
        fb ^= state[i] & poly[i+1]
    state.pop(0)
    state.append(fb)
    return fb


def transfer(text, poly, key):
    state = [int(bit) for bit in key]
    result = ''
    btext = ''.join(format(ord(char), '08b') for char in text)
    for idx in range(0, len(btext), 8):
        b = ''
        for i in range(8):
            fb = LFSR(state, poly)
            b += str(int(btext[idx+i]) ^ fb)
        r_char = ''
        r_char += chr(int(b, 2))
        result += r_char
    return result


plaintext = 'ATNYCUWEARESTRIVINGTOBEAGREATUNIVERSITYTHATTRANSCENDSDISCIPLINARYDIVIDESTOSOLVETHEINCREASINGLYCOMPLEXPROBLEMSTHATTHEWORLDFACESWEWILLCONTINUETOBEGUIDEDBYTHEIDEATHATWECANACHIEVESOMETHINGMUCHGREATERTOGETHERTHANWECANINDIVIDUALLYAFTERALLTHATWASTHEIDEATHATLEDTOTHECREATIONOFOURUNIVERSITYINTHEFIRSTPLACE'
poly = [1, 0, 0, 0, 1, 1, 1, 0, 1]
key = '00000001'
e = transfer(plaintext, poly, key)
print('Encrypted:\n',e)
d = transfer(e, poly, key)
print('Decrypted:\n',d)