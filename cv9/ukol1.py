write_file = open("myfile.txt", "w")
read_file = open("cv9/ukol1.py", "r")
data = read_file.readlines()

print(data)
for line in data:
    write_file.write("#" + line)

