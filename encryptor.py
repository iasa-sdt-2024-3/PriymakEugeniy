import random
import binascii

# GCD function (НСД)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# finding inverse element (upscaled Euclidean algorythm)
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# simple number test (Miller-Rabin's test)
def is_prime(n, k=5):  # k - number of tests
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Generate random number with given length
def generate_prime(bit_length):
    while True:
        candidate = random.getrandbits(bit_length) | (1 << (bit_length - 1)) | 1
        if is_prime(candidate):
            return candidate

# generate RSA keys
def generate_keypair(bit_length):
    p = generate_prime(bit_length // 2)
    q = generate_prime(bit_length // 2)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = mod_inverse(e, phi)
    return (e, n), (d, n)

# encrypt message
def encrypt(message, public_key):
    e, n = public_key
    plain_text = int(binascii.hexlify(message.encode()), 16)
    if plain_text >= n:
        raise ValueError("Повідомлення завелике для шифрування")
    return pow(plain_text, e, n)

# decrypt message
def decrypt(ciphertext, private_key):
    d, n = private_key
    decrypted = pow(ciphertext, d, n)
    try:
        return binascii.unhexlify(hex(decrypted)[2:]).decode()
    except (binascii.Error, UnicodeDecodeError):
        return None