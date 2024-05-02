# -*- coding: utf-8 -*-
"""Copia de Proyecto M7. Técnicas avanzadas

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1t4OYVPp2sAxgQDPUXai0GckIfhmRNpXC

## **Bootcamp: Ciencia de Datos e Inteligencia Artificial**
## **Proyecto del Módulo 7: Técnicas avanzadas para ciencia de datos y empleabilidad**

Hola, ya es el último proyecto, has avanzado y aprendido mucho hasta acá. ¡Muchas felicidades!

Es hora de poner en práctica todo lo que hemos aprendido a lo largo de nuestra travesía.

Lee el proyecto y revisa con cuidado cada una de las instrucciones. Procura plasmar todo tu potencial para que lo concluyas de manera sobresaliente.

¡Éxito!

# Objetivos
- Aplicar con éxito todos los conocimientos que has adquirido a lo largo del Bootcamp.
- Consolidar las técnicas de limpieza, entrenamiento, graficación y ajuste a modelos de *Machine Learning*.
- Generar una API que brinde predicciones como resultado a partir de datos enviados.

# Proyecto

1. Selecciona uno de los siguientes *datasets*:
  - *Reviews* de aplicaciones de la Google Play Store: https://www.kaggle.com/datasets/lava18/google-play-store-apps
  - Estadísticas demográficas de los ganadores del premio Oscar de la Academia: https://www.kaggle.com/datasets/fmejia21/demographics-of-academy-awards-oscars-winners
  - Aspiraciones profesionales de la generación Z: https://www.kaggle.com/datasets/kulturehire/understanding-career-aspirations-of-genz

Cada uno representa un *dataset*, un problema y una forma diferente de abordarlo. Tu tarea es identificar las técnicas y modelos que podrías usar para tu proyecto.

2. Debes hacer un análisis exploratorio y limpieza de los datos. Usa las ténicas que creas convenientes.

3. Entrena el modelo de *Machine Learning*, procesamiento de lenguaje natural o red neuronal que creas adecuado.

4. Genera por lo menos dos gráficas y dos métricas de rendimiento; explica las puntuaciones de rendimiento que amerite tu problema. Todas las gráficas de rendimiento que realices deben tener leyendas, colores y títulos personalizados por ti.

  - Además, antes de subir el modelo a "producción", deberás realizar un proceso de ensambles (*ensemblings*) y de ajuste de hiperparámetros o *tuning* para intentar mejorar la precisión y disminuir la varianza de tu modelo.

5. Construye una API REST en la que cualquier usuario pueda mandar datos y que esta misma devuelva la predicción del modelo que has hecho. La API debe estar en la nube, ya sea en un servicio como Netlify o Ngrok, para que pueda ser consultada desde internet.

6. Genera una presentación del problema y del modelo de solución que planteas. Muestra gráficas, datos de rendimiento y explicaciones. Esta presentación debe estar enfocada a personas que no sepan mucho de ciencia de datos e inteligencia artificial.

7. **Solamente se recibirán trabajos subidos a tu cuenta de GitHub con un README.md apropiado que explique tu proyecto**.

## Criterios de evaluación

| Actividad | Porcentaje | Observaciones | Punto parcial
| -- | -- | -- | -- |
| Actividad 1. Limpieza y EDA | 20 | Realiza todas las tareas necesarias para hacer el EDA y la limpieza correcta, dependiendo de la problemática. Debes hacer como mínimo el análisis de completitud, escalamiento (si aplica) y tokenización (si aplica). | Realizaste solo algunas tareas de exploración y limpieza y el modelo se muestra aún con oportunidad de completitud, escalamiento y/o mejora. |
| Actividad 2. Entrenamiento del modelo | 20 | Elige el modelo y algoritmo adecuados para tu problema, entrénalo con los datos ya limpios y genera algunas predicciones de prueba. | No has realizado predicciones de prueba para tu modelo de ML y/o tu modelo muestra una precisión menor al 60 %. |
| Actividad 3. Graficación y métricas | 20 | Genera por lo menos dos gráficas y dos muestras de métricas que permitan visualizar el rendimiento y precisión del modelo que construiste. Además, realizaste los procesos de *tuning* y ensambles adecuados para tu problema. | Las gráficas no tienen leyendas y colores customizados, solo muestras una gráfica o no realizaste el *tuning* de hiperparámetros.
| Actividad 4. API REST | 20 | Generaste con éxito un *link* público en el que, por método POST, se puede mandar información y la API REST devuelve una predicción junto con el porcentaje de confianza de esta misma. | N/A
| Actividad 5. Presentación | 20 | Genera una presentación en la que establezcas como mínimo: el problema, proceso de solución, metodologías usadas, gráficas de rendimiento, demostración del modelo y aprendizajes obtenidos. Debes redactarla con términos que pueda entender cualquier persona, no solo científicos de datos. | La presentación no expone con claridad o en términos coloquiales el proceso de creación del modelo, sus ventajas y muestras de rendimiento.

**Mucho éxito en tu camino como Data Scientist.**
"""

#from google.colab import drive
#drive.mount('/content/drive')

import pandas as pd
import numpy as np
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
import io
import requests
from os import path
import plotly.express as px
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from  functools import reduce
warnings.filterwarnings("ignore")
#pd.set_option("display.max_columns",800)

from collections import Counter
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_multilabel_classification
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.datasets import make_blobs
from sklearn import metrics
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import RidgeCV
from sklearn.linear_model import LassoCV
from sklearn.linear_model import ElasticNetCV
from sklearn.model_selection import KFold

#%pip install dash

data_set='./Your Career Aspirations of GenZ.csv'#'/content/drive/MyDrive/Your Career Aspirations of GenZ.csv'

data = pd.read_csv(data_set)

data.info()

data.columns

data.shape

data.head(5)

data['Your Current Country.'].unique()

fig_country = px.histogram(data, x="Your Current Country.")
#fig_country.show()

data_india = data[data['Your Current Country.'] == 'India']

#fig_gender_hist = px.histogram(data_india, x="Your Gender")
#fig_gender_hist.show()

x = data_india['Your Gender'].value_counts()
print(x)

fig_gender = px.pie(data_frame= x, values=x.values, names=x.index, title='Gender')
#fig_gender.show()

data['Which of the below factors influence the most about your career aspirations ?'].unique()

data['Would you definitely pursue a Higher Education / Post Graduation outside of India ? If only you have to self sponsor it.'].unique()

data['Which of the below Employers would you work with.'].unique()

data['What type of Manager would you work without looking into your watch ?'].unique()

data['How likely would you work for a company whose mission is misaligned with their public actions or even their product ?'].unique()

data['How likely would you work for a company whose mission is not bringing social impact ?'].unique()

data['What is the most preferred working environment for you.'].unique()

"""*SE TRABAJA INDIA*"""

data_india.shape

data_india['How likely is that you will work for one employer for 3 years or more ?'].unique()

#fig = px.histogram(data_india, x='How likely is that you will work for one employer for 3 years or more ?')
#fig.show()

Label_Encoder = LabelEncoder()

x = data_india['How likely is that you will work for one employer for 3 years or more ?'].value_counts()
print(x)

fig_joblasting = px.pie(data_frame= x, values=x.values, names=x.index, title='Working for +3Y')
#fig_joblasting.show()

'''y = data_india[data_india['Your Gender']== 'Male']
z=data_india[data_india['Your Gender']!= 'Male']
y = y['How likely is that you will work for one employer for 3 years or more ?'].value_counts()
z = z['How likely is that you will work for one employer for 3 years or more ?'].value_counts()
print(y)
print(z)

fig = px.pie(data_frame= y, values=y.values, names=y.index, title='Working for +3Y--Male')
fig.show()

fig = px.pie(data_frame= z, values=z.values, names=z.index, title='Working for +3Y--Female')
fig.show()

x = data_india['What is the most preferred working environment for you.'].value_counts()
print(x)

x = data_india['What type of Manager would you work without looking into your watch ?'].value_counts()
print(x)

x = data_india['How likely would you work for a company whose mission is misaligned with their public actions or even their product ?'].value_counts()
print(x)'''

contingency_table = pd.crosstab(data_india['Your Gender'], [data_india['How likely would you work for a company whose mission is misaligned with their public actions or even their product ?']])

sns.heatmap(contingency_table, cmap="YlGnBu", annot=True, fmt="d")  # Adjust cmap and fmt as needed
#plt.show()

df_data = data_india.copy()

"""*ANALISIS* *ACADEMICO*"""

df_data_cat = df_data.iloc[:,2:]

df_data_cat_num = df_data_cat.select_dtypes(exclude = 'object')
df_data_cat_cat= df_data_cat.select_dtypes(include = 'object')

df_data_cat_num.columns

df_data_cat_cat.columns

df_data_cat_cat = df_data_cat_cat.apply(LabelEncoder().fit_transform)

df_data_cat = pd.concat([df_data_cat_cat, df_data_cat_num], axis=1)

df_data_cat.head()

df_data_cat.shape

pca = PCA()

pca.fit_transform(df_data_cat)

pca_variance = pca.explained_variance_
pca_variance

pca_sample = PCA(n_components=13)
pca_sample_data = pca_sample.fit_transform(df_data_cat)
explained_variance_ratio_sample = pca_sample.explained_variance_ratio_.cumsum()
explained_variance_ratio_sample

'''plt.figure(figsize=(8, 6))
plt.bar(range(13), pca_variance, alpha=0.5, align='center', label="Varianza individual")
plt.legend()
plt.ylabel('% Varianza')
plt.xlabel('Componentes principales')
plt.show()

df_data_cat.corr()['How likely is that you will work for one employer for 3 years or more ?']

sns.heatmap(df_data_cat.corr(), annot=True, annot_kws={'size': 7})'''

"""*ANALISIS REAL*"""

df_data.head(3)

df_data_cat.head(3)

df_data_cat_no = df_data_cat[['Which of the below factors influence the most about your career aspirations ?','Would you definitely pursue a Higher Education / Post Graduation outside of India ? If only you have to self sponsor it.']]
df_data_cat_yes = df_data_cat.loc[:, ~df_data_cat.columns.isin(['Which of the below factors influence the most about your career aspirations ?','Would you definitely pursue a Higher Education / Post Graduation outside of India ? If only you have to self sponsor it.'])] #separa columnas que sobran

df_data_cat_yes.head(2)

df_data_cat_yes.shape

pca.fit_transform(df_data_cat_yes)

pca_sample = PCA(n_components=11)
pca_sample_data = pca_sample.fit_transform(df_data_cat_yes)
explained_variance_ratio_sample = pca_sample.explained_variance_ratio_.cumsum()
explained_variance_ratio_sample

'''plt.figure(figsize=(8, 6))
plt.bar(range(13), pca_variance, alpha=0.5, align='center', label="Varianza individual")
plt.legend()
plt.ylabel('% Varianza')
plt.xlabel('Componentes principales')
plt.show()'''

df_data_cat_yes.corr()['How likely is that you will work for one employer for 3 years or more ?']

#sns.heatmap(df_data_cat_yes.corr(), annot=True, annot_kws={'size': 7})

df_data_cat_yes_fem = df_data_cat_yes[df_data_cat_yes['Your Gender']==0]
df_data_cat_yes_men = df_data_cat_yes[df_data_cat_yes['Your Gender']==1]

"""MALE"""

df_data_cat_yes_men.shape

pca.fit_transform(df_data_cat_yes_men)

pca_sample = PCA(n_components=11)
pca_sample_data = pca_sample.fit_transform(df_data_cat_yes_men)
explained_variance_ratio_sample = pca_sample.explained_variance_ratio_.cumsum()
explained_variance_ratio_sample

'''plt.figure(figsize=(8, 6))
plt.bar(range(13), pca_variance, alpha=0.5, align='center', label="Varianza individual")
plt.legend()
plt.ylabel('% Varianza')
plt.xlabel('Componentes principales')
plt.show()'''

df_data_cat_yes_men.corr()['How likely is that you will work for one employer for 3 years or more ?']

#sns.heatmap(df_data_cat_yes.corr(), annot=True, annot_kws={'size': 7})

"""FEMALE"""

df_data_cat_yes_fem.shape

pca.fit_transform(df_data_cat_yes_fem)

pca_sample = PCA(n_components=11)
pca_sample_data = pca_sample.fit_transform(df_data_cat_yes_fem)
explained_variance_ratio_sample = pca_sample.explained_variance_ratio_.cumsum()
explained_variance_ratio_sample

'''plt.figure(figsize=(8, 6))
plt.bar(range(13), pca_variance, alpha=0.5, align='center', label="Varianza individual")
plt.legend()
plt.ylabel('% Varianza')
plt.xlabel('Componentes principales')
plt.show()'''

df_data_cat_yes_fem.corr()['How likely is that you will work for one employer for 3 years or more ?']

#sns.heatmap(df_data_cat_yes_fem.corr(), annot=True, annot_kws={'size': 7})

df_data_cat_yes.shape

X = df_data_cat_yes.drop(columns='How likely is that you will work for one employer for 3 years or more ?')
y = df_data_cat_yes['How likely is that you will work for one employer for 3 years or more ?']

X.shape

X_train, X_test, y_train, y_test = train_test_split(
                                        X,
                                        y,
                                        train_size   = 0.8,
                                        random_state = 42,
                                        shuffle      = True
                                    )

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score

dtc = DecisionTreeClassifier().fit(X_train, y_train)
dtc_predict = dtc.predict(X_test)
accuracy_dt =accuracy_score(dtc_predict, y_test)
print('El Accuracy usando Decition Tree es de: {}'.format(accuracy_score(dtc_predict, y_test)))

bc = BaggingClassifier(DecisionTreeClassifier(), n_estimators= 100, random_state= 19).fit(X_train, y_train)
bc_predict = bc.predict(X_test)
accuracy_bc_dt=accuracy_score(bc_predict, y_test)
print('El Accuracy usando Bagging con Decition Tree es de: {}'.format(accuracy_score(bc_predict, y_test)))

# Create the model with solver='lbfgs' (suitable for multiclass)
model = LogisticRegression(solver='lbfgs', multi_class='multinomial')

# Fit the model on the training data
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy_log_reg = accuracy_score(y_test, y_pred)
print(f"Test accuracy: {accuracy_log_reg*100:.4f}%")

from sklearn.ensemble import BaggingClassifier

#dtc = DecisionTreeClassifier().fit(X_train, y_train)
#dtc_predict = dtc.predict(X_test)
#print('El Accuracy usando Decition Tree es de: {}'.format(accuracy_score(dtc_predict, y_test)))

bc = BaggingClassifier(model,
                           n_estimators= 100,
                           random_state= 19).fit(X_train, y_train)
bc_predict = bc.predict(X_test)
accuracy_bc_logreg=accuracy_score(bc_predict, y_test)
print('El Accuracy usando Bagging con Decition Tree es de: {}'.format(accuracy_score(bc_predict, y_test)))

#KNEIGHBORS
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier().fit(X_train, y_train)
model_predict = model.predict(X_test)
accuracy_knn = accuracy_score(y_test, y_pred)
print('El Accuracy usando KNN es de: {}'.format(accuracy_score(model_predict, y_test)))

from sklearn.ensemble import BaggingClassifier

#dtc = DecisionTreeClassifier().fit(X_train, y_train)
#dtc_predict = dtc.predict(X_test)
#print('El Accuracy usando Decition Tree es de: {}'.format(accuracy_score(dtc_predict, y_test)))

bc = BaggingClassifier(model,
                           n_estimators= 100,
                           random_state= 19).fit(X_train, y_train)
bc_predict = bc.predict(X_test)
accuracy_bc_knn=accuracy_score(bc_predict, y_test)
print('El Accuracy usando Bagging con Decition Tree es de: {}'.format(accuracy_score(bc_predict, y_test)))

from sklearn.ensemble import RandomForestClassifier
# Create the Random Forest model with desired parameters
model_forest = RandomForestClassifier(n_estimators=100, random_state=42)

# Fit the model on the training data
model_forest.fit(X_train, y_train)

y_pred = model_forest.predict(X_test)

accuracy_randfor = accuracy_score(y_test, y_pred)
print(f"Test accuracy: {accuracy_randfor*100:.4f}%")

from sklearn.ensemble import BaggingClassifier

#dtc = DecisionTreeClassifier().fit(X_train, y_train)
#dtc_predict = dtc.predict(X_test)
#print('El Accuracy usando Decition Tree es de: {}'.format(accuracy_score(dtc_predict, y_test)))

bc = BaggingClassifier(model_forest,
                           n_estimators= 100,
                           random_state= 19).fit(X_train, y_train)
bc_predict = bc.predict(X_test)
accuracy_bc_randfor=accuracy_score(bc_predict, y_test)
print('El Accuracy usando Bagging con Decition Tree es de: {}'.format(accuracy_score(bc_predict, y_test)))

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten, Dense, Dropout

input_shape = (10, 1)  # Replace 'time_steps' and 'features' with your actual data dimensions

model = Sequential()
model.add(Conv1D(filters=64, kernel_size=3, activation='relu', input_shape=input_shape))
model.add(MaxPooling1D(pool_size=2))
model.add(Flatten())
model.add(Dense(100, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='softmax'))  # num_classes should be the number of your target classes

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(X_train, y_train, epochs=35, batch_size=64, validation_split=0.2)

loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test accuracy: {accuracy*100:.4f}%")

accuracy_cnn = model.evaluate(X_test, y_test)

data = {'Model':['Decission Tree','Bagging Class vs DT','Logistic Reg', 'Bag Clas vs LogReg','KNN', 'Bag vs KNN', 'Random Forest', 'BC vs RandFor'],'Score':[accuracy_dt, accuracy_bc_dt, accuracy_log_reg, accuracy_bc_logreg,accuracy_knn, accuracy_bc_knn, accuracy_randfor, accuracy_bc_randfor]}
df_accuracy=pd.DataFrame(data)

df_accuracy['Score %'] = df_accuracy['Score']*100

df_accuracy

# Create a new row dictionary
df_cnn = pd.DataFrame({'Model': ['CNN'], 'Score': [accuracy_cnn[1]], 'Score %':[accuracy_cnn[1]*100]})

# Append the new row to the DataFrame
df_accuracy = pd.concat([df_accuracy,df_cnn], axis=0)  # Optional: reset index for new row

df_accuracy

fig_acc=px.line(df_accuracy, x='Model', y='Score %', markers=True, title='Accury Models')
#fig_acc.show()

#from sklearn.ensemble import RandomForestClassifier
# Create the Random Forest model with desired parameters
#model = RandomForestClassifier(n_estimators=100, random_state=42)

# Fit the model on the training data
#model.fit(X_train, y_train)

data

data_notind = pd.read_csv(data_set)
data_notind = data_notind[data_notind['Your Current Country.'] != 'India']

data_notind.columns

df_data_cat_yes.columns

# List of columns to remove
cols_to_remove = ['Your Current Country.', 'Your Current Zip Code / Pin Code','Which of the below factors influence the most about your career aspirations ?', 'Would you definitely pursue a Higher Education / Post Graduation outside of India ? If only you have to self sponsor it.']

# Drop multiple columns using 'drop' method
df_data_notind = data_notind.drop(cols_to_remove, axis=1)

# Now 'df' only has 'col1' remaining
df_data_notind

df_data_notind_num = df_data_notind.select_dtypes(exclude = 'object')
df_data_notind_cat= df_data_notind.select_dtypes(include = 'object')

df_data_notind_cat = df_data_notind_cat.apply(LabelEncoder().fit_transform)

df_notind_cat = pd.concat([df_data_notind_cat, df_data_notind_num], axis=1)

X_notind = df_notind_cat.drop(columns='How likely is that you will work for one employer for 3 years or more ?')
y_notind = df_notind_cat['How likely is that you will work for one employer for 3 years or more ?']

y_pred_eval = model_forest.predict(X_notind)

accuracy_randfor_eval = accuracy_score(y_notind, y_pred_eval)
print(f"Test accuracy evaluation: {accuracy_randfor_eval*100:.4f}%")

data_eval = {'Model':['Random Forest', 'Random Forest Eval'],'Score':[accuracy_randfor,accuracy_randfor_eval]}
df_accuracy_eval=pd.DataFrame(data_eval)

df_accuracy_eval['Score %'] = df_accuracy_eval['Score']*100

df_accuracy_eval

fig_rafor_test_eval = px.bar(df_accuracy_eval, x='Model', y='Score %', title= 'TEST vs EVALUATION')
#fig_rafor_test_eval.show()

#predictions = model.predict(df_data_notind_2)  # make sure new_data is preprocessed similarly to your training data
#predicted_class = tf.argmax(predictions, axis=1)