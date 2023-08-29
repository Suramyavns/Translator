import translators as ts
from colorama import Fore,Style
def translation(source,lines,dest):
    try:
        print(Fore.GREEN + Style.BRIGHT + "[+]Resulting translation: ")
        for i in lines:
            print(Fore.GREEN + f"\t{ts.translate_text(i,to_language=dest,from_language=source)}")
    except:
        print(Fore.RED + Style.BRIGHT + "[!] Language code unsupported")
        main()

def main():
    source = input(Fore.CYAN + Style.BRIGHT + "[*] Enter source language code (as per ISO 639-1): ")
    dest = input(Fore.CYAN + Style.BRIGHT + "[*] Enter destination language code (as per ISO 639-1): ")
    while True:
        path = input(Fore.CYAN + Style.BRIGHT + '[*] Enter file path: ')
        try:
            with open(f"{path}",'r') as fh:
                lines = fh.readlines()
        except:
            print(Fore.RED + Style.BRIGHT + "[!] Invalid file path")
        else:
            translation(source,lines,dest)
            exit()
description = "[$] This program will translate all text in the provided file into destination language.\n"
print(Fore.YELLOW + Style.BRIGHT + f"{description}")
main()

