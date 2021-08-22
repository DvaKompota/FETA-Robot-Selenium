*** Settings ***
Library     SeleniumLibrary         run_on_failure=Nothing


*** Variables ***
${page_url}                         https://demoqa.com/elements

${header}                           //header
${header_link}                      ${header}/a
${header_img}                       ${header_link}/img

${page_heading}                     //*[@class="main-header"]
${page_heading_text}                Elements
${page_subheading}                  //*[@class="col-12 mt-4 col-md-6"]
${page_subheading_text}             Please select an item from left to start practice.


*** Keywords ***
Open Elements Page
    go to                           ${page_url}
    wait until element is visible   ${header}

List happy elements
    @{happy_elements}   create list    ${header}    ${header_link}    ${header_img}    ${page_heading}
    ...     ${page_subheading}
    [Return]    @{happy_elements}

Validate happy elements
    @{happy_elements}    List happy elements
    FOR    ${element}   IN    @{happy_elements}
        element should be visible   ${element}
    END

Validate page heading
    element text should be          ${page_heading}         ${page_heading_text}
    element text should be          ${page_subheading}      ${page_subheading_text}
