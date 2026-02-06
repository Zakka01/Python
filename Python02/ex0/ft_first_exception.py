def check_temperature(temp_str: str):
    print(f"Testing temperature: {temp_str}")
    try:
        x = int(temp_str)
        if 0 <= x <= 40:
            print(f"Temperature {x}°C is perfect for plants!\n")
        elif x < 0:
            print(f"Error: {x}°C is too cold for plants (min 0°C)\n")
        elif x > 40:
            print(f"Error: {x}°C is too cold for plants (max 40°C)\n")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        
def test_temperature_input():
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("All tests completed - program didn't crash!")
    
if __name__ == "__main__":
    test_temperature_input()