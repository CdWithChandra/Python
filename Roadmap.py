# ================================================
# Python Fundamentals in One Example
# ================================================

# VARIABLES & DATA TYPES
name = "Alice"  # string
age = 25  # int
height = 5.6  # float
skills = ["Python", "SQL"]  # list
scores = (85, 90, 95)  # tuple
profile = {"role": "Developer", "level": "Junior"}  # dictionary
unique_tags = {"python", "dev", "python"}  # set (duplicates removed)

#Print statements
print(f"Name: {name}, Age: {age}, Height: {height}")
print("Skills:", skills)
print("Scores:", scores)
print("Profile:", profile)
print("Unique Tags:", unique_tags)

# LOOPS & CONDITIONALS
print("\nLooping through skills:")
for skill in skills:
    if skill.lower() == "python":
        print(f"- {skill} ✅ (core skill)")
    else:
        print(f"- {skill}")


# FUNCTIONS & SCOPE
def calculate_average(marks):
    """Calculate average score."""
    total = sum(marks)  # local variable
    avg = total / len(marks)
    return avg


average_score = calculate_average(scores)
print(f"\nAverage Score: {average_score}")


# OBJECT-ORIENTED PROGRAMMING
class Developer:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

    def add_skill(self, new_skill):
        if new_skill not in self.skills:
            self.skills.append(new_skill)

    def show_profile(self):
        print(f"\n👩‍💻 Developer: {self.name}")
        print("Skills:", ", ".join(self.skills))


dev = Developer(name, skills)
dev.add_skill("Django")
dev.show_profile()

# FILE I/O
file_name = "developer_profile.txt"
with open(file_name, "w") as f:
    f.write(f"Name: {dev.name}\n")
    f.write(f"Skills: {', '.join(dev.skills)}\n")
    f.write(f"Average Score: {average_score}\n")

print(f"\nProfile saved to {file_name}")


# VIRTUAL ENVIRONMENTS
# (Demonstration only: run these commands in terminal, not inside Python)
# python -m venv venv
# source venv/bin/activate   # (Linux/Mac)
# venv\Scripts\activate      # (Windows)
# pip install requests       # example install inside venv