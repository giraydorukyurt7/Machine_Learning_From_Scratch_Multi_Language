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
#Turn into integer float lists
X = [float(x) for x in X]
Y = [float(y) for y in Y]



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

#print(X_train)
#print(y_train)
#print(X_test)
#print(y_test)

# y= mx+b

def find_m(X,Y):
    n = len(X)
    #sigma_xi_times_yi = 0
    #for i in range(n): #0,n-1
    #    xi_times_yi = X[i]*Y[i]
    #    sigma_xi_times_yi+=xi_times_yi
    
    #Find mean_X and mean_Y
    total_X = 0
    total_Y = 0
    for x in X:
        total_X+=x
    for y in Y:
        total_Y+=y
    mean_X = total_X/len(X)
    mean_Y = total_Y/len(Y)

    sigma_xi_minus_mean_X__times__yi_minus_mean_Y = 0
    for i in range(n): #0,n-1
        sigma_xi_minus_mean_X__times__yi_minus_mean_Y = (X[i]-mean_X)*(Y[i]-mean_Y)
    sigma_xi_minus_mean_X_squared = 0
    for i in range(n):
        sigma_xi_minus_mean_X = (X[i]*mean_X)**2
    
    m = sigma_xi_minus_mean_X__times__yi_minus_mean_Y /sigma_xi_minus_mean_X

    b = mean_Y-m*mean_X

    return m,b
#print(type(X_train))
#print(type(y_train))
#
#print(type(X_train[5]))

#print(any(not isinstance(x, (int, float)) for x in X_train))  # Check for non-numeric types
#print(any(not isinstance(y, (int, float)) for y in y_train))

m,b = find_m(X=X_train, Y=y_train)

print(m)
print(b)