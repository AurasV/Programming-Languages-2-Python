import random
import os

my_list = [1, 2, 3, 4, 5]
random_element = random.choice(my_list)
print("Random element from list: " + str(random_element))

my_dict = {"a": 1,
           "b": 2,
           "c": 3,
           "d": 4,
           "e": 5}
random_dict = random.choice(list(my_dict.keys()))
random_dict_value = my_dict[random_dict]
print("Random element from dictionary: " + str(random_dict) + ", " + str(random_dict_value))

directory = "New Folder"
random_file = random.choice(os.listdir(directory))
print("Random file from directory: " + str(random_file))
