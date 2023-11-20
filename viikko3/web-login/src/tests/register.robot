*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page


*** Test Cases ***
Register With Valid Username And Password
    Set Username  esim
    Set Password  viisi123
    Set Password Confirmation  viisi123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  es
    Set Password  viisi123
    Set Password Confirmation  viisi123
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Invalid Password
    Set Username  esim
    Set Password  viisiisiisii
    Set Password Confirmation  viisiisiisii
    Submit Credentials
    Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  esim
    Set Password  kuusi666
    Set Password Confirmation  viisi555
    Submit Credentials
    Register Should Fail With Message  Password not matching

#Register With Nonmatching Password And Password Confirmation
# ...

*** Keywords ***

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}