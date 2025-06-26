colors = ["red", "green", "blue", "yellow", "red"]
print("first element",colors[0])
print("Last element",colors[-1])
colors[2]="cyan"
print("after changed the blue to  cyan ",colors)
colors.append("orange")
colors.insert(2,"pink")
print("appended orange and pink inserted at index 2",colors)
colors.remove("red")
last_color = colors.pop()
del colors[1]
print("removed color is ",last_color, "deleted 2nd element is ",colors)
print(len(colors))
print("green" in colors)
for i in colors:
    print(i)

print(colors[1:3])
colors.sort()
print(colors)
colors_sorted = sorted(colors)
print(colors_sorted)
colors.reverse()
print(colors)
new_var = colors.copy()
print(new_var)
print(colors)
colors.clear()
print(colors)