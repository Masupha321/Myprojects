def sort_characters(input_string):
    char_list = input_string.split(',')
    char_list = [char.strip() for char in char_list]
    char_list.sort()
    return  char_list

def isLongerThan5(S):
    return len(S) > 5
if __name__ == '__main__':