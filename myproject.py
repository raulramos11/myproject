#Crie um programa para demoonstrar loops e demais estruturas de controle em Python.
def demonstrate_loops_and_control_structures():
    # Loop for
    print("Loop for:")
    for i in range(5):
        print(f"Iteration {i}")

    # Loop while
    print("\nLoop while:")
    count = 0
    while count < 5:
        print(f"Count is {count}")
        count += 1

    # If-elif-else structure
    print("\nIf-elif-else structure:")
    number = 3
    if number < 0:
        print("The number is negative.")
    elif number == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")

    # Try-except structure
    print("\nTry-except structure:")
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Caught a division by zero error!")
    finally:
        print("Execution completed.")
    # Function definition and call
    print("\nFunction definition and call:")
    def greet(name):
        return f"Hello, {name}!"
    print(greet("World"))
    # List comprehension
    print("\nList comprehension:")
    squares = [x**2 for x in range(5)]
    print(f"Squares: {squares}")
    # Dictionary iteration
    print("\nDictionary iteration:")
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    for key, value in sample_dict.items():
        print(f"Key: {key}, Value: {value}")
    # Exception handling with multiple exceptions
    print("\nException handling with multiple exceptions:")
    try:
        value = int("not_a_number")
    except ValueError:
        print("Caught a ValueError!")
    except TypeError:
        print("Caught a TypeError!")
    finally:
        print("Finished exception handling.")
    # Using break and continue in loops
    print("\nUsing break and continue in loops:")
    for i in range(10):
        if i == 5:
            print("Breaking the loop at i = 5")
            break
        if i % 2 == 0:
            print(f"Continuing at even number i = {i}")
            continue
        print(f"Current number is {i}")
if __name__ == "__main__":
    demonstrate_loops_and_control_structures()
    