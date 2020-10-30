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

### Brewer-Nash

**What is TOGAF**
- How does it differ from Zachman or SABSA

Helps break an enterprise into components so you can apply securry to help comm