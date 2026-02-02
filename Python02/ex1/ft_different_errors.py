def garden_operations():
    try:
        print("\nTesting ValueError...")
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
        
    try:
        print("\nTesting ZeroDivisionError...")
        10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
        
    try:
        print("\nTesting FileNotFoundError...")
        filename = "missing.txt"
        open(filename, "r")
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file '{filename}'")
    
    try:
        print("\nTesting KeyError...")
        garden = {
            "flower" : "white"
        }
        print(garden["Tree"])
    except KeyError as e:
        print(f"Caught KeyError: {e}")
        
        
def test_error_types():
    print("=== Garden Error Types Demo ===")
    garden_operations()
    
    print("\nTesting multiple errors together...")
    try:
        int("aa")
    except Exception:
        print("Caught an error, but program continues!")
        
    print("\nAll error types tested successfully!")
        
        
    
        

test_error_types()


        
    