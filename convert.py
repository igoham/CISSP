test = """
Quick Tips
• System architecture is a formal tool used to design computer systems in a manner
that ensures each of the stakeholders’ concerns is addressed.
• A system’s architecture is made up of different views, which are representations of
system components and their relationships. Each view addresses a different aspect of
the system (functionality, performance, interoperability, security).
• ISO/IEC/IEEE 42010 is an international standard that outlines how system
architecture frameworks and their description languages are to be used.
• A CPU contains a control unit, which controls the timing of the execution of
instructions and data, and an ALU, which performs mathematical functions and
logical operations.
• Memory managers use various memory protection mechanisms, as in base
(beginning) and limit (ending) addressing, address space layout randomization, and
data execution prevention.
• Operating systems use absolute (hardware addresses), logical (indexed addresses), and
relative address (indexed addresses, including offsets) memory schemes.
• Buffer overflow vulnerabilities are best addressed by implementing bounds checking.
• A garbage collector is a software tool that releases unused memory segments to help
prevent “memory starvation.”
• Different processor families work within different microarchitectures to execute
specific instruction sets.
• Early operating systems were considered “monolithic” because all of the code worked
within one layer and ran in kernel mode, and components communicated in an ad
hoc manner.
• Operating systems can work within the following architectures: monolithic kernel,
layered, microkernel, or hybrid kernel.
• Mode transition is when a CPU has to switch from executing one process’s
instructions running in user mode to another process’s instructions running in kernel
mode.
• CPUs provide a ringed architecture, which operating systems run within. The more
565
trusted processes run in the lower-numbered rings and have access to all or most of
the system resources. Nontrusted processes run in higher-numbered rings and have
access to a smaller amount of resources.
• Operating system processes are executed in privileged mode (also called kernel or
supervisor mode), and applications are executed in user mode, also known as
“problem state.”
• Virtual memory combines RAM and secondary storage so the system seems to have a
larger bank of memory.
• The more complex a security mechanism is, the less amount of assurance it can
usually provide.
• The trusted computing base (TCB) is a collection of system components that
enforces the security policy directly and protects the system. These components are
within the security perimeter.
• Components that make up the TCB are hardware, software, and firmware that
provide some type of security protection.
• A security perimeter is an imaginary boundary that has trusted components within it
(those that make up the TCB) and untrusted components outside it.
• The reference monitor concept is an abstract machine that ensures all subjects have
the necessary access rights before accessing objects. Therefore, it mediates all access to
objects by subjects.
• The security kernel is the mechanism that actually enforces the rules of the reference
monitor concept.
• The security kernel must isolate processes carrying out the reference monitor concept,
must be tamperproof, must be invoked for each access attempt, and must be small
enough to be properly tested.
• Processes need to be isolated, which can be done through segmented memory
addressing, encapsulation of objects, time multiplexing of shared resources, naming
distinctions, and virtual mapping.
• The level of security a system provides depends upon how well it enforces its security
policy.
• A closed system is often proprietary to the manufacturer or vendor, whereas an open
system allows for more interoperability.
• The Common Criteria was developed to provide globally recognized evaluation
criteria.
• The Common Criteria uses protection profiles, security targets, and ratings (EAL1 to
EAL7) to provide assurance ratings for targets of evaluation (TOEs).
• Certification is the technical evaluation of a system or product and its security
components. Accreditation is management’s formal approval and acceptance of the
security provided by a system.
• ISO/IEC 15408 is the international standard that is used as the basis for the
evaluation of security properties of products under the CC framework.
566
• Process isolation ensures that multiple processes can run concurrently and the
processes will not interfere with each other or affect each other’s memory segments.
• TOC/TOU stands for time-of-check/time-of-use. This is a class of asynchronous
attacks.
• A distributed system is a system in which multiple computing nodes, interconnected
by a network, exchange information for the accomplishment of collective tasks.
• Cloud computing is the use of shared, remote computing devices for the purpose of
providing improved efficiencies, performance, reliability, scalability, and security.
• Software as a Service (SaaS) is a cloud computing model that provides users access to
a specific application that executes on the service provider’s environment.
• Platform as a Service (PaaS) is a cloud computing model that provides users access to
a computing platform that is typically built on a server operating system, but not the
virtual machine on which it runs.
• Infrastructure as a Service (IaaS) is a cloud computing model that provides users
unfettered access to a cloud device, such as an instance of a server, which includes
both the operating system and the virtual machine on which it runs.
• Parallel computing is the simultaneous use of multiple computers to solve a specific
task by dividing it among the available computers.
• Any system in which computers and physical devices collaborate via the exchange of
inputs and outputs to accomplish a task or objective is a cyber-physical system.
• Cryptography is the science of protecting information by encoding it into an
unreadable format.
• The most famous rotor encryption machine is the Enigma used by the Germans in
World War II.
• A readable message is in a form called plaintext, and once it is encrypted, it is in a
form called ciphertext.
• Cryptographic algorithms are the mathematical rules that dictate the functions of
enciphering and deciphering.
• Cryptanalysis is the study of breaking cryptosystems.
• Nonrepudiation is a service that ensures the sender cannot later falsely deny sending a
message.
• Key clustering is an instance in which two different keys generate the same ciphertext
from the same plaintext.
• The range of possible keys is referred to as the keyspace. A larger keyspace and the full
use of the keyspace allow for more random keys to be created. This provides more
protection.
• The two basic types of encryption mechanisms used in symmetric ciphers are
substitution and transposition. Substitution ciphers change a character (or bit) out for
another, while transposition ciphers scramble the characters (or bits).
• A polyalphabetic cipher uses more than one alphabet to defeat frequency analysis.
567
• Steganography is a method of hiding data within another media type, such as a
graphic, WAV file, or document. This method is used to hide the existence of the
data.
• A key is a random string of bits inserted into an encryption algorithm. The result
determines what encryption functions will be carried out on a message and in what
order.
• In symmetric key algorithms, the sender and receiver use the same key for encryption
and decryption purposes.
• In asymmetric key algorithms, the sender and receiver use different keys for
encryption and decryption purposes.
• Symmetric key processes provide barriers of secure key distribution and scalability.
However, symmetric key algorithms perform much faster than asymmetric key
algorithms.
• Symmetric key algorithms can provide confidentiality, but not authentication or
nonrepudiation.
• Examples of symmetric key algorithms include DES, 3DES, Blowfish, IDEA, RC4,
RC5, RC6, and AES.
• Asymmetric algorithms are used to encrypt keys, and symmetric algorithms are used
to encrypt bulk data.
• Asymmetric key algorithms are much slower than symmetric key algorithms, but can
provide authentication and nonrepudiation services.
• Examples of asymmetric key algorithms include RSA, ECC, Diffie-Hellman, El
Gamal, knapsack, and DSA.
• Two main types of symmetric algorithms are stream ciphers and block ciphers.
Stream ciphers use a keystream generator and encrypt a message one bit at a time. A
block cipher divides the message into groups of bits and encrypts them.
• Many algorithms are publicly known, so the secret part of the process is the key. The
key provides the necessary randomization to encryption.
• Data Encryption Standard (DES) is a block cipher that divides a message into 64-bit
blocks and employs S-box-type functions on them.
• Because technology has allowed the DES keyspace to be successfully broken, TripleDES (3DES) was developed to be used instead. 3DES uses 48 rounds of computation
and up to three different keys.
• International Data Encryption Algorithm (IDEA) is a symmetric block cipher with a
key of 128 bits.
• RSA is an asymmetric algorithm developed by Rivest, Shamir, and Adleman and is
the de facto standard for digital signatures.
• Elliptic curve cryptosystems (ECCs) are used as asymmetric algorithms and can
provide digital signature, secure key distribution, and encryption functionality. They
use fewer resources, which makes them better for wireless device and cell phone
encryption use.
568
• When symmetric and asymmetric key algorithms are used together, this is called a
hybrid system. The asymmetric algorithm encrypts the symmetric key, and the
symmetric key encrypts the data.
• A session key is a symmetric key used by the sender and receiver of messages for
encryption and decryption purposes. The session key is only good while that
communication session is active and then it is destroyed.
• A public key infrastructure (PKI) is a framework of programs, procedures,
communication protocols, and public key cryptography that enables a diverse group
of individuals to communicate securely.
• A certificate authority (CA) is a trusted third party that generates and maintains user
certificates, which hold their public keys.
• The CA uses a certification revocation list (CRL) to keep track of revoked certificates.
• A certificate is the mechanism the CA uses to associate a public key to a person’s
identity.
• A registration authority (RA) validates the user’s identity and then sends the request
for a certificate to the CA. The RA cannot generate certificates.
• A one-way function is a mathematical function that is easier to compute in one
direction than in the opposite direction.
• RSA is based on a one-way function that factors large numbers into prime numbers.
Only the private key knows how to use the trapdoor and how to decrypt messages
that were encrypted with the corresponding public key.
• Hashing algorithms provide data integrity only.
• When a hash algorithm is applied to a message, it produces a message digest, and this
value is signed with a private key to produce a digital signature.
• Some examples of hashing algorithms include SHA-1, SHA-2, SHA-3, MD4, and
MD5.
• SHA produces a 160-bit hash value and is used in DSS.
• A birthday attack is an attack on hashing functions through brute force. The attacker
tries to create two messages with the same hashing value.
• A one-time pad uses a pad with random values that are XORed against the message to
produce ciphertext. The pad is at least as long as the message itself and is used once
and then discarded.
• A digital signature is the result of a user signing a hash value with a private key. It
provides authentication, data integrity, and nonrepudiation. The act of signing is the
actual encryption of the value with the private key.
• Examples of algorithms used for digital signatures include RSA, El Gamal, ECDSA,
and DSA.
• Key management is one of the most challenging pieces of cryptography. It pertains to
creating, maintaining, distributing, and destroying cryptographic keys.
• Crime Prevention Through Environmental Design (CPTED) combines the physical
569
environment and sociology issues that surround it to reduce crime rates and the fear
of crime.
• The value of property within the facility and the value of the facility itself need to be
ascertained to determine the proper budget for physical security so that security
controls are cost effective.
• Some physical security controls may conflict with the safety of people. These issues
need to be addressed; human life is always more important than protecting a facility
or the assets it contains.
• When looking at locations for a facility, consider local crime; natural disaster
possibilities; and distance to hospitals, police and fire stations, airports, and railroads.
• Exterior fencing can be costly and unsightly, but can provide crowd control and help
control access to the facility.
• If interior partitions do not go all the way up to the true ceiling, an intruder can
remove a ceiling tile and climb over the partition into a critical portion of the facility.
• The primary power source is what is used in day-to-day operations, and the
alternative power source is a backup in case the primary source fails.
• Smoke detectors should be located on and above suspended ceilings, below raised
floors, and in air ducts to provide maximum fire detection.
• A fire needs high temperatures, oxygen, and fuel. To suppress it, one or more of those
items needs to be reduced or eliminated.
• Gases like FM-200 and other halon substitutes interfere with the chemical reaction of
a fire.
• Portable fire extinguishers should be located within 50 feet of electrical equipment
and should be inspected quarterly.
• CO2
is a colorless, odorless, and potentially lethal substance because it removes the
oxygen from the air in order to suppress fires.
• CPTED provides three main strategies, which are natural access control, natural
surveillance, and natural territorial reinforcement.
• Window types that should be understood are standard, tempered, acrylic, wired, and
laminated.
"""

test = test.replace("•", "-")
x=1