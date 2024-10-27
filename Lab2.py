def calc_average(temp_list):
    average = sum(temp_list) / len(temp_list)
    print(f"Average temperature: {average}")
    return average

def find_min_max(temp_list):
    min_temp = min(temp_list)
    max_temp = max(temp_list)
    print(f"Minimum temperature: {min_temp}, Maximum temperature: {max_temp}")
    return [min_temp, max_temp]

def sort_temperature(temp_list):
    sorted_list = sorted(temp_list)
    print(f"Sorted temperatures: {sorted_list}")
    return sorted_list

def calc_median_temperature(temp_list):
    sorted_list = sorted(temp_list)
    n = len(sorted_list)
    if n % 2 == 1:
        median = sorted_list[n // 2]
    else:
        mid1, mid2 = sorted_list[n // 2 - 1], sorted_list[n // 2]
        median = (mid1 + mid2) / 2
    print(f"Median temperature: {median}")
    return median

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    user_input = input("Enter temperatures: ")
    temp_list = [float(x) for x in user_input.split(",")]
    print(f"User input temperatures: {temp_list}")
    return temp_list