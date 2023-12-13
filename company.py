departments = [
    {
        "title": "HR department",
        "employers": [
            {
                "first_name": "Daniel",
                "last_name": "Bergera",
                "position": "Junior HR",
                "salary_rub": 50000,
            },
            {
                "first_name": "Michelle",
                "last_name": "Frey",
                "position": "Middle HR",
                "salary_rub": 75000,
            },
            {
                "first_name": "Kevin",
                "last_name": "Jimenez",
                "position": "Middle HR",
                "salary_rub": 70000,
            },
            {
                "first_name": "Nicole",
                "last_name": "Rileya",
                "position": "HRD",
                "salary_rub": 120000,
            },
        ],
    },
    {
        "title": "IT department",
        "employers": [
            {
                "first_name": "Christina",
                "last_name": "Walker",
                "position": "Python dev",
                "salary_rub": 80000,
            },
            {
                "first_name": "Michelle",
                "last_name": "Gilberta",
                "position": "JS dev",
                "salary_rub": 85000,
            },
            {
                "first_name": "Caitlin",
                "last_name": "Bradley",
                "position": "Teamlead",
                "salary_rub": 950000,
            },
            {
                "first_name": "Brian",
                "last_name": "Hartmana",
                "position": "CTO",
                "salary_rub": 130000,
            },
        ],
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]
print("\n 1. Вывести названия всех отделов\n")

for department_index in range(len(departments)):
    print(departments[department_index]["title"])

print("\n 2. Вывести имена всех сотрудников компании\n")

for department_index in range(len(departments)):
    for employers_index in range(len(departments[department_index]["employers"])):
        print(
            departments[department_index]["employers"][employers_index]["first_name"],
            departments[department_index]["employers"][employers_index]["last_name"],
        )

print(
    "\n 3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают\n"
)

for department_index in range(len(departments)):
    for employers_index in range(len(departments[department_index]["employers"])):
        print(
            f'{departments[department_index]["employers"][employers_index]["first_name"]} {departments[department_index]["employers"][employers_index]["last_name"]} работает в {departments[department_index]["title"]}'
        )

print("\n 4. Вывести имена всех сотрудников компании, которые получают больше 100к\n")
for department_index in range(len(departments)):
    for employers_index in range(len(departments[department_index]["employers"])):
        if (
            departments[department_index]["employers"][employers_index]["salary_rub"]
            > 100000
        ):
            print(
                f'{departments[department_index]["employers"][employers_index]["first_name"]} {departments[department_index]["employers"][employers_index]["last_name"]} получает больше 100к'
            )

print(
    "\n 5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями)\n"
)
for department_index in range(len(departments)):
    for employers_index in range(len(departments[department_index]["employers"])):
        if (
            departments[department_index]["employers"][employers_index]["salary_rub"]
            < 80000
        ):
            print(
                f'{departments[department_index]["employers"][employers_index]["position"]} получают меньше 80к'
            )


print(
    "\n 6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела\n"
)

for department_index in range(len(departments)):
    total_sum_department = sum(
        departments[department_index]["employers"][employers_index]["salary_rub"]
        for employers_index in range(len(departments[department_index]["employers"]))
    )
    print(
        f'{total_sum_department} уходит на отдел {departments[department_index]["title"]}'
    )
print("\n Второй уровень\n")
print("\n 7. Вывести названия отделов с указанием минимальной зарплаты в нём\n")


for department_index in range(len(departments)):
    list_of_salaries = []
    for employers_index in range(len(departments[department_index]["employers"])):
        list_of_salaries.append(
            departments[department_index]["employers"][employers_index]["salary_rub"]
        )
    print(
        f'минимальная зарплата в отделе {departments[department_index]["title"]} составляет {min(list_of_salaries)}'
    )

print(
    "\n 8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.\n"
)

for department_index in range(len(departments)):
    list_of_salaries = []
    for employers_index in range(len(departments[department_index]["employers"])):
        list_of_salaries.append(
            departments[department_index]["employers"][employers_index]["salary_rub"]
        )
    print(
        f'В отделе {departments[department_index]["title"]} минимальная зарплата составляет {min(list_of_salaries)}, максимальная -  {max(list_of_salaries)}, средняя - {sum(list_of_salaries)/len(list_of_salaries)}'
    )

print("\n 9. Вывести среднюю зарплату по всей компании.\n")
total_salary = 0
list_of_total_salaries = []
for department_index in range(len(departments)):
    total_sum_department = sum(
        departments[department_index]["employers"][employers_index]["salary_rub"]
        for employers_index in range(len(departments[department_index]["employers"]))
    )
    total_salary += total_sum_department
    for employers_index in range(len(departments[department_index]["employers"])):
        list_of_total_salaries.append(
            departments[department_index]["employers"][employers_index]["salary_rub"]
        )
print(
    f"Средняя зарплата по всей компании: {total_salary / len(list_of_total_salaries)}"
)

print(
    "\n 10. Вывести названия должностей, которые получают больше 90к без повторений.\n"
)

list_of_positions = []

for department_index in range(len(departments)):
    for employers_index in range(len(departments[department_index]["employers"])):
        if (
            departments[department_index]["employers"][employers_index]["salary_rub"]
            > 90000
        ):
            if (
                departments[department_index]["employers"][employers_index]["position"]
                not in list_of_positions
            ):
                list_of_positions.append(
                    departments[department_index]["employers"][employers_index][
                        "position"
                    ]
                )
print(list_of_positions)

print(
    "\n 11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).\n"
)
list_of_women = ["Michelle", "Nicole", "Christina", "Caitlin"]
total_women_salaries = 0
count = 0
for department_index in range(len(departments)):
    count = 0
    for employers_index in range(len(departments[department_index]["employers"])):
        if (
            departments[department_index]["employers"][employers_index]["first_name"]
            in list_of_women
        ):
            total_women_salaries += departments[department_index]["employers"][
                employers_index
            ]["salary_rub"]
            count += 1
    print(
        f"Средняя зарплата по отделу {departments[department_index]['title']} среди девушек составляет {round(total_women_salaries / count, 2)}"
    )

print(
    "\n 12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.\n"
)
list_of_last_names_vowels = []
list_of_vowels = ["a", "e", "i", "o", "u"]
for department_index in range(len(departments)):
    for employers_index in range(len(departments[department_index]["employers"])):
        if (
            departments[department_index]["employers"][employers_index]["last_name"][-1]
            in list_of_vowels
            and departments[department_index]["employers"][employers_index]["last_name"]
            not in list_of_last_names_vowels
        ):
            list_of_last_names_vowels.append(
                departments[department_index]["employers"][employers_index][
                    "first_name"
                ]
            )
print(
    f"имена людей, чьи фамилии заканчиваются на гласную букву {' , '.join(list_of_last_names_vowels)}"
)

print(
    "\n Третий уровень: 13. Вывести список отделов со средним налогом на сотрудников этого отдела.\n"
)

for department in departments:
    total_sum_department = sum(
        employer["salary_rub"] for employer in department["employers"]
    )

    tax_per_department = next(
        (tax["value_percents"] for tax in taxes if tax["department"] is None), 0
    )
    for tax in taxes:
        tax_department = tax["department"]
        department_title = department["title"]
        if tax_department is not None and department_title is not None:
            if tax_department.lower() == department_title.lower():
                tax_per_department += tax["value_percents"]
    tax_sum_per_department = tax_per_department * total_sum_department / 100
    average_tax_sum_per_employee = tax_sum_per_department / len(department["employers"])
    print(
        f"Средняя сумма налога на сотрудника отдела {department_title} составляет {average_tax_sum_per_employee}"
    )

print(
    "\n 14. Вывести список всех сотредников с указанием зарплаты 'на руки' и зарплаты с учётом налогов.\n"
)

for department in departments:
    tax_per_department = next(
        (tax["value_percents"] for tax in taxes if tax["department"] is None), 0
    )
    for tax in taxes:
        name_tax_department = tax["department"]
        department_title = department["title"]
        if name_tax_department is not None and department_title is not None:
            if name_tax_department.lower() == department_title.lower():
                tax_per_department += tax["value_percents"]

    print(f'Налог для отдела {department["title"]} составляет {tax_per_department}')
    salary_without_taxes = 0
    for employee in department["employers"]:
        salary_without_taxes = employee["salary_rub"] * (1 - tax_per_department / 100)
        print(
            f'Зарплата сотрудника  {employee["first_name"]} {employee["last_name"]} без учета налога составляет {employee["salary_rub"]}, за вычетом налогов {salary_without_taxes}'
        )

print(
    "\n 15. Вывести список отделов, отсортированный по месячной налоговой нагрузки..\n"
)
list_of_department_with_taxes = []
for department in departments:
    dict_of_departments_with_taxes = {}
    total_sum_department = sum(
        employer["salary_rub"] for employer in department["employers"]
    )

    tax_per_department = next(
        (tax["value_percents"] for tax in taxes if tax["department"] is None), 0
    )

    for tax in taxes:
        tax_name_department = tax["department"]
        department_title = department["title"]
        if tax_name_department is not None and department_title is not None:
            if tax_name_department.lower() == department_title.lower():
                tax_per_department += tax["value_percents"]
    tax_sum_per_department = tax_per_department * total_sum_department / 100
    dict_of_departments_with_taxes["sum_of_taxes"] = tax_sum_per_department
    dict_of_departments_with_taxes["department_title"] = department["title"]
    list_of_department_with_taxes.append(dict_of_departments_with_taxes)


sorted_list_department_with_taxes = sorted(
    list_of_department_with_taxes, key=lambda x: x["sum_of_taxes"]
)
for department in sorted_list_department_with_taxes:
    print(department["department_title"])

print(
    "\n 16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.\n"
)

for department in departments:
    tax_per_department = next(
        (tax["value_percents"] for tax in taxes if tax["department"] is None), 0
    )
    for tax in taxes:
        name_tax_department = tax["department"]
        department_title = department["title"]
        if name_tax_department is not None and department_title is not None:
            if name_tax_department.lower() == department_title.lower():
                tax_per_department += tax["value_percents"]
    employee_sum_of_taxes_year = 0

    for employee in department["employers"]:
        employee_sum_of_taxes_year = (
            employee["salary_rub"] * tax_per_department / 100
        ) * 12
        if employee_sum_of_taxes_year > 100000:
            print(f'{employee["first_name"]} {employee["last_name"]}')

print(
    "\n 17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.\n"
)
list_sum_of_taxes = []
for department in departments:
    tax_per_department = next(
        (tax["value_percents"] for tax in taxes if tax["department"] is None), 0
    )
    for tax in taxes:
        name_tax_department = tax["department"]
        department_title = department["title"]
        if name_tax_department is not None and department_title is not None:
            if name_tax_department.lower() == department_title.lower():
                tax_per_department += tax["value_percents"]

    employee_sum_of_taxes_month = 0

    for employee in department["employers"]:
        employee_sum_of_taxes_month = employee["salary_rub"] * tax_per_department / 100

        list_sum_of_taxes.append(
            {
                "first_name": employee["first_name"],
                "last_name": employee["last_name"],
                "employee_sum_of_taxes_month": employee_sum_of_taxes_month,
            }
        )
min_employee = min(list_sum_of_taxes, key=lambda x: x["employee_sum_of_taxes_month"])
print(
    f'Сотрудник с самой маленькой суммой налогов: {min_employee["first_name"]} {min_employee["last_name"]}'
)
