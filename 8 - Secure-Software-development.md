# Secure software Development

## SDLC - Software Development life cycle

The SDLC is the software development portion of the systems life cycle, see below.

1. Planning and Management approval
    - First you must contruct the project plan have it approved by management
    - High level costs estimates
1. Requirements analysis
    - User needs
    - Data to be collected, stored and processed
    - Results in a detailed set of requirements
    - Requirements gathering Determine why to create this software, what the software
will do, and for whom the software will be created
1. Design Phase / prototyping phase
    - Requirements are transformed into detailed design docs
    - Design docs will outline
    - Design Deals with how the software will accomplish the goals identified, which are
encapsulated into a functional design
1. Development Phase
    - This is where the coding to write the system beginds.
    - Any of the different software development methodologies may be used, eg Agile, Waterfall, Devops
    - Development Programming software code to meet specifications laid out in the
design phase and integrating that code with existing systems and/or libraries
1. Testing
    - The application should be thoroughly tested
    = This is when Certification occurs 
    - Testing Verifying and validating software to ensure that the software works as
planned and that goals are met
1. Deployment
    - Final stage of SDLC
    - This is when arredication occurs
        - Official management signoff of the system for a specific period of time
1. Operations
    - This is when an application is in steady state operations
1. Disposal
    - The most critical component in the SLC as we need to properly dispose of the data in the systems that we shut down

![SDLC](https://gyazo.com/c404cbc7c33d8420a8cb1c705096e57f.png)


### Maturity Models

**Software specific mature model**
![SDLC](https://gyazo.com/2154733de2fd1a449dd468f6c0745252.png)

**General Maturity model**
![SDLC](https://gyazo.com/8134366fd399c1f0fb95b12fce44ab69.png)



**obfuscation techniques**
There are three common obfuscation techniques
- Lexical
    - Changes the names of functions and variables to random names
- Data
    - Modifies the data structure in use by the application
- Control flow
    - Modifies the control flow to create irrelevant loops, if statements, etc
    
    
**Covert Channels**
Two major types of covert channel
- Storage
    - Far more common!
- Timing


### Secure Programming
- Input Validation
    - Only properly formed data is accepted
- Session Managment
    - Ensureing that a session was allowed to be created and terminating sessions when they are no longer needed
        - Time outs
        - Screen savers
- Polyinstantiation 
    - Create different objects with the same name simultaneously 
    - Can be used to show two individuals with different clearances different information
        - Prevents inference attacks if data is missing due to not having a high enough clearance
        
        
        
## Databases

- A **tuple** is a **row** or **record** in a database
- A column can be referred to as an **attribute**
- The intersection of a tuple and a attribute is a **cell** or a **field**


**Define the following database terms**

- Atomicity
    - All changes occur or NOTHING changes
- Isolation
    - Transactions are invisibie to other users until they are complete
- Consistency
    - All updates to the database are consistent with the rules of the database
- Durability
    - Completed transactions will not be lost
- Cardinality 
    - is the number of rows in a table.
- Degree
    - is the number of columns in a table
    
    
**What is an object oriented database?**

An object-oriented database (OODBMS) or object database management system (ODBMS) is a database that is based on object-oriented programming (OOP). The data is represented and stored in the form of objects. OODBMS are also called object databases or object-oriented database management systems.

ZODB *(ZOPE DB)* for Python is an example of a OODBMS


**Data normalization Processes**
![Data Normalization](https://gyazo.com/b8f7f3d1d4e39c120404b9fba409340e.png)



**Define the following database backup terms**
- Remote journalling
    - Remote Journaling is the process of recording the product of a computer application in a distant data storage environment, concurrently with the normal recording of the product in the primary environment.
- Electronic vaulting
    - The term electronic vaulting is used to describe the transfer of data by electronic means to a backup site, as opposed to the physical shipment of backup tapes or disks. 
****



**What are candidate keys**

A candidate key is a combination of attributes that uniquely identify a database record without referring to any other data. Each table may have one or more candidate. One of these candidate keys is selected as the table primary key. A table contains only one primary key, but it can contain several candidate keys. If a candidate key is composed of two or more columns, then it's called a composite key.

**How to test coverate computed**


    (A) the total lines of code in the piece of software you are testing, and
    (B) the number of lines of code all test cases currently execute, and
    Find (B divided by A) multiplied by 100 – this will be your test coverage %.


- Formula = (A * B) * 100 = coverage%
    - (650 / 1000) * 100 = 65% 
 