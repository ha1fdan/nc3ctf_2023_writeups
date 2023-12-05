import secrets

# Funktion til at udføre XOR-operation på to sekvenser af bytes
def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

# Funktion til at dekryptere en given hexadecimalværdi med en given engangspad (OTP)
def decrypt(encrypted_hex, otp):
    # Konverter den hexadecimale værdi til bytes og lav en liste af bytes
    encrypted_flag = list(bytes.fromhex(encrypted_hex))

    # Udfør XOR-operation mellem den krypterede flag-byte-sekvens og OTP'en
    for i in range(2 * len(otp) + 1):
        encrypted_flag[max(0, i - len(otp)):i] = xor(encrypted_flag[max(0, i - len(otp)):i], otp[-i:])

    # Konverter resultatet til bytes og derefter til en streng ved at ignorere ukendte tegn
    return bytes(encrypted_flag).decode('latin-1', errors='ignore')

# Den krypterede værdi, som skal dekrypteres
encrypted_value = "e9e494dcd1c2c9d3f8d1c6d5f8c3c2d3f8c3d2cad3f8c6d3f8ffe8f5f8c6cbcbc2f8c5ded3c2d4f8cac2c3f8cfd1c2d5f8ccc2def8c5ded3c2989898da"
n = len(encrypted_value) // 2  # Længden af den krypterede værdi divideret med 2, da hver byte repræsenteres af 2 tegn i hex

# Initialisering af tæller og variabel til at gemme det fundne flag
attempts, found_flag = 0, None

# Brute force dekryptering indtil resultatet starter med "NC3{"
while not found_flag:
    # Generer en tilfældig engangspad (OTP) med længden n
    otp = secrets.token_bytes(n)

    # Dekrypter den krypterede værdi med den genererede OTP
    decrypted_flag = decrypt(encrypted_value, otp)

    # Hvis det dekrypterede resultat starter med "NC3{", gem resultatet og afslut løkken
    if decrypted_flag.startswith("NC3{"):
        found_flag = decrypted_flag
        break

    # Tæl antallet af forsøg
    attempts += 1

    # Udskriv antallet af forsøg hver 10000. gang
    if attempts % 10000 == 0:
        print(f"Forsøg: {attempts}")

# Udskriv det fundne flag
print("Fundet Flag:", found_flag)
