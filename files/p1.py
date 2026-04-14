# # Write a Python program to:

# # Accept 10 temperature readings from the user. Store them in a file called temperature.txt. Read the file and calculate the average and max temperature.

# temperatures = []
# for i in range(10):
#     temp = float(input(f"Enter temperature {i+1}: "))
#     temperatures.append(temp)

# with open("temperature.txt", "w") as f:
#     for temp in temperatures:
#         f.write(str(temp) + "\n")

# with open("temperature.txt", "r") as f:
#     temps = [float(line.strip()) for line in f]

# average = sum(temps) / len(temps)
# max_temp = max(temps)

# print(f"Average temperature: {average}")
# print(f"Maximum temperature: {max_temp}")

# //Read the file created in Exercise-1. Write a program to count how many temperature readings are above 30°C.
with open("temperature.txt", "r") as f:
    temps = [float(line.strip()) for line in f] 
count_above_30 = sum(1 for temp in temps if temp > 30)
print(f"Number of temperature readings above 30°C: {count_above_30}")   