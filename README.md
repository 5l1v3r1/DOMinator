#Dominator Guide

### finding all vulnerabilities for a target domain
- dominator -targeturl

looks for the top 10 OWASP vulnerabilities at the target url

    -Injection.
    -Broken Authentication.
    -Sensitive Data Exposure.
    -XML External Entities (XXE)
    -Broken Access control.
    -Security misconfigurations.
    -Cross Site Scripting (XSS)
    -Insecure Deserialization.

### finding DOM vulnerabilities for a specific URL
- dominator -targeturl -dvul

### finding XSS vulnerabilities for a specific URL
- dominator -targeturl -xssvul
"# DOMinator" 
