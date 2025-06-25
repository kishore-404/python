# ------------------------------
# Explicit Type Conversion (Type Casting)
# ------------------------------
# Manual conversion using built-in functions like int(), float(), str(), list(), tuple(), set(), dict()

# 1. Numeric Conversions
str_num = "100"                 # string representing number
int_num = int(str_num)          # string to int
print("Explicit Conversion str -> int:", int_num, type(int_num))

float_num = 3.14159             # float
int_from_float = int(float_num) # float to int (truncates decimal)
print("Explicit Conversion float -> int:", int_from_float, type(int_from_float))

int_to_float = float(int_num)   # int to float
print("Explicit Conversion int -> float:", int_to_float, type(int_to_float))

# 2. String conversions
num = 42
str_from_int = str(num)         # int to string
print("Explicit Conversion int -> str:", str_from_int, type(str_from_int))

float_val = 9.81
str_from_float = str(float_val) # float to string
print("Explicit Conversion float -> str:", str_from_float, type(str_from_float))

# 3. Collections conversions

# list to tuple
lst = [1, 2, 3, 4]
tpl = tuple(lst)
print("Explicit Conversion list -> tuple:", tpl, type(tpl))

# tuple to list
tup = (5, 6, 7)
lst2 = list(tup)
print("Explicit Conversion tuple -> list:", lst2, type(lst2))

# list to set (removes duplicates)
lst_dup = [1, 2, 2, 3, 3, 4]
st = set(lst_dup)
print("Explicit Conversion list -> set:", st, type(st))

# set to list
lst_from_set = list(st)
print("Explicit Conversion set -> list:", lst_from_set, type(lst_from_set))

# dict keys to list
my_dict = {"a": 1, "b": 2, "c": 3}
keys_list = list(my_dict.keys())
print("Explicit Conversion dict keys -> list:", keys_list, type(keys_list))

# dict values to list
values_list = list(my_dict.values())
print("Explicit Conversion dict values -> list:", values_list, type(values_list))