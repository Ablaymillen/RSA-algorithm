import random
from linereader import copen

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', ' ']


def index_of(letter):
    for i, ch in enumerate(ALPHABET):
        if letter == ch:
            return i


def character_of(num):
    for i, ch in enumerate(ALPHABET):
        if i == num:
            return ch


def generate_primes(primes_list=range(100, 2000)):
    with open('primes.txt', 'w') as fp:
        for item in primes_list:
            fp.write("%s\n" % item)


def get_random_prime():
    file = copen(file="primes.txt")
    lines = file.count('\n')
    random_line = file.getline(random.randint(1, lines))
    return int(random_line)


def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d


def is_prime(n):
    if n > 1:
        for k in range(2, n // 2 + 1):
            if n % k == 0:
                return False
        return True
    else:
        return False


def encrypt(plaintext, public):
    e, n = public
    encrypted = [pow(index_of(ch.lower()), e, n) for ch in plaintext]
    return encrypted


def decrypt(encryptedText, secret):
    d, n = secret
    decrypted = [character_of(pow(ch, d, n)) for ch in encryptedText]
    return ''.join(decrypted)


def generate_public_key(phi):
    while True:
        e = get_random_prime()
        if e < phi:
            break
    return e


def main():
    p = get_random_prime()
    q = get_random_prime()
    print(f"p= {p}, q= {q}")
    # get lcm(p, q)
    phi = int((p - 1) * (q - 1))
    # modulus
    n = q * p
    # public key generation
    e = generate_public_key(phi)
    # get inverse mod d
    d = mod_inverse(e, phi)
    plainText = input("Enter the message you want to encrypt: ")
    # save public keys
    with open('public keys.txt', 'a') as public:
        public.write(f'\n{e, n}')
    print(f"Your public key is:{e, n}")
    # save secret keys
    with open('secret keys.txt', 'a') as secret:
        secret.write(f'\n{d, n}')
    print(f"Your secret key is:{d, n}")
    # encrypt text
    encryptedText = encrypt(plainText, (e, n))
    print(f"Encrypted text: {encryptedText}")
    # decrypt text
    decryptedText = decrypt(encryptedText, (d, n))
    print(f"Decrypted text: {decryptedText}")


main()

