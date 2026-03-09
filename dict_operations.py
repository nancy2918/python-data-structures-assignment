# Creating dictionary
employee = {
    "id": 101,
    "name": "Rahul",
    "department": "Data Science"
}

print("Employee Details:", employee)

# Accessing values
print("Employee Name:", employee["name"])

# Updating value
employee["department"] = "Machine Learning"

print("Updated Department:", employee["department"])

# Adding new key-value
employee["salary"] = 50000

print("After Adding Salary:", employee)

# Removing element
employee.pop("salary")

print("After Removing Salary:", employee)

# Safe retrieval
print("Age:", employee.get("age", "Not available"))

# Merging dictionaries
extra_info = {
    "location": "Roorkee",
    "experience": "2 years"
}

merged = employee | extra_info

print("Merged Dictionary:", merged)