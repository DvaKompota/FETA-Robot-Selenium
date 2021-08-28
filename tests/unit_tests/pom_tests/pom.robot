*** Settings ***
Documentation   Validates Page Object Model's structure, inheritance and methods

Library         pom_steps.py

*** Test Cases ***

Inheritance TC
    [Tags]    unit_tests
    Given Validate Page Objects Inheritance