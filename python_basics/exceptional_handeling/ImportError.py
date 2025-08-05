# 🧠 Exception: ImportError

# ✅ Definition:
# ImportError occurs when the Python interpreter is unable to find or load a module or package that is being imported.

# ✅ When it arises:
# - Trying to import a module that does not exist
# - Typo in module or package name
# - Circular imports causing load failure
# - Module not installed in the environment

# ✅ Common causes:
# - Misspelled module name
# - Missing installation of third-party packages
# - Incorrect Python environment or path issues
# - Conflicts between module names and filenames

# -------------------------------------------------------

try:
   print # import non_existent_module   This will raise ImportError 
except ImportError:
    print("❌ Error: Module could not be imported. Check module name and installation.")
else:
    print("✅ Module imported successfully.")
finally:
    print("🔁 Import operation complete.\n")

# To avoid ImportError:
# - Make sure the module/package is installed (pip install ...)
# - Check spelling of the module name
# - Avoid circular imports in your code
