*** Settings ***
Library           SeleniumLibrary    20

*** Variables ***
${FIREFOX_BROWSER}     Firefox
${CHROME_BROWSER}      Chrome
${DESKTOP_HEIGHT}      1280
${DESKTOP_WIDTH}       1024
${MOBILE_HEIGHT}       640
${MOBILE_WIDTH}        360

${HOMEPAGE_URL}     http://web:5000

*** Keywords ***
# ------------------------------------------ ACTIONS --------------------------------------------

Open Default Browser Window
    [Arguments]
    ...    ${relative_url}

   Open Browser Window
   ...     ${relative_url}
   ...     ${CHROME_BROWSER}
   ...     ${DESKTOP_HEIGHT}
   ...     ${DESKTOP_WIDTH}

Open Browser Window
    [Arguments]
    ...    ${relative_url}
    ...    ${br}
    ...    ${height}
    ...    ${width}

    ${link}=    Catenate    SEPARATOR=/    ${HOMEPAGE_URL}    ${relative_url}
   #  Open Browser    ${link}    ${br}
   #  Set Window Size     ${height}   ${width}