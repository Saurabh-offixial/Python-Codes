#File Handling Write Program
a=open("ABC.txt","w")
a.write("Saurabh \n")
a.write("Diya \n")
a.write("Meet \n")
a.write("Fenil")

#File Handling Read Program
a=open("ABC.txt","r")
b=a.read()
print(b)

#File Handling Append Program
a=open("ABC.txt","a")
a.write("Hemin")
a.close()
