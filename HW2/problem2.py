import hashlib
from time import process_time

L = []


def hashing(func, name):
    start = process_time()
    for chunk in iter(lambda: vid.read(4096), b''):
        func.update(chunk)
    h = func.hexdigest()
    end = process_time()
    print(f'{name}: {h}\ntime: {end - start}\n-----------------------------')
    L.append([name, end - start])

# MD5, SHA1, SHA-2(sha224, sha256 and sha512), and SHA-3(sha3-224, sha3-256 and sha3-512)
vid = open('BigBuckBunny.mp4','rb')

# MD5
md5 = hashlib.md5()
hashing(md5, 'MD5')

# SHA1
sha1 = hashlib.sha1()
hashing(sha1, 'SHA1')

# SHA-2
sha224 = hashlib.sha224()
sha256 = hashlib.sha256()
sha512 = hashlib.sha512()
hashing(sha224, 'SHA-2(224)')
hashing(sha256, 'SHA-2(256)')
hashing(sha512, 'SHA-2(512)')

## SHA-3
sha3224 = hashlib.sha3_224()
sha3256 = hashlib.sha3_256()
sha3512 = hashlib.sha3_512()
hashing(sha3224, 'SHA-3(224)')
hashing(sha3256, 'SHA-3(256)')
hashing(sha3512, 'SHA-3(512)')

L.sort(key=lambda x: x[1])
for i in L:
    if i != L[-1]:
        print(i[0], '>' , end=' ')
    else:
        print(i[0])
