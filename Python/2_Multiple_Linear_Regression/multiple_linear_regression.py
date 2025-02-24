def read_data(dir):
    dataset = []
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()   #remove \n
            data = line.split(',')#split with ','
            dataset.append(data)
        #print column names:
        print(f"Columns:{dataset[0]}")
        del dataset[0] #delete column names
        return dataset

file_path = "Datasets/Housing.csv"

dataset = read_data(file_path)
#print(dataset)
print(type(dataset))
#print(dataset[0])
#print(dataset[0][0])

#print(dataset[5])
# Deal with non number values.
#print(dataset[5][5])
#print(dataset[5][6])
#print(dataset[5][7])
#print(dataset[5][8])
#print(dataset[5][9])
#print(dataset[5][11])
#print(dataset[5][12])

binary_var_list = [5,6,7,8,9,11]
triple_var_list = [12]
for var in binary_var_list:
    for i in range(len(dataset)):
        if dataset[i][var] =='yes':
            dataset[i][var] = 1
        elif dataset[i][var] == 'no':
            dataset[i][var] = 0

for var in triple_var_list:
    for i in range(len(dataset)):
        if dataset[i][var]=='furnished':
            dataset[i][var] = 2
        elif dataset[i][var]=='semi-furnished':
            dataset[i][var] = 1
        elif dataset[i][var]=='unfurnished':
            dataset[i][var] = 0
#for data in dataset:
#    print(data)



X = []
Y = []

for i in range(len(dataset)):
    Y.append(dataset[i][0])
for i in range(len(dataset)):
    X.append(dataset[i][1:])
#Turn into strings into float in lists
#Y = [float(y) for y in Y]
#X = [float(x) for x in X]

#print(X)
#print(Y)

#print(dataset[0])
print(Y[0])
print(X[0])