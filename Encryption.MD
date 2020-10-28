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



**Can RSA be used for secure key exchange**



**Review common crytoanalysis attacks**
![MULTI TASKING](https://gyazo.com/f56b0e183b53db9d58d4988c00b7a9b4.png)
![MULTI TASKING](https://gyazo.com/f56b0e183b53db9d58d4988c00b7a9b4.png)
![MULTI TASKING](https://gyazo.com/a8e7efb09bb0a65c63675412bf0b307a.png)



# Asymmetric Encryption

- Diffie Hellman
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

- HMAC
    - Joins the message with a symetric key pror to hashing the message. This creates a MAC that can be send wlong with the encrypted message
    - Send the MAC along with the message to prove message integrity 
    