
def search_all_vulnerabilites(url):
    print('searching for any known vulnerabilites')

def dom_vulnerability_check(url):
    # analyze the script files store them in the var and print them out
    script = 'webScript.js'
    line = 'line 32'
    print("Results -> : '%(url)s    %(script)s  %(line)s'" % {"url": url,"script":script,"line":line} )

def default_function():
    print("----- type -h for options -------")

