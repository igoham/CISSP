test = """
• What does does of the follow laws aim to do?
	• Sarbanes-Oxley act of 2002 AKA SOX - 
		○ Made it illeagal for a corporation to 'cook its books by putting teeth in the laws. It could send executives to jail if it was discovered that their company was submitting fraudulent accounting findings to the US SEC. SOX is based upon the COSO model, so for a corporation to be compliant with SOX it has to follow the COSO model.
	• Computer Fraud and bause acted - CFAA
		○ Enacted in 1984 
	• Computer security act of 1987 - 
		○  Mandate federnal agencies must security their computer systems. Must provide plans to NSA for review.  Some verbage around awareness training as well.
	• Federal information security mangement act of 2002 FISMA
		○ Ensure ORG wide Risk Management practices are in place
		○ Documentation of controls such as Authorization / authentication controls
		○ Protect information during processing, storage and in transit
	• Federal Privacy act of 1974 - 
		○ The Privacy Act dictates that an agency cannot disclose this information without written permission from the individual. However, like most government acts, legislation, and creeds, there is a list of exceptions. So what does all of this dry legal mumbo-jumbo mean? Basically, agencies can gather information about individuals, but it must be relevant and necessary to the agency’s official functions. In addition, an agency cannot share people’s private information. If it does, private citizens have the right to sue that agency to protect their privacy. The Privacy Act applies to the computer world because this information is usually held by one type of computer or another. If an agency’s computer holds an individual’s confidential information, the agency must provide the necessary security mechanisms to ensure that information cannot be compromised or copied in an unauthorized way.
	• Department of Veterans Affairs Information Security Protection Act - 
		○ This law has an extremely narrow scope (it only applies to the VA), but is representative of efforts to bolt on security after a breach. The VA was already required to comply with FISMA, but the fact that it failed to do so received a lot of attention in the wake of the theft of the laptop. Rather than simply enforcing FISMA, the federal government created a new law that requires the VA to implement additional controls and to report its compliance to Congress.
	• Health Insurance Portability and Accountability Act (HIPAA)
		○ HIPAA mandates steep federal penalties for noncompliance. If medical information is used in a way that violates the privacy standards dictated by HIPAA, even by mistake, monetary penalties of $100 per violation are enforced, up to $1,500,000 per year, per standard. If protected health information is obtained or disclosed knowingly, the fines can be as much as $50,000 and one year in prison. If the information is obtained or disclosed under false pretenses, the cost can go up to $250,000 with 10 years in prison if there is intent to sell or use the information for commercial advantage, personal gain, or malicious harm. This is serious business. 
	• Health Information Technology for Economic and Clinical Health (HITECH) Act
		○ y. Subtitle D of the HITECH Act addresses the privacy and security concerns associated with the electronic transmission of health information, in part through several provisions that strengthen the civil and criminal enforcement of the HIPAA rules. Section 13410(d) of the HITECH Act revised Section 1176(a) of the Social Security Act by establishing 
			• • Four categories of violations that reflect increasing levels of culpability • 
			• Four corresponding tiers of penalty amounts that significantly increase the minimum penalty amount for each violation • 
			• A maximum penalty amount of $1.5 million for all violations of an identical provision 
	• Gramm-Leach-Bliley Act (GLBA)
		○ The act dictates that the board of directors is responsible for many of the security issues within a financial institution, that risk management must be implemented, that all employees need to be trained on information security issues, and that implemented security measures must be fully tested. It also requires these institutions to have a written security policy in place. Major components put into place to govern the collection, disclosure, and protection of consumers’ nonpublic personal information, or PII, include 
			• • Financial Privacy Rule Provide each consumer with a privacy notice that explains the data collected about the consumer, where that data is shared, how that data is used, and how that data is protected. The notice must also identify the consumer’s right to opt out of the data being shared with unaffiliated parties pursuant to the provisions of the Fair Credit Reporting Act. • 
			• Safeguards Rule Develop a written information security plan that describes how the company is prepared to, and plans to continue to, protect clients’ nonpublic personal 131 information. • 
			• Pretexting Protection Implement safeguards against pretexting (social engineering). 
	• Personal Information Protection and Electronic Documents Act
		○ The law was enacted to help and promote consumer trust and facilitate electronic commerce. It was also put into place to reassure other countries that Canadian businesses would protect privacy data so that cross-border transactions and business activities could take place in a more assured manner. Some of the requirements the law lays out for organizations are as follows: 
			• • Obtain consent when they collect, use, or disclose their personal information • 
			• Collect information by fair and lawful means • 
			• Have personal information policies that are clear, understandable, and readily available
	• Payment Card Industry Data Security Standard (PCI DSS)
		○ Made up of 12 of the following requirements
			• Install and maintain a firewall configuration to protect cardholder data. 
			• 2. Do not use vendor-supplied defaults for system passwords and other security parameters. 
			• 3. Protect stored cardholder data. 
			• 4. Encrypt transmission of cardholder data across open, public networks.
			•  5. Use and regularly update anti-virus software or programs. 
			• 6. Develop and maintain secure systems and applications. 
			• 7. Restrict access to cardholder data by business need to know. 
			• 8. Assign a unique ID to each person with computer access. 133 
			• 9. Restrict physical access to cardholder data. 
			• 10. Track and monitor all access to network resources and cardholder data. 
			• 11. Regularly test security systems and processes. 
			• 12. Maintain a policy that addresses information security for employees and contractors."""

test = test.replace("•", "-")
test = test.replace("○", "-")
x=1