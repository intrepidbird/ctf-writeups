from Crypto.Util.number import inverse

e = 17
N = 7663
phi = 7488
# Change the ciphertext NINE times, with the first being 7477 and the last being 4183. 
#Basically, repeat this code 9 times, but changing the value of 'ciphertext' 7477, 1776, 4508, 1527, 7300, 2218, 5380, 6736, 4183
ciphertext = 7477

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
