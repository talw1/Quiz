# Program to read from a file and print its content

def read_and_print_file(filename):

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            i = 0
            content = file.read()
            print(i, content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def count_lines_in_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

def read_file_to_name_value_list(filename, delimiter=":"):
    name_value_list = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            i=0
            for line in file:
                # Split each line by the delimiter
                parts = line.strip().split(delimiter)

                if len(parts) == 2:  # Ensure there are exactly two parts
                    name, value = parts[0].strip(), parts[1].strip()
                    name_value_list.append((name, value))
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return name_value_list

# Function to read a file and print each line with line numbers
def read_and_number_lines(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                print(f"{line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


#file_name = ('example.csv')
#print(count_lines_in_file(file_name))
#read_and_number_lines(file_name)