*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Todos

*** Test Cases ***
After adding a book, there is one
    Go To  ${HOME_URL}
    Click Link  Lisää uusi kirja
    Input Text  author  Erkki Esimerkki
    Input Text  title  Otsikko
    Input Text  publisher  Julkaisia
    Input Text  year  2024
    Click Button  Submit
    Page Should Contain  Erkki Esimerkki Otsikko Julkaisia 2024