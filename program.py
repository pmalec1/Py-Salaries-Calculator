try:
    import sys
except ImportError:
    print("Library sys not found. This package is necessary for this program\n"
                    " consider reinstallation of python eviroment")


def get_data_from_file_to_database(input_file_path):
    file = open(input_file_path, "r", encoding='utf8')
    database = []                           #init database
    file.seek(0, 0)
    for current_line in file:
        temp_line = current_line.split(";") # make list of elements separated by ;
        temp_line.pop(len(temp_line) - 1)   # Remove new_line_sing "\n"  from list
        database.append(temp_line)          # Add each list at the end of the database
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


def switch_mode_of_salary_calculating(database, type_of_contract, number_of_employee):
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


def make_list_of_salaries(database):
    amount_of_employees = len(database)
    list_of_salaries = []
    for number_of_employee in range(amount_of_employees-1):
        type_of_contract = database[number_of_employee][1]
        salary = switch_mode_of_salary_calculating(database, type_of_contract, number_of_employee) #Mode of calculating depends on type of contract
        list_of_salaries.append(salary)         #Appends salary of each employee at the end of the list of salaries
    return list_of_salaries


def calculate_sum_of_salaries(list_of_salaries):
    sum_of_salaries = sum(list_of_salaries)
    return sum_of_salaries


def write_data_to_output_file(database, output_file_path, list_of_salaries, sum_of_salaries):
    file = open(output_file_path, "w", encoding='utf8')
    output_data = []
    output_data.append("Salary for employees\n")
    output_data.append("SUM OF SALARIES = {}\n" .format(sum_of_salaries))
    amount_of_workers = len(database)
    for number_of_worker in range(amount_of_workers-1):
        output_data.append([database[number_of_worker][0], list_of_salaries[number_of_worker]])
    for number_of_worker in range(amount_of_workers-1):
        file.writelines(str(output_data[number_of_worker]))
        file.writelines("\n")
    file.close()
    return output_data


def get_input_file_path_from_user():
    input_file_path = input(str("Please provide input file path: "))
    return input_file_path


def get_destination_file_path_from_user():
    destination_file_path = input(str("Please provide destitation path or name for new file: "))
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
    output_data = write_data_to_output_file(database, output_file_path, list_of_salaries, sum_of_salaries)
    print(output_data)


if __name__ == '__main__':
    main()
