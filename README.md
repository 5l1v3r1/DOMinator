#### Dominator Guide

### finding all vulnerabilities for a target domain
- dominator -targeturl

    #### looks for these OWASP vulnerabilities at the target url

    -Injection.
    -Broken Authentication.
    -Sensitive Data Exposure.
    -XML External Entities (XXE)
    -Broken Access control.
    -Security misconfigurations.
    -Cross Site Scripting (XSS)
    -Insecure Deserialization.

### finding DOM vulnerabilities for a specific URL
- dominator -dvul targeturl


### Current status and future developments
- dominator only works on html driven web pages, it will not work with front end frameworks (vue, react, angular etc...)
- the error handling currently relies on a wordlist not a DB
