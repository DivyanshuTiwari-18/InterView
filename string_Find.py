def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1

    return count

if __name__ == '__main__':
    string = input("Enter String :").strip()   ##ABCDCDC
    sub_string = input("Enter element u want to search in String :").strip()  ##CDC
    
    count = count_substring(string, sub_string)
    print("Element Found ",count,"times")
