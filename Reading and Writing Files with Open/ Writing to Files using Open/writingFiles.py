# Basic File Writing with write()
# Using open() function with the 'w'(write) mode
# if the file alread exists, it will be overwritten. if it doesn't exist, it will be created

with open('ExampleWrite.txt','w') as file1:
    file1.write('This is line A\n')
    file1.write('This is line B\n')

print('================================================')
# Writing a List of Lines to a File

lines = ['line 1\n','line 2\n','line 3\n']

with open('Example2.txt','w') as file2:
    for line in lines:
        file2.write(line)
    
print('================================================')
# Appending to a File 
# add text to an existing file without deleting it current content, using the 'a'(append) mode

with open('Example2.txt','a') as file2:
    file2.write('line 4\n')

print('================================================')
# Copying Contents from One File to Another

with open('Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
        for line in readfile:
            writefile.write(line)