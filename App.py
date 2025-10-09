from functools import reduce

# Exercice 1: Dictionary Operations
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 88
}

print("=== Exercice 1: Dictionary Operations ===")
print("1.", students.get("Charlie"))
print("2.", students.get("Eve", 0))
students.pop("Bob")
print("3. Après suppression de Bob:", students)
print("4.", list(students.keys()))
print("5.", list(students.values()))
print("6.", list(students.items()))

# Exercice 2: List Manipulation
languages = ["Python", "JavaScript", "SQL"]

print("\n=== Exercice 2: List Manipulation ===")
languages.append("Java")
languages.extend(["HTML", "CSS"])
languages.sort()
print("1-3.", languages)
print("4. Index de SQL:", languages.index("SQL"))
print("5. C++ in list?", "C++" in languages)
languages.remove("JavaScript")
print("6. Après suppression de JavaScript:", languages)

# Exercice 3: Set Operations
skills_candidate1 = {"Python", "SQL", "Git", "Docker"}
skills_candidate2 = {"Python", "HTML", "CSS", "Git"}

print("\n=== Exercice 3: Set Operations ===")
skills_candidate1.add("JavaScript")
print("1.", skills_candidate1)
print("2. Union:", skills_candidate1 | skills_candidate2)
print("3. Intersection:", skills_candidate1 & skills_candidate2)
print("4. Différence:", skills_candidate1 - skills_candidate2)
skills_candidate1.discard("Docker")
print("5. Après discard Docker:", skills_candidate1)

# Exercice 4: Functional Programming Tools
prices = [100, 250, 75, 300]
discounts = [0.1, 0.2, 0.05, 0.15]

print("\n=== Exercice 4: Functional Programming Tools ===")
discounted_prices = list(map(lambda p_d: p_d[0] * (1 - p_d[1]), zip(prices, discounts)))
print("1. Prix après réduction:", discounted_prices)
filtered = list(filter(lambda x: x > 200, discounted_prices))
print("2. Prix > 200:", filtered)
total_cost = reduce(lambda x, y: x + y, discounted_prices)
print("3. Total coût réduit:", total_cost)
paired = list(zip(prices, discounts))
print("4. Appariés (price, discount):", paired)
labeled = list(enumerate(prices))
print("5. Étiquetés:", labeled)

# Exercice 5: Stack Simulation
undo_stack = []

print("\n=== Exercice 5: Stack Simulation ===")
undo_stack.append("Type 'Hello'")
undo_stack.append("Bold")
undo_stack.append("Delete 'o'")
undo_stack.append("Undo Bold")
print("1. Stack:", undo_stack)
undo_stack.pop()
print("2. Après pop:", undo_stack)
print("3. Top action:", undo_stack[-1] if undo_stack else "Empty")
print("4. État final:", undo_stack)
