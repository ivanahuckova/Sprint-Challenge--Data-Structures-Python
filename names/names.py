import time

start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


# # First pass solution provided
# def compare_first(list_1, list_2):
#     duplicates = []
#     for item_1 in list_1:
#         for item_2 in list_2:
#             if item_1 == item_2:
#                 duplicates.append(item_1)
#     return duplicates

# duplicates = compare_first(names_1, names_2)


# # Second iteration
# def compare_second(list_1, list_2):
#     duplicates = []
#     for item_1 in list_1:
#         if item_1 in list_2:
#             duplicates.append(item_1)
#     return duplicates

# duplicates = compare_second(names_1, names_2)


# Third iteration
def compare_third(list_1, list_2):
    duplicates = []
    list_1_dictionary = {}

    for item_1 in list_1:
        list_1_dictionary[item_1] = item_1

    for item_2 in list_2:
        try:
            if list_1_dictionary[item_2]:
                duplicates.append(item_2)
        except:
            pass
    return duplicates


duplicates = compare_third(names_1, names_2)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
