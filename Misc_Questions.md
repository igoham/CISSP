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

- A type 1 error is a false positive
    - For Biometrics this is when the requestor is falsely REJECTED
    - FRR
    = Falsely rejected a VALID user
- A type 2 error is a false negative
    - Bor Biometrics this si when the requestor is falselt ACCEPTED
    - FAR
    - Falsely accepted an INVALID user


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




**What is a constrained process**



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

Synchronous communications uses start and stop flags in communications  

**Review alarm sensor types for physical security**

**Why destroy SSDs to prevent data leaks?**

Solid State Drives (SSD): These use flash memory to store data and data is not overwritten. It is way faster than HDD, as the data is accessed directly via a flash translation layer, thus reducing time for head movement. Because of this, when it comes to data remanence, simple overwriting won’t work with SSD. the following techniques should be used:

    Built in sanitization commands
    Crypto-erase
    Sanitization


**What are the different actions you can take with risk  minamize it?**

**Research Identity Proofing**

At its core, identity proofing is an approach for verifying and authenticating the identity of individuals accessing an application. It uses knowledge-based user attributes, document verification, wallet-based factors, ID verification, and national identity systems to confirm that a person logging in is who they say they are. This allows for users to self-verify, making for a secure authentication process that doesn’t compromise user experience.

**Difference between Due dilligence and due care**

See this URL - https://www.studynotesandtheory.com/single-post/due-care-vs-due-diligence

**What is it called when you capture traffic and then replay it against a sight for performance testing**

**Review Biometrics**

**Research evidence rules from book**

**What is NIST SP 800-18**

**Touch up on account provisioning**

**E discovery reference model** - 1
**Ethernet Cable speeds** - 4
**What is a smurf attack vs fragle vs teardrop vs land attack** - 5
**Review Fuzzing Types** - 8
**What is the devops model** - ???
**Touch up on cloud models**
- Private
- Public
- Shared
- Hybrid
                              
**Review pen test phases**
**Review PM tools**
- Work breakdown structure document

**ITSM vs ITIL**

**Review calculating ARO for and EF values for 200 - 400 year events**
**Review SOC1,2,3 and each types**
**Breakdown the following**
- Policy
- Standard
- Baseline
- Prodecure

**EAP vs PEAP vs EAP-TLS**
EAP expected phyicall security to be in place and thus did not require encryption.

**What is the difference between transpotion and subtitution**
**Evacuation proceedures?**
**differrence between tpyo squatting and cyber squatting**
**Reciew IEEE 802.11i**
**Review GRE Genetric routing encapsulation headers**
**GDPR**
- Does each member state have to create their own protetion authority?      
    - I Assume NO!

**Difference between Async and Synchronous dynamic password tokens**
**How do CRLs work**
****
****
****
****
****