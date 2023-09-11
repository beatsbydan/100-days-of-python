my_dictionary = {
    "Name": "Daniel"
}

# Grading Program
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermoine": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 80:
        student_grades[key] = "Exceeds Expectation"
    elif student_scores[key] > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
        
print(student_grades)

capitals = {
    "list": [],
    'dictionary': {}
}
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Di jon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]

def add_new_country(country, visits, cities):
    travel_log.append({
        "country": country,
        "visits": visits,
        "cities": cities
    })
add_new_country("Brazil", 2, ["Rio"])
print(travel_log)