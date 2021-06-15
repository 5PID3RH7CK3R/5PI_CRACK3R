#!/usr/bin/python3

#A barebones password cracker by 5PID3RH7CK3R

import subprocess
import codecs

hashing = ''
read_hash = ''
string_hash = ''
string_hash = ''
word = ''
wordlist = []

hashh  = input("Enter hash: ")
to_crack = hashh + '  -'

pswdl = input("Enter path to password list: ")

enc = input("Enter hash type: ")

pswdlist = codecs.open(pswdl, mode='rb', encoding=None, errors='ignore', buffering=-1)

for linee in pswdlist:
  wordlist.append(linee[:-1]) 
pswdlist.close()

for x in range(len(wordlist)):
	getword = wordlist[x]
	word = getword.decode('ascii')
	hashing = subprocess.Popen(f'python -c "import os;print(str(os.system(\'echo {(word)} ; echo {(word)} | {enc}\'))[:-1])"', shell=True, stdout=subprocess.PIPE)
	read_hash = hashing.stdout.read()
	string_hash = str(read_hash)
	show_hash = str(string_hash[len(word)+2:-5]).replace('\\n', '')

	if show_hash == to_crack:
		print('\n\nCracked!')
		print(f'Your password is : {word}')
		break
	else:
		print(f'\n{x+1}) {word}\n')
		print(show_hash)