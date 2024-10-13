# Question 3

import pandas as pd
import matplotlib.pyplot as plt


data = {
    "WDS": [205, 203, 229, 208, 146, 230, 215, 153, 205, 80, 208, 89, 49, 93, 46, 34, 39, 88, 191, 219, 205, 57, 105, 109, 82, 88, 39, 94, 206, 197, 68, 44, 203, 139, 72, 67, 162, 31, 85, 111, 88, 60, 97, 169, 78, 68, 32, 50, 208, 81, 83, 195, 111, 208],
    "SEN": [9, 20, 18, 16, 9, 16, 16, 9, 11, 13, 22, 16, 5, 18, 6, 6, 5, 12, 25, 17, 23, 7, 10, 9, 10, 10, 5, 11, 18, 18, 9, 9, 17, 13, 11, 7, 14, 6, 11, 12, 11, 15, 6, 12, 14, 11, 4, 9, 18, 12, 12, 17, 11, 20],
    "3SYL": [34, 21, 37, 31, 10, 24, 39, 10, 17, 18, 32, 17, 3, 10, 6, 5, 6, 6, 13, 22, 25, 3, 5, 2, 9, 3, 0, 4, 29, 26, 5, 5, 24, 15, 3, 8, 16, 9, 10, 3, 12, 10, 10, 11, 12, 13, 1, 9, 43, 13, 14, 32, 24, 15],
   "GRP": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
}


df = pd.DataFrame(data)

plt.figure(figsize=(10, 8))


plt.subplot(2, 1, 1)
plt.boxplot([df[df["GRP"] == i]["3SYL"] for i in range(1, 4)], labels=["Group 1", "Group 2", "Group 3"])
plt.title("3+ Syllable Wrods")
plt.ylabel("3+ Syllable Words")


plt.subplot(2, 1, 2)
plt.boxplot([df[df["GRP"] == i]["SEN"] for i in range(1, 4)], labels=["Group 1", "Group 2", "Group 3"])
plt.title("Sentences")
plt.ylabel("Sentences")


plt.tight_layout()
plt.show()
