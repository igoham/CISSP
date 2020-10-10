|Name|Symetric/Asymetrics|Key Lengths|Encryption Rounds| Cipher Type
|----|----|----|----|-----|  
| Data Encryption Algorithm (Lucifer/DES)| Symetric | 64 bits, 56 make up key, 8 bit parity | 16 rounds of confusion and diffusion | Block cipher
| Triple DES | Symetric | 112 bITS |  48 rounds | Block Cipher



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
- Cipher Feedback (CFB)
- Output Feedback (OFB)
- Counter (CTR)
