fname = input("Enter file name: ")
f1name = input("Enter file name: ")
content=open(fname, "r").readlines()

con_set=set(content)
nfile=open(f1name, "w")
for line in con_set:
	nfile.write(line)