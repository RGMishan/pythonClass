file1 = open("myfile.txt","w") 
L = ["This is Mishan \n","This is John \n","This is Doe \n"] 

file1.write("Hello \n") 
file1.writelines(L) 
file1.close()

file1 = open("myfile.txt","r+") 

print("Output of Read function is ")
print(file1.read()) 

file1.seek(0) 

print("Output of Readline function is ")
print(file1.readline())
print()

file1.seek(0) 
print("Output of Read(9) function is ")
print(file1.read(9)) 
print()

file1.seek(0) 

print("Output of Readline(9) function is ")
print(file1.readline(9))

file1.seek(0)
print("Output of Readlines function is ")
print(file1.readlines()) 
print()
file1.close() 

def update_binary(word, new):
	string = b"" 
	Flag = 0 
	with open('file.txt', 'r+b') as file: 
		pos = 0
		data = string = file.read(1) 
		while data: 
			data = file.read(1) 

			if data == b" ": 
				if string == word: 
					file.seek(pos) 
					file.write(new) 
					Flag = 1
					break
				else: 
					pos = file.tell() 
					data = string = file.read(1) 
			else: 
				string += data 
				continue

	if Flag: 
		print("Record successfully updated") 
	else: 
		print("Record not found") 
		
word = input("Enter the word to be replaced: ").encode() 
new = input("\nEnter the new word: ").encode() 

update_binary(word, new) 
