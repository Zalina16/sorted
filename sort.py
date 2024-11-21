def merge_files(file_names, output_file):
    files_data = []

    for file_name in file_names:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            files_data.append((file_name, len(lines), lines))

    files_data.sort(key=lambda x: x[1])

    with open(output_file, 'w', encoding='utf-8') as output:
        for file_name, line_count, lines in files_data:
            output.write(f'{file_name}\n')
            output.write(f'{line_count}\n')
            output.writelines(lines)

file_names = ['1.txt', '2.txt', '3.txt']
output_file = 'merged.txt'
merge_files(file_names, output_file)
