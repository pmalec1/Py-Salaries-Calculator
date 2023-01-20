# Piotr Malec 318544

## LAB 5 

### Inputs
User have to provide some inputs:
* input_file_path - This path points to the file containing the database
* output_file_path - This path points to the file where the output of the program will be saved

### Outputs
Output will be saved in extern file
Result  consist of
* Sum of salaries --variable part of installment
* A list of names and employees' pay

### Functions
1.
* get_data_from_file_to_database(input_file_path): --> collecting data about input_file and destination file

2. 
* calculate_salary_for_uop(basic_salary, extra_hours,     
exta_time_hourly_rate):
* calculate_salary_for_uod(execution_parameter, reward):
* calculate_salary_for_uz(work_time, hourly_rate):

3.
* switch_mode_of_salary_calculating(database, type_of_contract, number_of_employee):

4.
*  make_list_of_salaries(database):

5.
*  calculate_sum_of_salaries(list_of_salaries):

6.
*  write_data_to_output_file(database, output_file_path, list_of_salaries, sum_of_salaries):

7.
* get_input_file_path_from_user():

8. 
* get_destination_file_path_from_user():

### How it works?

1. The user must indicate where the database is
2. The user has to specify where the results will be saved
3.  Then program calculate each salary and make list of salaries
4. Program connect each salary with right person 
5. The last step is to write list of names and salaries in the output file .

### Necessary packages
   import sys
### Rules of usage

Each line in database should be in correct format.
Input file path must points to an existing file 

### Exemplary results

The image "EXEMPLARY_RESULTS" shows the usage and the result is in this repository.
