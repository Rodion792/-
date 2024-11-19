calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    length = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    return (length, upper_case, lower_case)

def is_contains(string, list_to_search):
    count_calls()

    normalized_string = string.lower()
    return normalized_string in (item.lower() for item in list_to_search)


info1 = string_info("Hello World")
info2 = string_info("Python Programming")

search_list = ["urban", "city", "town"]
contains_result1 = is_contains("URBAN", search_list)
contains_result2 = is_contains("village", search_list)


print(info1)
print(info2)
print(contains_result1)
print(contains_result2)
print("Количество вызовов функций:", calls)
