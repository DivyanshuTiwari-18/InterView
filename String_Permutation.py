def permute(input1):
    count_map = {}
    for ch in input1:
        if ch in count_map.keys():
            count_map[ch] = count_map[ch] + 1
        else:
            count_map[ch] = 1

    keys = sorted(count_map)
    str = []
    count = []
    for key in keys:
        str.append(key)
        count.append(count_map[key])
    result = [0 for x in range(len(input1))]
    permute_util(str, count, result, 0)

def permute_util(str, count, result, level):
    global P
    if level == len(result):
        P=P+1
        print(" ",result)
        return

    for i in range(len(str)):
        if count[i] == 0:
            continue;
        result[level] = str[i]
        count[i] -= 1
        permute_util(str, count, result, level + 1)
        count[i] += 1

if __name__ == '__main__':
	print("Hello, Here You can see all the possible permutations of Name You want\n(Repeated case also accepted) ")
	input1 = input("Input Name to see Its Combinations: ")
	P=0
	permute(input1)
	print("Total number of combinations for ",input1," is : ",P)
