student_file = open("Project2.txt", 'r')
all_files = student_file.readlines()
for student_line in all_files:
    #student_line = student_line.strip()
    student_names = student_line.split(":")
    print(f"Student ID: {student_names[0]},{student_names[2]} ")

