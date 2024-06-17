import os

os.system("cls")


student_names = [
    "Mark",
    "Katarina",
    "Jessica",
    "Homer",
    "Bart",
    "Lisa",
    "Marge",
    "Maggie",
    "Santa",
    "Alex",
    "John",
    "Jill",
    "Jack",
    "Tom",
    "Jerry",
    "Mike",
]

records_per_page = 5
total_records = len(student_names)
total_pages = 0

if (total_records % records_per_page) == 0:
    total_pages = (total_records // records_per_page)
else:
    total_pages = (total_records // records_per_page)+1

for i in range(records_per_page):
        print(f"{i+1}.{student_names[i]}")
print(f"Active page: 1/{total_pages}")
while True:
    print("==========| Pagination Program |==========")
    print("Total records: ",total_records)
    print("Record per page: ",records_per_page)
    print("Total page: ",total_pages)

    page = int(input("Enter page number: "))

    if page > total_pages:
        os.system("cls")
        print("⚠️ Invalid Input !")
        continue

    start = (page-1) * records_per_page
    end = start + records_per_page
    student_ID = start + 1

    new_student_namee = student_names[start:end]
    os.system("cls")
    for i in range(len(new_student_namee)):
        print(f"{i+student_ID}.{new_student_namee[i]}")
    print(f"Active page: {page}/{total_pages}")

