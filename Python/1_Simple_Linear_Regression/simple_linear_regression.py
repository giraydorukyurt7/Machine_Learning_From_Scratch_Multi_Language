def read_data(dir):
    dataset = []
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()   #remove \n
            data = line.split(',')#split with ','
            dataset.append(data)
        del dataset[0] #delete column names
        return dataset

#print(read_data("../../Datasets/simple_housing_data.csv"))

#print(read_data("test.txt"))
#f = open("test.txt","r")
#print(f.read())

file_path = "Datasets/simple_housing_data.csv"

dataset = read_data(file_path)
#data_ = list(data)
#print(type(data))
#print(data)
#print(len(data))

X = []
Y = []

for i in range(len(dataset)):
    X.append(dataset[i][0])
for i in range(len(dataset)):
    Y.append(dataset[i][1])

def test_train_split(X,Y,train_percentage):
    0.8

    if len(X) == len(Y):
        slice_index = int(len(X)*train_percentage)
        X_train = X[:slice_index]
        y_train = Y[:slice_index]
        X_test  = X[slice_index:]
        y_test  = Y[slice_index:]

        return X_train, y_train, X_test, y_test
    else:
        print("Lengths are inequal!")

X_train, y_train, X_test, y_test = test_train_split(X=X,
                                                    Y=Y,
                                                    train_percentage=0.8)

print(f"Length of X: {len(X)}")
print(f"Length of Y: {len(Y)}")

print(f"Length of X_train: {len(X_train)}")
print(f"Length of y_train: {len(y_train)}")
print(f"Length of X_test: {len(X_test)}")
print(f"Length of y_test: {len(y_test)}")

print(X_train)
print(y_train)
print(X_test)
print(y_test)