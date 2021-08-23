*** Settings ***
Documentation   Validates Elements Page functionality

Library         SeleniumLibrary  run_on_failure=Nothing
Library         PageObjectLibrary
Library         ../../tests/step_definitions/base_steps.py

Suite Setup     Setup Browser
Suite Teardown  Close Browser

Test Teardown   Run Keyword If Test Failed  Capture Page Screenshot


*** Test Cases ***
Elements Page - Validate page elements
    [Tags]              elements    elements_page
    [Documentation]     Varifies that Elements Page opens, has all the expected elements,
    ...                 and heading and subheading have the expected text
    When Open Page    Elements Page
    Then Happy Elements Should Be Visible    Elements Page
    And Page Heading Should Be Visible    Elements Page

Text Box Page - Validate page elements
    [Tags]              elements    text_box_page
    [Documentation]     Varifies that Text Box Page opens, has all the expected elements,
    ...                 and heading has the expected text
    When Open Page    Text Box Page
    Then Happy Elements Should Be Visible     Text Box Page
    And Page Heading Should Be Visible    Text Box Page

