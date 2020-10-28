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
# TODO


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
REVIEW THE TCP/IP DARPA MODEL!!!!!
How does change management and Configuration management interface
Which Symetric and Asymetric algrithms are the strongest
What is a Micro kernel and how is it used in a TCB
What is a DataGram
What are the different wireless modes a client can use to connect to enterprise wifi network
Are there any other populat x.XXx eg x.509 standards that are popular
What is x.400
Treatdrop vs Fraggle attack
What is the CRC used for in ethernet
What are the ESP and AH modes and how are they commonly used together - ESP tunnel vs Transfer modes
What is the average tempature and humidity for a server toom

**Which algorithms are strongest bit for bit**
**What is a meet in the middle attack**
**Certification vs Accredidation**
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

What is a constrained process
**What is the refernce monitor in the TCB**