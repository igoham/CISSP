**Authentication**

Authentication:

    “Prove you are Thor”. – Should always be done with Multifactor Authentication!
    Something you know – Type 1 Authentication (passwords, pass phrase, PIN etc.).
    Something you have – Type 2 Authentication (ID, Passport, Smart Card, Token, cookie on PC etc.).
    Something you are – Type 3 Authentication (and Biometrics) (Fingerprint, Iris Scan, Facial geometry etc.).
    Somewhere you are – Type 4 Authentication (IP/MAC Address).
    Something you do – Type 5 Authentication (Signature, Pattern unlock).



**What humiditity and tempatures are acceptable for a data center**

Server rooms  should be 68 (20*C) - 71(21.6*C) degrees Fahrenheit. The data center should be between 40% and 60% humidity.

**What layer does DNS and DHCP operate at?**

- DNS is an Application layer protocol
- DHCP works on the Data-link layer. This means that when a device needs an IP address they can only request one on the same network that its present on

**What is a birthday attack?**

*Used to cause collisions in hash functions*

A birthday attack is a type of cryptographic attack that exploits the mathematics behind the birthday problem in probability theory. This attack can be used to abuse communication between two or more parties. The attack depends on the higher likelihood of collisions found between random attack attempts and a fixed degree of permutations (pigeonholes). With a birthday attack, it is possible to find a collision of a hash function in 2 n = 2 n / 2 {\textstyle {\sqrt {2^{n}}}=2^{n/2}} {\textstyle {\sqrt {2^{n}}}=2^{n/2}}, with 2 n {\textstyle 2^{n}} {\textstyle 2^{n}} being the classical preimage resistance security. There is a general (though disputed[1]) result that quantum computers can perform birthday attacks, thus breaking collision resistance, in 2 n 3 = 2 n / 3 {\textstyle {\sqrt[{3}]{2^{n}}}=2^{n/3}} {\textstyle {\sqrt[{3}]{2^{n}}}=2^{n/3}}.[2]

**How does CVSS scoring work in detail?**

- Open framework for communicating the characteristics and severity software vulnerabilities


![PASTA](https://gyazo.com/2c81f9a026cad844b856b0b5f77cedeb.png)

- Base - Consistent over time and across environments (Affects all the same way)
- Temporal - characteristics that change over time
- Environmental - Unique to a users envrioment 


**What is an object oriented database?**

An object-oriented database (OODBMS) or object database management system (ODBMS) is a database that is based on object-oriented programming (OOP). The data is represented and stored in the form of objects. OODBMS are also called object databases or object-oriented database management systems.

ZODB *(ZOPE DB)* for Python is an example of a OODBMS

**What is the different between Multi-Tasking, m-threading, m-procressing and pipelining**


    Multiprogramming – A computer running more than one program at a time (like running Excel and Firefox simultaneously).
    Multiprocessing – A computer using more than one CPU at a time.
    Multitasking – Tasks sharing a common resource (like 1 CPU).
    Multithreading is an extension of multitasking.

*Multi Programming* - In a modern computing system, there are usually several concurrent application processes which want to execute. Now it is the responsibility of the Operating System to manage all the processes effectively and efficiently.
One of the most important aspects of an Operating System is to multi program.
In a computer system, there are multiple processes waiting to be executed, i.e. they are waiting when the CPU will be allocated to them and they begin their execution. These processes are also known as jobs. Now the main memory is too small to accommodate all of these processes or jobs into it. Thus, these processes are initially kept in an area called job pool. This job pool consists of all those processes awaiting allocation of main memory and CPU.
CPU selects one job out of all these waiting jobs, brings it from the job pool to main memory and starts executing it. The processor executes one job until it is interrupted by some external factor or it goes for an I/O task.

**The main idea of multi programming is to maximize the CPU time.**

*Multi Tasking* - Multitasking is a logical extension of multi programming. The major way in which multitasking differs from multi programming is that multi programming works solely on the concept of context switching whereas multitasking is based on time sharing alongside the concept of context switching.

![MULTI TASKING](https://gyazo.com/9eef70f19cdaac3d661cf1ffaee65645.png)


**What is Data execution prevention DEP and Heap metadata protection. Touch up on ALSR (brief) = Pointer Encoding?**

Data Execution Prevention (DEP) is a system-level memory protection feature that is built into the operating system starting with Windows XP and Windows Server 2003. DEP enables the system to mark one or more pages of memory as non-executable. Marking memory regions as non-executable means that code cannot be run from that region of memory, which makes it harder for the exploitation of buffer overruns.

DEP prevents code from being run from data pages such as the default heap, stacks, and memory pools. If an application attempts to run code from a data page that is protected, a memory access violation exception occurs, and if the exception is not handled, the calling process is terminated.
*heap metadata protection* - aa
*Function pointer encoding* - Function pointers (e.g. CommitRoutine) in heap data structures are encoded with a random value to prevent them from being replaced with an untrusted value. 

**Memorize SDLC process**
- Requirements gathering Determine why to create this software, what the software
will do, and for whom the software will be created
- Design Deals with how the software will accomplish the goals identified, which are
encapsulated into a functional design
- Development Programming software code to meet specifications laid out in the
design phase and integrating that code with existing systems and/or libraries
- Testing Verifying and validating software to ensure that the software works as
planned and that goals are met
- Operations and maintenance Deploying the software and then ensuring that it is
properly configured, patched, and monitored



**Review all SCAP components**

Starting with SCAP version 1.0 (November, 2009)
* CVE - Common Vulnerabilities and Exposures - http://cve.mitre.org/ 
* CCE -  Common Configuration Enumeration (CCE) - http://cce.mitre.org/
* CPE - Common Platform Enumeration - http://scap.nist.gov/specifications/cpe/  
* CVSS - Common Vulnerability Scoring System - http://www.first.org/cvss/ 
* XCCDF - Extensible Configuration Checklist Description Format - http://scap.nist.gov/specifications/xccdf/
* OVAL - Open Vulnerability and Assessment Language - [http://oval.mitre.org/ (OVAL)]
Starting with SCAP version 1.1 (February, 2011)
* OCIL - Open Checklist Interactive Language - http://scap.nist.gov/specifications/ocil/  
Starting with SCAP version 1.2 (September, 2011)
* AID - Asset Identification - [http://scap.nist.gov/specifications/ai/ 
* ARF - Asset Reporting Format - http://scap.nist.gov/specifications/arf/ 
* CCSS - Common Configuration Scoring System - http://csrc.nist.gov/publications/PubsNISTIRs.html#NIST-IR-7502 
* TMSAD - Trust Model for Security Automation Data - http://scap.nist.gov/specifications/tmsad/ 
Starting with SCAP version 1.3 (February, 2018)
* SWID - Software Identification - https://csrc.nist.gov/projects/Software-Identification-SWID 

**What is a pharming attack**

Pharming is a cyberattack intended to redirect a website's traffic to another, fake site. Pharming can be conducted either by changing the hosts file on a victim's computer or by exploitation of a vulnerability in DNS server software

**How can you configure a remote access server to preform a callback?**

**How does IPSec work**
##### ESP
- Transport mode -In transport mode, only the payload of the IP packet is usually encrypted or authenticated. The routing is intact, since the IP header is neither modified nor encrypted; however, when the authentication header is used, the IP addresses cannot be modified by network address translation, as this always invalidates the hash value. The transport and application layers are always secured by a hash, so they cannot be modified in any way, for example by translating the port numbers.

A means to encapsulate IPsec messages for NAT traversal has been defined by RFC documents describing the NAT-T mechanism.
Tunnel mode
Main article: Tunneling protocol

- In tunnel mode, the entire IP packet is encrypted and authenticated. It is then encapsulated into a new IP packet with a new IP header. Tunnel mode is used to create virtual private networks for network-to-network communications (e.g. between routers to link sites), host-to-network communications (e.g. remote user access) and host-to-host communications (e.g. private chat).[33]
Tunnel mode supports NAT traversal. 
##### AH

##### Security association

The IPsec protocols use a security association, where the communicating parties establish shared security attributes such as algorithms and keys. As such IPsec provides a range of options once it has been determined whether AH or ESP is used. Before exchanging data the two hosts agree on which algorithm is used to encrypt the IP packet, for example DES or IDEA, and which hash function is used to ensure the integrity of the data, such as MD5 or SHA. These parameters are agreed for the particular session, for which a lifetime must be agreed and a session key.[28]

The algorithm for authentication is also agreed before the data transfer takes place and IPsec supports a range of methods. Authentication is possible through pre-shared key, where a symmetric key is already in the possession of both hosts, and the hosts send each other hashes of the shared key to prove that they are in possession of the same key. IPsec also supports public key encryption, where each host has a public and a private key, they exchange their public keys and each host sends the other a nonce encrypted with the other host's public key. Alternatively if both hosts hold a public key certificate from a certificate authority, this can be used for IPsec authentication.[29]

The security associations of IPsec are established using the Internet Security Association and Key Management Protocol (ISAKMP). ISAKMP is implemented by manual configuration with pre-shared secrets, Internet Key Exchange (IKE and IKEv2), Kerberized Internet Negotiation of Keys (KINK), and the use of IPSECKEY DNS records.[19][30][31] RFC 5386 defines Better-Than-Nothing Security (BTNS) as an unauthenticated mode of IPsec using an extended IKE protocol. C. Meadows, C. Cremers, and others have used Formal Methods to identify various anomalies which exist in IKEv1 and also in IKEv2.[32]

In order to decide what protection is to be provided for an outgoing packet, IPsec uses the Security Parameter Index (SPI), an index to the security association database (SADB), along with the destination address in a packet header, which together uniquely identifies a security association for that packet. A similar procedure is performed for an incoming packet, where IPsec gathers decryption and verification keys from the security association database.

For IP multicast a security association is provided for the group, and is duplicated across all authorized receivers of the group. There may be more than one security association for a group, using different SPIs, thereby allowing multiple levels and sets of security within a group. Indeed, each sender can have multiple security associations, allowing authentication, since a receiver can only know that someone knowing the keys sent the data. Note that the relevant standard does not describe how the association is chosen and duplicated across the group; it is assumed that a responsible party will have made the choice. 

##### Cryptographic algorithms

Cryptographic algorithms defined for use with IPsec include:

    HMAC-SHA1/SHA2 for integrity protection and authenticity.
    TripleDES-CBC for confidentiality
    AES-CBC for confidentiality.
    AES-GCM providing confidentiality and authentication together efficiently.
    ChaCha20 + Poly1305 providing confidentiality and authentication together efficiently.

**What are type 1 and 2 for biomeethics errors?**

- A type 1 error is a false positice
- A type 2 error is a false negative


**What are the differentces bettwen CSMA/CA and CSMA/CD**

*CSMA/CA*

CSMA/CA stands for Carrier Sense Multiple Access/ Collision Avoidance. It is a network protocol for transmission. It operates in the Medium Access Control Layer. This protocol is effective before the collision.

*CSMA/CD*

CSMA/CD stands for Carrier Sense Multiple Access/ Collision Detection. It is also a network protocol for transmission and operates in the Medium Access Control Layer. In this protocol, each station senses the collision by broadcast sensing. In case of collision, the transmission is stopped and they send a jam signal and then wait for a random time context before retransmission.
![MULTI TASKING](https://gyazo.com/8f5b4455c396c553b89475a5465ec1b5.png)


What are no the differences between Multilevel, compartmented, systemhigh and dedicated
**OSI to TCP/IP Darpa Model**
![OSI to TCP IP models](https://gyazo.com/ab0362ff7c33f7648122d4bc0fdd0f94.png)

**How does change management and Configuration management interface**

##### The change management plan oversees  how any change to the “process” should be done.

##### The configuration management oversees how any change to the “product” should be done.

The Key Elements of Configuration Management are:

- Version Control
    - The ablity to check the work into a common repository, retrieve it anytime to see any changes done by anyone, and maintain full version history.
- Baseline and release information
    - When was the last version released, what did it contain, and having a baseline version to deploy at any time.
- Audits & Review
    - Audit of the process to ensure that people are actually following the configuration management and versioning system properly, correctly, consistently.
- Documented Process
    - An agreed upon process by all team members to ensure compliance in actual implementation. No point having a great system that no one uses or uses it at random.
- Build, Integrate and Deploy Scripts:
    - Common, standard scripts that automate the work of building, testing, integrating, deploying, and removing manual errors from the process. Standardization of the processes and its implementation is the key here.

Which Symetric and Asymetric algorithms are the strongest
What is a Micro kernel and how is it used in a TCB
**What is a DataGram**

A datagram is a basic transfer unit associated with a packet-switched network

Each datagram has two components, a header and a data payload. The header contains all the information sufficient for routing from the originating equipment to the destination without relying on prior exchanges between the equipment and the network. Headers may include source and destination addresses as well as a type field. The payload is the data to be transported. This process of nesting data payloads in a tagged header is called encapsulation.
![OSI to TCP IP models](https://gyazo.com/9823118ba732fe0c677cbc3ac948159f.png)

What are the different wireless modes a client can use to connect to enterprise wifi network
Are there any other populat x.XXx eg x.509 standards that are popular
What is x.400
Treatdrop vs Fraggle attack
What is the CRC used for in ethernet
What are the ESP and AH modes and how are they commonly used together - ESP tunnel vs Transfer modes
What is the average tempature and humidity for a server toom
What are the relevant US and EU laws around privacy

**Define the following terms**
- Trademark
- Copyright
- IP
- Patent

**Which algorithms are strongest bit for bit**
**What is a meet in the middle attack**

The meet-in-the-middle attack (MITM), a known plaintext attack[1], is a generic space–time tradeoff cryptographic attack against encryption schemes that rely on performing multiple encryption operations in sequence. The MITM attack is the primary reason why Double DES is not used and why a Triple DES key (168-bit) can be bruteforced by an attacker with 256 space and 2112 operations.

Diffie and Hellman first proposed the meet-in-the-middle attack on a hypothetical expansion of a block cipher in 1977.[4] Their attack used a space–time tradeoff to break the double-encryption scheme in only twice the time needed to break the single-encryption scheme. 

he MITM is a generic attack which weakens the security benefits of using multiple encryptions by storing intermediate values from the encryptions or decryptions and using those to improve the time required to brute force the decryption keys. This makes a Meet-in-the-Middle attack (MITM) a generic space–time tradeoff cryptographic attack.

The MITM attack attempts to find the keys by using both the range (ciphertext) and domain (plaintext) of the composition of several functions (or block ciphers) such that the forward mapping through the first functions is the same as the backward mapping (inverse image) through the last functions, quite literally meeting in the middle of the composed function. For example, although Double DES encrypts the data with two different 56-bit keys, Double DES can be broken with 257 encryption and decryption operations. 


**Certification vs Accredidation**



Accreditation is the formal acceptance of the adequacy of a system’s overall security and
functionality by management. The certification information is presented to management,
or the responsible body, and it is up to management to ask questions, review the reports
and findings, and decide whether to accept the product and whether any corrective action
needs to take place

**NOTE**
*Certification is a technical review that assesses the security mechanisms and
evaluates their effectiveness. Accreditation is management’s official acceptance of the
information in the certification process findings.*


Certification is the comprehensive technical evaluation of the security components and their
compliance for the purpose of accreditation. A certification process may use safeguard
evaluation, risk analysis, verification, testing, and auditing techniques to assess the
appropriateness of a specific system

**Review lesser encryption algorithms**
- El Gamal
- Knapscak
- Blowfish
- Twofish
- Skipjack


**Define the following system security modes**
##### Dedicated Security mode

In this mode of operation, all users must have:

    Signed NDA for ALL information on the system.
    Proper clearance for ALL information on the system.
    Formal access approval for ALL information on the system.
    A valid need to know for ALL information on the system.

All users can access ALL data. 

#####  System high security mode

In system high mode of operation, all users must have:

    Signed NDA for ALL information on the system.
    Proper clearance for ALL information on the system.
    Formal access approval for ALL information on the system.
    A valid need to know for SOME information on the system.

All users can access SOME data, based on their need to know. 

##### Compartmented security mode

In this mode of operation, all users must have:

    Signed NDA for ALL information on the system.
    Proper clearance for ALL information on the system.
    Formal access approval for SOME information they will access on the system.
    A valid need to know for SOME information on the system.

All users can access SOME data, based on their need to know and formal access approval. 
##### Multilevel secuirt mode

In multilevel security mode of operation (also called Controlled Security Mode), all users must have:

    Signed NDA for ALL information on the system.
    Proper clearance for SOME information on the system.
    Formal access approval for SOME information on the system.
    A valid need to know for SOME information on the system.

All users can access SOME data, based on their need to know, clearance and formal access approval 
****
**Research x.509 certificiates**
- Do they use DSS for authentication?


**Define the following Access Control Models**
- Bell-Lapadula Model
- Biba Model
- Clark Wilson Model
- Noneinterference Model
- Brewer nash model
- Graham-Denning Model
- Harrison Ruzzo Ulman Model

**What is a constrained process**

**What is the refernce monitor in the TCB**

**Define the following Definitions**
- Security Policy
- Standards
- Baselines
- Guidelines
- Procedures

**What are the core differences between BCP and DRP**

**What are the stages or steps in a BCP**
**What are the stages or steps in a DRP**
**What are the ISC code of ethics IN ORDER**
**Review public and military classification names**
**Review Memory Types**
**Review x.25 VS ATM vs SONNET vs FDDI**
**Review wireless standards**

For example a,b,c,g,n,ac

**What are the different wireless modes for enterprise**
**Review Cabling**
**Review PBX's**
**What is a take-grant permission model**
**Review IDS / IDPS from domain 5**
**Review remote access topics in book**
**Review federation, SSO, 0auth, SAML, OIDC**
**Review the following access control mechanisms**

- Discretionary Access Control
- Mandatory Access Control
- Role-Based Access Control
- Rule-Based Access Control
- Attribute-Based Access Control
- Constrained User Interfaces
- Remote Access Control Technologies
- Access Control Matrix
- Content-Dependent Access Control
- Context-Dependent Access Control



**Review The Identify and access provisioning live cycle**

**Review the following software Development methodologies**
- Waterfall Methodology
- V-Shaped Methodology
- Prototyping
- Incremental Methodology
- Spiral Methodology
- Rapid Application Development
- Agile Methodologies
- Integrated Product Team
- DevOps

**review rootkits**
**Define the following database terms**

- Atomicity
- Isolation
- Consistency
- Durability


**Kerberos**

**TCP Handshake**
 
1. SYN - Client1 -> Client2
1. SYN-ACK - Client2 -> client 1
1. ACk - Client 1 -> client 2

**What uses start and stop flags in transmission**

**Review alarm sensor types for physical security**

****



Quick Tips
- System architecture is a formal tool used to design computer systems in a manner
that ensures each of the stakeholders’ concerns is addressed.
- A system’s architecture is made up of different views, which are representations of
system components and their relationships. Each view addresses a different aspect of
the system (functionality, performance, interoperability, security).
- ISO/IEC/IEEE 42010 is an international standard that outlines how system
architecture frameworks and their description languages are to be used.
- A CPU contains a control unit, which controls the timing of the execution of
instructions and data, and an ALU, which performs mathematical functions and
logical operations.
- Memory managers use various memory protection mechanisms, as in base
(beginning) and limit (ending) addressing, address space layout randomization, and
data execution prevention.
- Operating systems use absolute (hardware addresses), logical (indexed addresses), and
relative address (indexed addresses, including offsets) memory schemes.
- Buffer overflow vulnerabilities are best addressed by implementing bounds checking.
- A garbage collector is a software tool that releases unused memory segments to help
prevent “memory starvation.”
- Different processor families work within different microarchitectures to execute
specific instruction sets.
- Early operating systems were considered “monolithic” because all of the code worked
within one layer and ran in kernel mode, and components communicated in an ad
hoc manner.
- Operating systems can work within the following architectures: monolithic kernel,
layered, microkernel, or hybrid kernel.
- Mode transition is when a CPU has to switch from executing one process’s
instructions running in user mode to another process’s instructions running in kernel
mode.
- CPUs provide a ringed architecture, which operating systems run within. The more
565
trusted processes run in the lower-numbered rings and have access to all or most of
the system resources. Nontrusted processes run in higher-numbered rings and have
access to a smaller amount of resources.
- Operating system processes are executed in privileged mode (also called kernel or
supervisor mode), and applications are executed in user mode, also known as
“problem state.”
- Virtual memory combines RAM and secondary storage so the system seems to have a
larger bank of memory.
- The more complex a security mechanism is, the less amount of assurance it can
usually provide.
- The trusted computing base (TCB) is a collection of system components that
enforces the security policy directly and protects the system. These components are
within the security perimeter.
- Components that make up the TCB are hardware, software, and firmware that
provide some type of security protection.
- A security perimeter is an imaginary boundary that has trusted components within it
(those that make up the TCB) and untrusted components outside it.
- The reference monitor concept is an abstract machine that ensures all subjects have
the necessary access rights before accessing objects. Therefore, it mediates all access to
objects by subjects.
- The security kernel is the mechanism that actually enforces the rules of the reference
monitor concept.
- The security kernel must isolate processes carrying out the reference monitor concept,
must be tamperproof, must be invoked for each access attempt, and must be small
enough to be properly tested.
- Processes need to be isolated, which can be done through segmented memory
addressing, encapsulation of objects, time multiplexing of shared resources, naming
distinctions, and virtual mapping.
- The level of security a system provides depends upon how well it enforces its security
policy.
- A closed system is often proprietary to the manufacturer or vendor, whereas an open
system allows for more interoperability.
- The Common Criteria was developed to provide globally recognized evaluation
criteria.
- The Common Criteria uses protection profiles, security targets, and ratings (EAL1 to
EAL7) to provide assurance ratings for targets of evaluation (TOEs).
- Certification is the technical evaluation of a system or product and its security
components. Accreditation is management’s formal approval and acceptance of the
security provided by a system.
- ISO/IEC 15408 is the international standard that is used as the basis for the
evaluation of security properties of products under the CC framework.
566
- Process isolation ensures that multiple processes can run concurrently and the
processes will not interfere with each other or affect each other’s memory segments.
- TOC/TOU stands for time-of-check/time-of-use. This is a class of asynchronous
attacks.
- A distributed system is a system in which multiple computing nodes, interconnected
by a network, exchange information for the accomplishment of collective tasks.
- Cloud computing is the use of shared, remote computing devices for the purpose of
providing improved efficiencies, performance, reliability, scalability, and security.
- Software as a Service (SaaS) is a cloud computing model that provides users access to
a specific application that executes on the service provider’s environment.
- Platform as a Service (PaaS) is a cloud computing model that provides users access to
a computing platform that is typically built on a server operating system, but not the
virtual machine on which it runs.
- Infrastructure as a Service (IaaS) is a cloud computing model that provides users
unfettered access to a cloud device, such as an instance of a server, which includes
both the operating system and the virtual machine on which it runs.
- Parallel computing is the simultaneous use of multiple computers to solve a specific
task by dividing it among the available computers.
- Any system in which computers and physical devices collaborate via the exchange of
inputs and outputs to accomplish a task or objective is a cyber-physical system.
- Cryptography is the science of protecting information by encoding it into an
unreadable format.
- The most famous rotor encryption machine is the Enigma used by the Germans in
World War II.
- A readable message is in a form called plaintext, and once it is encrypted, it is in a
form called ciphertext.
- Cryptographic algorithms are the mathematical rules that dictate the functions of
enciphering and deciphering.
- Cryptanalysis is the study of breaking cryptosystems.
- Nonrepudiation is a service that ensures the sender cannot later falsely deny sending a
message.
- Key clustering is an instance in which two different keys generate the same ciphertext
from the same plaintext.
- The range of possible keys is referred to as the keyspace. A larger keyspace and the full
use of the keyspace allow for more random keys to be created. This provides more
protection.
- The two basic types of encryption mechanisms used in symmetric ciphers are
substitution and transposition. Substitution ciphers change a character (or bit) out for
another, while transposition ciphers scramble the characters (or bits).
- A polyalphabetic cipher uses more than one alphabet to defeat frequency analysis.
567
- Steganography is a method of hiding data within another media type, such as a
graphic, WAV file, or document. This method is used to hide the existence of the
data.
- A key is a random string of bits inserted into an encryption algorithm. The result
determines what encryption functions will be carried out on a message and in what
order.
- In symmetric key algorithms, the sender and receiver use the same key for encryption
and decryption purposes.
- In asymmetric key algorithms, the sender and receiver use different keys for
encryption and decryption purposes.
- Symmetric key processes provide barriers of secure key distribution and scalability.
However, symmetric key algorithms perform much faster than asymmetric key
algorithms.
- Symmetric key algorithms can provide confidentiality, but not authentication or
nonrepudiation.
- Examples of symmetric key algorithms include DES, 3DES, Blowfish, IDEA, RC4,
RC5, RC6, and AES.
- Asymmetric algorithms are used to encrypt keys, and symmetric algorithms are used
to encrypt bulk data.
- Asymmetric key algorithms are much slower than symmetric key algorithms, but can
provide authentication and nonrepudiation services.
- Examples of asymmetric key algorithms include RSA, ECC, Diffie-Hellman, El
Gamal, knapsack, and DSA.
- Two main types of symmetric algorithms are stream ciphers and block ciphers.
Stream ciphers use a keystream generator and encrypt a message one bit at a time. A
block cipher divides the message into groups of bits and encrypts them.
- Many algorithms are publicly known, so the secret part of the process is the key. The
key provides the necessary randomization to encryption.
- Data Encryption Standard (DES) is a block cipher that divides a message into 64-bit
blocks and employs S-box-type functions on them.
- Because technology has allowed the DES keyspace to be successfully broken, TripleDES (3DES) was developed to be used instead. 3DES uses 48 rounds of computation
and up to three different keys.
- International Data Encryption Algorithm (IDEA) is a symmetric block cipher with a
key of 128 bits.
- RSA is an asymmetric algorithm developed by Rivest, Shamir, and Adleman and is
the de facto standard for digital signatures.
- Elliptic curve cryptosystems (ECCs) are used as asymmetric algorithms and can
provide digital signature, secure key distribution, and encryption functionality. They
use fewer resources, which makes them better for wireless device and cell phone
encryption use.
568
- When symmetric and asymmetric key algorithms are used together, this is called a
hybrid system. The asymmetric algorithm encrypts the symmetric key, and the
symmetric key encrypts the data.
- A session key is a symmetric key used by the sender and receiver of messages for
encryption and decryption purposes. The session key is only good while that
communication session is active and then it is destroyed.
- A public key infrastructure (PKI) is a framework of programs, procedures,
communication protocols, and public key cryptography that enables a diverse group
of individuals to communicate securely.
- A certificate authority (CA) is a trusted third party that generates and maintains user
certificates, which hold their public keys.
- The CA uses a certification revocation list (CRL) to keep track of revoked certificates.
- A certificate is the mechanism the CA uses to associate a public key to a person’s
identity.
- A registration authority (RA) validates the user’s identity and then sends the request
for a certificate to the CA. The RA cannot generate certificates.
- A one-way function is a mathematical function that is easier to compute in one
direction than in the opposite direction.
- RSA is based on a one-way function that factors large numbers into prime numbers.
Only the private key knows how to use the trapdoor and how to decrypt messages
that were encrypted with the corresponding public key.
- Hashing algorithms provide data integrity only.
- When a hash algorithm is applied to a message, it produces a message digest, and this
value is signed with a private key to produce a digital signature.
- Some examples of hashing algorithms include SHA-1, SHA-2, SHA-3, MD4, and
MD5.
- SHA produces a 160-bit hash value and is used in DSS.
- A birthday attack is an attack on hashing functions through brute force. The attacker
tries to create two messages with the same hashing value.
- A one-time pad uses a pad with random values that are XORed against the message to
produce ciphertext. The pad is at least as long as the message itself and is used once
and then discarded.
- A digital signature is the result of a user signing a hash value with a private key. It
provides authentication, data integrity, and nonrepudiation. The act of signing is the
actual encryption of the value with the private key.
- Examples of algorithms used for digital signatures include RSA, El Gamal, ECDSA,
and DSA.
- Key management is one of the most challenging pieces of cryptography. It pertains to
creating, maintaining, distributing, and destroying cryptographic keys.
- Crime Prevention Through Environmental Design (CPTED) combines the physical
569
environment and sociology issues that surround it to reduce crime rates and the fear
of crime.
- The value of property within the facility and the value of the facility itself need to be
ascertained to determine the proper budget for physical security so that security
controls are cost effective.
- Some physical security controls may conflict with the safety of people. These issues
need to be addressed; human life is always more important than protecting a facility
or the assets it contains.
- When looking at locations for a facility, consider local crime; natural disaster
possibilities; and distance to hospitals, police and fire stations, airports, and railroads.
- Exterior fencing can be costly and unsightly, but can provide crowd control and help
control access to the facility.
- If interior partitions do not go all the way up to the true ceiling, an intruder can
remove a ceiling tile and climb over the partition into a critical portion of the facility.
- The primary power source is what is used in day-to-day operations, and the
alternative power source is a backup in case the primary source fails.
- Smoke detectors should be located on and above suspended ceilings, below raised
floors, and in air ducts to provide maximum fire detection.
- A fire needs high temperatures, oxygen, and fuel. To suppress it, one or more of those
items needs to be reduced or eliminated.
- Gases like FM-200 and other halon substitutes interfere with the chemical reaction of
a fire.
- Portable fire extinguishers should be located within 50 feet of electrical equipment
and should be inspected quarterly.
- CO2
is a colorless, odorless, and potentially lethal substance because it removes the
oxygen from the air in order to suppress fires.
- CPTED provides three main strategies, which are natural access control, natural
surveillance, and natural territorial reinforcement.
- Window types that should be understood are standard, tempered, acrylic, wired, and
laminated.
