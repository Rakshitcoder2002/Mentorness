# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1A1_EI3axBv3mCjdwVZ5TnbTpGGKinWH4
"""

from google.colab import files
import pandas as pd
uploaded = files.upload()

class FastagFraudDetection:
    def __init__(self, some_parameter):
        self.some_parameter = some_parameter

    def detect_fraud(self):
        pass

for filename in uploaded.keys():
    print(f'Uploaded file: {filename}')
filename = 'FastagFraudDetection.csv'

df = pd.read_csv(filename)
print(df.head())

print(df.isnull().sum())

print(df.describe())

print(df['Fraud_indicator'].value_counts())

import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(x='Fraud_indicator', data=df)
plt.show()

df.hist(bins=50, figsize=(20,15))
plt.show()

from sklearn.preprocessing import LabelEncoder, StandardScaler
df = df.dropna()

categorical_features = ['Vehicle_Type', 'Lane_Type', 'Geographical_Location', 'Vehicle_Plate_Number', 'Vehicle_Dimensions']
for feature in categorical_features:
    le = LabelEncoder()
    df[feature] = le.fit_transform(df[feature])

if 'Timestamp' in df.columns:
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df['Hour'] = df['Timestamp'].dt.hour
    df['Day'] = df['Timestamp'].dt.day
    df['Month'] = df['Timestamp'].dt.month
    df = df.drop(columns=['Timestamp'])

df = df.drop(columns=['Vehicle_Plate_Number'])

print(df.head())

X = df.drop(columns=['Fraud_indicator'])
y = df['Fraud_indicator']

categorical_columns = X.select_dtypes(include=['object']).columns

X_encoded = pd.get_dummies(X, columns=categorical_columns)

smote = SMOTE()
X_resampled, y_resampled = smote.fit_resample(X_encoded, y)

print(y_resampled.value_counts())

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score, roc_curve

X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]

print(classification_report(y_test, y_pred))

from sklearn.metrics import classification_report

from sklearn.metrics import accuracy_score, confusion_matrix

print('Accuracy Score : ' + str(accuracy_score(y_test,y_pred)))
print("Confusion Matrix: \n", confusion_matrix(y_test,y_pred))

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy Score : ", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

np.random.seed(42)
X = np.random.rand(100, 5)
y = np.random.choice([0, 1], 100)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred_prob = model.predict_proba(X_test)[:, 1]


fpr, tpr, _ = roc_curve(y_test, y_pred_prob)
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt


np.random.seed(42)
X = np.random.rand(100, 5)
y = np.random.choice([0, 1], 100)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestClassifier()
model.fit(X_train,y_train)
y_pred_prob = model.predict_proba(X_test)[:, 1]

fpr, tpr, _ = roc_curve(y_test, y_pred_prob)
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()

print("AUC: {:.2f}".format(roc_auc))

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_recall_curve, average_precision_score
import matplotlib.pyplot as plt

np.random.seed(42)
X = np.random.rand(100, 5)
y = np.random.choice([0, 1], 100)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred_prob = model.predict_proba(X_test)[:, 1]

precision, recall, _ = precision_recall_curve(y_test, y_pred_prob)
average_precision = average_precision_score(y_test, y_pred_prob)

plt.figure()
plt.step(recall, precision, color='b', alpha=0.2, where='post')
plt.fill_between(recall, precision, step='post', alpha=0.2, color='b')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.ylim([0.0, 1.05])
plt.xlim([0.0, 1.0])
plt.title('2-class Precision-Recall curve: AP={0:0.2f}'.format(average_precision))
plt.show()

print("Average Precision: {:.2f}".format(average_precision))

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

cm = confusion_matrix(y_test, model.predict(X_test))

disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
disp.plot(cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.show()

importances = model.feature_importances_
indices = np.argsort(importances)[::-1]

plt.figure()
plt.title("Feature Importances")
plt.bar(range(X.shape[1]), importances[indices], align="center")
plt.xticks(range(X.shape[1]), indices)
plt.xlim([-1, X.shape[1]])
plt.show()

from sklearn.calibration import calibration_curve

prob_true, prob_pred = calibration_curve(y_test, y_pred_prob, n_bins=10)

plt.figure()
plt.plot(prob_pred, prob_true, marker='o', label='Model')
plt.plot([0, 1], [0, 1], linestyle='--', label='Perfectly calibrated')
plt.xlabel('Predicted probability')
plt.ylabel('True probability in each bin')
plt.title('Calibration Curve')
plt.legend()
plt.show()

from sklearn.model_selection import cross_val_score

cv_scores = cross_val_score(model, X, y, cv=5, scoring='roc_auc')

print("Cross-Validation AUC Scores: ", cv_scores)
print("Mean AUC Score: ", np.mean(cv_scores))

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
data_size = 1000
df = pd.DataFrame({
    'feature1': np.random.randn(data_size),
    'feature2': np.random.rand(data_size),
    'feature3': np.random.randint(1, 100, data_size),
    'feature4': np.random.choice(['A', 'B', 'C'], data_size),
    'target': np.random.choice([0, 1], data_size)
})

print("Basic Data Information:")
print(df.info())
print("\nDescriptive Statistics:")
print(df.describe(include='all'))

print("\nMissing Values:")
print(df.isnull().sum())

plt.figure(figsize=(10, 6))
sns.boxplot(data=df.select_dtypes(include=[np.number]))
plt.title('Boxplot for Numerical Features')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='feature4', data=df)
plt.title('Distribution of Categorical Feature4')
plt.show()

plt.figure(figsize=(10, 6))
corr_matrix = df.select_dtypes(include=[np.number]).corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

sns.pairplot(df.select_dtypes(include=[np.number]))
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='target', data=df)
plt.title('Target Distribution')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='target', y='feature1', data=df)
plt.title('Feature1 vs Target')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='target', y='feature2', data=df)
plt.title('Feature2 vs Target')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='target', y='feature3', data=df)
plt.title('Feature3 vs Target')
plt.show()

