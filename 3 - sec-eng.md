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


# Security Models - Lattice
When tealing with security models there are a few key things to remember:

- Simple generally refers to read
- Star generally refers to write

### Bell La-Padula Confidentiality Model

- Lattice based model

This is an older DOD confidentiality model. 
In this model all objects must be labeled from Top secret to public.
All objects must have a label for the system to work properly.
Systems are divided into subjects(Users) and Labeled Objects 

The model has the following properties:


![OSI to TCP IP models](https://gyazo.com/e61f4150c9b8a9be40ecf13948c828b9.png)



### Biba System Integrity Model
- Lattice based mode
- Defines rules of what a subject can do with the goal of maintaning interity 
This model is only concerned with the interity of data.

![OSI to TCP IP models](https://gyazo.com/b3aa6ec94cccb301d4abe0d6318bd877.png)


### The Lipner implementation

Combines both Biba and Bell La-padula into a working implmentation
with both. This is not its own moddle but rather a melding of both models into a working implementation that supports both confidentiaility
and integrity. 


# Security Models - Rule based


### Clark Wilson Integrity model

- More indepth than Biba
- 3 Goals of integirty
    - Preventing unauthorzed subjects from making chaninges
    - Preceting authorized subject from making BAD changes
    - Maintaining the consistency of the system
- 3 Rules
    - You must have well formed transactions
    - You must have seperation of duties
    - You must have the access triplet
        - Subject
        - Program
        - Object

### Brewer-Nash - Chinese Wall Model

Only one goal **Prevents conflicts of interest** 

### Graham Denning

DOn't need the specifics - Specifies rules to allow subjects access to objects

### Harrision Ruzzo - Ulman

An enchancement of Ghram Denning, added generic rights

### Noneinterference Model

In simple terms, a computer is modeled as a machine with inputs and outputs. Inputs and outputs are classified as either low (low sensitivity, not highly classified) or high (sensitive, not to be viewed by uncleared individuals). A computer has the non-interference property if and only if any sequence of low inputs will produce the same low outputs, regardless of what the high level inputs are.

That is, if a low (uncleared) user is working on the machine, it will respond in exactly the same manner (on the low outputs) whether or not a high (cleared) user is working with sensitive data. The low user will not be able to acquire any information about the activities (if any) of the high user. 

### The grant take model

Provides a framework for granting and taking permissions from a subject.

There are a total of four such rules:

    take rule allows a subject to take rights of another object (add an edge originating at the subject)
    grant rule allows a subject to grant own rights to another object (add an edge terminating at the subject)
    create rule allows a subject to create new objects (add a vertex and an edge from the subject to the new vertex)
    remove rule allows a subject to remove rights it has over on another object (remove an edge originating at the subject)

**What is TOGAF**
- How does it differ from Zachman or SABSA
- Sabsa defines a risk driven enterprise security model. Derived from the business requirements for security.  
- ZACHMAN defines an enterprise architecture
- TOGAF is the third major framework.
    - Breaks org down to components
    
https://gyazo.com/cfbfa012a3f0152d2694d46b4eb18a79


Helps break an enterprise into components so you can apply securry to help comm


## The Trusted Computing Base
https://www.youtube.com/watch?v=fwU7n_3h058
The TCB refers to ALL of the protection mechanisms that are responsible for protection of a system

- Reference Monitor Concept
    - What subjects are allowed to access what objects
    - The TCB mediates the access between all subjects and objects
    - Mediation occurs based on a set of rules - MAC / DAC?
    - Every control should have an assurance 
    
![OSI to TCP IP models](https://gyazo.com/c50a521ef31069e5d67a48981b53f592.png)
    
- Security Kernel - All security kernels must follow 3 rules
    - Subject can never bypass mediation in RMC
    - Isolation - Rules are tamper proof! 
        - The rules are isolated from user space
    - Verifiability
        - Logging and monitoring to verify mediation is working properly 
        
### Storage Types

There are three types of storage

- Primrcy
    - CPU registers, RAM
- Secondary
    - Optical drives, HDDS,
- Virtual Memory - Paging or swapping
    - Temporarily puts data from RAM onto secondary storage as RAM is full.

### Memory Types

- Dynamic RAM - DRAM
    - If the memory controller
does not “refresh” the value of 1, the capacitor will start losing its electrons and become a 0
or a corrupted value. This explains how dynamic RAM (DRAM) works. The data being held
in the RAM memory cells must be continually and dynamically refreshed so your bits do
not magically disappear. This activity of constantly refreshing takes time, which is why
DRAM is slower than static RAM. 
    - Cheaper
    - SLower


- Static RAM - SRAM
    - Does not need to be refreshed
    - Requires more transitors the dram
    - Expensive - Manufacturers cannot fit as many SRAM memory cells on a memory
chip as they can DRAM memory cells, which is why SRAM is more expensive
    - 

-  Synchronous DRAM (SDRAM) 
    -Synchronizes itself with the system’s CPU and
synchronizes signal input and output on the RAM chip. It coordinates its activities
333
with the CPU clock so the timing of the CPU and the timing of the memory
activities are synchronized. This increases the speed of transmitting and executing
data.

- Extended data out DRAM (EDO DRAM) 
    - This is faster than DRAM because
DRAM can access only one block of data at a time, whereas EDO DRAM can
capture the next block of data while the first block is being sent to the CPU for
processing. It has a type of “look ahead” feature that speeds up memory access.

- Burst EDO DRAM (BEDO DRAM) 
    - Works like (and builds upon) EDO DRAM
in that it can transmit data to the CPU as it carries out a read option, but it can send
more data at once (burst). It reads and sends up to four memory addresses in a small
number of clock cycles.

- Double data rate SDRAM (DDR SDRAM) 
    - Carries out read operations on the
rising and falling cycles of a clock pulse. So instead of carrying out one operation per
clock cycle, it carries out two and thus can deliver twice the throughput of SDRAM.
Basically, it doubles the speed of memory activities, when compared to SDRAM, with
a smaller number of clock cycles. Pretty groovy


- ROM - Standard read only memory
- PROM  - Programmable read-only memory (PROM) is a form of ROM that can be modified after it
has been manufactured. PROM can be programmed only one time because the voltage that
is used to write bits into the memory cells actually burns out the fuses that connect the
individual memory cells. The instructions are “burned into” PROM using a specialized
PROM programmer device
- EPROM - Erasable programmable read-only memory (EPROM) can be erased, modified, and
upgraded. EPROM holds data that can be electrically erased or written to. To erase the
data on the memory chip, you need your handy-dandy ultraviolet (UV) light device that
provides just the right level of energy. The EPROM chip has a quartz window, which is
where you point the UV light. Although playing with UV light devices can be fun for the
whole family, we have moved on to another type of ROM technology that does not require
this type of activity.
- EEPROM - EEPROM is similar to EPROM, but its data storage can be erased and modified
electrically by onboard programming circuitry and signals. This activity erases only 1 byte
at a time, which is slow. And because we are an impatient society, yet another technology
was developed that is very similar, but works more quickly
- Flask Memory - Small, generally used as ROM. Can we wiped with a single function so much faster then eeprom.







### Software Components
- System Kernel
    - Different from security kernel
- Firmware
    - Provides low level control of hardware
- Middleware 
    - is a translator for two pieces of software that do not know how to communicate directly

### Protection Mechanisms
All modern OS's are multi tasking systems so we need to ensure that processes cant interfere with each other

- Process isolation
- Time division multiplexing
    - Processess can access resouces ( such as cpu ) one at a time
- Processor States - CPus provide a few different levels of access to their functions
    - Problem state - Normal app levels
        - Lower privledge level ( user land)
        - Name comes from the fact that programs running at this level are meant to solve problems
    - Supervisor - Higher pricledge levels
        - Full access to CPU capabilities
- Operating system modes
    - User mode
    - Kernel Mode
- Ring protection Model
    - Ring 0 - Kernel, Firmware
    - Ring 1 - Drivers
    - Ring 2 - Not used in windows
    - Ring 3 - User Programs




### EAL Ratings

- **EAL1**: Functionally Tested

- **EAL2**: Structurally Tested

- **EAL3**: Methodically Tested and Checked

- **EAL4**: Methodically Designed, Tested and Reviewed

- **EAL5**: Semiformally Designed and Tested

- **EAL6**: Semiformally Verified Design and Tested
- **EAL7**: Formally Verified Design and Tested


### Multi Programming


**Research the process scheduler and its modes**
There are two modes or states in which a process can be in
    - Running = When a new process is created, it enters into the system as in the running state. 
    - Not running -Processes that are not running are kept in queue, waiting for their turn to execute. Each entry in the queue is a pointer to a particular process. Queue is implemented by using linked list. Use of dispatcher is as follows. When a process is interrupted, that process is transferred in the waiting queue. If the process has completed or aborted, the process is discarded. In either case, the dispatcher then selects a process from the queue to execute.

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



**What are type 1 and 2 for biomeethics errors?**

- A type 1 error is a false positive
    - For Biometrics this is when the requestor is falsely REJECTED
    - FRR
    = Falsely rejected a VALID user
- A type 2 error is a false negative
    - Bor Biometrics this si when the requester is falsely ACCEPTED
    - FAR
    - Falsely accepted an INVALID user
    
    



## System Security Modes
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

**Why destroy SSDs to prevent data leaks?**

Solid State Drives (SSD): These use flash memory to store data and data is not overwritten. It is way faster than HDD, as the data is accessed directly via a flash translation layer, thus reducing time for head movement. Because of this, when it comes to data remanence, simple overwriting won’t work with SSD. the following techniques should be used:

    Built in sanitization commands
    Crypto-erase
    Sanitization 
    
    
### Backup Modes

- Full backup – everything is backed up on a regular schedule regardless if anything has changed. The archive bit is reset upon each backup.
- Incremental backup – everything that has changed since the last full backup is backed up. The archive bit is reset.
- Differential backup – all files that have been modified since the last full backup are backed up. The archive bit is not reset. A full weekly backup with differential daily backups is preferred/faster restore than the full and incremental as in an incremental restore, all incremental backups need to be restored.
- Copy backup – same as a full backup but archive bit is not reset. This form is typically used for unscheduled backups and is used to prevent interfering with the regularly-scheduled daily backups.


**EAP vs PEAP vs EAP-TLS**

- EAP sends unencrypted credentials. EAP expected physically security to be in place and thus did not require encryption.
- PEAP - Protected EAP
- EAP-TLS - Sends a certificate to the server after a one time enrollment.
