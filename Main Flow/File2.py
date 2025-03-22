import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'student-mat.csv'  # Update the path if necessary
data = pd.read_csv(file_path, delimiter=';')

# 1. Histogram of Final Grades (G3)
plt.figure()
plt.hist(data['G3'], bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram of Final Grades (G3)')
plt.xlabel('Final Grade (G3)')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# 2. Scatter Plot between Study Time and Final Grade (G3)
plt.figure()
sns.scatterplot(x='studytime', y='G3', data=data, hue='sex', palette='Set2')
plt.title('Study Time vs Final Grade (G3)')
plt.xlabel('Study Time (hours per week)')
plt.ylabel('Final Grade (G3)')
plt.grid(alpha=0.5)
plt.show()

# 3. Bar Chart Comparing Average Scores of Male and Female Students
average_scores_by_gender = data.groupby('sex')['G3'].mean()
plt.figure()
average_scores_by_gender.plot(kind='bar', color=['blue', 'pink'])
plt.title('Average Final Grade (G3) by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Final Grade (G3)')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
