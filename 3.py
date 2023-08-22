"""
Write a program to create "BCA.txt" file which contain information about BCA course. 
count and print the total number of lines starting with ‘A’, ‘B’, and ‘C’ in "intro.txt" file.
"""

f1="c:\\sqlite3\\bca.txt"
f2="c:\\sqlite3\\intro.txt"
data="""BCA course subjects include web technology, database management system,
        software engineering, operating systems, web technology, and computer languages
        like c, C++, JAVA, HTML.A BCA degree is considered to be at par with a BTech/BE
        degree in Computer Science or Information Technology."""
count=0;
with open(f1,"w")as textfile:
    data=textfile.write(data)
with open(f1,"r")as textfile:
    data=textfile.readlines()
with open(f2,"w") as txtfile:
    for i in data:
         if(i[0]=="a" or i[0]=="A" or i[0]=="b" or i[0]=="B" or i[0]=="c" or i[0]=="C"):
               count=count+1
print("total lines:",count)

