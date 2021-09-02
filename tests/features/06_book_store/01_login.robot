*** Settings ***
Documentation   Validates Elements Page functionality

Library         SeleniumLibrary  run_on_failure=Nothing
Library         PageObjectLibrary
Library         ../../../tests/step_definitions/base_steps.py

Suite Setup     Setup Browser
Suite Teardown  Close Browser

Test Teardown   Run Keyword If Test Failed  Capture Page Screenshot


*** Test Cases ***

Login Page - Validate page elements
    [Tags]              book_store    login_page
    [Documentation]     Varifies that Login Page opens, has all the expected elements,
    ...                 and heading and subheadings have the expected text

    Given Open Page    Login Page
    Then Happy Elements Should Be Visible    Login Page
    And Page Heading Should Be Correct    Login Page
