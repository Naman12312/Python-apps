import sys

from colorama import Fore, Style
from mypy import api
result = api.run(["home"])
to_print = True
if result[0]:
    
    if "Success" not in result[0] and to_print:
        print()
        print(Fore.RED + Style.BRIGHT + result[0])  # stdout
        to_print = False
    elif to_print:
        print()
        print(Fore.GREEN + Style.BRIGHT + result[0])  # stdout
        to_print = False


    
        
elif result[1]:

    if "Success" not in result[1] and to_print:
        print()

        print(Fore.RED + Style.BRIGHT + result[1])  # stdout
        to_print = False
    elif to_print:
        print()

        print(Fore.GREEN + Style.BRIGHT + result[1])  # stdout
        to_print = False

to_print = True