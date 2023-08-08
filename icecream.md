# icecream

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

![image](https://github.com/realrealAlexS/litctfwriteups/assets/140008493/7dc8c255-56f0-4571-9ac9-993b4b68fe01)
^Ice Cream

I downloaded the text messages html, which showed me this below image
![image](https://github.com/realrealAlexS/litctfwriteups/assets/140008493/e8abea16-981a-4eb6-abfc-7f87da2980c1)

WOAH. There's a lot of hints in this pair of text messages. First, I quickly knew that the image must have Least-Significant-Bit steghide in it. 

After decoding the image with the help of [this calculator](https://planetcalc.com/9345/), I found out that the message was 747717764508152773002218538067364183.

NICE! We're making quick progress! The next part took 7.5 entire hours though.

First, from the Alice and Bob I'm used to, I assumed this was DHKE (Diffie-Hellman Key Exchange). However, the only values Alice would give Bob in this scenario are capital A, p, and g. I tried this, but it doesn't work.

Next, I tried public key encryption. There's no need to go into detail because it's not right in the end. However, this is a valid assumption by me as Alice is leaking the public key in the set of text messages.

Afterwards, I came upon something. I searched "What kind of encryption was 2 publically known key values". I got RSA. The reason is e, the PUBLIC exponent and N, the PUBLIC modulus, can be used to ENCRYPT but not DECRYPT. It's quite complicated, but basically math says if N is the product of two insanely large primes, there's no decryption method as you cannot get phi / the totient.

HOWEVER, in this challenge, e can be 17, as that is a valid prime, and N (7663) is the product of two primes, p, and q, but what makes this vulnerable is the fact that N is really small, and p/q are also really small.

Using [this calculator](https://www.alpertron.com.ar/ECM.HTM), I was able to arrive at phi, (along with some useless values of p and q).

![image](https://github.com/realrealAlexS/litctfwriteups/assets/140008493/12ca1225-3c18-4f3d-a782-7f34e39ecb37)

Nice, now I know that Phi (the totient) is 7488. I can use this to decrypt RSA.

I wrote a basic [script](https://github.com/realrealAlexS/litctfwriteups/blob/main/testscript.py) that decrypts RSA given N, e, and phi, (it uses e and phi to calculate d)

However, this prints out something that is obviously NOT the flag, so I knew something was changed.

The low value of N tells us that the plaintext decrypted has to be a number modulo 7663, hence being only about 1 ascii character long. If I wanted a flag, I would have to approach this differently.

After splitting the ciphertext up into 6 strings of 6, I then had the idea to split it into 9 strings of 4.

This method worked, with all of my code located here: [solve script](https://github.com/realrealAlexS/litctfwriteups/blob/main/solvescripticecream.py)

This printed out i,C,3,_,c,r,4,e,m.

This is clearly readable plaintext, so it's the flag. I submitted succesfully!

![image](https://github.com/realrealAlexS/litctfwriteups/assets/140008493/b1c9a3eb-dbd4-4054-9d2b-1c0f7519d9f4)



## Flag

`LITCTF{ic3_cr4em}`

---

## Referenced materials

[Alpertron](https://www.alpertron.com.ar/ECM.HTM) [LSB Calculator](https://planetcalc.com/9345/)
