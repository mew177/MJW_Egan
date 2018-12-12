import os
import shutil
from sys import argv

if len(argv) >= 3:
    students = argv[1]
    source = argv[2]
else:
	print('To copy rubric to all students in a list:\n\npython ' + argv[0] + ' username_list.txt')
	quit(-1)

students = open(students, 'r')
students = {user.strip() for user in students.read().split('\n') if not user.startswith('#') and user.strip() != ''}

files = os.listdir(source)

for file in files:
    if file != "!grading" and file != "!template":
        print(file + "\n")
        userid = file.split('-')
        if userid[2] not in students:
            shutil.rmtree(source + '/' + file)




