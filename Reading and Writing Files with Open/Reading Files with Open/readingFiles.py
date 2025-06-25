# read(): This method reads the entire file as a string

with open('example.txt','r') as file:
    file_stuff1=file.read()
    print(file_stuff1)


print('================================================')
# readline(): This method reads one line at a time from the file. Each call to readline() reads the next line

with open('example.txt','r') as file:
    first_line=file.readline()
    print(first_line)

    second_line=file.readline()
    print(second_line)

print('================================================')
# readlines(): This method reads all lines and returns them as a list, where each line is an element in the list

with open('example.txt','r') as file:
    lines=file.readlines()
    print(lines)

print('================================================')
# Reading a Specific Number of Characters

with open('example.txt','r') as file:
    content=file.read(10)
    print(content) # Output the first 10 characters

print('================================================')
# Using Loops to Read Lines

with open('example.txt','r') as file:
    for line in file:
        print(line.strip())  # strip() removes the newline character