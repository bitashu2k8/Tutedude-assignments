#Program to creat a dictionary of student's name and their marks
stu_dict={'ashu':90,'sruthi':89,'hema':79}
stu_name=input("Enter the student's name:").lower()
if stu_name in stu_dict.keys():
    print(f"{stu_name.capitalize()}'s marks: {stu_dict[stu_name]}")
else:
    print('Student not found.')