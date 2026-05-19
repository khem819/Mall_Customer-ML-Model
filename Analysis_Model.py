<<<<<<< HEAD
=======
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import os

import joblib

## Load dataset
df = pd.read_csv("mall_customers.csv")
print(df)

print(df.head())
print(df.shape)
print(df.info())

### Missing values
print(df.isna().sum())

### Duplicate values
print(df.duplicated().sum())

### Statistical summary
print(df.describe())

### Gender count
print(df['Gender'].value_counts())

### Gender percentage
print(df['Gender'].value_counts(normalize=True) * 100)

### Age statistics
print(df['Age'].describe())

os.makedirs("Image",exist_ok=True)

#### KDE Plot for Age Distribution
plt.figure(figsize=(10,6))
sns.kdeplot(df['Age'], fill=True, color='pink')
plt.title('Customer Age Profile')
plt.xlabel('Age')
plt.ylabel('Density')
plt.savefig("Image/KDE_plot_age.png")
plt.show()

### Annual income (k$) statistics
print(df['Annual Income (k$)'].describe())

#### KDE Plot for Annual Income Distribution 
plt.figure(figsize=(10,6))
sns.kdeplot(df['Annual Income (k$)'],fill=True,color='red')
plt.title('Annual Income')
plt.xlabel('Annual')
plt.ylabel('Density')
plt.savefig("Image/KDE_plot_annualincome.png")
plt.show()

### Spending Score(1-100) statistics
print(df['Spending Score (1-100)'].describe())

#### KDE Plot for Spending Score (1-100) Distribution 
plt.figure(figsize=(10,6))
sns.kdeplot(df['Spending Score (1-100)'],fill=True,color='blue')
plt.title('Customer score profile')
plt.xlabel('Spending score')
plt.ylabel('Density')
plt.savefig("Image/KDE_plot_spendingscore.png")
plt.show()


print(df.groupby(['Gender'])['Age'].mean())

### BoxPlot for Age and Gender Distribution
plt.figure(figsize=(10,6))
sns.boxplot(data=df,y='Age',x='Gender',color='violet')
plt.title('Age by gender')
plt.xlabel('Gender')
plt.ylabel('Age')
plt.savefig("Image/Box_plot.png")
plt.show()

### Annual Income Distribution
plt.figure(figsize=(10,6))
plt.hist(df['Annual Income (k$)'], bins=20, color='skyblue')
plt.title('Distribution of Annual Income')
plt.xlabel('Income (k$)')
plt.ylabel('Frequency')
plt.savefig("Image/Annual_distribution.png")
plt.show()


### Spending Level Classification
def spending_level(score):
    if score < 40:
        return "low"
    elif score >= 40 and score < 70:
        return "Medium"
    else:
        return "High"
    
df['Spending_level'] = df['Spending Score (1-100)'].apply(spending_level)


levels = ['low','Medium','High']

for level in levels:
    count = len(df[df['Spending_level'] == level])
    print(level, ":",count)


### features selection
features = ['Gender', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)']
x = df[features].copy()

# Encode Gender
x['Gender'] = x['Gender'].map({'Male': 0, 'Female': 1}).fillna(0)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(x)


wcss = []
for i in range(2, 10):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

####Plot elbow curve
plt.figure(figsize=(10, 6))
plt.plot(range(2, 10), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.savefig("Image/elbow.png")
plt.show()


optimal_clusters = 4  
kmeans_final = KMeans(n_clusters=optimal_clusters, random_state=42)
x['Cluster'] = kmeans_final.fit_predict(X_scaled)


cluster_summary = x.groupby("Cluster").mean()
# print(cluster_summary)

print(x["Cluster"].value_counts())


pca = PCA(n_components=2)
pca_data = pca.fit_transform(X_scaled)
pca_df = pd.DataFrame(pca_data, columns=["PCA1", "PCA2"])
pca_df["Cluster"] = x["Cluster"].values


sns.scatterplot(x="PCA1",y="PCA2",hue="Cluster",data=pca_df,palette="Set1")
plt.title("customer segmentation (PCA)")
plt.savefig("Image/clustering.png")
plt.show()

#### tarin model

joblib.dump(kmeans,"kmeans_model.pkl")
joblib.dump(scaler,"scaler.pkl")

print("=" *60)
print("KMEANS segmentation works sucessfully")
print("=" *60)
>>>>>>> 329ed10 (image add)
