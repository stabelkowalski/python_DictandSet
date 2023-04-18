morning = ["java", "c", "ruby", "lisp", "c#"]
afternoon = ["python", "c#", "java", "c", "ruby"]

possible_courses = set(morning).symmetric_difference(afternoon)
print(possible_courses)

