🛍️ Mall Customers Segmentation (K-Means Clustering)

📌 Project Overview

This project applies Unsupervised Machine Learning (K-Means Clustering) to segment mall customers based on their Age, Annual Income, and Spending Score.
The goal is to help businesses understand customer groups and improve marketing strategies.

🎯 Problem Statement

Retail businesses want to identify different types of customers to:
Improve targeted marketing
Increase customer engagement
Optimize sales strategies

We use K-Means Clustering to group customers into meaningful segments.




 ************* see model in dashboard ********************
 python -m streamlit run app.py



📊 Dataset Information

The dataset contains:
🧑 Customer ID
⚧ Gender
🎂 Age
💰 Annual Income (k$)
🛒 Spending Score (1–100)

🧠 Machine Learning Workflow

1️⃣ Data Preprocessing
Checked missing values and duplicates
Encoded categorical feature (Gender)
Standardized features using StandardScaler

2️⃣ Exploratory Data Analysis (EDA)
Age distribution analysis
Income distribution visualization
Spending score analysis
Gender-based comparisons

3️⃣ Feature Engineering
Created additional feature:
Spending Level (Low / Medium / High)

4️⃣ Clustering Model
Used K-Means Algorithm
Optimal clusters found using Elbow Method
Final model trained with best K value

5️⃣ Dimensionality Reduction
Applied PCA (Principal Component Analysis)
Visualized customer clusters in 2D space

📈 Elbow Method

Used to determine optimal number of clusters by plotting WCSS (Within Cluster Sum of Squares).

📊 Customer Segments Identified

The model groups customers into different segments such as:
🟢 Low Income – Low Spending Customers
🔵 High Income – High Spending Customers
🟡 Moderate Customers
🔴 Target Premium Customers

🛠️ Technologies Used

Python 🐍
Pandas & NumPy
Matplotlib & Seaborn 📊
Scikit-learn 🤖
PCA (Dimensionality Reduction)
Joblib (Model Saving)

👨‍💻 Author
Khem  Raj Bhatta
