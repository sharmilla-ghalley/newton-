# Lab02_pairNumber.py
# Smart Classroom Quiz & Performance Analyzer
# Each step is explained with comments

# Step 1: collecting of last 2 digtits from student ID
student1_id = int(input("Enter Student 1 ID: "))
student2_id = int(input("Enter Student 2 ID: "))

# Take last 2 digits
last_two_1 = student1_id % 100
last_two_2 = student2_id % 100

# Generate unique value
unique_value = (last_two_1 + last_two_2) % 10
print(f"Unique value generated: {unique_value}")

# Step 2: prompt names
students = {}
while True:
    name = input("Enter student name (or type 'exit' to stop): ").strip()
    if name.lower() == "exit":
        break
    if name == "":
        print("Warning: Blank name entered. Skipping...")
        continue
    students[name] = 0  # 0 score initialized 

# Step 3: show names of students
print("Registered Students:")
for student in students.keys():
    print(student)

# Step 4: Conduct quiz for each student
for student in students.keys():
    print(f"Quiz for {student}:")
    score = 0

    # Question 1
    ans1 = int(input(f"Q1: {unique_value} + 2 = "))
    if ans1 == unique_value + 2:
        score += 1

    # Question 2
    ans2 = int(input(f"Q2: {unique_value} × 3 = "))
    if ans2 == unique_value * 3:
        score += 1

    # Question 3
    ans3 = int(input(f"Q3: {unique_value} + 5 = "))
    if ans3 == unique_value + 5:
        score += 1

    # Store score
    students[student] = score

    # Step 5: Performance level
    if score == 3:
        performance = "Excellent"
    elif score == 2:
        performance = "Good"
    elif score == 1:
        performance = "Needs Improvement"
    else:
        performance = "Poor"
