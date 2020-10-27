Threat-modeling methods are used to create

- an abstraction of the system
- profiles of potential attackers, including their goals and methods
- a catalog of potential threats that may arise


Threat modeling should be performed early in the development cycle when potential issues can be caught early and remedied, preventing a much costlier fix down the line. Using threat modeling to think about security requirements can lead to proactive architectural decisions that help reduce threats from the start. 
Threat modeling can be particularly helpful in the area of cyber-physical systems.



![PASTA](https://gyazo.com/141d712a513198988071e5f425870cb4.png)
![PASTA](https://gyazo.com/8b6ea2189b6986541a3941605ab13693.png)



## STRIDE 
    - SPOOFING
    - Tampering 
    - REPUDIATION
    - Information Disclosure
    - Denial of service
    = Elevation pf privilege
    
## DREAD 
    - Damage potential
    - Reproducibility, 
    - Ex-ploitability, 
    - Affected users, 
    - Discoverability

Microsoft developed another Threat Model. It assigns one of three values (0, 5, 10) to the first four categories and one of four values (0, 5, 9, 10) to the last category, which “allows for an average value to be calculated to represent the risk of the entire sys-tem”

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
