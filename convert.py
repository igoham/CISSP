test = """
• Security should be addressed in each phase of system development. It should not be
addressed only at the end of development because of the added cost, time, and effort
and the lack of functionality.
• The attack surface is the collection of possible entry points for an attacker. The
reduction of this surface reduces the possible ways that an attacker can exploit a
system.
• Threat modeling is a systematic approach used to understand how different threats
could be realized and how a successful compromise could take place.
• Computer-aided software engineering refers to any type of software that allows for
the automated development of software, which can come in the form of program
editors, debuggers, code analyzers, version-control mechanisms, and more. The goals
are to increase development speed and productivity and reduce errors.
• Various levels of testing should be carried out during development: unit (testing
individual components), integration (verifying components work together in the
production environment), acceptance (ensuring code meets customer requirements),
regression (testing after changes take place), static analysis (reviewing programming
code), and dynamic analysis (reviewing code during execution).
• Fuzzing is the act of sending random data to the target program in order to trigger
failures.
• Zero-day vulnerabilities are vulnerabilities that do not currently have a resolution or
solution.
• The ISO/IEC 27034 standard covers the following items: application security
overview and concepts, organization normative framework, application security
management process, protocols and application security control data structure, case
studies, and application security assurance prediction.
• The Open Web Application Security Project (OWASP) is an organization dedicated
to helping the industry develop more secure software.
• An integrated product team (IPT) is a multidisciplinary development team with
representatives from many or all the stakeholder populations.
• The CMMI model uses five maturity levels designated by the numbers 1 through 5.
Each level represents the maturity level of the process quality and optimization. The
1423
levels are organized as follows: 1 = Initial, 2 = Repeatable, 3 = Defined, 4 = Managed,
5 = Optimizing.
• CMMI (Capability Maturity Model Integration) is a process improvement approach
that provides organizations with the essential elements of effective processes, which
will improve their performance.
• Change management is a systematic approach to deliberately regulating the changing
nature of projects. Change control, which is a subpart of change management, deals
with controlling specific changes to a system.
• There are several SDLC methodologies: Waterfall (sequential approach that requires
each phase to complete before the next one can begin), V-shaped (emphasizes
verification and validation at each phase), Prototyping (creating a sample of the code
for proof-of-concept purposes), Incremental (multiple development cycles are carried
out on a piece of software throughout its development stages), Spiral (iterative
approach that emphases risk analysis per iteration), Rapid Application Development
(combines prototyping and iterative development procedures with the goal of
accelerating the software development process), and Agile (iterative and incremental
development processes that encourage team-based collaboration, where flexibility and
adaptability are used instead of a strict process structure).
• Software configuration management (SCM) is the task of tracking and controlling
changes in the software through the use of authentication, revision control, the
establishment of baselines, and auditing. It has the purpose of maintaining software
integrity and traceability throughout the software development life cycle.
• Programming languages have gone through evolutionary processes. Generation one is
machine language (binary format). Generation two is assembly language (which is
translated by an assembler into machine code). Generation three is high-level
language (which provides a level of abstraction). Generation four is a very high-level
language (which provides more programming abstraction). Generation five is natural
language (which is translated using artificial intelligence).
• Data modeling is a process used to define and analyze data requirements needed to
support the business processes within the scope of corresponding systems and
software applications.
• Object-oriented programming provides modularity, reusability, and more granular
control within the programs themselves compared to classical programming
languages.
• Objects are members, or instances, of classes. The classes dictate the objects’ data
types, structure, and acceptable actions.
• In OOP, objects communicate with each other through messages, and a method is
functionality that an object can carry out. Objects can communicate properly because
they use standard interfaces.
• Polymorphism is when different objects are given the same input and react
differently.
1424
• Data and operations internal to objects are hidden from other objects, which is
referred to as data hiding. Each object encapsulates its data and processes.
• Object-oriented design represents a real-world problem and modularizes the problem
into cooperating objects that work together to solve the problem.
• If an object does not require much interaction with other modules, it has low
coupling.
• The best programming design enables objects to be as independent and as modular as
possible; therefore, the higher the cohesion and the lower the coupling, the better.
• An object request broker (ORB) manages communications between objects and
enables them to interact in a heterogeneous and distributed environment.
• Common Object Request Broker Architecture (CORBA) provides a standardized
way for objects within different applications, platforms, and environments to
communicate. It accomplishes this by providing standards for interfaces between
objects.
• Component Object Model (COM) provides an architecture for components to
interact on a local system. Distributed COM (DCOM) uses the same interfaces as
COM, but enables components to interact over a distributed, or networked,
environment.
• Open Database Connectivity (ODBC) enables several different applications to
communicate with several different types of databases by calling the required driver
and passing data through that driver.
• Object linking and embedding (OLE) enables a program to call another program
(linking) and permits a piece of data to be inserted inside another program or
document (embedding).
• Service-oriented architecture (SOA) provides standardized access to the most needed
services to many different applications at one time. Service interactions are selfcontained and loosely coupled so that each interaction is independent of any other
interaction.
• Java security employs a sandbox so the applet is restricted from accessing the user’s
hard drive or system resources. Programmers have figured out how to write applets
that escape the sandbox.
• SOAP allows programs created with different programming languages and running
on different operating systems to interact without compatibility issues.
• There are three main types of cross-site scripting (XSS) attacks: nonpersistent XSS
(exploiting the lack of proper input or output validation on dynamic websites),
persistent XSS (attacker loads malicious code on a server that attacks visiting
browsers), and DOM (attacker uses the DOM environment to modify the original
client-side JavaScript).
• A database management system (DBMS) is the software that controls the access
restrictions, data integrity, redundancy, and the different types of manipulation
available for a database.
1425
• A database primary key is how a specific row is located from other parts of the
database in a relational database.
• A view is an access control mechanism used in databases to ensure that only
authorized subjects can access sensitive information.
• A relational database uses two-dimensional tables with rows (tuples) and columns
(attributes).
• A hierarchical database uses a tree-like structure to define relationships between data
elements, using a parent/child relationship.
• Most databases have a data definition language (DDL), a data manipulation language
(DML), a query language (QL), and a report generator.
• A data dictionary is a central repository that describes the data elements within a
database and their relationships.
• Database integrity is provided by concurrency mechanisms. One concurrency control
is locking, which prevents users from accessing and modifying data being used by
someone else.
• Entity integrity makes sure that a row, or tuple, is uniquely identified by a primary
key, and referential integrity ensures that every foreign key refers to an existing
primary key.
• A rollback cancels changes and returns the database to its previous state. This takes
place if there is a problem during a transaction.
• A commit statement saves all changes to the database.
• A checkpoint is used if there is a system failure or problem during a transaction. The
user is then returned to the state of the last checkpoint.
• Aggregation can happen if a user does not have access to a group of elements, but has
access to some of the individual elements within the group. Aggregation happens if
the user combines the information of these individual elements and figures out the
information of the group of data elements, which is at a higher sensitivity level.
• Inference is the capability to derive information that is not explicitly available.
• Common attempts to prevent inference attacks are partitioning the database, cell
suppression, and adding noise to the database.
• Polyinstantiation is the process of allowing a table to have multiple rows with the
same primary key. The different instances can be distinguished by their security levels
or classifications.
• Data warehousing combines data from multiple databases and data sources.
• Data mining is the process of searching, filtering, and associating data held within a
data warehouse to provide more useful information to users.
• Data-mining tools produce metadata, which can contain previously unseen
relationships and patterns.
• A virus is an application that requires a host application for replication.
• Macro viruses are common because the languages used to develop macros are easy to
1426
use and they infect Microsoft Office products, which are everywhere.
• A polymorphic virus tries to escape detection by making copies of itself and
modifying the code and attributes of those copies.
• A worm does not require a host application to replicate.
• A logic bomb executes a program when a predefined event takes place, or a date and
time are met.
• A Trojan horse is a program that performs useful functionality apparent to the user
and malicious functionally without the user knowing it.
• Botnets are networks of bots that are controlled by C&C servers and bot herders.
• Antimalware software is most effective when it is installed in every entry and end
point and covered by a policy that delineates user training as well as software
configuration and updating.
• Assessing the security of acquired software, in addition to internal or third-party tests,
requires that we assess the reliability and maturity of the vendor.
"""

test = test.replace("•", "-")
x=1