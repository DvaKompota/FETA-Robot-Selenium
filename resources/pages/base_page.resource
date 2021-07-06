*** Settings ***
Library           SeleniumLibrary  run_on_failure=Nothing


*** Variables ***
${browser}      Chrome
${headless}     add_argument('--headless')
${maximized}    add_argument("--start-maximized")
${size}         add_argument('--window-size=1920,1280')
${timeout}      20 seconds


*** Keywords ***
Set Browser Options
#    set global variable    ${options}   None
    set global variable    ${options}   ${headless}
#    set global variable    ${options}   ${maximized}
#    set global variable    ${options}   ${size}
#    set global variable    ${options}   ${headless}; ${maximized}
#    set global variable    ${options}   ${headless}; ${size}
    [Return]        ${options}

Setup Browser
    ${options}      Set Browser Options
    open browser    browser=${browser}    options=${options}
    set selenium timeout  ${timeout}
