*** Settings ***
Documentation   Validates Elements Page functionality

Library         SeleniumLibrary
Library         PageObjectLibrary
Library         ../resources/pages/elements/ElementsPage.py
Library         ../resources/pages/elements/TextBoxPage.py
Resource        ../resources/pages/base_page.resource

Suite Setup     Setup Browser
Suite Teardown  Close Browser

Test Teardown   Run Keyword If Test Failed  Capture Page Screenshot


*** Test Cases ***
Elements Page - Validate happy elements
    [Tags]              elements_page
    [Documentation]     Validates Elements Page opens and has all the expected elements

    When ElementsPage.Open Page
    Then ElementsPage.Validate happy elements

Elements Page - Validate page heading
    [Tags]              elements_page
    [Documentation]     Validates Elements Page heading and subheading have expected text

    When ElementsPage.Open Page
    Then ElementsPage.Validate page heading

Text Box Page - Validate happy elements
    [Tags]              text_box_page
    [Documentation]     Validates Text Box Page opens and has all the expected elements

    When TextBoxPage.Open Page
    Then TextBoxPage.Validate happy elements

Text Box Page - Validate page heading
    [Tags]              text_box_page
    [Documentation]     Validates Text Box Page heading has expected text

    When TextBoxPage.Open Page
    Then TextBoxPage.Validate page heading


