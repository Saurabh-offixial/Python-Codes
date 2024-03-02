a=open("ABC.txt","w")
a.write("Saurabh")
a.write(" Diya")
a.write(" Meet")
a.write(" Fenil")

a=open("ABC.txt","r")
b=a.read()
print(b)

a=open("ABC.txt","a")
a.write("Hemin")
a.close()
