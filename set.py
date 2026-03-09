# Creating sets
subjects_A = {"Python", "Math", "Statistics"}
subjects_B = {"Statistics", "Machine Learning", "AI"}

print("Subjects A:", subjects_A)
print("Subjects B:", subjects_B)

# Adding subject
subjects_A.add("Data Science")
print("After Adding Subject:", subjects_A)

# Removing subject
subjects_A.remove("Math")
print("After Removing Subject:", subjects_A)

# Union
print("Union:", subjects_A.union(subjects_B))

# Intersection
print("Intersection:", subjects_A.intersection(subjects_B))

# Difference
print("Difference A-B:", subjects_A.difference(subjects_B))

# Symmetric Difference
print("Symmetric Difference:", subjects_A.symmetric_difference(subjects_B))