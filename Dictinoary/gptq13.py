from collections import Counter

# Step 1: Take input from the user
list1 = []
n = int(input("Enter the size of the list: "))
for i in range(n):
    number = input(f"Enter number {i+1}: ")
    list1.append(number)  # you can use int(number) if you want numeric keys

# Step 2: Count the frequency of each number
frequency = Counter(list1)  # Creates a dictionary-like object with counts

# Step 3: Filter out values that occur only once
filtered = {}
for key, value in frequency.items():
    if value > 1:
        filtered[key] = value

# Step 4: Display the final dictionary
print("\nFinal frequency dictionary (more than once):")
print(filtered)
