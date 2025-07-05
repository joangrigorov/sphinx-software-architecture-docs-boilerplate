.. _roadmap/viewpoint_definitions:

*********************
Viewpoint Definitions
*********************
This document employs a stakeholder-focused, multiple view approach to architecture documentation, as required by
ISO/IEC/IEEE 42010:2011, the recommended best practice for documenting the architecture of software-intensive systems
:cite:`ISO42010`.

As described in :ref:`roadmap/purpose_and_scope`, a software architecture comprises more than one software structure,
each of which provides an engineering handle on different system qualities. A view is the specification of one or more
of these structures, and documenting a software architecture, then, is a matter of documenting the relevant views and
then documenting information that applies to more than one view :cite:`ClementsBachmannEtAl10`.

.. note::

    ISO/IEC/IEEE 42010:2011 provides guidance for choosing the best set of views to document, by bringing stakeholder
    interests to bear. It prescribes defining a set of viewpoints to satisfy the stakeholder community. A viewpoint
    identifies the set of concerns to be addressed, and identifies the modeling techniques, evaluation techniques,
    consistency checking techniques, etc., used by any conforming view. A view, then, is a viewpoint applied to a
    system. It is a representation of a set of software elements, their properties, and the relationships among them
    that conform to a defining viewpoint. Together, the chosen set of views show the entire architecture and all of its
    relevant properties. A Software Architecture Document contains the viewpoints, relevant views, and information that
    applies to more than one view to give a holistic description of the system.

The remainder of :ref:`roadmap/viewpoint_definitions` defines the viewpoints used in this document. The following table
summarizes the stakeholders in this project and the viewpoints that have been
included to address their concerns.

.. csv-table:: Stakeholders and Relevant Viewpoints
   :file: stakeholders_and_viewpoints.csv
   :widths: 20 30 50
   :header-rows: 1


.. _roadmap/viewpoint_definitions/module_decomposition_viewpoint:

Module Decomposition Viewpoint Definition
#########################################

Abstract
--------
Views conforming to the module decomposition viewpoint partition the system into a unique non-overlapping set of
hierarchically decomposable implementation units (modules).

Stakeholders and Their Concerns Addressed
-----------------------------------------
- **Product Management**: Defines product scope, formulates project plans; Interested in schedules.
- **Software Developers**: Need to understand the code structure and how it is organized for implementation,
  maintenance, testing.

Elements, Relations, Properties, and Constraints
------------------------------------------------
Elements of the module decomposition viewpoint are modules, which are units of implementation that provide defined
functionality. Modules are hierarchically decomposable; hence, the relation is "is-part-of." Properties of elements
include their names, the functionality assigned to them (including a statement of the quality attributes associated with
that functionality), and their software-to-software interfaces. The module properties may include requirements
allocation, supporting requirements traceability.

Language(s) to Model/Represent Conforming Views
-----------------------------------------------
Views conforming to the module decomposition viewpoint may be represented by UML, using subsystems or classes to
represent elements and “is part of” or nesting to represent the decomposition relation.

Applicable Evaluation/Analysis Techniques and Consistency/Completeness Criteria
-------------------------------------------------------------------------------
Completeness/consistency criteria include:

a. no element has more than one parent;
b. major functionality is provided for by exactly one element;
c. the union of all elements' functionality covers the requirements for the system;
d. every piece of source code can be mapped to an element in the module decomposition view (if not, the view is not
   complete);
e. the selection of module aligns with current and proposed procurement decisions.

Additional consistency/completeness criteria apply to the specifications of the elements’ interfaces. Applicable
evaluation/analysis techniques include:

a. scenario-based evaluation techniques such as ATAM :cite:`bass2012software` to assure that projected changes are
   supported economically by the decomposition;
b. disciplined and detailed mapping to requirements to assure coverage and non-overlapping functionality;
c. cost-based techniques that determine the number and composition of modules for efficient procurement.

Viewpoint Source
----------------
Chapter 2, Section 2.1 of :cite:`ClementsBachmannEtAl10` describes the module decomposition style, which corresponds to
this viewpoint.

.. _roadmap/viewpoint_definitions/component_and_connector_viewpoint:

Component-and-Connector (C&C) Viewpoint Definition
##################################################

Abstract
--------
Views conforming to the component-and-connector viewpoint represent the system as a set of interacting components and
connectors. Components are the elements that perform computation, store data, and interface with the system's
environment. Connectors are the elements that enable communication, coordination, or cooperation among components.

Stakeholders and Their Concerns Addressed
-----------------------------------------
- **System End Users**: indirectly, as they are dependant on the runtime reliability and responsiveness of the system;
- **Software Developers**: who implement components and design their runtime interaction; who ensure components
  communicate and interact correctly; who analyze the system's runtime behavior for performance bottlenecks; who focus
  on potential vulnerabilities arising from component interactions; who manage and configure deployed components and
  their connections;

Elements, Relations, Properties, and Constraints
------------------------------------------------
Elements of the component-and-connector viewpoint are components and connectors. Components are the elements that
perform computation, store data, and interface with the system's environment. Connectors are the elements that enable
communication, coordination, or cooperation among components. The relations among components and connectors are
interactions, which are the ways in which components and connectors collaborate to perform the system's functions.
Properties of elements include their names, the functionality assigned to them (including a statement of the quality
attributes associated with that functionality), and their interfaces. The component-and-connector properties may include
requirements allocation, supporting requirements traceability.

Language(s) to Model/Represent Conforming Views
-----------------------------------------------
Views conforming to the component-and-connector viewpoint may be represented by UML, using components and connectors to
represent elements and interactions to represent the relations among them. The UML component diagram is a common
representation of this viewpoint. However, custom languages or notations may be used to represent the viewpoint.

Applicable Evaluation/Analysis Techniques and Consistency/Completeness Criteria
-------------------------------------------------------------------------------
Completeness/consistency criteria include:

a. All components required to fulfill system functionality are represented and appropriately connected.
b. Each connector specifies the required interaction properties (e.g., protocol and latency).
c. All specified interactions are traceable to system requirements and quality attributes.
d. The runtime view is consistent with the static structural view (e.g., module decomposition).

Viewpoint Source
----------------
Chapter 4 of :cite:`ClementsBachmannEtAl10` describes a set of component-and-connector styles, which correspond to this
viewpoint.


.. _roadmap/viewpoint_definitions/allocation_viewpoint:

Allocation Viewpoint Definition
###############################

Abstract
--------
Views conforming to the allocation viewpoint map the software system to elements of its development, execution, or
physical environments. These views highlight how software artifacts relate to their environment and address concerns
about resource usage, deployment, and organizational alignment.

Stakeholders and Their Concerns Addressed
-----------------------------------------
- **Investors**: indirectly, since work allocation and deployment influence the cost-effectiveness of
  the system development and operation;
- **Product Management**: who is concerned with allocating financial resources and task management for timelines and
  budgets;
- **Software Developers**: who are concerned with the deployment of the system; who are concerned with the distribution
  of work among internal/external developers and their management; who are concerned with the system's operational and
  maintenance requirements in terms of the infrastructural environment; who are concerned with system quality attributes
  such as performance, reliability, and security.

Elements, Relations, Properties, and Constraints
------------------------------------------------
Elements of the allocation viewpoint vary depending on the type of allocation and include:

- **Software artifacts**, such as components, modules, or data stores.
- **Environment elements**, such as (*hardware or virtualized*) nodes, networks, development teams, or geographic
  locations.

The primary relations are **allocated-to** or **hosted-on**, representing the mapping between software and environment
elements.

Properties of elements include:

- **Software artifacts**: name, resource requirements (e.g., memory, CPU, bandwidth), and runtime behavior
  characteristics.
- **Environment elements**: capacity (e.g., CPU credits, storage), availability, and constraints (e.g., physical
  location or redundancy requirements).

Constraints may include:

- **Resource constraints** (e.g., no single node can exceed 80% CPU usage).
- **Security requirements** (e.g., personal identifiable information cannot remain stored in a specific runtime
  component).
- **Redundancy and failover requirements** (e.g., critical components must have backup strategies).

Language(s) to Model/Represent Conforming Views
-----------------------------------------------
Views conforming to the allocation viewpoint can be represented using:

- **UML deployment diagrams**, showing the mapping of software artifacts to hardware elements.
- **Text-based tables or spreadsheets**, listing software elements and their allocations.
- **Custom architecture modeling notations**, such as AWS Reference Architecture Diagrams :cite:`awsrefarch`.

Applicable Evaluation/Analysis Techniques and Consistency/Completeness Criteria
-------------------------------------------------------------------------------
Completeness/consistency criteria include:

- All software artifacts are mapped to an environment element.
- No environment element is over-allocated based on its resource capacity.
- Deployment maps are consistent with system constraints, such as latency or geographic regulations.
- Allocation satisfies failover and redundancy requirements.

Applicable evaluation/analysis techniques include:

- **Resource analysis**: to verify adequate allocation of processing, memory, and storage resources.
- **Performance testing**: to confirm that deployment meets required performance thresholds.
- **Fault-tolerance testing**: to evaluate resilience under node or resource failure scenarios.
- **Scalability analysis**: to ensure the deployment supports expected growth in resource demands.

Viewpoint Source
----------------
Chapter 5 of :cite:`ClementsBachmannEtAl10` describes some allocation styles, which corresponds to this viewpoint.
