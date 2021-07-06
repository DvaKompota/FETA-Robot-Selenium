*** Settings ***
Documentation   Validates Home Page functionality

Resource     ../resources/pages/base_page.resource
Resource     ../resources/pages/home_page.resource

Suite Setup     Setup Browser
Suite Teardown  Close Browser

Test Teardown   Run Keyword If Test Failed  Capture Page Screenshot

*** Test Cases ***

Home Page - Validate happy elements
    [Tags]              home_page
    [Documentation]     Validates Home Page opens and has all the expected elements

    When Open Home Page
    Then Validate happy elements
