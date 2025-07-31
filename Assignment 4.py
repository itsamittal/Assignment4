Module 5: Files, Exceptions, and Errors in Python

# coding: utf-8

# In[1]:


def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("File content:\n")
            for line in file:
                print(line, end='')  # end='' to avoid extra newlines
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function with 'sample.txt'
read_file('sample.txt')




def write_to_file(filename):
    user_input = input("Enter text to write to the file: ")
    with open(filename, 'w') as file:
        file.write(user_input + '\n')
    print("Data Successfully written to output.txt.")

def append_to_file(filename):
    more_input = input("Enter additional text to append.: ")
    with open(filename, 'a') as file:
        file.write(more_input + '\n')
    print("Additional data appended to file.")

def read_file(filename):
    print("\nFinal content of output.txt.:")
    with open(filename, 'r') as file:
        for line in file:
            print(line, end='')

# File name
filename = 'output.txt'

# Perform operations
write_to_file(filename)
append_to_file(filename)
read_file(filename)
