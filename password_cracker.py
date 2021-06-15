import hashlib
import codecs
import os
from urllib.request import urlopen

global guesspasswordlist
guesspasswordlist = []

global skip
skip = 0

global guesspasswordlist_path
guesspasswordlist_path = ''

global actual_password_hash
actual_password_hash = ''

def readwordlist(url):
    try:
        wordlistfile = urlopen(url).read()
    except Exception as error:
        print("\nThere was an error while reading the wordlist ->", error)
        exit()
    return wordlistfile
 
def hash(wordlistpassword):
	
    result = hashlib.sha1(wordlistpassword.encode())
    return result.hexdigest()
 
def bruteforce(guesspasswordlist, actual_password_hash):
    for guess_password in guesspasswordlist:
        if hash(guess_password) == actual_password_hash:
            print("\nYour password is:", guess_password)
            # If the password is found then it will terminate the script here
            exit()

def local():
	global skip
	global actual_password_hash
	global guesspasswordlist_path

	guesspasswordlist = []
	if skip == 0:
		actual_password_hash = input("\nEnter hash\n\n>> ")
		guesspasswordlist_path = input("\nEnter wordlist path\nPlease give the Full Path, unless the wordlist is in the same folder as this script\n\n>> ")
	enc = int(input("\nIs the encoding\n1) Ascii.\n2) UTF-8.\n3) Check\n\n>> "))

	if enc == 1:
		encodee = 'ascii'
	elif enc == 2:
		encodee = 'utf-8'
	elif enc ==3:
		skip = 1
		os.system(f'file {guesspasswordlist_path}')
		input()
		local()

	try:
	    guesspasswordlistfile = codecs.open(guesspasswordlist_path, mode='r', encoding=encodee, errors='ignore', buffering=-1)
	except Exception as error:
	    print("T\nThere was an error while reading the wordlist ->", error)
	    exit()

	print("\nProcessing Wordlist.\nTime taken will depend upon the length of the wordlist.\n ")

	for linee in guesspasswordlistfile:
		word = linee
		guesspasswordlist.append(word[:-1]) 
		# text_guesspasswordlist = convertTuple(guesspasswordlist)
	guesspasswordlistfile.close()

	print('\nBruteforcing now\n')
	bruteforce(guesspasswordlist, actual_password_hash)

def online():
	url = input("\nEnter url.\nIt should end in .txt\n\n>> ")
	actual_password_hash = input("\nEnter password hash\n\n>> ")
	print("\nProcessing Wordlist.\nTime taken will depend upon the length of the wordlist and your internet connection\n ")
	wordlist = readwordlist(url).decode('UTF-8')
	guesspasswordlist = wordlist.split('\n')

	print('\nBruteforcing now\n')
	bruteforce(guesspasswordlist, actual_password_hash)

check_online = int(input("""\nIs your wordlist TEXT file

1) Locally saved
2) Online (url ending in .txt)

>> """))

if check_online == 1:
	local()
elif check_online == 2:
	online()

print("Failed to crack the password with the given wordlist. Try another list.")