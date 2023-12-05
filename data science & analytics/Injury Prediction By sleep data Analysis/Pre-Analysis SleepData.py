# -*- coding: utf-8 -*-
"""ProjectSleepAnalysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14mOwB9DnCMr2AUtwQFPFarUPH-Tnu4SD

# Task : Pre-Analysis (Sleep Health Analysis of athletes to reduce sports injuries)

StudentID: 222476542(Aman kag)
"""

#We are installing and importing the necessary libraries -
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file -
pathOfFile = '/content/drive/MyDrive/Project/sleep data final.csv'
data = pd.read_csv(pathOfFile)

# Extract systolic blood pressure -
data['Systolic Blood Pressure'] = data['Blood Pressure'].str.split('/').str[0].astype(float)

# Pie Chart for "Injury Risk" Categories -

injury_risk_counts = data['Injury Risk'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(injury_risk_counts, labels=injury_risk_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Injury Risk Categories')
plt.show()

# Histograms for Key Variables -
fig, axes = plt.subplots(3, 2, figsize=(15, 15))
fig.suptitle('Histograms of Key Variables', fontsize=16)

# Histogram for Age -
sns.histplot(data['Age'], bins=30, ax=axes[0, 0], kde=True, color='skyblue')
axes[0, 0].set_title('Age Distribution')

# Histogram for Sleep Duration -
sns.histplot(data['Sleep Duration'], bins=30, ax=axes[0, 1], kde=True, color='lightgreen')
axes[0, 1].set_title('Sleep Duration Distribution')

# Histogram for Physical Activity Level -
sns.histplot(data['Physical Activity Level'], bins=30, ax=axes[1, 0], kde=True, color='salmon')
axes[1, 0].set_title('Physical Activity Level Distribution')

# Histogram for Stress Level -
sns.histplot(data['Stress Level'], bins=30, ax=axes[1, 1], kde=True, color='gold')
axes[1, 1].set_title('Stress Level Distribution')

# Histogram for Heart Rate -
sns.histplot(data['Heart Rate'], bins=30, ax=axes[2, 0], kde=True, color='lightcoral')
axes[2, 0].set_title('Heart Rate Distribution')

# Histogram for Daily Steps -
sns.histplot(data['Daily Steps'], bins=30, ax=axes[2, 1], kde=True, color='orchid')
axes[2, 1].set_title('Daily Steps Distribution')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

# Box Plots for Blood Pressure and Sleep Duration by Injury Risk
plt.figure(figsize=(14, 6))

# Box Plot for Systolic Blood Pressure by Injury Risk
plt.subplot(1, 2, 1)
sns.boxplot(x='Injury Risk', y='Systolic Blood Pressure', data=data)
plt.title('Systolic Blood Pressure by Injury Risk')

# Box Plot for Sleep Duration by Injury Risk
plt.subplot(1, 2, 2)
sns.boxplot(x='Injury Risk', y='Sleep Duration', data=data)
plt.title('Sleep Duration by Injury Risk')

plt.tight_layout()
plt.show()

# Scatter Plots for Age vs. Physical Activity Level and Sleep Duration
plt.figure(figsize=(14, 6))

# Scatter Plot for Age vs. Physical Activity Level
plt.subplot(1, 2, 1)
sns.scatterplot(x='Age', y='Physical Activity Level', hue='Injury Risk', data=data)
plt.title('Age vs. Physical Activity Level')

# Scatter Plot for Age vs. Sleep Duration
plt.subplot(1, 2, 2)
sns.scatterplot(x='Age', y='Sleep Duration', hue='Injury Risk', data=data)
plt.title('Age vs. Sleep Duration')

plt.tight_layout()
plt.show()

# Counting the number of individuals for each age group
age_group_counts = data['Age'].value_counts().sort_index()

# Displaying the count for each age group in the specified format
print("Count of Individuals by Age Group:")
for age, count in age_group_counts.items():
    print(f"Age: {age} - Counts: {count}")