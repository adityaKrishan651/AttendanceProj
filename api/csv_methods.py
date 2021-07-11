import csv
from datetime import date

def view_students(file_name):
	students = []
	with open(file_name, 'r') as csv_file:
		csv_reader = csv.DictReader(csv_file)

		for row in csv_reader:
			students.append(row['Roll Number'])

	return students

def view_classes(file_name):
	classes = []
	with open(file_name, 'r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		for row in csv_reader:
			classes.append(row['name'])

	return classes


def add_students(details):
	file_name = 'files/{}.csv'.format(details['class_name'])
	dict_from_csv = {}
	with open(file_name) as csv_file:
		csv_reader = csv.DictReader(csv_file)
		reader = csv.reader(csv_file)

		i = 0
		for row in reader:
			i += 1
			dict_from_csv[i] = row

		list_of_column_names = ['Roll Number'] 

		with open(file_name, 'a') as csv_file:
			csv_writer = csv.DictWriter(csv_file, fieldnames=list_of_column_names)
			if len(list(dict_from_csv.keys())) == 0:
				csv_writer.writeheader()
			csv_writer.writerow({'Roll Number': details['Roll Number']})


def write_attendance(absent_students, date, class_name):
	dict_from_csv = {}
	correct_absent_students = []
	file_name = 'files/{}.csv'.format(class_name)

	for student in absent_students:
		if int(student) < 10:
			student = "CO1750" + str(student) 
		else:
			student = "CO175" + str(student)
		correct_absent_students.append(student)

	with open(file_name, 'r') as csv_file:
		reader = csv.DictReader(csv_file, delimiter=',')

		i = 0
		for row in reader:
			i += 1
			dict_from_csv[i] = row

		for student in dict_from_csv.values():
			student[date] = 'P'

		for student in dict_from_csv.values():
			if student['Roll Number'] in correct_absent_students:
				student[date] = 'A'
	
	with open(file_name, 'w') as csv_file:
		field_names = list(dict_from_csv[1].keys())
		writer = csv.DictWriter(csv_file, fieldnames=field_names)

		writer.writeheader()
		for student in dict_from_csv.values():
			writer.writerow(student)


def add_new_class(details, file_name):
	with open(file_name) as csv_file:
		dict_from_csv = {}
		csv_reader = csv.DictReader(csv_file)

		list_of_column_names = ['name']

		i = 0
		for row in csv_reader:
			i += 1
			dict_from_csv[i] = row

		list_of_column_names = ['name'] 

		with open(file_name, 'a') as csv_file:
			csv_writer = csv.DictWriter(csv_file, fieldnames=list_of_column_names)
			if len(list(dict_from_csv.keys())) == 0:
				csv_writer.writeheader()
			csv_writer.writerow(details)

		new_file_name = 'files/{}.csv'.format(details['name'])
		with open(new_file_name, 'w') as csv_file:
			print('Class file created')


def class_list(file_name):
    with open(file_name) as csv_file: 
        dict_from_csv = {}
        csv_reader = csv.DictReader(csv_file)
        i = 0
        for row in csv_reader:
            i += 1
            dict_from_csv[i] = row

        return dict_from_csv