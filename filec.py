import re
fname = input("Enter file name: ")
f1name = input("Enter file name: ")
with open(fname, "r") as f:
	with open(f1name, "w") as f1:
		for line in f:
			word=re.split('[ :;.,/"?]',str(line))
			for i in word:
				f1.write(str(i) + "\n")	
			##f1.write(str(word) + "\n\n\n")