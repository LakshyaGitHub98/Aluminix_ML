import random
import csv

branches = ["CSE", "IT", "ECE", "ME", "CE"]

skills_pool = {
    "CSE": [
        "python machine learning ai data analysis",
        "html css javascript react",
        "nodejs express mongodb api",
        "django python sql backend",
        "flutter mobile apps firebase",
        "ai deep learning neural networks"
    ],
    "IT": [
        "java spring boot microservices",
        "react node mongodb fullstack",
        "aws docker kubernetes cloud",
        "python flask apis backend",
        "cyber security linux networking"
    ],
    "ECE": [
        "iot sensors arduino embedded",
        "verilog vlsi design circuits",
        "embedded c microcontrollers",
        "signal processing electronics"
    ],
    "ME": [
        "autocad solidworks design",
        "thermal systems manufacturing",
        "mechanical cad cam",
        "robotics automation design"
    ],
    "CE": [
        "structure planning autocad",
        "construction surveying site work",
        "geotechnical civil engineering",
        "infrastructure design planning"
    ]
}

careers = {
    "CSE": ["Data Scientist", "AI Engineer", "Backend Developer", "Frontend Developer", "Mobile App Developer"],
    "IT": ["Software Engineer", "Full Stack Developer", "DevOps Engineer", "Backend Developer", "Security Analyst"],
    "ECE": ["IoT Engineer", "Hardware Engineer", "Embedded Engineer"],
    "ME": ["Mechanical Engineer", "Design Engineer"],
    "CE": ["Civil Engineer", "Site Engineer"]
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

for i in range(1500):
    branch = random.choice(branches)
    skills = random.choice(skills_pool[branch])
    career = random.choice(careers[branch])

    rows.append([
        branch,
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

print("Dataset generated with 1500 rows 🚀")