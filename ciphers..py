#!/usr/bin/env python3

# Import Statements
import os
import math
from collections import OrderedDict, deque
from operator import itemgetter

# Constants
MAIN_MENU = [
    'Rotation (Caesar Cipher)',
    'Substitution',
    'Permutation (Block)',
    'Quit Program'
]

ED_CRYPT_MENU = [
    'Encrypt Plaintext',
    'Decrypt Ciphertext'
]

INPUT_METHOD_MENU = [
    'Enter Text Through Keyboard',
    'Input Text From File'
]

OUTPUT_METHOD_MENU = [
    'Output Solution To Screen',
    'Output Solution To File'
]


ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

FRQ_TBL = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99,
           'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97,
           'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}

# Global Variables
ltr_frq = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0,
           'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

frq_tbl_by_val = OrderedDict(sorted(FRQ_TBL.items(), key=itemgetter(1), reverse=True))

def display_menu(menu,
                 title="",
                 title1="",
                 prompt="Please enter your selection: "):

    # Displays menu on the screen
    # Returns user selection from menu
    # Arguments:
    #   menu = menu line items as a list object
    #   title = menu title as a string
    #   title1 = menu subtitle as a string
    #   prompt = user selection prompt as a string

    # Clear the screen to display new menu
    os.system('clear')

    # Print the menu title
    if title != "":
        print(title + '\n')
    if title1 != "":
        print(title1 + '\n')

    # Print the menu items
    for i in range(len(menu)):
        print("{}.{}".format(i+1, ' ' + menu[i]))

    # Get user selection
    print('\n')
    choice = input(prompt)

    return choice


def rot_encrypt(plaintext, shift):

    # Encrypts a plaintext using the rotation cipher
    # Arguments:
    #   plaintext = the text to encrypt as a string
    #   shift = the rotation shift as an integer

    # Create our substitution dictionary
    # key = plaintext, value = ciphertext
    dic = {}
    for i in range(0, len(ALPHABET)):
        dic[ALPHABET[i]] = ALPHABET[(i + shift) % len(ALPHABET)]

    # Convert each letter of plaintext to the corresponding
    # substitution letter in our dictionary creating the ciphertext
    ciphertext = ""
    for l in plaintext.lower():
        if l in dic:
            l = dic[l]
        ciphertext += l

    return ciphertext


def rot_decrypt(ciphertext):

    # Decrypts a ciphertext using the rotation cipher.
    # Rotates through every potential shift
    # and prints each resulting decryption.
    # User must view the results to determine the valid decryption
    # Arguments:
    #   ciphertext = the text to decrypt as a string

    # Print title for the list of potential decryptions
    print('\n')
    print('SHIFT   POSSIBLE DECRYPTION')

    # Loop through all potential shifts and print a list of resulting decryptions
    for shift in range(1, 25):

        plaintext = ""  # Initialize plaintext for each shift

        # Create a substitution dictionary based upon current shift value
        # key = ciphertext, value = plaintext
        dic = {}
        for i in range(0, len(ALPHABET)):
            dic[ALPHABET[i]] = ALPHABET[(i - shift) % len(ALPHABET)]

        # Convert each letter of ciphertext to the corresponding
        # plaintext letter in our dictionary
        for l in ciphertext.lower():
            if l in dic:
                l = dic[l]
            if l != '\n':
                plaintext += l

        # Print decryption list line item
        # Prints shift value and the corresponding potential decryption
        print(' ' if shift < 10 else '', shift, '  ', plaintext)


def find_freq(ciphertext):

    # Reinitialize ltr_frq dictionary in case user is doing a second decryption
    for l in ltr_frq:
        ltr_frq[l] = 0

    # Determine letter frequency
    # Count the number of times a letter appears in ciphertext
    for l in ciphertext:
        if l.upper() in ltr_frq:
            ltr_frq[l.upper()] += 1

    # Display the frequency count
    # --- ACTION ITEM
    # ---   DELETE this or give user choice
    # ---   to display count
    print('LETTER FREQ SORTED BY FREQUENCY')
    ltr_frq_by_val=OrderedDict(sorted(ltr_frq.items(), key=itemgetter(1), reverse=True))
    for k, v in ltr_frq_by_val.items():
        print(k, v)


def englishFreqMatchScore(message):
    # Return the number of matches that the string in the message
    # parameter has when its letter frequency is compared to English
    # letter frequency. A "match" is how many of its six most frequent
    # and six least frequent letters is among the six most frequent and
    # six least frequent letters for English.
    freqOrder = getFrequencyOrder(message)

    matchScore = 0
    # Find how many matches for the six most common letters there are:
    for commonLetter in ETAOIN[:6]:
        if commonLetter in freqOrder[:6]:
            matchScore += 1
    # Find how many matches for the six least common letters there are:
    for uncommonLetter in ETAOIN[-6:]:
        if uncommonLetter in freqOrder[-6:]:
            matchScore += 1

    return matchScore


def build_sub_correlation():

    # Correlate the frequency of letters from cipher text (ltr_frq_by_val)
    # to frequency of letters as found in English language (frq_tbl_by_val)
    # frq_tbl_by_val = FRQ_TBL sorted by frequency
    # ltr_frq_by_val = Ciphertext sorted by frequency

    frqT_keylist = list(frq_tbl_by_val.keys())
    print('KEYLIST')
    for i in range(0, len(frqT_keylist)):
        print(frqT_keylist[i])

    frqA_keylist = list(OrderedDict(sorted(ltr_frq.items(), key=itemgetter(1), reverse=True)))
    sub_pairs = []
    for i in range(0, len(frqT_keylist)):
        sub_pairs.append([frqT_keylist[i], frqA_keylist[i]])

    print('FREQ TBL CORRELATION')
    for i in range(0, len(sub_pairs)):
        print(sub_pairs[i])

    tmp = input('Press <ENTER> to continue. ')
    return frqT_keylist, frqA_keylist


def sub_decrypt(ciphertext):

    # Decrypts a ciphertext using the substitution cipher.
    # Rotates through every potential shift
    # and prints each resulting decryption.
    # User must view the results to determine the valid decryption
    # Arguments:
    #   ciphertext = the text to decrypt as a string

    find_freq(ciphertext)
    frqT_keylist, frqA_keylist = build_sub_correlation()

    pre_dic = zip(frqT_keylist, frqA_keylist)
    print(pre_dic)

    subst_dic={}
    for frqT, frqA in pre_dic:
        subst_dic[frqT] = frqA

    print('SUBSTITUTION DICTIONARY')
    for k, v in subst_dic.items():
        print(k, v)

    tmp = input('Press <ENTER> to continue. ')

    for l in ciphertext:
        if l in subst_dic.items():
            print(subst_dic[l])


def validate_int(str_num, boundary=False, lo_bound=0, hi_bound=0):

    # Validates that input from a user which is supposed to be an
    # integer is, in fact, a valid integer.
    # Also, if necessary, verifies that the integer value falls within 
    # a valid range.
    # Arguments:
    #   str_num = the input string value which is supposed to represent an integer
    #   boundary = identifies if the integer needs to fall within a range as boolean
    #   lo_bound = if boundary=True, identifies the boundary's low value as integer
    #   hi_bound = if boundary=True, identifies the boundary's high value as integer

    if str_num.isnumeric() and math.fmod(float(str_num), 1) == 0:

        # str_num is an integer
        # see if it must fall within a range
        # if so, check its value against the range limits
        if boundary:
            num = int(str_num)
            if num >= lo_bound and num <= hi_bound:
                return True  # str_num is an integer and falls within required range
            else:
                return False  # str_num is an integer, but falls outside required range
        else:
            return True  # str_num is an integer - no range check required
    else:
        return False  # str_num is not an integer


def get_input_to_process(title=''):
    os.system('clear')
    action = display_menu(INPUT_METHOD_MENU,
                          title,
                          title1='ENTER TEXT INPUT METHOD')

    print('\n')
    if action == '1':  # Input text through keyboard
        txt = input('(Keyboard) Enter text to be processed: ')
    elif action == '2':  # Input text from file
        while True:
            path = input('(File) Enter filename: ')
            if os.path.exists(path):
                # Get input from specified file
                fh = open(path, 'r')
                txt = fh.read()
                fh.close()
                break
            else:
                tmp = input('File not found! \n\n'
                            'Be sure to enter absolute filepath\n'
                            'if file is not in current working directory.\n\n'
                            'Press <ENTER> to continue. ')
                os.system('clear')

    return txt



def get_output_location(title='', txt):
    os.system('clear')
    action = display_menu(OUTPUT_METHOD_MENU,
                          title,
                          title1='ENTER SOLUTION OUTPUT LOCATION')

    print('\n')
    if action == '1':  # Output to screen
        location = 'SCREEN'
    elif action == '2':  # Output to file
#        while True:

        path = input('(File) Enter filename: ')

        # Get input from specified file
        fh = open(path, 'w')
        fh.write(txt)
        fh.close()

 #           break

           # if os.path.exists(path):

                # Get input from specified file
            #    fh = open(path, 'w')
            #    fh.write(txt)
            #    fh.close()
             #   break

            #else:
             #   tmp = input('File not found! \n\n'
             #               'Be sure to enter absolute filepath\n'
             #               'if file is not in current working directory.\n\n'
             #               'Press <ENTER> to continue. ')
             #   os.system('clear')


def rot_cipher():
    action = display_menu(ED_CRYPT_MENU,
                          title='ROTATION CIPHER')

    if action == '1':  # Encrypt

        # Get shift value
        while True:
            os.system('clear')
            print('ROTATION CIPHER ENCRYPTION \n')
            shift = input('Enter shift # (1-25) for encryption: ')
            if validate_int(shift, True, 1, 25):
                shift = int(shift)
                break
            else:
                tmp = input('Invalid shift value. Press any key to continue. ')

        # Get plaintext to encrypt
        txt = get_input_to_process('ROTATION CIPHER ENCRYPTION')
        encryption = rot_encrypt(txt, shift)

        os.system('clear')
        print(encryption)
        tmp = input('Press <ENTER> to continue. ')

    elif action == '2':  # Decrypt

        # Get ciphertext to decrypt
        txt = get_input_to_process('ROTATION CIPHER DECRYPTION')
        rot_decrypt(txt)


        tmp = input('Press <ENTER> to continue. ')


def sub_cipher():
    action = display_menu(ED_CRYPT_MENU,
                          title='SUBSTITUTION CIPHER')

    if action == '1':  # Encrypt



        # Get substitution key
        while True:

            tmp = input('Encryption algorithm not completed. Press <ENTER> to continue. ')
            break

            # Do NOT process following code
            os.system('clear')
            print('SUBSTITUTION CIPHER ENCRYPTION \n')
            shift = input('Enter substitution key for encryption: ')
            if validate_int(shift, True, 1, 25):
                shift = int(shift)
                break
            else:
                tmp = input('Invalid shift value. Press any key to continue. ')

            # Get plaintext to encrypt
            txt = get_input_to_process('SUBSTITUTION CIPHER ENCRYPTION')
            encryption = rot_encrypt(txt, shift)

            os.system('clear')
            print(encryption)
            tmp = input('Press <ENTER> to continue. ')

    elif action == '2':  # Decrypt

        # Get ciphertext to decrypt
        txt = get_input_to_process('SUBSTITUTION CIPHER DECRYPTION')
        sub_decrypt(txt)


        tmp = input('Press <ENTER> to continue. ')


def perm_encrypt(blocks, key):

    # Get number of blocks
    x = len(blocks)

    encrypted_blocks=[]
    for blocknum in range(0, x):
        encrypted_blocks.append('')
        for k in key:
            encrypted_blocks[blocknum] += blocks[blocknum][k-1]

    # Format for output
    
    block_length = len(key)
    blocks_per_line = int(80/block_length)
    for i in range(0, x):
        for b in range(0, blocks_per_line-1):
           txt = encrypted_blocks[i] + ' '
        txt += '\n'
 
    return txt

def perm_decrypt(blocks, key):

    # Get number of blocks
    # Get length of key
    x = len(blocks)
    key_len = len(key)

    decrypted_blocks=[]
    for blocknum in range(0, x):
        ltr_list = list('0'*key_len)
        i = 0
        for k in key:
            ltr_list[k-1] = blocks[blocknum][i]
            i +=1

        decrypted_blocks.append(''.join(map(str, ltr_list)))

    return decrypted_blocks



def perm_cipher():
    action = display_menu(ED_CRYPT_MENU,
                          title='PERMUTATION CIPHER')

    if action == '1':  # Encrypt

        # Get key value
        os.system('clear')
        print('PERMUTATION CIPHER ENCRYPTION \n')
        key = input('Enter key for encryption: ')

        perm = build_perm_key(key)

        # Get plaintext to encrypt
        txt = get_input_to_process('PERMUTATION CIPHER ENCRYPTION')

        txt_blocks = build_blocks(txt, len(perm))

        encryption = perm_encrypt(txt_blocks, perm)

        os.system('clear')
        print(encryption)
        tmp = input('Press <ENTER> to continue. ')

    elif action == '2':  # Decrypt



        # Get ciphertext to decrypt
        txt = get_input_to_process('PERMUTATION CIPHER DECRYPTION')
        key = input('Enter key for decryption: ')

        perm = build_perm_key(key)


        txt_blocks = build_blocks(txt, len(perm))

        perm_decrypt(txt_blocks, perm)


def remove_spaces(txt):
    new_ptxt = ''
    for i in range(0,len(txt)):
        if txt[i] != ' ':
            new_ptxt += txt[i]

    return new_ptxt



def build_blocks(ptxt, block_len):

    # Remove spaces from the plaintext
    # If ptxt does not evenly divide into blocks
    # ensure an extra block with padding is processed
    ptxt = remove_spaces(ptxt)
    orig_i = len(ptxt)/block_len

    if math.fmod(float(orig_i), 1) != 0:
        i = int(orig_i)+1
    else:
        i = int(orig_i)


    block_list = []
    start = 0
    end = block_len
    for x in range(0, i):
        block_list.append(ptxt[start:end])
        start += block_len
        end += block_len

    # Add padding to last block if needed
    if i != orig_i:
        blocks = len(block_list) -1
        x = block_len - len(block_list[blocks])
        for i in range(0, x):
            if i % 2 == 0:
                pad = 'o'
            else:
                pad = 'x'
            block_list[blocks] += pad

    return block_list


def build_perm_key(key):
    # Get key length and sort it
    blocksize = len(key)
    keysorted = sorted(key.lower())

    # Create key mapping
    # Use a dictionary of stacks
    key_map = {}
    for l in range(0, blocksize):
        if keysorted[l] in ALPHABET:
            stack=[]
            if keysorted[l] in key_map:
                stack = key_map[keysorted[l]]
                stack.append(l)
                key_map[keysorted[l]] = stack
            else:
                stack.append(l)
                key_map[keysorted[l]] = stack

    print('key map', key_map)

    # Map back to original key
    perm_list = []
    for i in range(0, blocksize):
        if key[i] in ALPHABET:
            perm_list.append(key_map[key[i]].pop(0))

    return perm_list



if __name__ == '__main__':
    while True:
        user_choice = display_menu(MAIN_MENU,
                                   title="CIPHER ENCRYPTION/DECRYPTION")
        if user_choice == '4':  # Quit Program
            os.system('clear')
            break
        elif user_choice == '1':  # Rotation Cipher
            rot_cipher()
        elif user_choice == '2':  # Substitution Cipher
            sub_cipher()
        elif user_choice == '3':  # Permutatution Cipher
            perm_cipher()

    #Example useage
    #ciphertext = 'wkh fdw vdw rq wkh pdw'
    #rot_decrypt(ciphertext)
    #plaintext= "the cat sat on the mat"
    #print("Plaintext:", plaintext)
    #print("Cipertext:", rot_encrypt(plaintext, 3))
    #This will result in:
    #Plaintext: the cat sat on the mat
    #Cipertext: wkh fdw vdw rq wkh pdw