*** Settings ***
Documentation   Validates Elements Page functionality

Resource     ../resources/pages/base_page.resource
Resource     ../resources/pages/elements_page.resource

Suite Setup     Setup Browser
Suite Teardown  Close Browser

Test Teardown   Run Keyword If Test Failed  Capture Page Screenshot


*** Test Cases ***
Elements Page - Validate happy elements
    [Tags]              elements_page
    [Documentation]     Validates Elements Page opens and has all the expected elements

    When Open Elements Page
    Then Validate happy elements

Elements Page - Validate page heading
    [Tags]              elements_page
    [Documentation]     Validates Elements Page heading and subheading have expected text

    When Open Elements Page
    Then Validate page heading
