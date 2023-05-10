def get_birth_century(birth_year):

    century = int(birth_year[:2]) + 1

    return century


def get_gender_code(gender, birth_date):
    birth_date = birth_date.split("-")
    century = get_birth_century(birth_date[0])
    gender_code = 0

    if gender == "men":
        if century == 19:
            gender_code = 1
        elif century == 20:
            gender_code = 3
        elif century == 21:
            gender_code = 5
    elif gender == "woman":
        if century == 19:
            gender_code = 2
        elif century == 20:
            gender_code = 4
        elif century == 21:
            gender_code = 6

    return gender_code



def check_LT_id_number(gender, birth_date, serial_number, person_id_number = False):

    if person_id_number:
        gender_code = person_id_number[0]

        if int(gender_code) % 2 == 0:
            gender = "woman"
        else:
            gender = "men"
        person_data = person_id_number[1:7]
        serial_number = person_id_number[7:10]
    else:
        gender_code = str(get_gender_code(gender,birth_date))
        person_data = birth_date.split("-")[0][2:] + birth_date.split("-")[1][:] + birth_date.split("-")[2]

    # print(f"gender_code {gender_code}")
    # print(f"serial_number {serial_number}")
    #
    #
    # print(f"person_data {person_data}")

    person_id = gender_code + person_data + serial_number
    last_number_sum = 0
    for index in range(1,9):
        s = index * int(person_id[index-1])
        last_number_sum += s
    last_number_sum += int(person_id[-1])

   # person_id_last_number = sum([int(number) for number  in person_id])/11

    if last_number_sum % 11 != 10:
        person_id_last_number = last_number_sum % 11
    else:
        for index in range(3, 9):
            s = index * int(person_id[index - 3])
            last_number_sum += s

        last_number_sum += int(person_id[-3])
        last_number_sum += int(person_id[-2] * 2)
        last_number_sum += int(person_id[-1] * 3)

        if last_number_sum % 11 != 10:
            person_id_last_number = last_number_sum % 11
        else:
            person_id_last_number = 0
    person_id += str(person_id_last_number)
    return person_id


print(check_LT_id_number("","","","39209043025"))
print(check_LT_id_number("","","","39209043025")=="39209043025")


