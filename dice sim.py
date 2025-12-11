import random as r

c1,c2,c3,c4,c5,c6 = 0,0,0,0,0,0
n = int(input("Enter the no. of times you want to roll the dice : "))

for i in range(n):

    #generating a random number
    rn = r.randint(1,6)

    #updating frequency
    if rn == 1:
        c1 += 1
    elif rn == 2:
        c2 += 1
    elif rn == 3:
        c3 += 1
    elif rn == 4:
        c4 += 1
    elif rn == 5:
        c5 += 1
    elif rn == 6:
        c6 += 1

print("Ideal frequency :", n//6)
print("Digit | Frequency")
print("1     | ", c1, "\n", "2     | ", c2, "\n", "3     | ", c3, "\n", "4     | ", c4, "\n", "5     | ", c5, "\n","6     | ", c6 ,sep = "")

#plotting part
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5, 6]
y = [c1, c2, c3, c4, c5, c6]

# Create the plot
plt.plot(x, y)

# Customize the plot

plt.plot(x, y, label="Actual Frequency")
plt.axhline(y=n//6, color='r', linestyle='--', label="Ideal Frequency")

plt.title("Dice rolling simulation")
plt.xlabel("Dice value")
plt.ylabel(f"Frequency (Ideal : {n//6})")
plt.grid(True)
plt.legend()

# Display the plot
plt.show()