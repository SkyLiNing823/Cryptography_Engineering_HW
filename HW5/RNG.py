import secrets

random_bytes = secrets.token_bytes(1024*1024)
with open('random.bin', 'wb') as f:
    f.write(random_bytes)