
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

