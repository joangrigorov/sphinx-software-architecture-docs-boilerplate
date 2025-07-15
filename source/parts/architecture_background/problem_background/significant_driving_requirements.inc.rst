.. _architecture_background/problem_background/significant_driving_requirements:

Significant Driving Requirements
################################

This section describes behavioral and quality attribute requirements (original or derived) that shaped the
:term:`software architecture`. Included are any scenarios that express driving behavioral and quality attribute goals.

Quality Attribute Scenarios
===========================
The quality attribute scenarios are a way to represent architecturally-significant requirements, organized by quality
attribute such as performance, security, availability, etc. Each scenario is named and includes a stimulus, source of
the stimulus, environment, artifact, response measure, and response. These scenarios formalize how the system is
expected to behave in response to a stimulus, what part of the system is being stimulated, under what circumstances
(environment) and how the expected response is measured for the design to be considered successful.

Scalability
***********

.. qas::
   :stimulus_source: Driver
   :stimulus: Requests new route due to roadblock
   :environment: production
   :artifact: API
   :response: System provides alternative routing
   :response_measure: High system availability 99.99%
   :caption: Quality Attribute Scenario for map rerouting system availability
   :name: qas/availability/map-rerouting
