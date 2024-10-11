import csv
from datetime import datetime
import numpy as np
from faker import Faker

date = "2003.09.25"

faker_uk = Faker('uk_UA')

then_row = []; man=0; woman=0; p=0
while(p<3000):
    p=p+1
    if (0.6 >= (man / (man + woman + 1))):
       male = 'male'
       last_name = faker_uk.last_name_male()
       name = faker_uk.first_name_male()
       last_name_female = faker_uk.middle_name_male()
       man = man + 1
    else:
       male = 'female'
       last_name = faker_uk.last_name_female()
       name = faker_uk.first_name_female()
       last_name_female = faker_uk.middle_name_female()
       woman = woman + 1
    time = 0
    while (time != 1):
       try:
           year = np.random.randint(1938, 2008)
           month = np.random.randint(1, 13)
           day = np.random.randint(1, 31)
           datetime(year,month,day)
           date = str(year) + '.' + str(month) + '.' + str(day)
           time = 1
       except:
           print()

    year = (2024 - year)
    month = (9 - month)
    day = (22 - day)
    if (day < 0) & (month == 0):
       year = year - 1
    elif (month < 0):
       year = year - 1
    post = faker_uk.job()
    # post -hard!!!
    if year < 4:
       post = "Сидить дома"
    elif year < 6:
       post = np.random.choice(["Ходить в садок", "Сидить дома"])
    elif year < 14:
       post = "Ходить до школи"
    elif year < 18:
       post = np.random.choice(["Ходить до школи", "Ходить на підробіток та дошколи"])
    elif year < 22:
       post = np.random.choice(["Ходить в університет", post])

    address = faker_uk.address()
    i = 0
    for a in address:
       if (a == ','):
           first_address = address[:i - 1]
           break
       i = 1 + i
    telephone = np.random.randint(380500000000, 380999999999)
    email = faker_uk.email()

    then_row.append([last_name, name, last_name_female, male, date, post, first_address,
                     address, telephone, email])
# Under main element for excel
first_row = ["Прізвище", "Ім'я", "По батьковій", "Стать", "Дата народження", "Посада", "Місце проживання", "Адрес проживання", "Телефон", "Email"]
for row in then_row:
    print(row)
with open("work.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(first_row)

for row in then_row:
    with open("work.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow(row)

