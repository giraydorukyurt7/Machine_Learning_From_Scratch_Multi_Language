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

file_path = "Datasets/simple_housing_data.csv"

dataset = read_data(file_path)

X = []
Y = []

for i in range(len(dataset)):
    X.append(dataset[i][0])
for i in range(len(dataset)):
    Y.append(dataset[i][1])
#Turn into strings into float in lists
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
        print("Lengths are unequal!")

X_train, y_train, X_test, y_test = test_train_split(X=X,
                                                    Y=Y,
                                                    train_percentage=0.8)

print(f"Length of X: {len(X)}")
print(f"Length of Y: {len(Y)}")

print(f"Length of X_train: {len(X_train)}")
print(f"Length of y_train: {len(y_train)}")
print(f"Length of X_test: {len(X_test)}")
print(f"Length of y_test: {len(y_test)}")

# y= mx+b

def find_m_b(X,Y):
    n = len(X)
    #Find mean_X and mean_Y
    total_X = 0
    total_Y = 0
    for x in X:
        total_X+=x
    for y in Y:
        total_Y+=y
    mean_X = total_X/n
    mean_Y = total_Y/n

    sigma_xi_minus_mean_X__times__yi_minus_mean_Y = 0
    for i in range(n): #0,n-1
        sigma_xi_minus_mean_X__times__yi_minus_mean_Y += (X[i]-mean_X)*(Y[i]-mean_Y)
    sigma_xi_minus_mean_X_squared = 0
    for i in range(n):
        sigma_xi_minus_mean_X_squared+= (X[i]-mean_X)**2
    
    m = sigma_xi_minus_mean_X__times__yi_minus_mean_Y /sigma_xi_minus_mean_X_squared
    b = mean_Y-m*mean_X

    return m,b

m,b = find_m_b(X=X_train, Y=y_train)

print("m: ", m)
print("b: ", b)
print("y=mx+b")
print(f"{m}*x+{b}")

def predict(X_test, m,b):
    y_pred = []
    for x in X_test:
        y_pred.append(m*x+b)
    return y_pred

y_pred = predict(X_test=X_test,
                 m=m,
                 b=b)

def mse(Y_test, y_pred):
    mse = 0
    y_total = 0
    y_testi_minus_y_predi_squared=0
    n = len(Y_test)
    if(n == len(y_pred)):
        for i in range(n):
            y_total += Y_test[i]
            y_testi_minus_y_predi_squared += ((Y_test[i]-y_pred[i])**2)
        mse = y_testi_minus_y_predi_squared/n
        rmse = mse**(1/2)
        y_mean = y_total/n
        rmse_percentage = (rmse/y_mean)*100
        return mse, rmse, rmse_percentage
    else:
        print("Lengths are unequal!")
        return None, None, None

MSE,RMSE, RMSE_Percentage = mse(Y_test=y_test,
                                y_pred=y_pred)

print(f"MSE    : {MSE}")
print(f"RMSE   : {RMSE}")
print(f"RMSE % : {RMSE_Percentage}")