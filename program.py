try:
    import os.path
except:
    print("Library os not found, please consider reinstalling Python enviroment")


try:
    import sys
except:
    raise Exception("Library sys not found, please consider reinstalling Python enviroment")


def get_data_from_file_to_database(input_file_path):
    file = open(input_file_path, "r", encoding='utf8')
    database = []
    file.seek(0, 0)
    for current_line in file:
        temp_line = current_line.split(";")
        temp_line.pop(len(temp_line) - 1)  # Remove /n from the table
        database.append(temp_line)
    file.close()
    return database


def calculate_salary_for_uop(basic_salary, extra_hours, exta_time_hourly_rate):
    salary = int(basic_salary) + int(extra_hours) * int(exta_time_hourly_rate)
    return salary


def calculate_salary_for_uod(execution_parameter, reward):
    if execution_parameter == "DONE":
        return int(reward)
    elif execution_parameter == "NOT_DONE":
        return 0


def calculate_salary_for_uz(work_time, hourly_rate):
    return int(work_time)*int(hourly_rate)


def make_list_of_salaries(database):
    amount_of_employees = len(database)
    list_of_salaries = []
    for number_of_employee in range(amount_of_employees-1):
        type_of_contract = database[number_of_employee][1]
        salary = calculate_salary(database, type_of_contract, number_of_employee)
        list_of_salaries.append(salary)
    return list_of_salaries


def calculate_salary(database, type_of_contract, number_of_employee):
    salary = 0
    if type_of_contract == "UoP":
        basic_salary = database[number_of_employee][2]
        extra_hours = database[number_of_employee][4]
        exta_time_hourly_rate = database[number_of_employee][3]
        salary = calculate_salary_for_uop(basic_salary, extra_hours, exta_time_hourly_rate)
    elif type_of_contract == "UoD":
        reward = database[number_of_employee][2]
        execution_parameter = database[number_of_employee][3]
        salary = calculate_salary_for_uod(execution_parameter, reward)
    elif type_of_contract == "UZ":
        work_time = database[number_of_employee][3]
        hourly_rate = database[number_of_employee][2]
        salary = calculate_salary_for_uz(work_time, hourly_rate)
    return salary


def calculate_sum_of_salaries(list_of_salaries):
    sum_of_salaries = sum(list_of_salaries)
    return sum_of_salaries


def write_data_to_output_file(database, output_file_path, list_of_salaries, sum_of_salaries):
    file = open(output_file_path, "w", encoding='utf8')
    output_data = []
    output_data.append("SUM OF SALARIES = {}" .format(sum_of_salaries))
    amount_of_workers = len(database)
    for number_of_worker in range(amount_of_workers-1):
        output_data.append([database[number_of_worker][0], list_of_salaries[number_of_worker]])
    for number_of_worker in range(amount_of_workers-1):
        file.writelines(str(output_data[number_of_worker]))
        file.writelines("\n")
    file.close()


def get_input_file_path_from_user():
    input_file_path = input(str("Please provide input file path:"))
    return input_file_path


def get_destination_file_path_from_user():
    destination_file_path = input(str("Please provide destitation file path:"))
    return destination_file_path


def main():
    input_file_path = get_input_file_path_from_user()
    output_file_path = get_destination_file_path_from_user()
    database = []
    try:
        database = get_data_from_file_to_database(input_file_path)
    except:
        sys.exit("Input file not found. Path must point to an existing file")
    list_of_salaries = make_list_of_salaries(database)
    sum_of_salaries = calculate_sum_of_salaries(list_of_salaries)
    write_data_to_output_file(database, output_file_path, list_of_salaries, sum_of_salaries)


if __name__ == '__main__':
    main()
