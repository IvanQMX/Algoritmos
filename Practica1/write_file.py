start = 0
end = 10000
file_path = "test.txt"

output = str([i for i in range(start, end)])
output = output.replace('[', '')
output = output.replace(']', '')

file = open(file_path, 'w')
file.write(output)
file.close()
