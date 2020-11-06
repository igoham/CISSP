
# VPNS

### PPP - Point-To-Point Protocol

- Layer: 2
- Developer: Microsoft
- Authentication: PAP, CHAP, and Microsoft Challenge Handshake Authentication Protocol (MS-CHAP).

PPP supports the transmission of network packets over a serial point-to-point link by specifying framing mechanisms for encapsulating network protocols such as Internet Protocol (IP), Internetwork Packet Exchange (IPX), or NetBEUI into PPP frames. 

PPP was largley replaced by Serial over IP (SLIP)

PPP encapsulation is based on the High-level Data Link Control (HDLC) derived from the mainframe environment. These PPP frames can be transmitted over serial transmission lines such as Plain Old Telephone Service (POTS), Integrated Services Digital Network (ISDN), and packet-switched networks such as X.25. 

### PPTP - Point-To-Point tunneling protocol

- Layer: 2
- Developer: Microsoft
- port 1723
- Uses TCP

PPTP is an extension of PPP and is based on PPP negotiation, authentication, and encryption schemes. PPTP encapsulates Internet Protocol (IP), Internetwork Packet Exchange (IPX), or NetBEUI packets into PPP frames, creating a “tunnel” for secure communication across a LAN or WAN link. The PPTP tunnel is responsible for authentication and data encryption and makes it safe to transmit data over unsecured networks.
Uses PPP for authentication; however, you can use EAP-TLS for authenticaton as well.


### L2TP

- Layer: 2
- Lacks its own confidentaility of its own
- Uses UDP

- The only one of the four common vpn protovols that can natively support non-ip protocols. 
    - PPTP, l2f, and IPSEC are all only IP protocols
    
The entire L2TP packet, including payload and L2TP header, is sent within a User Datagram Protocol (UDP) datagram. A virtue of transmission over UDP (rather than TCP) is that it avoids the "TCP meltdown problem".[3][4] It is common to carry PPP sessions within an L2TP tunnel. L2TP does not provide confidentiality or strong authentication by itself. IPsec is often used to secure L2TP packets by providing confidentiality, authentication and integrity. The combination of these two protocols is generally known as L2TP/IPsec (discussed below). 

An L2TP tunnel can extend across an entire PPP session or only across one segment of a two-segment session. This can be represented by four different tunneling models, namely: 
    
### GRE - Generic Routing Encryption


## WAN technologies

### Packet switch technologies
#### x.25

An old packet switched wan technology that has alrgeley been replaced by frame replay. Unlike greame replay x.25 provides
error correction but doing so comes at expense of latency.



## Circuit switched technologies
Circuits are dedicated lines. Any time you think of a circit switched technology you have a direct connection to the ISP backbone.
Other examples of circuit switched technologies include ISDN, POTS and PPP

#### T lines - T1/2/3/4/5
T carrier lines are are circuit switched WAN techn that require a dedicated circut. This technology would be used to connect the 
customer to the the ISP. Cir

### Cell Switching Technologies
#### ATM

ATM is a **cell-switched** wan technology. Cell switching is similar to packet switching but instead of using varaible length packaged it uses fixed length cells.
ATM uses cells that are 53 bytes long. As a result ATM is mcuh more predictable than packet switched technologies.


| Protocol | Frequency |  Multiplexing method | Speed/throughput | description
| --- | --- | --- | --- | ---|
|802.11a|5 Ghz|OFDM| 11Mbps | Original enterprise grade - Came to market second. Only allowed in US markets due to frequency restrictions
|802.11B|2.4 Ghz|DSSS| 11Mbps | Original consumer grade - came to market first and won the market share
|802.11e|?|?| ? | Introduced QOS to wireless
|802.11f|n/a| n/a | n/a|The standard that introduced roaming between APs
|802.11g|2.4 Ghz|DSSS| 54 Mbps|Speed enhancement for 802.11b. If a product meets the specifications of 802.11b, its data transfer rates are up to 11 Mbps, and if a product is based on 802.11g, that new product can be backward-compatible with older equipment but work at a much higher transfer rate
|802.11h|5 Ghz|OFDM|11Mbps | Build on the 802.11a standard to me the EU frequiency requirements
|802.11j|Ghz|?| 11Mbps | Task force was tasked with together many of the different standards and streamlining their development to allow for better interoperability across borders.
|802.11n|5 Ghz|OFDM| 100Mbps | This standard uses a concept called multiple input, multiple output (MIMO) to increase the throughput. This requires the use of two receive and two transmit antennas to broadcast in parallel using a 20-MHz channel.
|802.11ac|5 Ghz| 1.3 Gbps | The IEEE 802.11ac WLAN standard is an extension of 802.11n. It also operates on the 5- GHz band, but increases throughput to 1.3 Gbps. 802.11ac is backward compatible with 802.11a, 802.11b, 802.11g and 802.11n, but if in compatibility mode it slows down to the speed of the slower standard. Another benefit of this newer standard is its support for beamforming, which is the shaping of radio signals to improve their performance in specific directions. In simple terms, this means that 802.11ac is better able to maintain high data rates at longer ranges than its predecessors.
|802.11|Ghz| 11Mbps | aa


### WiFiMax

All the wireless standards covered so far are WLAN-oriented standards. 802.16 is a MAN
wireless standard, which allows for wireless traffic to cover a much wider geographical area.
This technology is also referred to as broadband wireless access. (A commercial technology
that is based upon 802.16 is WiMAX.) A common implementation of 802.16 technology
is shown inthe below picture


![KERBEROS](https://gyazo.com/fd9fc774b43260248d411bc417460569.png)



*Network classes and maximum hosts per class network**

**802.11 table MUST be known**

**Research DNSSEC**

**How do CRLs work**

There are two methods for validating certificate revocation.

1. The client must check wtih the CA and download the CRL. The client is 100% responsbile for checking and validating the cert is not revoked.
 This process fails open as to not stop clients that could not validate if the cert was on a CRL from accessessing content.
 1. OSCP - Preforms realtime look up of cert revocation lookup
    - website sends cert to client
    - client concerned cert may be revoked, sends cert to CA
    - OSCP response from CA can have one of three possible responses
        - Good
        - Unknown
        - Revoked
    - If the CA fails to connect there are two options
        - Terminate conneciton
        - Accept the connection

1. OCSP stapling - Shifts burden to the webserver
    - Webserver checks the cert at regular intervals
    - Webserver Requests an advanced check of the cert
    - CA Response with the cert validity
    - Webserver caches until a client request the cert
    - CLient connects
    - Webserver sends stapled, timestamped and digitally signed response to client with to save it the effort of asking the CA


Both methods put a huge burden on the client however OSCP removes the burden of the client to download and validate massive CRLS.
This is done server side and interfaces via OSCP.

**Research Kerberos**

1. KDC typically contains both the AS (authentication server) and TGS (Ticket granting server)
1. Messages can be the following
    1. Authenticators are a record containing information that is generated using information that is ONLY known to the client and KDC
        - Uses Session key to create data
        - Used to preform mutual authentication
    1. Tickets
    
    
### Workflow

1. User messages KDC (AS) -> I want to auth ( unencrypted)
1. KDC (AS) - Validates the request is coming from a known user and generates TGt -> User
1. User Decrypted TGT from privat key (password)
1. User sends TGS its newly recieved TGT message requesting access to downstream app
1. TGS approves the request and sends back a Service Ticket aka ST
1. User sends Service Ticket to Service Principal with authenticator
1. Service validates authenticator and sends back its own authenticator.
1. Both parties can now authenticate each other and have sessions keys to do so
    
![KERBEROS](https://gyazo.com/62f2ebcc98a0658997f00efc69b6de53.png)
![KERBEROS](https://gyazo.com/9ad258f04aa3331f74346b21f4be5ae8.png)



**Research Simple Provisioning Markup Language - SPML**

		○ What is SPML? 943
			§ What does it allow for the automation of?
			§ What generates SPLM requests? 
			§ What is a PSP in this context
			§ What is a PST in this context?
			§ What is a SOA? 947
                    What is XACML

**xTacas vs tacas+**

Tacas was the original implementation. Then came Extened tacas as xtacas. This was replaced by Tacas+.

Tacas+
- Introduced 2fa
- ONLY tcp


## XSS Explained

- Input validation needs to be preformed in all input!
- This is the best way to prevert XSS

#### Stored XSS 
1. Stores resulting javascript in the backend database to be trigged when a user loads a specific page

#### Reflected XSS
1. Requires input that is not escaped properly
1. Requires a user to be sent a link
    - User gets link with xss javascript in the URL
    - Javascript makes a call to external webserver to steal your cookie
    
#### Dom-Based XSS

This attack can be preformed when you user javascript to dynamically load different page values on the same page. 
For example a user can do training withing having to send multiple http requests to get the next page.

- Requests are processed by a local script rather than being sent back to server
- Requests typically have the # in them as everything after the # doesn't re-load the page


### PDU - Protocol Data Unit

In telecommunications, a protocol data unit (PDU) is a single unit of information transmitted among peer entities of a computer network. A PDU is composed of protocol-specific control information and user data. In the layered architectures of communication protocol stacks, each layer implements protocols tailored to the specific type or mode of data exchange. 

#### OSI Model

    The Layer 4: transport layer PDU is the segment or the datagram.
    The Layer 3: network layer PDU is the packet.
    The Layer 2: data link layer PDU is the frame.
    The Layer 1: physical layer PDU is the bit or, more generally, symbol.
    

Each datagram has two components, a header and a data payload. The header contains all the information sufficient for routing from the originating equipment to the destination without relying on prior exchanges between the equipment and the network. Headers may include source and destination addresses as well as a type field. The payload is the data to be transported. This process of nesting data payloads in a tagged header is called encapsulation.
![OSI to TCP IP models](https://gyazo.com/9823118ba732fe0c677cbc3ac948159f.png)
 
#### DARPA IP Suite
    The transport layer PDU is the TCP segment for TCP, and the datagram for UDP.
    The Internet layer PDU is the packet.
    The link layer PDU is the frame.
    
    
    
**IPv6 loopback addresses**

In IPv6, the IPv6 address reserved for loopback use is 0000:0000:0000:0000:0000:0000:0000:0001/128. 
This loopback address is so lengthy and can be further simplified as ::1/128. Click the below links to learn more about how to simplify and shorten an IPv6 address.



**TCP Handshake**
 
1. SYN - Client1 -> Client2
1. SYN-ACK - Client2 -> client 1
1. ACk - Client 1 -> client 2

**What layer does DNS and DHCP operate at?**

- DNS is an Application layer protocol
- DHCP works on the Data-link layer. This means that when a device needs an IP address they can only request one on the same network that its present on



**What are the differentces bettwen CSMA/CA and CSMA/CD**

*CSMA/CA*

CSMA/CA stands for Carrier Sense Multiple Access/ Collision Avoidance. It is a network protocol for transmission. It operates in the Medium Access Control Layer. This protocol is effective before the collision.

*CSMA/CD*

CSMA/CD stands for Carrier Sense Multiple Access/ Collision Detection. It is also a network protocol for transmission and operates in the Medium Access Control Layer. In this protocol, each station senses the collision by broadcast sensing. In case of collision, the transmission is stopped and they send a jam signal and then wait for a random time context before retransmission.
![MULTI TASKING](https://gyazo.com/8f5b4455c396c553b89475a5465ec1b5.png)

**OSI to TCP/IP Darpa Model**
![OSI to TCP IP models](https://gyazo.com/ab0362ff7c33f7648122d4bc0fdd0f94.png)


Network Cable Lengths

![OSI to TCP IP models](https://gyazo.com/544e2b76808dd3a08ad8e8abe9de9fa5.png)
![OSI to TCP IP models](https://gyazo.com/695ae4ad8f348a97397a40925927cc45.png)
