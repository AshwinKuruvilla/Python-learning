# ==========================================
# EXAMPLE 1: Basic List Operations & Slicing
# ==========================================
print("--- Start of Example 1: Basic List Operations & Slicing ---")

courses = ["History", "Math", "Physics", "CompSci"]

# Prints the full list of courses
print(courses)

# len() finds and prints the total number of items in the list
print(len(courses))

# Slices the list to print elements starting from index 2 to the end
print(courses[2:])


# ==========================================
# EXAMPLE 2: Modifying Lists (Add/Remove)
# ==========================================
print("\n--- Start of Example 2: Modifying Lists ---")

# .append() adds an item to the very end of the list
courses.append("Art")
print(courses)

# .insert() adds an item at a specific index (0 is the very beginning)
courses.insert(0, "Biology")
print(courses)

# .remove() searches for and deletes the first matching value
courses.remove("Math")
print(courses)

# .pop() removes and returns the last item from the list
popped = courses.pop()
print(popped)


# ==========================================
# EXAMPLE 3: List Utilities (Sorting & Searching)
# ==========================================
print("\n--- Start of Example 3: List Utilities ---")

# .reverse() flips the order of the list in place
courses.reverse()
print(courses)

# min() returns the item that comes first alphabetically (or lowest numerically)
print(min(courses))

# max() returns the item that comes last alphabetically (or highest numerically)
print(max(courses))

# .index() searches for an item and returns its position/index number
print(courses.index("CompSci"))


# ==========================================
# EXAMPLE 4: Looping and Enumeration
# ==========================================
print("\n--- Start of Example 4: Loops and Enumeration ---")

courses = ["History", "Math", "Physics", "CompSci"]
numbers = [1, 5, 2, 4, 3]

# Standard 'for' loop to iterate through every item in a list
for course in courses:
    print(course)

# enumerate() tracks both the current index and the item value as it loops
for index, trash in enumerate(numbers):
    print(f"{index}: {trash}")


# ==========================================
# EXAMPLE 5: Sorting Techniques
# ==========================================
print("\n--- Start of Example 5: Sorting Techniques ---")

# sorted() creates a brand new sorted list without modifying the original
sorted_numbers = sorted(numbers)
# Adding reverse=True sorts the new list in descending order
descending_numbers = sorted(numbers, reverse=True)

print("start of sorted numbers")
for index, number in enumerate(sorted_numbers):
    print(f"{index}: {number}")

print("start of descending numbers")
for index, number in enumerate(descending_numbers):
    print(f"{index}: {number}")

# Utilizing the 'start' argument in enumerate to begin counting from 101 instead of 0
print("start of courses")
for index, course in enumerate(courses, start=101):
    print(f"{index}: {course}")


# ==========================================
# EXAMPLE 6: Lists vs. Tuples (Mutability)
# ==========================================
print("\n--- Start of Example 6: Lists vs. Tuples (Mutability) ---")

# Lists are mutable (changeable). list_2 points to the exact same list as list_1
list_1 = ['football', 'basketball', 'tennis', 'baseball']
list_2 = list_1
print(list_1)
print(list_2)

# Changing list_1 also changes list_2 because they share the same memory location
list_1[0] = 'Art'
print(list_1)
print(list_2)

# Tuples use parentheses () and are immutable (cannot be changed after creation)
tuple_1 = ('football', 'basketball', 'tennis', 'baseball')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)
# tuple_1[0] = 'Art' <- This cannot be done and would crash the program if uncommented


# ==========================================
# EXAMPLE 7: Set Operations (Uniqueness)
# ==========================================
print("\n--- Start of Example 7: Set Operations ---")

# Sets use curly braces {}, ignore duplicates, and have no guaranteed order
cs_courses = {"OOP", "Data Structures", "Algorithms", "Databases", "Algorithms"}
print(cs_courses)
ecom_courses = {"E-commerce", "SEO", "Content Creation", "OOP"}
print(ecom_courses)

# .intersection() finds items shared by BOTH sets
print(cs_courses.intersection(ecom_courses))

# .union() combines ALL unique items from both sets
print(cs_courses.union(ecom_courses))

# .difference() returns items that are only in cs_courses but NOT in ecom_courses
print(cs_courses.difference(ecom_courses))


# ==========================================
# EXAMPLE 8: Initializing Empty Structures
# ==========================================
print("\n--- Start of Example 8: Empty Data Structures ---")

# Creates an empty list
empty_list = []

# Creates an empty tuple
empty_tuple = ()

# Creates an empty set (you must use set() because {} creates an empty dictionary)
empty_set = set()

print("Empty data structures initialized successfully.")