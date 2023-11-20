*** Settings ***
Resource  resource.robot
Test Setup  Input Register Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kaksikymmenta  viisi555
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kaksikymmenta  kuusi666
    Input Register Command
    Input Credentials  kaksikymmenta  viisi555
    Output Should Contain  Username already taken

Register With Too Short Username And Valid Password
    Input Credentials  ka  viisi555
    Output Should Contain  Username too short

Register With Long Enough But Invalid Username And Valid Password
    Input Credentials  kaksikymmenta666  viisi555
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input Credentials  kaksikymmenta  v55
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kaksikymmenta  viisiviisi
    Output Should Contain  Password cannot contain only letters