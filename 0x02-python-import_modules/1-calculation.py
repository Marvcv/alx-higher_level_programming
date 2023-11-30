# Check if this module is being run as the main module
if __name__ == "__main__":
    # Import the add function from add_0 module
    from add_0 import add

    # Define two numbers to add
    a = 1
    b = 2

    # Perform addition and display the result
    print("{} + {} = {}".format(a, b, add(a, b)))
