#dictionary of courses and their information
courses={
    "CSC101": {
        "room": 3004,
        "instructor": "Haynes",
        "time": "8:00 a.m."
    },
    "CSC102": {
        "room": 4501,
        "instructor": "Alvarado",
        "time": "9:00 a.m."
    },
    "CSC103": {
        "room": 6755,
        "instructor": "Rich",
        "time": "10:00 a.m."
    },
    "NET110": {
        "room": 1244,
        "instructor": "Burke",
        "time": "11:00 a.m."
    },
    "COM241": {
        "room": 1411,
        "instructor": "Lee",
        "time": "1:00 p.m."
    }
}

while True:
    #continuously prompt the user for the course number
    print(f"Here are the courses available: {', '.join(courses.keys())}")
    course_num = input("Enter the course number for more information?\nEnter 'q' to exit.\n")
    if course_num.lower() == "q":
        break #exit the loop
   
    course = courses.get(course_num.upper(), None)

    if (course == None):
        print("Course not found")
        continue
    
    #print the course information
    print()
    print(f"Here is the course information for '{course_num.upper()}'.")
    print()
    print(f"Room: {course['room']}")
    print(f"Instructor: {course['instructor']}")
    print(f"Time: {course['time']}")
    print()