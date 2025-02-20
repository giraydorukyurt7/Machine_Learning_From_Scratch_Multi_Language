def read_data(dir):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

#print(read_data("../../Datasets/simple_housing_data.csv"))

#print(read_data("test.txt"))
#f = open("test.txt","r")
#print(f.read())

file_path = "Datasets/simple_housing_data.csv"



print(read_data(file_path))