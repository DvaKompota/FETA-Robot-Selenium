*** Settings ***
Documentation   Validates Page Object Model's structure, inheritance and methods

Library         pom_steps.py

*** Test Cases ***

Inheritance TC
    [Tags]    unit_tests
    [Documentation]     Varifies that Child Page object inherits Parent Page Object's attributes and methods,
    ...                 while overriding those, that are redifined in Child Page object
    Given Validate Page Objects Inheritance