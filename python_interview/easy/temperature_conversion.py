def celsius_to_fahrenheit(c):
    # Converts temperature from Celsius to Fahrenheit
    return (c * 9/5) + 32

print(celsius_to_fahrenheit(0))   # 32
print(celsius_to_fahrenheit(100)) # 212


def fahrenheit_to_celsius(f):
    # Converts temperature from Fahrenheit to Celsius
    return (f - 32) * 5 / 9

print(fahrenheit_to_celsius(32))    # 0 (Freezing point)
print(fahrenheit_to_celsius(212))   # 100 (Boiling point)
