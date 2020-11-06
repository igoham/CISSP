

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







**What are no the differences between Multilevel, compartmented, systemhigh and dedicated**



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


What are the different wireless modes a client can use to connect to enterprise wifi network
Are there any other populat x.XXx eg x.509 standards that are popular
What is x.400
Treatdrop vs Fraggle attack
What is the CRC used for in ethernet
What are the ESP and AH modes and how are they commonly used together - ESP tunnel vs Transfer modes
What is the average tempature and humidity for a server toom
What are the relevant US and EU laws around privacy



**Which algorithms are strongest bit for bit**

**Review lesser encryption algorithms**
- El Gamal
- Knapscak
- Blowfish
- Twofish
- Skipjack


****
**Research x.509 certificiates**
- Do they use DSS for authentication?




**What is a constrained process**




**What are the core differences between BCP and DRP**

**What are the stages or steps in a BCP**

**What are the stages or steps in a DRP**

**What are the ISC code of ethics IN ORDER**

**Review public and military classification names**

**Review x.25 VS ATM vs SONNET vs FDDI**

**What are the different wireless modes for enterprise**

**Review PBX's**

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

There are two different types of models, prefictive bs adaptive. Most models are a mixture of booth

- Predictive 
    - the client knows what they want and it is built
    - Few changes
    
- Adaptive
    - Has an idea of what they want but its not fully identified
    - Team builds a prototype and iterates on feedback

The second type of model is incremental vs iterative
- incremental
    - You have a good idea of what you want to build but you build the entire car in many iterations
    - Good if the company can use the incremental portion or will use feedback to improve
- Iterative
    - works well on feedback
    - idea is not fully flushed uut yet

https://gyazo.com/7dc1830dc89ecd5948e1d6ec797fb70d

- Waterfall Methodology
    - plan -> define
    - build
    - test
    - release / maintainance
    
You cannot go back and fix anything that was fixed! If you missed a key requirement you need to wait for the next design or requiremnts phase to fix it.
 Best for projects that will not have changing requirements
 
    
- Agile Methodologies
    - plan -> define
    - build
    - test
    - release
    
Agile follows the same steps as waterfall however it does so in two week springs. Better suited for many changes throughout dev process.

- DevOps
    - Operations
    - Development
    - QA
    
Not focused on security nativley but there is DevSecOps.


- V-Shaped Methodology
https://gyazo.com/fe37e474c6bfada57be31d5f07a782b6

- Spiral Methodology
- Prototyping
- Incremental Methodology

- Rapid Application Development
    - Follows the iterative odel

- Integrated Product Team



**What uses start and stop flags in transmission**

Synchronous communications uses start and stop flags in communications  

**Review alarm sensor types for physical security**




**What are the different actions you can take with risk  minamize it?**

**Research Identity Proofing**

At its core, identity proofing is an approach for verifying and authenticating the identity of individuals accessing an application. It uses knowledge-based user attributes, document verification, wallet-based factors, ID verification, and national identity systems to confirm that a person logging in is who they say they are. This allows for users to self-verify, making for a secure authentication process that doesn’t compromise user experience.



**What is it called when you capture traffic and then replay it against a sight for performance testing**

**Review Biometrics**

**Research evidence rules from book**

**What is NIST SP 800-18**

**Touch up on account provisioning**

**E discovery reference model** - 1

**Ethernet Cable speeds** - 4
- Cable speeds
- Max cable runs in M

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


**EAP vs PEAP vs EAP-TLS**

EAP expected phyicall security to be in place and thus did not require encryption.

**What is the difference between transpotion and subtitution**

**Evacuation proceedures?**

**differrence between tpyo squatting and cyber squatting**

**Reciew IEEE 802.11i**

**Review GRE Genetric routing encapsulation headers**

**Difference between Async and Synchronous dynamic password tokens**

**Enticement vs entrapment**


**Common code review techniues?**


**Need to review the incident response phases**
- Detection 
- Response
    - assemble the team 
    - Analysis
- Mitigation
    - The goal of mitigation is to prevent or reduce any further damage from this incident so
that you can begin to recover and remediate. A proper mitigation strategy buys the incident
response team time for a proper investigation and determination of the incident’s root
cause.
- Reporting
- Recovery
    - Fix the problem
- Remediation / Lessons Learned
    - Fix the inital problem that allowed ther breach to occur


**Review the following pen test types**
- White / Crystal bic
- Blackbox
- gray box

**How to test coverate computed**


    (A) the total lines of code in the piece of software you are testing, and
    (B) the number of lines of code all test cases currently execute, and
    Find (B divided by A) multiplied by 100 – this will be your test coverage %.


- Formula = (A * B) * 100 = coverage%
    - (650 / 1000) * 100 = 65% 


**Research Cali online priv protection act**

**Looks up FTP ports**
20 - data plane
21 - control plane
22 - ssh
23 - telnet

**OWASP top 10 2020**

**Attacks against RSA**

**Research KRI**

Key Risk Indicators (KRIs), as the name suggests, measure risk. KRIs are used by organisations to determine how much risk they are exposed to or how risky a particular venture or activity is.

KRIs are a way to quantify and monitor the biggest risks an organisation (or activity) is exposed to. By measuring the risks and their potential impact on business performance, organisations are able to create early warning systems that allow them to monitor, manage and mitigate key risks. 

Effective KRIs help to:

    Identify the biggest risks.
    Quantify those risks and their impact.
    Put risks into perspective by providing comparisons and benchmarks.
    Enable regular risk reporting and risk monitoring.
    Alert key people in advance of risks unfolding.
    Help people to manage and mitigate risks.



**Review Broadcast and collision domains**

Definitions:
- A broadcast domain is a group of nodes that can reach each other via broadcast. 
- A collision domain is when devices electrical signals can interfere with one another on the wire

### Hub

Since hubes are very dumb they simply extend networks / collision domains. 
- Extends collision domains

### Switches

Switches on the other hand are smart and generally 
support 1-1 conversations. As a result it knows when to expect frames ( think pdu ) and can avoid collisions.
This is because a switch has an arp table so it knows exactly ehere each device is.  
- Does NOT extend collision domains
- Extend broadcast domains to allow each device to talk to any device on the same switched network

### Routers
- Separates collision domains
- Separates broadcast domains


