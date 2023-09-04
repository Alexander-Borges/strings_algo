""" Create a function that, given a string, returns all of that string’s contents, but without blanks. 

If given the string " Pl ayTha tF u nkyM usi c ", return "PlayThatFunkyMusic". """

def remove_spaces(input_string):
    return ''.join(input_string.split()) 

input_string = " Pl ayTha tF u nkyM usi c "
result = remove_spaces(input_string)
print(result)

""" Create a JavaScript function that given a string, returns the integer made from the string’s digits. Given "0s1a3y5w7h9a2t4?6!8?0", the function should return the number 1357924680.
"""
def extract_digits(input_string):
    result = ""

    for char in input_string:
        if char.isdigit():
            result += char 

    if result:
        return int(result)
    else: 
        return 0

input_string = "0s1a3y5w7h9a2t4?6!8?0"
result = extract_digits(input_string)
print(result)

""" Create a function that, given a string, returns the string’s acronym (first letters only, capitalized). 

Given " there's no free lunch - gotta pay yer way. ", return "TNFL-GPYW". 

Given "Live from New York, it's Saturday Night!", return "LFNYISN".
"""
def get_acronym(input_string):
    words = input_string.split()
    acronym = ""

    for word in words:
        if word and word[0].isalpha():
            acronym += word[0].upper()

    return acronym

input_string1 = "there's no free lunch - gotta pay yer way."
result1 = get_acronym(input_string1)
print(result1)

input_string2 = "Live from New York, it's Saturday Night!"
result2 = get_acronym(input_string2)
print(result2)

""" Dictionaries are sometimes called maps because a key (string) maps to a value. Given two arrays, create an associative array (map) containing keys of the first, and values of the second. For arr1 = ["abc", 3, "yo"] and arr2 = [42, "wassup", true], return {"abc": 42, 3: "wassup", "yo": true}. """

def create_associative_array(arr1, arr2):
    associative_dict = {}

    for i in range(min(len(arr1), len(arr2))):
        key = arr1[i]
        value = arr2[i]
        associative_dict[key] = value

    return associative_dict

arr1 = ["abc", 3, "yo"]
arr2 = [42, "wassup", True]
result = create_associative_array(arr1, arr2)
print(result)


""" Dictionaries are also called hashes (we’ll learn why later). Build invertHash(assocArr) to convert hash keys to values, and values to keys. 

Example: given {"name": "Zaphod", "charm": "high", "morals": "dicey"}, return object {"Zaphod": "name", "high":"charm", "dicey": "morals"}. """ 
def inverted_hash(associative_arr):
    inverted_dict = {}

    for key, value in associative_arr.items():
        inverted_dict[value] = key

    return inverted_dict

original_dict = {"name": "Zaphod", "charm": "hight", "morals": "dicey"}
inverted_dict = inverted_hash(original_dict)
print(inverted_dict)
