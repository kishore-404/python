# Python Looping Statements
# Loops allow repeating a block of code multiple times until a condition is met.
# Python doesn’t have a built-in do-while loop !!!
# ~ Initialization: Set up a loop control variable (e.g., i = 0).

# ~ Condition Check: Before each iteration, check if the loop condition is true.

# ~ Execution: If the condition is true, execute the loop body (the code inside the loop).

# ~ Update: Modify the loop control variable (e.g., increment i).

# ~ Repeat: Go back to step 2 until the condition becomes false.

# ~ Stop: Exit the loop when the condition is false.

# 1. for loop
# Iterates over a sequence (like list, tuple, string) and executes the block for each item.

fruits = ["apple", "banana", "cherry"]
print("For loop example:")
for fruit in fruits:
    print(fruit)  # Prints each fruit in the list

print("-----")

# 2. while loop (Entry control loop )
# Repeats the block as long as the condition is True.

count = 3  #initialize
print("While loop example:")
while (count > 0):
    print("Counting down:", count)
    count -= 1  # Decrease count by 1 each iteration

print("-----")

# 3. Nested loops
# One loop inside another loop, useful for multi-dimensional data.

print("Nested loop example:")
for i in range(1, 4):        # Outer loop: 1 to 3
    for j in range(1, 3):    # Inner loop: 1 to 2
        print(f"i={i}, j={j}")

print("-----")

# 4. Loop control: break
# Immediately exits the loop when a condition is met.

print("Break example:")
for num in range(1, 6):
    if num == 4:
        print("Breaking at", num)
        break                # Exit the loop here
    print(num)

print("-----")

# 5. Loop control: continue
# Skips the rest of the current loop iteration and continues with the next iteration.

print("Continue example:")
for num in range(1, 6):
    if num == 3:
        print("Skipping", num)
        continue             # Skip printing 3
    print(num)

print("-----")

# 6. else with loops
# The else block executes after the loop finishes normally (no break).

print("Else with loop example:")
for i in range(3):
    print(i)
else:
    print("Loop completed without break")

print("-----")

# 7. Using else with break
print("Else skipped due to break:")
for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("This will not print because loop was broken")

# Summary of Python loop types:
# - for: iterate over sequences
# - while: loop while condition is True
# - nested loops: loops inside loops
# - break: exit loop early
# - continue: skip current iteration
# - else: execute code if loop was not broken
