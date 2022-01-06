*** Settings ***
Documentation   Validates Elements Page functionality

Library         SeleniumLibrary  run_on_failure=Nothing
Library         PageObjectLibrary
Library         ../../base_steps.py
Library         ../../step_definitions/elements_steps.py

Suite Setup     Setup Browser
Suite Teardown  Close Browser

Test Teardown   Run Keyword If Test Failed  Capture Page Screenshot


*** Test Cases ***

Elements Page - Validate page elements
    [Tags]              elements    elements_page
    [Documentation]     Varifies that Elements Page opens, has all the expected elements,
    ...                 and heading and subheading have the expected text

    Given Open Page    Elements Page
    Then Happy Elements Should Be Visible    Elements Page
    And Page Heading Should Be Correct    Elements Page
