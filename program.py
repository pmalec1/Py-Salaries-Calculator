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
