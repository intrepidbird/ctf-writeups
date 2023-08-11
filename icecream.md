# icecream

## Context

This is a Cryptography challenge in LIT CTF 2023.

## Overview

Points: 337

Year: 2023

Author: swan07

## Description

ice cream (wrap the flag in LITCTF{})

- [icecream.zip](http://34.29.19.233/dl/?crypto/icecream/icecream.zip)

## Hints

N/A

## Approach

First I read the problem description very carefully.

I downloaded the files and then unzipped, which gives me a nice image of ice-cream, and a set of text messages.

![image](https://github.com/realrealAlexS/litctfwriteups/assets/140008493/3fd1127f-9db1-466c-8dde-7e0324734a49)

I downloaded the text messages html, which showed me this below page (which is screenshotted of course, and it contains the image file)
![image](https://github.com/realrealAlexS/litctfwriteups/assets/140008493/e8abea16-981a-4eb6-abfc-7f87da2980c1)

WOAH. There's a lot of hints in this pair of text messages. First, from the sentence "Don't worry about the image, that's the least significant bit of the entire message." I quickly knew that the image must have Least Significant Bit (LSB) steghide in it. 

## LSB

What's LSB? Here's a quick overview: Least significant bit (LSB) steganography is a technique used to hide confidential data within a cover image. The least significant bit of each byte of the image is replaced with a bit from the data being hidden. This technique is simple and efficient, and the changes made to the image are usually undetectable if you don't know that it was encoded this way. However, the size and secrecy of the hidden data can be a challenge when using LSB techniques. Basically, all you need to know here is that it's LSB, and you can use a decoder.

## Approach

After decoding the image with the help of [this calculator](https://planetcalc.com/9345/), I found out that the message was 747717764508152773002218538067364183.

NICE! We're making quick progress! The next part is a bit harder though.

First, from the Alice and Bob I'm used to, I assumed this was DHKE (Diffie-Hellman Key Exchange). However, the only values Alice would give Bob in this scenario are capital A, p, and g. I tried this, but it doesn't work.

Next, I tried public key encryption. There's no need to go into detail because it's the wrong method for this problem. However, I still tried it because Alice is leaking the public key in the set of text messages. Basically, in a nutshell, Alice doesn't leak the private key, hence it cannot be decrypted.

Afterwards, I came upon something. I searched "What kind of encryption can be decoded from 2 publically known key values". I got RSA. The reason being e, the PUBLIC exponent and N, the PUBLIC modulus, can be used to ENCRYPT but not DECRYPT. It's quite complicated, but basically math says if N is the product of two insanely large primes, there's no decryption method as you cannot get phi / the totient.

## RSA

Wikipedia explains this pretty well so here's the link: [RSA wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem))

## Approach
But, in this challenge, e can be 17, as that is a valid prime, and N (7663) is the product of two primes, p, and q, but what makes this vulnerable is the fact that N is really small, and p/q are also really small.

Using [this calculator](https://www.alpertron.com.ar/ECM.HTM), I was able to arrive at phi, (along with some useless values of p and q).

![image](https://github.com/realrealAlexS/litctfwriteups/assets/140008493/12ca1225-3c18-4f3d-a782-7f34e39ecb37)

Nice, now I know that Phi (the totient) is 7488. I can use this to decrypt RSA.

I wrote a basic [script](https://github.com/realrealAlexS/litctfwriteups/blob/main/testscript.py) that decrypts RSA given N, e, and phi, (it uses e and phi to calculate d)

However, this prints out something that is obviously NOT the flag, so I knew something was changed.

The low value of N tells us that the plaintext decrypted has to be a number modulo 7663, hence being only about 1 ascii character long. If I wanted a flag, I would have to approach this differently.

After splitting the ciphertext up into 6 strings of 6, I then had the idea to split it into 9 strings of 4. The explanation being, that N's really small, and having a big number mod 7663 and a small number mod 7663 both result in a value under 7663 (one ascii character)

This method worked, with all of my code located here: [solve script](https://github.com/realrealAlexS/litctfwriteups/blob/main/solvescripticecream.py)

```
from Crypto.Util.number import inverse

e = 17
N = 7663
phi = 7488
# Change the ciphertext NINE times, with the first being 7477 and the last being 4183. 
# Basically, repeat this code 9 times, but changing the value of 'ciphertext' 7477, 1776, 4508, 1527, 7300, 2218, 5380, 6736, 4183
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

print(message)
```
This printed out i,C,3,_,c,r,4,e,m.

This is clearly readable plaintext (with meaning), so it's the flag.

![image](https://github.com/realrealAlexS/litctfwriteups/assets/140008493/b1c9a3eb-dbd4-4054-9d2b-1c0f7519d9f4)

## Flag

`LITCTF{ic3_cr4em}`

## Personal Opinion

I thought this challenge was very well made by the developer. It let me have a better understanding of Diffie-Hellman Key Exchange, practice my public-key encryption, and find out tricks to cracking RSA. It was a well made challenge, not very guessy, and quite fun. The infrastructure was pretty well made, and the flag was meaningful and not like `flag{never_gonna_give_u_up`. I hope the XOR chall was kind of similar and I'm interested to see the writeup for that.

## Referenced materials

[Alpertron](https://www.alpertron.com.ar/ECM.HTM)     [LSB Calculator](https://planetcalc.com/9345/)     [wikipedia](wikipedia.org)

### More Stuff

Check out my discord bot which has vulnerabilities! https://sites.google.com/view/intrepidbot
