import os
from datetime import datetime

def create_project_file():
    # Prompt for directory name
    dir_name = input("Enter the directory name: ")

    # Prompt for project name
    project_name = input("Enter the project name: ")

    # Create the specified directory if it doesn't exist
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    # Define file name
    file_name = f"Aidan-Arredondo-{project_name}-7th.py"

    # Get current date
    current_date = datetime.now().strftime("%m-%d-%Y")

    # Prompt for program description
    program_description = input("Enter the program description: ")

    # Create and write to the file
    with open(os.path.join(dir_name, file_name), 'w') as file:
        file.write(f"# {program_description}\n")
        file.write("# Aidan Arredondo 7th\n")
        file.write(f"# {current_date}\n")
        file.write("# \n")  # Enter space
        file.write("# \n")  # Print blank line
        file.write("print()\n")  # Print statement

    print(f"File '{file_name}' created successfully in '{dir_name}' directory.")

if __name__ == "__main__":
    create_project_file()