import hashlib
import random
import string

def find_hash():
    for _ in range(1000):
        data = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
        h = hashlib.sha256(data.encode()).hexdigest()
        if h.startswith("00"):
            return True
    return False