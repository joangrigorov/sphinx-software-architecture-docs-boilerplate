.. _roadmap/how_a_view_is_documented:

************************
How a View is Documented
************************
Each view is documented as follows, where the letter i stands for the number of the view:  1, 2, etc.:

#. **Name of the View**
#. **View Description** - This section describes the purpose and contents of the view. It should refer
   to (and match) the viewpoint description in :ref:`roadmap/viewpoint_definitions` to which this view conforms.
#. **View packet overview** - This section shows the set of view packets in this view, and provides
   rationale that explains why the chosen set is complete and non-duplicative. The set of view packets may be listed
   textually, or shown graphically in terms of how they partition the entire architecture being shown in the view.
#. **Architecture background** - Whereas the architecture background of :ref:`architecture_background`
   pertains to those constraints and decisions whose scope is the entire architecture, this section provides any
   architecture background (including significant driving requirements, design approaches, patterns, analysis results,
   and requirements coverage) that applies to this view.
#. **Variability mechanisms** - This section describes any architectural variability mechanisms (e.g., adaptation
   data, compile-time parameters, variable replication, and so forth) described by this view, including a description of
   how and when those mechanisms may be exercised and any constraints on their use.
#. **View packets** - This section presents all of the view packets given for this view. Each view packet is
   described using the following outline, where the letter i stands for the number of the view packet being described:
   1, 2, etc.
    - **Name of view packet #i**
    - **i.1: Primary presentation** - This section presents the elements and the relations among them that populate
      this view packet, using an appropriate language, languages, notation, or tool-based representation.
    - **i.2: Element catalog** - Whereas the primary presentation shows the important elements and relations of the
      view packet, this section provides additional information needed to complete the architectural picture. It
      consists of the following subsections:
        - **i.2.1: Elements** - This section describes each element shown in the primary presentation, details its
          responsibilities of each element, and specifies values of the elements’ relevant properties, which are defined
          in the viewpoint to which this view conforms.
        - **i.2.2: Relations** - This section describes any additional relations among elements shown in the primary
          presentation, or specializations or restrictions on the relations shown in the primary presentation.
        - **i.2.3: Interfaces** - This section specifies the software interfaces to any elements shown in the
          primary presentation that must be visible to other elements.
        - **i.2.4: Behavior** - This section specifies any significant behavior of elements or groups of interacting
          elements shown in the primary presentation.
        - **i.2.5: Constraints** - This section lists any constraints on elements or relations not otherwise
          described.
    - **i.3: Context diagram** - This section provides a context diagram showing the context of the part of the
      system represented by this view packet. It also designates the view packet’s scope with a distinguished symbol, and
      shows interactions with external entities in the vocabulary of the view.
    - **i.4: Variability mechanisms** - This section describes any variabilities that are available in the portion
      of the system shown in the view packet, along with how and when those mechanisms may be exercised.
    - **i.5: Architecture background** - This section provides rationale for any significant design decisions whose
      scope is limited to this view packet.
    - **i.6: Relation to other view packets** - This section provides references for related view packets, including
      the parent, children, and siblings of this view packet. Related view packets may be in the same view or in
      different views.
