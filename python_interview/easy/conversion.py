def convert_input(value):
    """
    This function takes an input value and determines its type:
    - If it's a single alphabet, convert to its ASCII (decimal) value.
    - If it's a decimal number:
        Convert to binary and hexadecimal.
    - If it's a binary (only 0s and 1s), convert to decimal and hex.
    - If it's a hex (like 0xFF or FF), convert to decimal and binary.
    """

    # If input is a single alphabet character
    if value.isalpha() and len(value) == 1:
        print(f"Character: {value}")
        print(f"ASCII (Decimal) value: {ord(value)}")  # ord() gives ASCII
        print(f"Binary: {bin(ord(value))[2:]}")        # bin() converts to binary
        print(f"Hexadecimal: {hex(ord(value))[2:].upper()}")  # hex() to hex
        return

    # If the input is a binary number (contains only 0s and 1s)
    if value.isdigit() and set(value).issubset({'0', '1'}):
        decimal = int(value, 2)  # Interpret value as base-2
        print(f"Binary input: {value}")
        print(f"Decimal: {decimal}")
        print(f"Hexadecimal: {hex(decimal)[2:].upper()}")
        return

    # If the input is a hexadecimal (starts with '0x' or all valid hex digits)
    hex_digits = set("0123456789abcdefABCDEF")
    if value.startswith("0x") or set(value).issubset(hex_digits):
        try:
            # Remove 0x if present
            clean_value = value[2:] if value.startswith("0x") else value
            decimal = int(clean_value, 16)
            print(f"Hexadecimal input: {value.upper()}")
            print(f"Decimal: {decimal}")
            print(f"Binary: {bin(decimal)[2:]}")
            return
        except ValueError:
            pass  # Not a valid hex

    # Else assume it's a decimal integer input
    try:
        num = int(value)
        print(f"Decimal input: {num}")
        print(f"Binary: {bin(num)[2:]}")
        print(f"Hexadecimal: {hex(num)[2:].upper()}")
        return
    except ValueError:
        print("Invalid input. Please enter a single alphabet, decimal, binary, or hexadecimal number.")

# 🔹 Example Usage:
# You can change this to accept input from the user using input()
test_inputs = ['a', 'Z', '65', '1010', '0x1F', 'FF']

for val in test_inputs:
    print(f"\n--- Converting: {val} ---")
    convert_input(val)
