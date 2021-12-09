import os


root_dir = './some_data'
file_size_dict = {10: (0, [])}
file_size = 0
count = 0
test_set = list()

for root, dirs, files in os.walk(root_dir):
    for file in files:
        f_path = os.path.join(root, file)
        file_size = os.stat(f_path).st_size
        if file_size == 0:
            test_set = list(file_size_dict[10])
            test_set[0] += 1
            test_set[1].append(file)
            file_size[10] = tuple(test_set)
            continue
        while file_size:
            if file_size // 10:
                count += 1
                file_size = file_size // 10
                continue
            if 10 ** (count + 1) not in file_size_dict:
                file_size_dict[10 ** (count + 1)] = (1, [file])
            else:
                test_set = list(file_size_dict[10 ** (count + 1)])
                test_set[0] += 1
                test_set[1].append(file)
                file_size_dict[10 ** (count + 1)] = tuple(test_set)
            file_size = file_size // 10
            count = 0

print(file_size_dict)
