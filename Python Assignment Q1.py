# PROGRAMMING TASKS
# QUESTION 5
import numpy as np
import matplotlib.pyplot as plt


cost = np.array([345.39, 460.05, 452.99, 443.22, 652.23, 642.23, 272.37, 317.21, 457.12, 690.19,
                 350.63, 402.59, 412.18, 495.56, 394.36, 423.32, 712.27, 289.66, 881.24, 490.88,
                 567.79, 665.99, 621.45, 608.80, 473.64, 697.14, 207.51, 288.48, 284.88, 280.36,
                 217.38, 270.71])

mwatts = np.array([514, 687, 1065, 1065, 1065, 1065, 822, 457, 822, 792,
                   560, 790, 530, 1050, 850, 778, 845, 530, 1209, 1050,
                   913, 828, 786, 821, 538, 1130, 745, 821, 886, 886,
                   745, 886])

sorted_cost = np.sort(cost)
sorted_mw = np.sort(mwatts)

#  OUTLIER CHECKING
n1 = len(sorted_cost)
n2 = len(sorted_mw)

#q1
Q1_cost = sorted_cost[int(0.25 * n1)]
Q1_mw = sorted_mw[int(0.25 * n2)]

#q3
Q3_cost = sorted_cost[int(0.75 * n1)]
Q3_mw = sorted_mw[int(0.75 * n2)]

#iqr
IQR_cost = Q3_cost - Q1_cost
IQR_mw = Q3_mw - Q1_mw

#lower n upper bound defined
lower_bound_cost = Q1_cost - (1.5 * IQR_cost)
upper_bound_cost = Q3_cost + (1.5 * IQR_cost)

lower_bound_mw = Q1_mw - (1.5 * IQR_mw)
upper_bound_mw = Q3_mw + (1.5 * IQR_mw)

#outliers
outliers_cost = []
outliers_mw = []

for value in cost:
    if value < lower_bound_cost or value > upper_bound_cost:
        outliers_cost.append(value)

for value in mwatts:
    if value < lower_bound_mw or value > upper_bound_mw:
        outliers_mw.append(value)

#filtering data
filtered_cost = [x for x in cost if x not in outliers_cost]
filtered_mw = [y for y in mwatts if y not in outliers_mw]

#mean n std for cost
mean_cost = np.mean(filtered_cost)
std_cost = np.std(filtered_cost)


filtered_cost = np.array(filtered_cost)
filtered_mw = np.array(filtered_mw)

cost_per_mw = filtered_cost / filtered_mw

# mean n std for mean n std
mean_cost_per_mw = np.mean(cost_per_mw)
std_cost_per_mw = np.std(cost_per_mw)

if len(outliers_cost) == 0:
  print("No Outliers in Cost")
else:
  print("Outliers in Cost", outliers_cost)

if len(outliers_mw) == 0:
  print("No Outliers in MegaWatts")
else:
  print("Outliers in MegaWatts", outliers_cost)

print("Mean Cost: $", f"{mean_cost:.4g}")
print("Standard Deviation of Cost: $", f"{std_cost:.4g}")
print("Mean of Cost Per Megawatt: $", f"{mean_cost_per_mw:.4g}")
print("Standard Deviation of Cost Per Megawatt: $", f"{std_cost_per_mw:.4g}")



plt.hist(cost_per_mw, bins=10, color='blue', edgecolor='black')
plt.xlabel('Cost per Megawatt ($100,000)')
plt.ylabel('Frequency')
plt.title('Histogram of Cost per Megawatt')

plt.show()
