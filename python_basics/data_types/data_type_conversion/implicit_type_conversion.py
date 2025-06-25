# ------------------------------
# Implicit Type Conversion (Type Coercion)
# ------------------------------
# Happens automatically when Python mixes types, mostly numeric (int, float, complex).
# Python converts smaller type to bigger type to avoid data loss.

# Constraints:
# - Implicit conversion only works for compatible numeric types.
# - It does NOT convert strings to numbers or between unrelated types.
# - Trying to mix incompatible types like int + str causes a TypeError.


a_int = 10              # int
b_float = 2.5          # float

# int implicitly converted to float for addition
result_implicit = a_int + b_float  
print("Implicit Conversion int + float:", result_implicit, type(result_implicit))