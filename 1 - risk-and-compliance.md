


## Security and Risk Frameworks

- NIST SP 800-53 - Provides a list of privacy and security controls. These controls map to the required security level identified in NIST SP 800-37.
    - System with high level of security = high impact controls 
    - for us federal agencies and organizations
    - Provides 3 impact levels
        - Low
        - Medium
        - High
    - You must identify which impact level the system is identifed as. This is done in step one of NIST SP 800-37

- HIPPA - 
- SOX - Requires top management to individually certify the accuracy of each finacial report and if the reports and found
to be flase the exec can be held personally liable 




### NIST SP 800-37 - Risk Management Framework

The RMF has six steps

- Categorize Information Systems
    - Determine the classification of the systems
    - Categorzation is applied based off FIPS 199
- Selection of security controls 
    - Fully based off the impact level of the determined in previous step
    - Controls can be found in NIST SP 800-53
- Implement the security controls
    - Take a long time as requires all of the work to be done
    - Requires SMEs, for example databases require a DBA to preform special configurations 
- Assessment
    - Assess the level of implementation per control
    - Looks at the evidence put in place, documentation with accreditation 
    - Ensure in a secure phyiscal location
    - Ensure technical controls are in place
- Authorize the system
    - An Authorizing official must accept the risk that is not mitigated by the controls
- Continuous monitoring
    - One the system is approved we contineously monitor the controlls to ensure they are effective
    - Ensures the system always maintains the same level of risk as it was initially accepted with
### Fips-199

Used to determine classification levels of systems in NIST SP 800-37


![FIPS 199](https://gyazo.com/4712f7210d654bcb15e1caa28a8d9db8.png)



## COSO

-  identifies 17
internal control principles that are grouped into five internal control components as
listed here.
- Mainly conferned with preventing internal financial fraud but does contain guidance on security
### Control Environment:
1. Demonstrates commitment to integrity and ethical values
2. Exercises oversight responsibilities
3. Establishes structure, authority, and responsibility
4. Demonstrates commitment to competence
5. Enforces accountability
### Risk Assessment:
6. Specifies suitable objectives
7. Identifies and analyzes risk
8. Assesses fraud risk
9. Identifies and analyzes significant change
### Control Activities:
10. Selects and develops control activities
11. Selects and develops general controls over technology
12. Deploys through policies and procedures
### Information and Communication:
13. Uses relevant, quality information
14. Communicates internally
15. Communicates externally
84
### Monitoring Activities:
16. Conducts ongoing and/or separate evaluations
17. Evaluates and communicates deficiencies

- ISO 31000
- ISACA RISK IT

# Privacy
## EU-US Privacy shield

https://www.privacyshield.gov/

The Privacy sheild has the following principles

1. Notice
    - Must provide notice for a long list of items - https://www.privacyshield.gov/article?id=1-NOTICE
2. Choice
    - Individuals should have the opportunity to opt out
    - (i) to be disclosed to a third party or 
    - (ii) to be used for a purpose that is materially different from the purpose(s) for which it was originally collected or subsequently authorized by the individuals
3. Accountability for Onward Transfer
    - 3p must also use for the agreed upon purpose
    - Must adbive by above rules
    - ascertain that the agent is obligated to provide at least the same level of privacy protection as is required by the Principles; 
    - (iii) take reasonable and appropriate steps to ensure that the agent effectively processes the personal information transferred in a manner consistent with the organization’s obligations under the Principles;
4. Security
5. Data Integrity and Purpose Limitation
6. Access
    - ndividuals must have access to personal information about them that an organization holds and be able to correct, amend, or delete that information where it is inaccurate, or has been processed in violation of the Principles, except where the burden or expense of providing access would be disproportionate to the risks to the individual’s privacy in the case in question, or where the rights of persons other than the individual would be violated.
7. Recourse, Enforcement and Liability

## 8 principles of GDPR

Each member state has their own Data Protection Authority! https://ec.europa.eu/info/law/law-topic/data-protection/reform/what-are-data-protection-authorities-dpas_en

1. The right to be informed

    - Both data processors and controllers are now obliged to provide information to data subjects about the personal data being collected, how it is going to be used, who it will be shared with, for how long it will be kept and the purpose of its processing.

1. The right of access

    - With request, individual data subjects are entitled to confirmation that their data is being processed, access to that data as well as further information regarding any automated decision making, or the envisioned period of retention.

1. The right to rectification

    - With its corresponding principle in ‘accuracy’, data subjects hold the right to have personal data rectified should it be either inaccurate or incomplete.

1. The right to erasure

    - Also known as ‘the right to be forgotten’, this right allows data subjects to request the removal or deletion of data in the eventuality there is no compelling reason for its continued processing or availability. This right may in some circumstances also obligate, for instance, a search engine company to remove certain results, or limit their discoverability.

1. The right to restrict processing

    - Processing is any operation performed on personal data. This includes using, viewing, altering or deleting the data. Individuals may block or suppress processing of personal data for the following reasons: Inaccurate data, the unlawful processing of that data or a pending objection to processing the data by the data subject

1. The right to data portability

    - Allowing individuals to obtain and reuse their personal data across different services, this right means an individual’s data should be available in a commonly used machine-readable format, in a way which allows data not to be constantly resubmitted.

1. The right to object

    - Allowing individual to object (for certain reasons) to the processing of their personal data, as well as obliging organisations to inform individuals of this right at the time of first communication.

1. Rights in relation to automated decision making and profiling.

    - One of the more detailed and technical rights afforded under the GDPR, among other things, entitles individuals either opt out of automated decision-making processes, challenge decisions, and/or have automated decisions reviewed by a human. More about this right can be found here.



**Define the following Definitions**
- Security Policy - Mandatory - EX. Passwords MUST be changed every 90 days
- Standards - Mandatory - Admins must use Windows server 2020 R2 for the base OS
- Baselines - Discretionary -EX. the specific settings for windows servers to be configured to match the CIS benchmarks
- Guidelines(suggestions) - Discretionary - EX. To create a strong password use the first letter of every work in a sentense
- Procedures - - Mandatory - 


**Define the following terms**
- Trademark
    - Can be renewed indefinitely  
- Copyright
    - Protection for 70 years or the death of the author
    - if in a group the death of the last author
- IP
    - Intellectual property is any data, software, algorithm or knowledge created within a company or by an individual
- Trade Secret 
    - Any information that would give a company an operational edge
    - Maints its status as a secret as long as the secret is not given up
- Patent
    - A patent is the strong form of IP protection
    - Must be novel, useful and not obvious
    - Lasts 20 years

- Which hash the shortest protection mechanism?
    - **A**: Patent

    
**Software Piracy**

This is a huge issue!

![Piracy numbers](https://gyazo.com/aa8f441b52a8192d68184a7b717d3b0f.png)


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


**How does CVSS scoring work in detail?**

- Open framework for communicating the characteristics and severity software vulnerabilities


![CVSS](https://gyazo.com/2c81f9a026cad844b856b0b5f77cedeb.png)

- Base - Consistent over time and across environments (Affects all the same way)
- Temporal - characteristics that change over time
- Environmental - Unique to a users envrioment 



**Difference between Due dilligence and due care**

See this URL - https://www.studynotesandtheory.com/single-post/due-care-vs-due-diligence







- What does does of the follow laws aim to do?
	- Sarbanes-Oxley act of 2002 AKA SOX - 
		- Made it illeagal for a corporation to 'cook its books by putting teeth in the laws. It could send executives to jail if it was discovered that their company was submitting fraudulent accounting findings to the US SEC. SOX is based upon the COSO model, so for a corporation to be compliant with SOX it has to follow the COSO model.
	- Computer Fraud and bause acted - CFAA
		- Enacted in 1984
		- Criminalized the act of connecting to a computer in an unauthorized manner. 
	- Computer security act of 1987 - 
		- Mandate federnal agencies must security their computer systems. Must provide plans to NSA for review.  Some verbage around awareness training as well.
		- Repealed and replaced by FISMA 2002
	- Federal information security mangement act of 2002 FISMA
		- Ensure ORG wide Risk Management practices are in place
		- Documentation of controls such as Authorization / authentication controls
		- Protect information during processing, storage and in transit
	- Federal Privacy act of 1974 - 
		- The Privacy Act dictates that an agency cannot disclose this information without written permission from the individual. However, like most government acts, legislation, and creeds, there is a list of exceptions. So what does all of this dry legal mumbo-jumbo mean? Basically, agencies can gather information about individuals, but it must be relevant and necessary to the agency’s official functions. In addition, an agency cannot share people’s private information. If it does, private citizens have the right to sue that agency to protect their privacy. The Privacy Act applies to the computer world because this information is usually held by one type of computer or another. If an agency’s computer holds an individual’s confidential information, the agency must provide the necessary security mechanisms to ensure that information cannot be compromised or copied in an unauthorized way.
	- Department of Veterans Affairs Information Security Protection Act - 
		- This law has an extremely narrow scope (it only applies to the VA), but is representative of efforts to bolt on security after a breach. The VA was already required to comply with FISMA, but the fact that it failed to do so received a lot of attention in the wake of the theft of the laptop. Rather than simply enforcing FISMA, the federal government created a new law that requires the VA to implement additional controls and to report its compliance to Congress.
	- Health Insurance Portability and Accountability Act (HIPAA)
		- HIPAA mandates steep federal penalties for noncompliance. If medical information is used in a way that violates the privacy standards dictated by HIPAA, even by mistake, monetary penalties of $100 per violation are enforced, up to $1,500,000 per year, per standard. If protected health information is obtained or disclosed knowingly, the fines can be as much as $50,000 and one year in prison. If the information is obtained or disclosed under false pretenses, the cost can go up to $250,000 with 10 years in prison if there is intent to sell or use the information for commercial advantage, personal gain, or malicious harm. This is serious business. 
	- Health Information Technology for Economic and Clinical Health (HITECH) Act
		- y. Subtitle D of the HITECH Act addresses the privacy and security concerns associated with the electronic transmission of health information, in part through several provisions that strengthen the civil and criminal enforcement of the HIPAA rules. Section 13410(d) of the HITECH Act revised Section 1176(a) of the Social Security Act by establishing 
			- Four categories of violations that reflect increasing levels of culpability - 
			- Four corresponding tiers of penalty amounts that significantly increase the minimum penalty amount for each violation - 
			- A maximum penalty amount of $1.5 million for all violations of an identical provision 
	- Gramm-Leach-Bliley Act (GLBA)
		- The act dictates that the board of directors is responsible for many of the security issues within a financial institution, that risk management must be implemented, that all employees need to be trained on information security issues, and that implemented security measures must be fully tested. It also requires these institutions to have a written security policy in place. Major components put into place to govern the collection, disclosure, and protection of consumers’ nonpublic personal information, or PII, include 
			- Financial Privacy Rule Provide each consumer with a privacy notice that explains the data collected about the consumer, where that data is shared, how that data is used, and how that data is protected. The notice must also identify the consumer’s right to opt out of the data being shared with unaffiliated parties pursuant to the provisions of the Fair Credit Reporting Act. - 
			- Safeguards Rule Develop a written information security plan that describes how the company is prepared to, and plans to continue to, protect clients’ nonpublic personal 131 information. - 
			- Pretexting Protection Implement safeguards against pretexting (social engineering). 
	- Personal Information Protection and Electronic Documents Act
		- The law was enacted to help and promote consumer trust and facilitate electronic commerce. It was also put into place to reassure other countries that Canadian businesses would protect privacy data so that cross-border transactions and business activities could take place in a more assured manner. Some of the requirements the law lays out for organizations are as follows: 
			- Obtain consent when they collect, use, or disclose their personal information - 
			- Collect information by fair and lawful means - 
			- Have personal information policies that are clear, understandable, and readily available
	- Payment Card Industry Data Security Standard (PCI DSS)
		- Made up of 12 of the following requirements
			- Install and maintain a firewall configuration to protect cardholder data. 
			- 2. Do not use vendor-supplied defaults for system passwords and other security parameters. 
			- 3. Protect stored cardholder data. 
			- 4. Encrypt transmission of cardholder data across open, public networks.
			-  5. Use and regularly update anti-virus software or programs. 
			- 6. Develop and maintain secure systems and applications. 
			- 7. Restrict access to cardholder data by business need to know. 
			- 8. Assign a unique ID to each person with computer access. 133 
			- 9. Restrict physical access to cardholder data. 
			- 10. Track and monitor all access to network resources and cardholder data. 
			- 11. Regularly test security systems and processes. 
			    - Requirement 11.2 covers scanning. It states that you need to "Run internal and external network vulnerability scans at least quarterly and after any significant change in the network."
			    - Both scans must be done quarterly
			- 12. Maintain a policy that addresses information security for employees and contractors.
			
			
			
## Change Management

The change management process includes six steps:
- Request the change
- Review the change
- Approve / Reject the change
- Test the change
- Schedule and implement the change
- Document the change

The last phase, document the change results 


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

