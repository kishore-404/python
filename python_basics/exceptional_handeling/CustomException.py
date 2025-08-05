# 🧠 Custom Exceptions in Python

# ✅ Why:
# Built-in exceptions may not always fit your domain-specific errors.
# Custom exceptions let you create meaningful, descriptive error types.

# ✅ How to create:
# 1. Define a new exception class inheriting from Exception or a subclass.
# 2. Raise it when needed using `raise`.

# -------------------------------------------------------

class UnderAgeError(Exception):
    """Exception raised when user is under the allowed age."""
    pass

def check_voting_eligibility(age):
    if age < 18:
        raise UnderAgeError("You must be at least 18 years old to vote.")
    else:
        print("✅ You are eligible to vote.")

# Handling the custom exception
try:
    user_age = int(input("Enter your age: "))
    check_voting_eligibility(user_age)
except UnderAgeError as e:
    print(f"❌ Custom Exception: {e}")
except ValueError:
    print("❌ Invalid input! Please enter a valid integer.")
finally:
    print("🔁 Check complete.\n")
