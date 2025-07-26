#Program to read a file line by line and handle errors gracefully
try:
    with open('sample.txt','r') as file1:
        reading_file1=file1.readline()
        reading_file2=file1.readline()
        print("Line 1:",reading_file1)
        print("Line 2:",reading_file2)

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
except Exception as e:
    print("An unexpected error occurred:",e)
