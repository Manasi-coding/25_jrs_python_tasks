import random
import numpy as np
import pandas as pd
# Numpy

# Q1: Given a 2D NumPy array A of shape (5, 5), subtract the mean of each row from every element in that row without using a loop.
a=np.random.randint(0,11,(5,5))
print("Original array:\n",a)
row_mean = a.mean(axis=1,keepdims=True)
b=a-row_mean
print("Final array:\n",b)
print("\n\n")

# Q2: You have a NumPy array of integers from 1 to 1000. Return a new array containing only the numbers that are divisible by both 3 and 7 but not by 5.
c=np.arange(0,1001)
print("Original array:\n",a)
div_21=np.arange(21,1001,21)
final=[]
for i in div_21:
    if(i%5!=0):
        final.append(i)
final_2=np.array(final)
print(final_2)
print("\n\n")

# Q3: Create an 8x8 NumPy array with a chessboard pattern (alternating 0s and 1s), where the top-left element is 0.
d=np.zeros((8,8),dtype=int)
d[1:8:2, 0:8:2]=1
d[0:8:2, 1:8:2]=1
print(d)
print("\n\n")

# Pandas (Create a DataFrame with the specified columns and perform the operations)

# Q1: Given a DataFrame df with columns: ["department", "employee", "salary"],  normalize the salary within each department (i.e., for each department, subtract the mean and divide by the std of that department).
data_1 = {
    "department": ["IT", "IT", "HR", "HR", "SALES", "SALES"],
    "employee": ['A', 'B', 'C', 'D', 'E', 'F'],
    "salary": [25, 50, 75, 100, 125, 150]
}
df_1 = pd.DataFrame(data_1)
mean_sal = df_1.groupby("department")["salary"].mean()
std_sal = df_1.groupby("department")["salary"].std()
normalized = []
for i in range(len(df_1)):
    dept = df_1.loc[i, "department"]
    sal = df_1.loc[i, "salary"]
    norm = (sal - mean_sal[dept]) / std_sal[dept]
    normalized.append(norm)

df_1["norm"] = normalized
print(df_1)

# Q2: Given a DataFrame with columns ["timestamp", "user_id", "action"], where timestamp is in string format, find the average number of actions per user per day.
data_2 = {
    "timestamp" : ["2025-07-03", "2025-07-03", "2025-07-03", "2025-07-02", "2025-07-02", "2025-07-02"],
    "user_id" : [1, 1, 2, 2, 2, 1],
    "action" : ["CLICK","VIEW","VIEW","CLICK","CLICK", "CLICK"]
}
df_2 = pd.DataFrame(data_2)
count = df_2.groupby(["user_id","timestamp"]).size().reset_index(name="count")
avg = count.groupby("user_id")["count"].mean().reset_index(name="average")
print(avg)

# Q3: You have a DataFrame with columns: ["user_id", "product", "price", "quantity", "date"]. Calculate the total amount spent by each user on "Laptop" purchases only, and return the result as a new DataFrame with columns: ["user_id", "total_spent_on_laptops"].
data_3 = {
    "user_id" : [1,1,2,2,3,3],
    "product" : ["Laptop","Keyboard","Mouse","Laptop","Laptop","Printer"],
    "price" : [100,75,50,200,150,80],
    "quantity" : [1,2,1,2,1,1],
    "date" : ["2025-07-03", "2025-07-03", "2025-07-03", "2025-07-02", "2025-07-02", "2025-07-02"]
}
df_3 = pd.DataFrame(data_3)
lp_df = df_3[df_3["product"]=="Laptop"]
lp_df["amount"] = lp_df["price"]*lp_df["quantity"]
total = lp_df.groupby("user_id")["amount"].sum().reset_index(name="total_spent_on_laptops")
print(total)