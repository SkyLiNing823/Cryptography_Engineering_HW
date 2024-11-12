import hashlib
from time import process_time

filename = "test.txt"

Easy = 'ef0ebbb77298e1fbd81f756a4efc35b977c93dae'
Medium = '0bc2f4f2e1f8944866c2e952a5b59acabd1cebf2'
Q = [Easy, Medium]

table = open(filename,'r').read().split('\n')

def get_Answer(hashed):
    count = 0
    start = process_time()
    for line in table:
        m = hashlib.sha1()
        m.update(line.encode('utf-8'))
        h = m.hexdigest()
        count += 1
        if h == hashed:
            end = process_time()
            print(f'Hash: {h}')
            print(f'Password: {line}')
            print(f'Took {count} attempts to crack input hash. Time Taken: {end - start}... and so on')
            print('------------------------')
            break


# E & M
for q in Q:
    get_Answer(q)

# Leet
Leet = '9d6b628c1f81b4795c0266c0f12123c1e09a7ad3'
Leet_salt = 'dfc3e4f0b9b5fb047e9be9fb89016f290d2abb06'
get_Answer(Leet_salt)  # redbull
count = 0
start = process_time()
for line in table:
    line = 'redbull' + line
    m = hashlib.sha1()
    m.update(line.encode('utf-8'))
    h = m.hexdigest()
    count += 1
    if h == Leet:
        end = process_time()
        print(f'Hash: {h}')
        print(f'Password: {line}')
        print(f'Took {count} attempts to crack input hash. Time Taken: {end - start}... and so on')
        print('------------------------')
        break

