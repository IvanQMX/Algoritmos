start = 0
end = 100
file_path = "test.txt"

output = str([i for i in reversed(range(start, end))])
output = output.replace('[', '')
output = output.replace(']', '')

file = open(file_path, 'w')
file.write(output)
file.close()