#!/usr/bin/python3

import os

Alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m', \
            'n','o','p','q','r','s','t','u','v','w','x','y','z')

main_menu = []
main_menu.append('Pick the cipher type you wish to use:\n')
main_menu.append('1. Rotation')
main_menu.append('2. Substitution')
main_menu.append('Q. Exit Program')

def print_menu(menu_list):
    try:
        os.system('cls')
    except:
        os.system('clear')

    for i in range(len(menu_list)):
        print(menu_list[i])
    print('\n')

def Rotation_Encrypt(plain_text, shift):
    return

def Rotation_Decrypt(cipher_text, shift):
    return

def Substitution_Encrypt():
    return

def Substitution_Decrypt():
    return

def Rotation():
    rot_menu=[]
    rot_menu.append('Rotation Cipher\n')
    rot_menu.append('E/ncrypt')
    rot_menu.append('D/ncrypt')
    print_menu(rot_menu)

def Substitution():
    return

print_menu(main_menu)
selection = input('Enter Selection: ')

# Sanitize selection
# ENTER VALIDATION CODE HERE

selection = int(selection)
# If selection is valid proceed with processing cipher type selected
if selection == 1:
    Rotation()
elif selection == 2:
    Rotation()





