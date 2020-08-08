data = [12,45,67,78,3,5,76,34,234,56,78,34,56,76,2,45]

# without lambda
data_10 = []
for i in data:
    data_10.append(i + 10)


# with lambda
updated_data =  list(map(lambda x: x + 10, data))

print(data_10)
print(updated_data)