import random
import csv

branches = ["CSE", "IT", "ECE", "ME", "CE"]

# ✅ FIXED mapping (NO randomness in career)
skills_to_career = {
    "python machine learning ai data analysis": "Data Scientist",
    "ai deep learning neural networks": "AI Engineer",
    "html css javascript react": "Frontend Developer",
    "nodejs express mongodb api": "Backend Developer",
    "django python sql backend": "Backend Developer",
    "flutter mobile apps firebase": "Mobile App Developer",

    "java spring boot microservices": "Software Engineer",
    "react node mongodb fullstack": "Full Stack Developer",
    "aws docker kubernetes cloud": "DevOps Engineer",
    "python flask apis backend": "Backend Developer",
    "cyber security linux networking": "Security Analyst",

    "iot sensors arduino embedded": "IoT Engineer",
    "verilog vlsi design circuits": "Hardware Engineer",
    "embedded c microcontrollers": "Embedded Engineer",
    "signal processing electronics": "Embedded Engineer",

    "autocad solidworks design": "Design Engineer",
    "thermal systems manufacturing": "Mechanical Engineer",
    "mechanical cad cam": "Mechanical Engineer",
    "robotics automation design": "Design Engineer",

    "structure planning autocad": "Civil Engineer",
    "construction surveying site work": "Site Engineer",
    "geotechnical civil engineering": "Civil Engineer",
    "infrastructure design planning": "Site Engineer"
}

def random_cgpa():
    return round(random.uniform(6.5, 9.5), 2)

def random_projects():
    return random.randint(1, 5)

def random_internships():
    return random.randint(0, 2)

def random_comm():
    return random.randint(6, 10)

rows = []

skills_list = list(skills_to_career.keys())

for i in range(2000):
    skills = random.choice(skills_list)
    career = skills_to_career[skills]

    rows.append([
        "CSE",  # optional (not important now)
        skills,
        random_cgpa(),
        random_projects(),
        random_internships(),
        random_comm(),
        career
    ])

with open("dataset.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["branch","skills","cgpa","projects","internships","communication","career"])
    writer.writerows(rows)

print("✅ Clean dataset generated successfully 🚀")