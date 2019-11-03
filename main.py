from os import chdir
from subprocess import call
from hashing import hashing_main
from files import files_main
from emails import emails_main
from dirs import create_dirs
from updates import updates_main



choices = {
    1: 'Hashing Things',
    2: 'File/Directory Automation',
    3: 'Automate Updates.',
}


if __name__ == "__main__":
    
    for key, val in choices.items():

        print(key, val)

    print() # Blank line for readability

    u_choice = int(input('Enter a choice, based on the above values: '))

    if u_choice == 1:
        hashing_main()
        input('Mission accomplished. Press enter to exit.')
    elif u_choice == 2:
        files_main()
        input('Mission accomplished. Press enter to exit.')
    elif u_choice == 3:
        updates_main()
        input('Mission accomplished. Press enter to exit.')    
    else:
        raise Exception('Invalid value entered.')
