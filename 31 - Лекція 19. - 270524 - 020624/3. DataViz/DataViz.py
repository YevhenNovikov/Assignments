import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")

sns.histplot(data=titanic, x="age", bins=20)

plt.title("Histogram of Passenger Ages")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()