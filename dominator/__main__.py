# import all the functions
# these functions will perform different web app enumeration techniques

import sys
import requests
from .funcmodule import dom_vulnerability_check
from .funcmodule import search_all_vulnerabilites
from .funcmodule import display_options
from bs4 import BeautifulSoup

# we will do the crawling here in the main file 
# then send the data off to our functions for analysis

def main():
    
    args = sys.argv[1:]
    #print('count of args :: {}'.format(len(args)))
    
    for arg in args:
        #print('passed argument :: {}'.format(arg))

        if arg == '-dvul' and args[args.index(arg)+1]:
            url = args[args.index(arg)+1]

            page = requests.get(url)
            # Create a BeautifulSoup object
            soup = BeautifulSoup(page.text, 'html.parser')
            buttons = soup.find_all('button')
            inputs = soup.find_all('input')

            dom_vulnerability_check(url,buttons,inputs) #pass in the data to evaluate

        elif arg == '-a' and args[args.index(arg)+1]: 
            url = args[args.index(arg)+1]

            page = requests.get(url)
            # Create a BeautifulSoup object
            soup = BeautifulSoup(page.text, 'html.parser')

            search_all_vulnerabilites(url) #pass in the URL 
            
        elif arg == '-h':
            display_options()
    print('\ntype dominator -h for OPTIONS')

if __name__ == '__main__':
    main()