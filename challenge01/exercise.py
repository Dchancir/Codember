text_file = open(r"C:\Users\daniel.chancir\Desktop\Autoestudio\codember\challenge01\users.txt")
lines = text_file.readlines()
test_list = ['usr', 'eme', 'psw', 'age', 'loc', 'fll']
list_index = 0
new_lists = [[]]
for line in lines:
    if line == '\n':
        list_index += 1
        new_lists.append([])
        continue
    else:
        new_lists[list_index].append(line)
new_lists = list(map(lambda x: [element.replace('\n', '') for element in x], new_lists))
new_lists = [" ".join(list) for list in new_lists]

new_lists = list(filter(lambda userData : [ele for ele in test_list if ele in userData] == test_list, new_lists))
print(len(new_lists), new_lists[-1])