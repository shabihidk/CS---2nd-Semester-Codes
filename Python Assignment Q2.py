# QUESTION 2
import pandas as pd
import matplotlib.pyplot as plt


mydataset2 = {
    "Type": [
        "Beef", "Beef", "Beef", "Beef", "Beef", "Beef", "Beef", "Beef", "Beef", "Beef", "Beef", "Beef", "Beef", "Beef", "Beef", "Beef", "Beef", "Beef", "Beef", "Beef",
        "Meat", "Meat", "Meat", "Meat", "Meat", "Meat", "Meat", "Meat", "Meat", "Meat", "Meat", "Meat", "Meat", "Meat", "Meat", "Meat", "Meat", "Meat", "Meat", "Meat",
        "Poultry", "Poultry", "Poultry", "Poultry", "Poultry", "Poultry", "Poultry", "Poultry", "Poultry", "Poultry", "Poultry", "Poultry", "Poultry", "Poultry"
    ],
    "Calories": [
        186, 181, 176, 149, 194, 190, 181, 139, 175, 148, 152, 111, 141, 153, 189, 157, 131, 149, 135, 122, 173, 191, 184, 190, 172, 147, 146, 139, 175, 136,
        179, 153, 197, 195, 135, 140, 189, 122, 102, 129, 129, 132, 102, 196, 94, 102, 87, 99, 197, 113, 142, 86, 143, 144
    ],

    "Sodium": [
        495, 477, 425, 322, 482, 587, 370, 322, 479, 375, 338, 300, 395, 481, 645, 449, 317, 319, 298, 253,
        458, 596, 473, 545, 496, 360, 387, 386, 597, 393, 485, 372, 144, 511, 485, 428, 339, 375, 396, 430,
        438, 375, 396, 383, 387, 342, 359, 357, 528, 513, 426, 358, 581, 522
    ]
}


df = pd.DataFrame(mydataset2)

beef_c = df[df["Type"] == "Beef"]["Calories"]
meat_c = df[df["Type"] == "Meat"]["Calories"]
poultry_c = df[df["Type"] == "Poultry"]["Calories"]

beef_s = df[df["Type"] == "Beef"]["Sodium"]
meat_s= df[df["Type"] == "Meat"]["Sodium"]
poultry_s = df[df["Type"] == "Poultry"]["Sodium"]


fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))


# DISTRIBUTION COLORS FOR BOTH CHARTS
#  RED FOR BEEF
#  BLUE FOR MEAT
#  GREEN FOR POULTRY


ax1.hist(beef_c, bins=10, alpha=0.5, label = 'beef', color='red')
ax1.hist(meat_c, bins=10, alpha=0.5, label = 'meat', color='blue')
ax1.hist(poultry_c, bins=10, alpha=0.5, label = 'poultry', color='green')
ax1.set_xlabel('Calories')
ax1.set_ylabel('Frequency')
ax1.set_title('Calories')
ax1.legend(loc='upper right')

ax2.hist(beef_s, bins=10, alpha=0.5, label= 'beef', color='red')
ax2.hist(meat_s, bins=10, alpha=0.5, label=  'meat', color='blue')
ax2.hist(poultry_s, bins=10, alpha=0.5, label= 'poultry', color='green')

ax2.set_xlabel('Sodium')
ax2.set_ylabel('Frequency')
ax2.set_title('Sodium Count')
ax2.legend(loc='upper right')


plt.tight_layout()


plt.show()