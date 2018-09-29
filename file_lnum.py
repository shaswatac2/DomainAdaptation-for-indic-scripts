fname = input("Enter file name: ")
 
num_words = 0
 
with open(fname, 'r') as f:
    for num,line in enumerate(f,1):
        words = line.split()
        num_words += len(words)
        if num_words==30000:
        	print(num)
