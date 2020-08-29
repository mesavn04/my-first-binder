#Another method using full location
text_file2 = open(r"C:\Users\nhungtth\Desktop\Test_python.txt")
print(text_file2)
#get the list of line
line_list = text_file2.readlines();

#for each line from the list, print the line
for line in line_list:
    print(line)

text_file2.close() #don't forget to close the file
