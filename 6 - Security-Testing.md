**Real user monitoring**

Monitoring the real time transactions of users. 


**Synthetic Pref monitoring**

Running scripted transactions to monitor the responses againts the application. This could also feed into dashboards


**Postitive testing**

Verifies the application does what it should. For example the login page actually logs you in.

**Negative testing**

Is looking for noraml and common errors. For example the login page does not log you in if you enter the wrong password.

**Soc1**

Financial reports

**Soc2**

Soc 2 type 2 is the most valued report
Security, Availability, confidentiality, Process integrity and privacy



Type 1 - Looks at the the design in a specific point in time

Type 2 - Verifies the design and the operating effectiveness of the design over a period of time.


**Soc 3**

Summarize and sanatied verion for public distribution 



**How auditing is supported**
The executive management team provides funding and support. An audit committee is  composed of members of the board and senior stake holders. The com

****
****
****
****
****
#### Pre-Engagement Interactions

One over-looked step to penetration testing is pre-engagement interactions or scoping. During this pre-phase, a penetration testing company will outline the logistics of the test, expectations, legal implications, objectives and goals the customer would like to achieve.

During the Pre-Engagement phase, the penetration testers should work with your company to fully understand any risks, your organizational culture, and the best pentesting strategy for your organization. You may want to perform a white box, black box, or gray box penetration test. It’s at this stage when the planning occurs along with aligning your goals to specific pentesting outcomes.
#### Reconnaissance or Open Source Intelligence (OSINT) Gathering

Reconnaissance or Open Source Intelligence (OSINT) gathering is an important first step in penetration testing. A pentester works on gathering as much intelligence on your organization and the potential targets for exploit.

Depending on which type of pentest you agree upon, your penetration tester may have varying degrees of information about your organization or may need to identify critical information on their own to uncover vulnerabilities and entry points in your environment.
Common intelligence gathering techniques include:

    Search engine queries
    Domain name searches/WHOIS lookups
    Social Engineering
    Tax Records
    Internet Footprinting – email addresses, usernames, social networks,
    Internal Footprinting –Ping sweeps, port scanning, reverse DNS, packet sniffing
    Dumpster Diving
    Tailgating

A pentester uses an exhaustive checklist for finding open entry points and vulnerabilities within the organization. The OSINT Framework provides a plethora of details for open information sources.
#### Threat Modeling & Vulnerability Identification

During the threat modeling and vulnerability identification phase, the tester identifies targets and maps the attack vectors. Any information gathered during the Reconnaissance phase is used to inform the method of attack during the penetration test.
The most common areas a pentester will map and identify include:

    Business assets – identify and categorize high-value assets
        Employee data
        Customer data
        Technical data
    Threats – identify and categorize internal and external threats
        Internal threats – Management, employees, vendors, etc.
        External threats – Ports, Network Protocols, Web Applications, Network Traffic, etc.

A pentester will often use a vulnerability scanner to complete a discovery and inventory on the security risks posed by identified vulnerabilities. Then the pentester will validate if the vulnerability is exploitable. The list of vulnerabilities is shared at the end of the pentest exercise during the reporting phase.
#### Exploitation

With a map of all possible vulnerabilities and entry points, the pentester begins to test the exploits found within your network, applications, and data. The goal is for the ethical hacker is to see exactly how far they can get into your environment, identify high-value targets, and avoid any detection.

If you established a scope initially, then the pentester will only go as far as determined by the guidelines you agreed upon during the initial scoping. For example, you may define in your scope to not pentest cloud services or avoid a zero-day attack simulation.
Some of the standard exploit tactics include:

    Web Application Attacks
    Network Attacks
    Memory-based attacks
    Wi-Fi attacks
    Zero-Day Angle
    Physical Attacks
    Social engineering

The ethical hacker will also review and document how vulnerabilities are exploited as well as explain the techniques and tactics used to obtain access to high-value targets. Lastly, during the exploitation phase, the ethical hacker should explain with clarity what the results were from the exploit on high-value targets.
#### Post-Exploitation, Risk Analysis & Recommendations

After the exploitation phase is complete, the goal is to document the methods used to gain access to your organization’s valuable information. The penetration tester should be able to determine the value of the compromised systems and any value associated with the sensitive data captured.

Some pentesters are unable to quantify the impact of accessing data or are unable to provide recommendations on how to remediate the vulnerabilities within the environment. Make sure you ask to see a sanitized penetration testing report that clearly shows recommendations for fixing security holes and vulnerabilities.

Once the penetration testing recommendations are complete, the tester should clean up the environment, reconfigure any access he/she obtained to penetrate the environment, and prevent future unauthorized access into the system through whatever means necessary.
Typical cleanup activities include:

    Removing any executables, scripts, and temporary files from compromised systems
    Reconfiguring settings back to the original parameters prior to the pentest
    Eliminating any rootkits installed in the environment
    Removing any user accounts created to connect to the compromised system

#### Reporting

Reporting is often regarded as the most critical aspect of a pentest. It’s where you will obtain written recommendations from the penetration testing company and have an opportunity to review the findings from the report with the ethical hacker(s).

The findings and detailed explanations from the report will offer you insights and opportunities to significantly improve your security posture. The report should show you exactly how entry points were discovered from the OSINT and Threat Modeling phase as well as how you can remediate the security issues found during the Exploitation phase.

Learn about 25 benefits of performing a pentest here!  

Your penetration report will also include a helpful overall security risk score. It may be inspired by ITIL, FAIR, or DREAD methods and look something like this:

#### TCP Scans

##### TCP SYN
TCP SYN scanning sends a single packet to each scanned port with the SYN flag set. This indicates a request to open a new connection. If the scanner receives a response that has the SYN and ACK flags set, this indicates that the system is moving to the second phase in the three-way TCP handshake and that the port is open. TCP SYN scanning is also known as "half-open" scanning. 

##### TCP Connect
TCP connect scanning opens a full connection to the remote system on the specified port. This scan type is used when the user running the scan does not have the necessary permissions to run a half-open scan.