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

### Harrision Ruzzo - Ulman

### Noneinterference Model

### The grant take model

**Define the following Access Control Models**

- Noneinterference Model
- Graham-Denning Model
- Harrison Ruzzo Ulman Model


**What is TOGAF**
- How does it differ from Zachman or SABSA

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
