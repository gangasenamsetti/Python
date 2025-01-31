# *For reading file ,the file must be saved
# *For writing file,the file automatically creates a new file
# *Write() will truncates or override the existing file
# *append will append the data to the file
# *read and write mode is represented as r+
# * read only in binary is represented as rb similar as write only and append b
# *in w+ mode, the old content of the file gets erased



# *The with statement is a replacement for commonly used try/finally error-handling statements
# *The with statement automatically closes the file after you’ve completed writing it.

#Read file
f=open("users.txt",'r')
res=f.read()
res=f.readline() #prints only first line

res=f.readlines(1)   #prints how many lines we have to print
res=f.readline(4) # returns number of charcters
print(res)


#write file
f=open("users.txt",'w')
l=["delhi \n","Mumbai \n","London \n"]
f.write("Python programming \n")
f.write("ganga \n")
f.write("good morng \n")
f.writelines(l)
f.close()
f=open("users.txt",'r')
res=f.read()
print(res)


#Taking input from user
f=open("users.txt",'w')
for i in range(3):
    s=input("enter string")
    f.write(s)
f.close()
f=open("users.txt",'r')
res=f.read()
print(res)



#APPENDING DATA
f=open("users.txt",'a')
f.write("python programming \n")
f.write("java")
f.close()




f=open("users.txt",'a')
for i in range(3):
    s=input("enter string \n")
    f.write(s)
f.close()
f=open("users.txt",'r')
res=f.read()
print(res)



#                                        WITH STATEMENT

# *The with statement is a replacement for commonly used try/finally error-handling statements
# *The with statement automatically closes the file after you’ve completed writing it.

with open("users.txt",'a') as file:
    file.write("appending something \n")

#USING TRY FINALLY BLOCKS INPLACE OF WITH
f=open("users.txt",'a')
try:
    f.write("Add \n")
finally:
    f.close()


                #SEEK() AND TELL() FUNCTIONS

with open("users.txt",'w+') as file:
    file.write("Python programming UST \n")
with open("users.txt",'r+') as file:
    print(file.read(6)) #reads first 5 characters
    file.seek(8)  #moves the cursor to specified pos and starts index with 0
    print(file.read(5)) #reads next 5 charcters
    print(file.tell()) #get current position of file cursor
    
    #file.seek(0) #moves the cursor to 0th position



with open("users.txt",'r+') as f:
    f.seek(0)
    f.write("python")
    f.write("java")
    print(f.read())
    


with open("users.txt",'w+') as f:

    print(f.read())
    f.write("java ust")
    print(f.read())














