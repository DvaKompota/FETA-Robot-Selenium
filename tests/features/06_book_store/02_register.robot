*** Settings ***
Documentation   Validates Elements Page functionality

Library         SeleniumLibrary  run_on_failure=Nothing
Library         PageObjectLibrary
Library         ../../../tests/step_definitions/base_steps.py
Library         ../../../tests/step_definitions/book_store_steps.py

Suite Setup     Setup Browser
Suite Teardown  Close Browser

Test Teardown   Run Keyword If Test Failed  Capture Page Screenshot


*** Test Cases ***

Register Page - Validate page elements
    [Tags]              book_store    register_page
    [Documentation]     Varifies that Register Page opens, has all the expected elements,
    ...                 and heading and subheading have the expected text

    Given Open Page    Register Page
    Then Happy Elements Should Be Visible    Register Page
    And Page Heading Should Be Correct    Register Page
