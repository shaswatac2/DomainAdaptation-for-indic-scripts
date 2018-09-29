fname = input("Enter file name: ")
f1name = input("Enter file name: ")
with open(fname, "r") as f:
	with open(f1name, "w") as f1:
		for line in f:
			f1.write(line+"\n\n\n")