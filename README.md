# Investigating the Predictability of Heart Attacks through ML ❤️

## Project Overview 📊
This project aims to develop a machine learning model to predict the risk of heart attacks, thereby enhancing preventive healthcare strategies. Utilizing individual health data from Kaggle, the model focuses on early and accurate detection of risk factors, aiming to improve patient outcomes and reduce the burden of heart disease on health systems globally.

## Data Source 📁
The data used in this project was sourced from Kaggle. It includes personal key indicators of heart disease, which are essential for developing our predictive model. You can view and download the dataset [here](https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease).

## Objective 🎯
Develop a predictive model to accurately estimate the risk of heart attacks and support preventive healthcare measures.

## Features and Innovation 🌟
* **Global Impact**: Heart disease is the leading cause of death worldwide.
* **Innovation**: Focuses on the early and accurate detection of cardiovascular risk factors.
* **Potential Benefits**:
  * Improve patient outcomes through early intervention.
  * Reduce the overall healthcare burden by managing heart disease more effectively.

## Model Selection 🔍
### XGBoost (Extreme Gradient Boosting)
* **Why Chosen**:
  * Highly effective for binary classification tasks.
  * Capable of managing large datasets with excellent accuracy.
  * Robust against overfitting, particularly useful in unbalanced data scenarios.

## Key Features and Their Importance 📈

## Key Features and Their Importance 📈

Based on evidence from research and the feature importance derived from our model, the following are key predictors of heart attacks:

* **Had Angina**: Angina pectoris (chest pain) is a symptom of coronary artery disease, which often precedes heart attacks.
* **Physical Health Days**: The number of days with poor physical health can indicate underlying issues, including those related to the heart.
* **Physical Activities**:Regular activity helps protect against heart disease.
* **Had Stroke**: Previous stroke events are linked to an increased risk of heart attacks due to shared risk factors like hypertension and atherosclerosis.
* **BMI (Body Mass Index)**: High BMI is indicative of greater cardiovascular strain.
* **Smoking Status**: A known risk factor for various heart diseases.
* **Diabetes (0.25 Importance Score)**: A significant risk factor for heart disease.

To determine these key features, a RandomForestClassifier was trained on the dataset. The model's feature importance scores revealed which variables had the most influence on predicting heart attacks. The most significant features, as listed above, align with known medical research on heart disease risk factors.

The following chart visualizes the feature importance as determined by the RandomForestClassifier:

![Key Features](https://github.com/Asal-zou/Predicting-Heart-Attacks-with-ML/assets/134029102/21b329b6-e1ec-4a6b-a07a-95b3593429b4)

The visual representation of feature importance shows some differences from the online evidence but still effectively highlights the significant predictors for heart attacks.


## Model Performance 🚀
* **ROC**: 0.97
* **True Positive Rate**: 0.84
* **Importance of True Positive Rate**: In the context of imbalanced data, it is crucial to detect as many true positives as possible (i.e., correctly predicting those who may have a heart attack). This focus helps minimize the risk of falsely predicting that someone will not have a heart attack when they actually will.
  
![ROC curve](https://github.com/Asal-zou/Predicting-Heart-Attacks-with-ML/assets/134029102/073f39d4-2cde-4ff5-af84-f06a84639fb8)

### Youden's J Statistic 📊
* **Youden's J statistic** is a `single number` calculated from a `point on the ROC curve`. It is defined as `J = sensitivity + specificity - 1`, simplifying to `J = true positive rate - false positive rate`.
* This statistic provides a method to **identify the optimal threshold**: the `point on the ROC curve that maximizes the J statistic is considered the best trade-off` between `true positives` and `false positives` for a given classifier. It effectively maximizes the classifier's performance in terms of both sensitivity and specificity.
* **Optimal Threshold Used**: 0.07548561

**Note**: My model worked super well, and I used precision to ensure no data leakage from the test data. However, the exceptional performance makes me concerned about potential unnoticed mistakes or the possibility that the data I had was exceptionally good.

**Observation**: When deploying the model, I noticed that some features did not change the percentage of likelihood of having a heart attack, and I'm not sure why. This warrants further investigation to understand the underlying cause.

## Challenges and Solutions 🛠️
* **Imbalanced Data**: Utilized SMOTE and specialized sampling techniques to address the imbalance in medical datasets.
  
![Proportion of HadHeartAttack](https://github.com/Asal-zou/Predicting-Heart-Attacks-with-ML/assets/134029102/f504f600-960c-45eb-b569-4d879b5adf8c)

## Data Handling Techniques 🗂️
* **Handling Nulls**: Used KNN for imputation of missing values in columns like "SmokerStatus", "GeneralHealth", and "AgeCategory".
* **Data Scaling**: Applied scaling techniques to normalize the data for better model performance.

## Data Preprocessing 🔄
### Binary Encoding
Transformed the following columns from Yes/No to 0/1:
* HadHeartAttack
* HadAngina
* PhysicalActivities
* HadStroke
* HadDiabetes
* HadDepressiveDisorder
* HadCOPD
* HadKidneyDisease
* HadArthritis

### One-Hot Encoding
Applied one-hot encoding to the `RaceEthnicityCategory` to convert categorical data into a format that could be fed into the model to improve prediction accuracy.

### Encoding General Health Status
Manually encoded general columns like Health Status for quantitative analysis:
* **Excellent**: 0
* **Very Good**: 1
* **Good**: 2
* **Fair**: 3
* **Poor**: 4

## Future Work 🔮
* **Adding More Features**: Continuously exploring the addition of relevant features that could improve the model’s predictive accuracy and robustness.
* **Data Integration**: Evaluating opportunities to link with additional datasets, such as hospital records or geographic health data, to enrich the model's understanding and predictive capabilities.

## Deployment 🚀
* **Application**: Deployed via a Streamlit application for real-time risk assessment.
* **Access**: [Prediction Tool](http://localhost:8501/Prediction_Tool)
