# Task 4
filepath = "/file.txt";
file = open(filepath, 'r');

# now reversing the data in the file
data = file.read();
data1 = data[::-1]; # fore reversing the list
file2 = open("/res.txt", "w");
##data2 = data1;
file2.write(data1);
print(data1)
file2.close();
file.close();
