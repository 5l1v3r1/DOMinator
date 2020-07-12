input_wordlist= open("inputs.txt")
button_wordlist= open("buttons.txt")

def search_all_vulnerabilites(url):
    print('searching for any known vulnerabilites')

def dom_vulnerability_check(url,buttons,inputs):
    # analyze the script files store them in the var and print them out
    vulns = []

    for tag in buttons:
        #print(tag)
        tagstring = str(tag)

        for line in button_wordlist:
            print(tag)
            print(line)  
            if line.rstrip() in tagstring:
                vulns.append(line.rstrip()) #add the vulnerability to the list
    
    
    for tag in inputs:
        #print(tag)
        tagstring = str(tag)

        for line in input_wordlist:
            print(tag)
            print(line)
            if line.rstrip() in tagstring:
                 vulns.append(line.rstrip()) #add the vulnerability to the list
        
    print('vulns',vulns)

    script = 'webScript.js'
    line = 'line 32'
    

    for vuln in vulns:
        print('Vulnerability Found : ',vuln)
        print("Details -> : '%(url)s    %(script)s   %(line)s'" % {"url": url,"script":script,"line":line} )

def default_function():
    print("----- type -h for options -------")

def display_options():
    print('dominator -a url      find all vulnerabilities')
    print('dominator -dvul url   find DOM vulnerabilites')

