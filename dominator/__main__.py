# import all the functions
# these functions will perform different web app enumeration techniques

import sys
from .funcmodule import dom_vulnerability_check
from .funcmodule import search_all_vulnerabilites
from .funcmodule import default_function

def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))

        if arg == '-dvul' and args[args.index(arg)+1]:
            url = args[args.index(arg)+1]
            dom_vulnerability_check(url) #pass in the URL 

        elif arg == '-a' and args[args.index(arg)+1]: 
            url = args[args.index(arg)+1]
            search_all_vulnerabilites(url) #pass in the URL 
            
        else:
            default_function()

if __name__ == '__main__':
    main()