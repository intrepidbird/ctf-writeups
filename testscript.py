from Crypto.Util.number import inverse

e = 17
N = 7663
phi = 7488
ciphertext = 747717764508152773002218538067364183

# Calculate the private key d
d = inverse(e, phi)

# Decrypt the ciphertext
plaintext = pow(ciphertext, d, N)
print(plaintext)

# Convert the plaintext from an integer to a string
message = ""
while plaintext > 0:
    message += chr(plaintext % 256)
    plaintext //= 256
message = message[::-1]

print("Decrypted message:", message)
