**Encrpytion Keys**
- The number of keys for a specific keyspace can be determined by doing 2^N where N = key length in bits
    - If the keyspace is 5 bits long how many possible keys
        - 32
- The number of keys required to connect N parties using symmetric crypto is given by the forumal -( N * (N-1))/2
    - How many encryption keys are required to implement a symmetric algorithm with 12 participants?
        - 66
- For Asymmetric keys the formula is 2n
    - if there are 10 particians you need 20 keys
    
    
- Triple DES works in two modes: Number of modes dictates steps of encryption
    - Two key more
    - Three key mode
    - If only ONE key is used it is a very weak cipher
        - Never use one key with 3des!!!!

# Symmetric Encryption

As described earlier in the chapter, using purely symmetric key cryptography has three
drawbacks, which affect the following:
- Security services Purely symmetric key cryptography provides confidentiality only,
not authentication or nonrepudiation.
- Scalability As the number of people who need to communicate increases, so does the
number of symmetric keys required, meaning more keys must be managed.
- Secure key distribution The symmetric key must be delivered to its destination
through a secure courier.

|Name|Symetric/Asymetrics|Key Lengths|Encryption Rounds| Cipher Type | Block Size | notes
|----|----|----|----|-----|-----|----|
| Data Encryption Algorithm (Lucifer/DES)| Symetric | 64 bits, 56 make up key, 8 bit parity | 16 rounds of confusion and diffusion | Block cipher
| Triple DES | Symetric | 112 bITS |  48 rounds | Block Cipher
| AES | Symetric | 128, 192, 256 | 128 bits = 10 rounds, 192 bits = 12, 256 bits = 14 | Block Cipher
| Internation Data Encrpytion Algorithm (IDEA) | | 64 bit blocks, then divided into 8 bit blocks |  8 rounds on each 8 bit block | Block Cipher
| Blowfish | Symetric | 64 bit blocks | 32 - 448 bits | 16 runds | Block Cipher
| RC4 |  Symetric | ? | ? | Stream | 2
| RC5 |  Symetric | up to 2041 bits |? | Block | 32/64/128 bits
| RC6 |  Symetric | up to 2041 bits |? |? | 32/64/128 bits | Built on RC5



### DES Modes
Block ciphers have several modes of operation. Each mode specifies how a block cipher will
operate. One mode may work better in one type of environment for specific functionality,
whereas another mode may work better in another environment with totally different
requirements. *It is important that vendors who employ DES (or any block cipher)
understand the different modes and which one to use for which purpose.*

- Electronic Code Book (ECB)
    - The is simply a code book that instructs the block Cipher on how to encrypt that block of data.
    - This is the last security mode BUT the fastest
    - so we use it to encrypt small amounts of data, such as PINs, challenge-response values in authentication processes, and encrypting keys.
    - Not to be used on large amounts of data as it does NOT use chaining


- Cipher Block Chaining (CBC)
    - IV is used for the first block. This 64 bit IV is XOR'ed against the first block
    - The results of Cipher Text 1 are XORed with Plain text 2 before encryption. This chains them together and ensures
    That the same two peices of text are random.
    - A different inital IV will result in different CIphertext even if the message is identical
    
- Cipher Feedback (CFB)
    - Cipher feed back mode acts as a stream cipher rather than a block ciper
    - Since this mode is used to send 8 bits of data at a time, a block cipher won't work as there is not enough data
    - An IV  is used in correlation with the key to create the keystream
    - the Cipher text is then used with the key to create the keystream
    
- Output Feedback (OFB)
    - Rather than relying on the output of the previous block being encrypted we use the keystream to generate the next IV
    
- Counter (CTR)
    - iters the IV by 1 rather than using any sort of prevous output
    - Can be run in parallel 

### Hash Lengths
|Name|Digest Length| Block Size|
|---|----|----|
|MD5| 128 Bits| 512 bits
SHA256| 256 Bits | 512 Bits
SHA384| 384 Bits | 512 Bits
SHA512| 512 Bits | 512 Bits

# Asymmetric Encryption

- When using Asymmetric encryption the sender encrypts the message with the recipients public key.
- The recipient uses their private key to decrypt.
- This ensures that ONLY the intended recipient of the message can read it thus enforcing confidentiality.


- Diffie Hellman
    - https://www.khanacademy.org/computing/computer-science/cryptography/modern-crypt/v/diffie-hellman-key-exchange-part-2
    - Used for key Agreement
    - Can be used by two parties that have never interacted with each other previously 

- RSA
    - Works by creating a very large number and factoring two primes of that number. That primes are then used in encryption and decryption processess
    - Can be used for Key Exchange NOT key agreement
    - Most commonly used with DES

- El Gamal
    - Used for digital signatures, Encryption and Key Exchange
    - Based on calculating discrete logarithms in a finite field
    - All of the same functionality but its slower
    
- ECC - Elliptic Curve
    - Provides digital signatures, secure key distribution, and encryption
    - More efficient and can be used on devices with little CPU
    
- Knapsack
    - Over the years, different versions of knapsack algorithms have arisen. The first to be
    developed, Merkle-Hellman, could be used only for encryption, but it was later improved
    upon to provide digital signature capabilities. These types of algorithms are based on the
    “knapsack problem,” a mathematical dilemma that poses the following question: If you
    have several different items, each having its own weight, is it possible to add these items to a
    knapsack so the knapsack has a specific weight?

- Zero Knowledge Proof
    - When military representatives are briefing the news media about some big world event,
they have one goal in mind: Tell the story that the public is supposed to hear and nothing
more. Do not provide extra information that someone could use to infer more information
than they are supposed to know. The military has this goal because it knows that not just
the good guys are watching CNN. This is an example of zero knowledge proof. You tell
someone just the information they need to know without “giving up the farm.”
Zero knowledge proof is used in cryptography also. For example, if Irene encrypts
something with her private key, you can verify her private key was used by decrypting the
data with her public key. By encrypting something with her private key, Irene is proving to
you that she has her private key—but she does not give or show you her private key. Irene
485
does not “give up the farm” by disclosing her private key. In a zero knowledge proof, the
verifier cannot prove to another entity that this proof is real because the verifier does not
have the private key to prove it. So, only the owner of the private key can prove she has
possession of the key



# One Way Hashes

- MAC - Message Authentication Code
    - A MAC function is an authentication scheme derived by applying a secret key to a
message in some form. This does not mean the symmetric key is used to encrypt the
message, though. 
    - You should be aware of three basic types of MAC functions: a hash MAC
(HMAC), CBC-MAC, and CMAC.


![MULTI TASKING](https://gyazo.com/eadef5dc04ec38e50a484e2c80f1a29d.png)

**The Diffie-Hellman key exchange & RSA**
the Diffie-Hellman key exchange is often implemented alongside RSA or other algorithms to provide authentication for the connection. If you are familiar with RSA, you may be wondering why anyone would bother using the Diffie-Hellman key exchange as well, since RSA enables parties who have never previously met to communicate securely

Instead, RSA is often only used as a means to authenticate both parties. It does this with the digital certificates of each party, which will have been verified by a certificate authority to prove that a certificate owner is truly who they say they are, and that the public key on the certificate actually belongs to them.

For mutual authentication, each party will sign a message using their private key and then send it to their communication partner. Each recipient can then verify the identity of the other party by checking the signed messages against the public key on their communication partner’s digital certificate (see the above-mentioned article on RSA for more detail on how this works, particularly the Signing messages section).

Now that both parties have been authenticated, it’s technically possible to continue using RSA to safely send encrypted messages between themselves, however it would end up being too inefficient.

To get around this inefficiency, many security protocols use an algorithm such as the Diffie-Hellman key exchange to come up with a common secret that can be used to establish a shared symmetric-key. This symmetric key is then used in a symmetric-key algorithm, such as AES, to encrypt the data that the two parties intend to send securely between themselves.

It may seem like a complex and convoluted process, but it ends up being much quicker and less-demanding on resources when compared to using a public-key algorithm for the whole exchange. This is because symmetric-key encryption is orders of magnitude more efficient than public-key encryption.

In addition to the inefficiencies that we just mentioned, there are some other downsides that would come from solely using RSA. RSA needs padding to make it secure, so an additional algorithm would need to be implemented appropriately alongside it to make it safe.

RSA doesn’t provide perfect forward secrecy, either, which is another disadvantage when compared to the ephemeral Diffie-Hellman key exchange. Collectively, these reasons are why, in many situations, it’s best to only apply RSA in conjunction with the Diffie-Hellman key exchange.

Alternatively, the Diffie-Hellman key exchange can be combined with an algorithm like the Digital Signature Standard (DSS) to provide authentication, key exchange, confidentiality and check the integrity of the data. In such a situation, RSA is not necessary for securing the connection.


**ElGamal**

ElGamal is a public-key algorithm built on top of the Diffie-Hellman key exchange. Like Diffie-Hellman, it contains no provisions for authentication on its own, and is generally combined with other mechanisms for this purpose.

ElGamal was mainly used in PGP, GNU Privacy Guard and other systems because its main rival, RSA, was patented. RSA’s patent expired in 2000, which allowed it to be implemented freely after that date. Since then, ElGamal has not been implemented as frequently.


**Review common crytoanalysis attacks**


![MULTI TASKING](https://gyazo.com/f56b0e183b53db9d58d4988c00b7a9b4.png)
![MULTI TASKING](https://gyazo.com/f56b0e183b53db9d58d4988c00b7a9b4.png)
![MULTI TASKING](https://gyazo.com/a8e7efb09bb0a65c63675412bf0b307a.png)

**ECC and ECDSA**

Elliptic Curve Cryptography (ECC) or Elliptic Curve Digital Signature Algorithm (ECDSA) was known and studied in the world of mathematics for 150 years before being applied to cryptography; Neal Koblitz and Victor S. Miller originally suggested it in 1985. However, in 2005, the NSA released a new set of U.S. government-endorsed security algorithms that also included ECC, in a release entitled “Suite B”.

Elliptic curve cryptography is a new cryptographic algorithm that has been developed for increased security and more robust network performance. Some researchers have claimed that ECC cryptography can provide as much strong security with a 164-bit key as other systems achieve with a 1024-bit key. With the advent of mobile devices being used for highly private transactions, more secure, low-overhead encryption schemes are becoming highly desirable. ECC cryptography helps to establish a level security equal to or greater than RSA or DSA, the two most widely-adopted encryption methods – and it does it with less computational overhead, requiring less processing power, and moving well beyond the mobile sphere in implementation.

ECDSA (Elliptic Curve Digital Signature Algorithm) is based on DSA, but uses yet another mathematical approach to key generation. ECC is a mathematical equation taken on its own, but ECDSA is the algorithm that is applied to ECC to make it appropriate for security encryption. Like RSA and DSA, it is another asymmetric cryptographic scheme, but in ECC, the equation defines the public/private key pair by operations on points of elliptic curves, instead of describing it as the product of very large prime numbers.



**What is a birthday attack?**

*Used to cause collisions in hash functions*

A birthday attack is a type of cryptographic attack that exploits the mathematics behind the birthday problem in probability theory. This attack can be used to abuse communication between two or more parties. The attack depends on the higher likelihood of collisions found between random attack attempts and a fixed degree of permutations (pigeonholes). With a birthday attack, it is possible to find a collision of a hash function in 2 n = 2 n / 2 {\textstyle {\sqrt {2^{n}}}=2^{n/2}} {\textstyle {\sqrt {2^{n}}}=2^{n/2}}, with 2 n {\textstyle 2^{n}} {\textstyle 2^{n}} being the classical preimage resistance security. There is a general (though disputed[1]) result that quantum computers can perform birthday attacks, thus breaking collision resistance, in 2 n 3 = 2 n / 3 {\textstyle {\sqrt[{3}]{2^{n}}}=2^{n/3}} {\textstyle {\sqrt[{3}]{2^{n}}}=2^{n/3}}.[2]
