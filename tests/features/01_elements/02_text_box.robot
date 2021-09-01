*** Settings ***
Documentation   Validates Elements Page functionality

Library         SeleniumLibrary  run_on_failure=Nothing
Library         PageObjectLibrary
Library         ../../../tests/step_definitions/base_steps.py
Library         ../../../tests/step_definitions/elements_steps.py

Suite Setup     Setup Browser
Suite Teardown  Close Browser

Test Teardown   Run Keyword If Test Failed  Capture Page Screenshot


*** Test Cases ***

Text Box Page - Validate page elements
    [Tags]              elements    text_box_page
    [Documentation]     Varifies that Text Box Page opens, has all the expected elements,
    ...                 and heading has the expected text

    Given Open Page    Text Box Page
    Then Happy Elements Should Be Visible     Text Box Page
    And Page Heading Should Be Correct    Text Box Page


Text Box Page - Validate Full Name field
    [Tags]              elements    text_box_page
    [Documentation]     Varifies that Name output field shows up only when,
    ...                 Full Name field is filled with a valid text

    Given Open Page    Text Box Page
    And Generate Test Customer Data
    And Fill Field With    Full Name field    Nothing
    When Push Button    Submit button
    Then Output Field Should Not Be Visible    Output Name
    Given Fill Field With    Full Name field   Customer Name
    When Push Button    Submit button
    Then Output Field Should Be Visible    Output Name
    And Output Field Text Should Contain    Output Name   Customer Name


Text Box Page - Validate Email field
    [Tags]              elements    text_box_page
    [Documentation]     Varifies that Email output shows up only when,
    ...                 Email field is filled with a valid email address

    Given Open Page    Text Box Page
    And Generate Test Customer Data
    And Fill Field With    Email field    Nothing
    When Push Button    Submit button
    Then Output Field Should Not Be Visible    Output Email
    Given Fill Field With    Email field    Invalid Email
    When Push Button    Submit button
    Then Output Field Should Not Be Visible    Output Email
    Given Fill Field With    Email field   Customer Email
    When Push Button    Submit button
    Then Output Field Should Be Visible    Output Email
    And Output Field Text Should Contain    Output Email    Customer Email


Text Box Page - Validate Current Address field
    [Tags]              elements    text_box_page
    [Documentation]     Varifies that Current Address output shows up only when,
    ...                 Current Address field is filled with a valid text

    Given Open Page    Text Box Page
    And Generate Test Customer Data
    And Fill Field With    Current Address field    Nothing
    When Push Button    Submit button
    Then Output Field Should Not Be Visible    Output Current Address
    Given Fill Field With    Current Address field   Customer Address
    When Push Button    Submit button
    Then Output Field Should Be Visible    Output Current Address
    And Output Field Text Should Contain    Output Current Address   Customer Address


Text Box Page - Validate Permanent Address field
    [Tags]              elements    text_box_page
    [Documentation]     Varifies that Permanent Address output shows up only when,
    ...                 Permanent Address field is filled with a valid text

    Given Open Page    Text Box Page
    And Generate Test Customer Data
    And Fill Field With    Permanent Address field    Nothing
    When Push Button    Submit button
    Then Output Field Should Not Be Visible    Output Permanent Address
    Given Fill Field With    Permanent Address field   Customer Address
    When Push Button    Submit button
    Then Output Field Should Be Visible    Output Permanent Address
    And Output Field Text Should Contain    Output Permanent Address   Customer Address
