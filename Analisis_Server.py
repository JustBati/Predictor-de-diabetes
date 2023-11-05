import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression

def cargar_data():
    df = pd.read_csv("./Data/diabetes_binary_health_indicators_BRFSS2015.csv")
    return df

def limpieza(df):
    df.drop_duplicates(inplace=True)
    df['Diabetes'] = df['Diabetes_binary']
    df.drop(columns = 'Diabetes_binary', inplace=True)
    df = df.astype('int32')
    return df

def train(df):
    X_train, X_test, y_train, y_test = train_test_split(df.drop('Diabetes', axis=1), df['Diabetes'], test_size=0.4, random_state=42)
    lr = LogisticRegression(solver='saga').fit(X_train, y_train)
    return lr

def  get_sample():
   # column_names = ["HighBP", "HighChol", "CholCheck", "BMI", "Smoker", "Stroke", "HeartDiseaseorAttack", "PhysActivity", "Fruits", "Veggies", "HvyAlcoholConsump", "AnyHealthcare", "NoDocbcCost", "GenHlth", "MentHlth", "PhysHlth", "DiffWalk", "Sex", "Age", "Education", "Income"]
    sample= pd.read_csv("./Data/Sample.csv")
    return sample

def clasify_sample(sample, lr):
    answer = lr.predict(sample)
    return answer

def save_sample(sample):
    sample = pd.DataFrame(sample, columns=['Resultados'])
    sample.to_csv("./Data/Answer.csv", index=False)

def Step1():
    df = cargar_data()
    df = limpieza(df)
    lr = train(df)
    return lr

def Step2(lr):
    sample = get_sample()
    answer = clasify_sample(sample, lr)
    save_sample(answer)
