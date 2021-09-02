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
    ...                 and heading and subheadings have the expected text

    Given Open Page    Register Page
    Then Happy Elements Should Be Visible    Register Page
    And Page Heading Should Be Correct    Register Page


Register Page - Validate Captcha
    [Tags]              book_store    register_page
    [Documentation]     Registers a new Book Store user

    Given Open Page    Register Page
    And Generate Test Customer Data
    And Fill Field With    First Name field   Customer First Name
    And Fill Field With    Last Name field   Customer Last Name
    And Fill Field With    Username field   Customer Email
    And Fill Field With    Password field   Customer Password
    And Check Captcha
    When Push Button    Register button
    Then Captcha Verification Message Should Be Visible
    And Captcha Verification Text Should Be Correct
