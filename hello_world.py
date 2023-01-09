def print_hello_name(name: str):
    '''
        A basic Method to print User Input Name
    '''

    print(f"Hello {name}")


if (__name__ == "__main__"):
    input_name = input("Enter the Name: ")
    print_hello_name(input_name)
