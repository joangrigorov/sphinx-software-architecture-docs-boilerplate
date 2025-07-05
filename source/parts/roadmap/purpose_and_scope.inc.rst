.. _roadmap/purpose_and_scope:

**********************************
Purpose and Scope of this document
**********************************
This document specifies the :term:`software architecture` of the {PROJECT_NAME} platform. All information
regarding the software architecture may be found in this document.

Elements and relationships
##########################
The contents of this document aims to embody information about how the {PROJECT_NAME} platform elements relate to each
other. This means that information about elements that does not pertain to their interaction will be omitted. Thus, this
software architecture document suppresses details of elements that do not affect how they use, are used by, relate to,
or interact with other elements.

.. _roadmap/purpose_and_scope/multiple_structures:

Multiple structures
###################
The {PROJECT_NAME} platform comprise a set of :term:`structures <structure>`. Although these structures are pictured
differently and have considerably different properties, all are inherently related; together they describe the
architecture of the entire system:

- **Module structures**
The {PROJECT_NAME} platform as a software system can be partitioned into units of implementation (Modules); Module
structures represent a code-based way of considering the system. They are assigned areas of functional responsibility.
There is less emphasis on how {PROJECT_NAME} manifests itself at runtime. For example, the {PROJECT_NAME} high-level
modules are its Administrative Backoffice portal, Client mobile application, the API :code:`{PROJECT_NAME}::Inbox` or
:code:`{PROJECT_NAME}\\PhoneCallScheduler` namespaces/packages, and so on. However, a module structure does not describe
how and when {PROJECT_NAME} interact at runtime.

- **Component-and-connector structures**
C&C are the runtime structures of the {PROJECT_NAME} platform. They represent the interaction between elements of the
system as it executes. For example, an {PROJECT_NAME} platform's component-and-connector structure is the communication
flow between microservices and the pub/sub, databases and other runtime components, how it is achieved, with the help of
what other software it works, and how it answers to architecturally significant requirements. All
component-and-connectors structures are orthogonal to the module structures, as in they deal with the dynamic aspects of
the running {PROJECT_NAME} system.

- **Allocation structures**
Allocation structures embody how the system relates to its environment. That includes the deployment of
the {PROJECT_NAME} platform elements, the distribution of work among external developers and their management.

The architecture of {PROJECT_NAME} consists of these structures.
These structures will be described further in this document as Views.

.. note::
    None of these structures alone is the entire architecture, although they all convey architectural information. The
    architecture consists of these structures as well as many others. This example shows that since architecture can
    comprise more than one kind of structure, there is more than one kind of element (e.g., implementation unit and
    processes), more than one kind of interaction among elements (e.g., subdivision and synchronization), and even more
    than one context (e.g., development time versus runtime). :cite:`ClementsBachmannEtAl10`
