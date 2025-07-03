**Classification and Prediction of Bipolar Disorder using Machine Learning**

**Overview**

This project explores the use of machine learning algorithms to classify and predict the states of patients with Bipolar Disorder using symptom-based patient data. The primary objective is to assist psychiatrists in early identification of depressive, manic, or euthymic episodes—enabling timely intervention and better management of the disorder.

**Table of Contents**

- [Introduction](#introduction)
- [Project Workflow](#project-workflow)
- [Data](#data)
- [Technologies Used](#technologies-used)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Machine Learning Models](#machine-learning-models)
- [Results](#results)
- [Deployment](#deployment)
- [Conclusion & Future Work](#conclusion--future-work)
- [References](#references)

**Introduction**

Bipolar disorder is a mental health condition characterized by extreme mood swings. Timely and accurate episode prediction can drastically improve patient outcomes. This project utilizes machine learning algorithms on real-world patient data to build predictive models that can aid clinicians in diagnosis and monitoring.

**Project Workflow**

1. **Data Gathering**: Collecting anonymized patient data from psychiatrists (multiple Excel sheets covering episodes, clinical scales, interviews, and interventions).
2. **Data Cleaning & Preprocessing**: Removing inconsistencies, handling missing values, standardizing formats.
3. **Exploratory Data Analysis (EDA)**: Visualizing and analyzing feature distributions, outliers, and correlations.
4. **Model Building**: Training and evaluating multiple classification models.
5. **Model Evaluation**: Comparing performance and selecting the best model(s).
6. **Deployment**: Exposing the model as a web service using Flask.

**Data**

The project uses multiple datasets derived from real psychiatric assessments:

- **Episodes**: States of patients (Depression, Mania, Euthymic) over time.
- **YMRS (Young Mania Rating Scale)**: Assesses manic symptoms.
- **HDRS (Hamilton Depression Rating Scale)**: Measures depression symptoms.
- **Interviews**: Subjective and objective patient data (mood, motivation, anxiety, irritability, sleep, substance use, etc.).
- **Interventions**: Records of clinical interventions and patient functioning.

Data is anonymized and originally collected in Excel files, later converted to CSV for analysis.

**Technologies Used**

- **Python 3.7+**: Core programming language
- **Jupyter Notebook**: For interactive prototyping and analysis
- **Pandas, NumPy**: Data manipulation
- **Matplotlib, Seaborn**: Data visualization
- **Scikit-learn**: Machine learning algorithms (Decision Tree, Random Forest, SVM, Logistic Regression)
- **Flask**: Deployment as a REST API (for predictions)
- **Heroku**: Optional deployment platform for the Flask app

**Exploratory Data Analysis**

- **Histograms & Boxplots**: Analyzed feature distributions and detected outliers.
- **Heatmaps**: Examined feature correlations (e.g., mood vs. motivation, depressed mood vs. work).
- **Scatterplots, Marginal plots, 2D density plots**: Explored relationships between important features.
- **Outlier Correction**: Detected and fixed outliers (e.g., unrealistic caffeine/cigarette consumption).

Findings from EDA helped select relevant features and informed model selection.

**Machine Learning Models**

**Algorithms Applied:**

- **Decision Tree**
- **Random Forest**
- **Support Vector Machine (SVM)**
- **Logistic Regression**

**Process:**

- Data split into training and test sets (typically 70/30).
- Evaluated models on multiple datasets (episodes, interviews, interventions).
- Hyperparameters tuned based on data size and structure.
- Compared accuracy and interpretability.

**Key Insights:**

- **Interview dataset** provided the most reliable predictions (up to 76% accuracy with Random Forest).
- **Random Forest** outperformed other algorithms on average.

**Results**

- **Best Model:** Random Forest on Interview data (accuracy: **76%**)
- **Other Models:** Decision Tree, SVM, Logistic Regression performed reasonably but less accurately
- **Model Reasoning:** Analyzed and visualized decision splits for interpretability
- **Real Data Tests:** Predictions generally aligned with clinical expectations

**Accuracy Summary Table:**

| **Dataset** | **Decision Tree** | **Random Forest** | **SVM** | **Logistic Regression** |
| --- | --- | --- | --- | --- |
| YMRS | 36% | 54% | 45% | 45% |
| HDRS | 63% | 54% | 45% | 45% |
| Interview | 74% | **76%** | 70% | 69% |
| Intervention | 55% | 61% | 66% | 40% |

**Deployment**

The final model is deployed as a web service using **Flask**. Clinicians (or patients) can enter new data and receive instant predictions of the patient’s state.

**Why Flask?**

- Lightweight and easy to set up
- Good for prototyping ML APIs
- Can be deployed to cloud platforms (e.g., Heroku)

**Conclusion & Future Work**

- **Conclusion**: This project demonstrates the feasibility of using symptom-based machine learning models to support early detection of bipolar episodes. With real-world data, Random Forest proved most effective.
- **Future Work**:
  - Extend to larger, more diverse datasets for improved generalization
  - Integrate automated reporting to send results directly to clinicians
  - Explore treatment/drug prediction based on predicted state
  - Enhance the cloud-based deployment for broader accessibility

**References**

A full bibliography is included in the project report, covering foundational works in bipolar disorder research, machine learning in psychiatry, and algorithm theory.

**Acknowledgements**

- Psychiatrists and medical staff for anonymized data
- Open-source Python and ML communities
