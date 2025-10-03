with open("my_file.txt","a") as file:
#statements
  writing_file = file.write("Hello ")
  print(writing_file)
file1= open("my_file.txt","r")
reading_file = file1.read()
print(reading_file)
file1.close()

file1= open("my_file.txt","a")
appending_file = file1.write(" welcome to this lecture")
print(appending_file)
file1.close() 