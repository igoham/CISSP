Threat-modeling methods are used to create

- an abstraction of the system
- profiles of potential attackers, including their goals and methods
- a catalog of potential threats that may arise


Threat modeling should be performed early in the development cycle when potential issues can be caught early and remedied, preventing a much costlier fix down the line. Using threat modeling to think about security requirements can lead to proactive architectural decisions that help reduce threats from the start. 
Threat modeling can be particularly helpful in the area of cyber-physical systems.



![PASTA](https://gyazo.com/141d712a513198988071e5f425870cb4.png)
![PASTA](https://gyazo.com/8b6ea2189b6986541a3941605ab13693.png)



## STRIDE 
STRIDE is an acronym that stands for 6 categories of security risks: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, and Elevation of Privileges.

Each category of risk aims to address one aspect of security.

Let's dive into each of these categories.

##### Spoofing

Spoofing refers to the act of posing as someone else (i.e. spoofing a user) or claiming a false identity (i.e. spoofing a process).

This category is concerned with authenticity.

Examples:

    One user spoofs the identify of another user by brute-forcing username/password credentials.
    A malicious, phishing host is set up in an attempt to trick users into divulging their credentials.

You would typically mitigate these risks with proper authentication.


##### Tampering

Tampering refers to malicious modification of data or processes. Tampering may occur on data in transit, on data at rest, or on processes.

This category is concerned with integrity.

Examples:

    A user performs bit-flipping attacks on data in transit.
    A user modifies data at rest/on disk.
    A user performs injection attacks on the application.

You would typically mitigate these risks with:

    Proper validation of users' inputs and proper encoding of outputs.
    Use prepared SQL statements or stored procedures to mitigate SQL injections.
    Integrate with security static code analysis tools to identify security bugs.
    Integrate with composition analysis tools (e.g. snyk, npm audit, BlackDuck ...etc) to identify 3rd party libraries/dependencies with known security vulnerabilities.

##### Repudiation

Repudiation refers to the ability of denying that an action or an event has occurred.

This category is concerned with non-repudiation.

Examples:

    A user denies performing a destructive action (e.g. deleting all records from a database).
    Attackers commonly erase or truncate log files as a technique for hiding their tracks.
    Administrators unable to determine if a container has started to behave suspiciously/erratically.

You would typically mitigate these risks with proper audit logging.


##### Information Disclosure

Information Disclosure refers to data leaks or data breaches. This could occur on data in transit, data at rest, or even to a process.

This category is concerned with confidentiality.

Examples:

    A user is able to eavesdrop, sniff, or read traffic in clear-text.
    A user is able to read data on disk in clear-text.
    A user attacks an application protected by TLS but is able to steal x.509 (SSL/TLS certificate) decryption keys and other sensitive information. Yes, this happened.
    A user is able to read sensitive data in a database.

You would typically mitigate these risks by:

    Implementing proper encryption.
    Avoiding self-signed certificates. Use a valid, trusted Certificate Authority (CA).

##### Denial of Service

Denial of Service refers to causing a service or a network resource to be unavailable to its intended users.

This category is concerned with availability.

Examples:

    A user performs SYN flood attack.
    The storage (i.e. disk, drive) becomes too full.
    A Kubernetes dashboard is left exposed on the Internet, allowing anyone to deploy containers on your company's infrastructure to mine cryptocurrency and starve your legitimate applications of CPU. Yes, that happened too.

Mitigating this class of security risks is tricky because solutions are highly dependent on a lot of factors.

For the Kubernetes example, you would mitigate resource consumption with resource quotas.

For a storage example, you would mitigate this with proper log rotation and monitoring/alerting when disk is nearing capacity.
##### Elevation of Privileges

Elevation of Privileges refers to gaining access that one should not have.

This category is concerned with authorization.

Example:

    A user takes advantage of a Buffer Overflow to gain root-level privileges on a system.
    A user with limited to no permissions to Kubernetes can elevate their privileges by sending a specially crafted request to a container with the Kubernetes API server's TLS credentials. Yes, this was possible.

Mitigating these risks would require a few things:

    Proper authorization mechanism (e.g. role-based access control).
    Security static code analysis to ensure your code has little to no security bugs.
    Compositional analysis (aka dependency checking/scanning), like snyk or npm audit, to ensure that you're not relying on known-vulnerable 3rd party dependencies.
    Generally practicing least privilege principle, like running your web server as a non-root user.

    
## DREAD 
    - Damage potential
    - Reproducibility, 
    - Ex-ploitability, 
    - Affected users, 
    - Discoverability

Microsoft developed another Threat Model. It assigns one of three values (0, 5, 10) to the first four categories and one of four values (0, 5, 9, 10) to the last category, which “allows for an average value to be calculated to represent the risk of the entire sys-tem”

![PASTA](https://gyazo.com/ebf9d564b1f074df04cbb566dce17fb8.png)
## PASTA 
The Process for Attack Simulation and Threat Analysis (P.A.S.T.A) is a risk-centric threat modeling framework developed in 2012 by Tony UcedaVélez. It contains seven stages, each with multiple ac-tivities

![PASTA](https://i.gyazo.com/116f7317d238bf3d9962c9e44e924ca6.png)

- PASTA aims to bring business objectives and technical requirements together [22]. It uses a variety of design and elicitation tools in different stages. For example, high-level architectural diagrams are used
during stage two for identifying the technical scope. DFDs are used in stage three. During stage six, attack trees and use and abuse cases are built for analysis and attack modeling

This method elevates the threat modeling process to a strategic level by involving key decision makers and requiring security input from operations, governance, architecture, and development [21]. Widely regarded as a risk-centric framework, PASTA has an attacker-centric perspective. In the end, the pro-cess produces an asset-centric output in the form of threat enumeration and scoring [31, 21].

# LINDDUN 
    - Linkability, 
    - Identifiability, 
    - Non-Repudiation, 
    - Detectability, 
    - Disclosure of Information,
    - Unawareness, 
    - Non-Compliance) 

- Privacy threat modeling framework
- Systematic support for elicitation and mitigation of privacy threats in software architectures

LINDDUN is a threat modeling method that focuses on privacy concerns and can be used for data security [12]. 
Similar to STRIDE, this method is a mnemonic, meaning the threat cat-egories in question are coded in the method name. 
Consisting of six steps, (see Figure 3), LINDDUN provides a systematic approach to privacy assessment [34, 35]


![LINDUN](https://i.gyazo.com/65866910b718430406043e7b3205332c.png)

## Attack Trees

Using attack trees to model threats is one of the oldest and most widely applied techniques on cyber-only systems as well as cyber-physical and physical systems [3]. Developed by Bruce Schneider in 1999, it was initially applied as its own method and has since been combined with other methods and frameworks [17, 3].

Attack trees are essentially diagrams that depict attacks on a system in tree form. The tree root is the goal for the attack, and the leaves are ways to achieve that goal [17]. Each goal is represented as a sep-arate tree. Thus, the system threat analysis produces a set of attack trees.


![Attack Trees](https://i.gyazo.com/3832ba23fb6aaa5bafa65fb1e8c6b752.png)


Usually it takes a few iterations of decomposing the goal to build the tree. Once all leaf nodes are identified, markers of possibility can be assigned. These values should be assigned only after relevant research on the step is done [17]. 
While examining different methods to achieve the goal, it may be-come obvious that this can be accomplished in multiple ways. 

To incorporate these different options into the tree, AND and OR nodes should be used. (See Figure 6; AND nodes are connected by a note that says “and,” indicating that both nodes must be performed to move to the next step. OR nodes are all other nodes.) In the case of a complex system, attack trees can be built for each component instead of for the whole system [2]. When attack trees are built, they can be used to make security decisions, see if the systems are vulnerable to an attack, and evaluate a spe-cific type of attack [17].

Attack trees are easy to understand and adopt but are only useful when the system and security con-cerns are well understood. The method assumes that analysts have high cybersecurity expertise and thus does not provide guidelines for assessing sub-goals, attacks, or risks [2].

In recent years, this method has often been used in combination with other techniques and within frameworks like STRIDE, CVSS, and PASTA [3, 2, 31].


## Persona Non Grata
As a threat modeling method, Persona non Grata (PnG) focuses on the motivations and skills of hu-man attackers. It characterizes users as archetypes that can misuse the system and forces analysts to view the system from an unintended use point of view [23]. 

When used, PnG can help visualize threats from the counterpart side, which can be helpful in the early stages of the threat modeling [15]. The idea is to “introduce” a technical expert to a potential attacker of the system and their skills, motivations, and goals that help the expert to see the system’s vulnera-bilities and points of compromise from the other side [15]

![Attack Trees](https://i.gyazo.com/c792e8c97afa554223202d41b8cec60b.png)


## Trike

Trike was created as a security audit framework in 2005 that uses threat modeling as a technique [15]. 
It looks at threat modeling from a risk management and defensive perspective [42].  

Trike, as with many other methods, starts with defining a system. The analyst must build a require-ment model by enumerating and understanding the system’s actors, assets, intended actions, and rules.
 
 As a result of this step, an actor-asset-action matrix can be created, where the columns represent as-sets, and the rows represent actors.  Each cell of the matrix should be divided into four parts, one for each action of CRUD (creating, read-ing, updating, and deleting). In these cells, the analyst should assign one of three values: allowed ac-tion, disallowed action, or action with rules. A rule tree should be attached to each cell [42, 43]. After defining requirements, a DFD is built. Each element is mapped to a selection of actors and as-sets.
  
  Iterating through the DFD, the analyst identifies threats, which fall into one of two categories: elevations of privilege or denials of service [42, 43]. Each discovered threat becomes a root node in an attack tree [42].To assess the risk of attacks that may impact assets through CRUD, Trike uses a five-point scale for each action, based on its probability. Actors are rated on five-point scales for the risks they are as-sumed to present (lower number = higher risk) to the asset. Also, actors are evaluated on a three-di-mensional scale (always, sometimes, never) for each action they may perform on each asset.The Trike scale system seems too vague to represent a formal method. Unfortunately, Trike version 2.0 is not well maintained, and there is no documentation, even though its site is up and running.
  
  
  
## VAST Modeling 
 
 The Visual, Agile, and Simple Threat (VAST) Modeling method was created by Anurag Agarwal and is based on ThreatModeler, an automated threat modeling platform [15]. The fundamental value of the method is the scalability and usability that allow it to be adopted in large organizations throughout the entire infrastructure to produce actionable and reliable results for different stakeholders [22]. 
 
 Recognizing differences in operations and concerns among development and infrastructure teams, VAST requires creating two types of models: application threat models and operational threat models. Application threat models use process flow diagrams, representing the architectural point of view. Op-erational threat models are created with an attacker point of view in mind based on DFDs [15, 22]. This approach allows for the integration of VAST into the organization’s development and DevOps lifecycles [22]
 
 
## OCTAVE
 
The Operationally Critical Threat, Asset, and Vulnerability Evaluation (OCTAVE) method is a risk-based strategic assessment and planning method for cybersecurity [36]. It was created by the CERT Division of the Software Engineering Institute in 2003 and refined in 2005. OCTAVE focuses on as-sessing organizational risks and does not address technological risks. Its main aspects are operational risk, security practices, and technology [22, 43].

OCTAVE has three phases, which can be seen in Figure 11 [36]:
![Attack Trees](https://gyazo.com/7a13db4b225a990655695fec6f0fdbb9.png)

1. Build asset-based threat profiles. (This is an organizational evaluation.) 
2. Identify infrastructure vulnerability. (This is an evaluation of the information infrastructure.)
3. Develop a security strategy and plans. ( This is an identification of risks to the organization’s criti-cal assets and decision making.) 