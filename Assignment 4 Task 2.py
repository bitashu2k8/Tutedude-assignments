#program to input data, append and output the result
try:
    with open('output.txt','w') as file1:
        writing=input("Enter text to write to the file:")
        file1.write(writing+ '\n')
        print("Data successfully written to output.txt.")

    with open('output.txt','a') as file1:
        appending=input("\nEnter additional text to append:")
        file1.write(appending+ '\n')
        print("Data successfully appended.")

    with open('output.txt','r') as file1:
        print("\nFinal content of output.txt:")
        print(file1.read())

except FileNotFoundError:
    print("This file doesn't exits.")
except Exception as e:
    print("There was an unexpected error:",e)