import pickle

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

st.title("Penguin Classifier")

st.write("This app uses 6 inputs to predict the species of penguin using"
         "a model built on the Palmer Penguins dataset. Use the form below"
         "to get started!")

penguin_df = pd.read_csv('/workspaces/Streamlit/streamlit_apps/penguin_ml/penguin_ml.csv')

penguin_df = st.file_uploader('Upload the penguin csv file')

rf_pickle = open('/workspaces/Streamlit/streamlit_apps/penguin_ml/random_forest_penguin.pickle', 'rb')
map_pickle = open('/workspaces/Streamlit/streamlit_apps/penguin_ml/output_penguin.pickle', 'rb')
rfc = pickle.load(rf_pickle)
unique_penguin_mapping = pickle.load(map_pickle)
rf_pickle.close()
map_pickle.close()
penguin_df = pd.read_csv('/workspaces/Streamlit/streamlit_apps/penguin_ml/penguin_ml.csv')
penguin_df = penguin_df.dropna()
output = penguin_df['species']
features = penguin_df[
  [
    'island', 
    'bill_length_mm', 
    'bill_depth_mm',
    'flipper_length_mm', 
    'body_mass_g', 
    'sex'
  ]
]
features = pd.get_dummies(features)
output, unique_penguin_mapping = pd.factorize(output)
x_train, x_test, y_train, y_test = train_test_split(
  features, output, test_size=.8
)
rfc = RandomForestClassifier(random_state=15)
rfc.fit(x_train.values, y_train)
y_pred = rfc.predict(x_test)
score = round(accuracy_score(y_pred, y_test), 2)
st.write(f"""We trained a Random Forest model on these
          data, it has a score of {score}! Use the 
          inputs below to try out the model!""")
# with st.form("user_inputs"):
island = st.selectbox('Penguin Island', options=['Biscoe', 'Dream', 'Torgerson'])
sex = st.selectbox('Sex', options=['Female', 'Male'])
bill_length = st.number_input('Bill Length (mm)', min_value=0)
bill_depth = st.number_input('Bill Depth (mm)', min_value=0)
flipper_length = st.number_input('Flipper Length (mm)', min_value=0)
body_mass = st.number_input('Body Mass (g)', min_value=0)
#   st.form_submit_button()
  
user_inputs = [island, sex, bill_length, bill_depth, flipper_length, body_mass]
st.write(f"""The user inputs are {user_inputs}""".format())

island_biscoe, island_dream, island_torgerson = 0, 0, 0
if island == 'Biscoe': 
  island_biscoe = 1
elif island == 'Dream':
  island_dream = 1
elif island == 'Torgerson':
  island_torgerson = 1
  
sex_female, sex_male = 0, 0
if sex == 'Female':
  sex_female = 1
elif sex == 'Male':
  sex_male = 1
  
new_prediction = rfc.predict([[bill_length, bill_depth, flipper_length, body_mass, island_biscoe, island_dream, island_torgerson, sex_female, sex_male]])
prediction_species = unique_penguin_mapping[new_prediction][0]

st.subheader('rfc')
st.write(rfc)
st.subheader('unique_penguin_mapping')
st.write(unique_penguin_mapping)
st.subheader('Predicting Your Penguin\'s Species')
st.write(f"We predict your penguin is of the {prediction_species} species")
st.write(
  """We used a machine learning (Random Forest)
  model to predict the species, the features
  used in this prediction are ranked by 
  relative importance below."""
)
fig, ax = plt.subplots()
ax = sns.barplot(x=rfc.feature_importances_, y=features.columns)
plt.title('Which features are the most important for species prediction?')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.tight_layout()
# plt.style('seaborn-v0_8-deep')
st.pyplot(fig)
fig.savefig('feature_importance.png')
st.image('feature_importance.png')
st.write(
  """Below are the histograms for each 
  continuous variable separated by penguin
  species. The vertical line represents
  your the inputted value."""
)
fig, ax = plt.subplots()
ax = sns.displot(x=penguin_df['bill_length_mm'],
                hue=penguin_df['species'])
plt.axvline(bill_length)
plt.title('Bill Length By Species')
st.pyplot(ax)
fig, ax = plt.subplots()
ax = sns.displot(x=penguin_df['bill_depth_mm'],
                hue=penguin_df['species'])
plt.axvline(bill_depth)
plt.title('Bill Depth By Species')
st.pyplot(ax)
fig, ax = plt.subplots()
ax = sns.displot(x=penguin_df['flipper_length_mm'],
                hue=penguin_df['species'])
plt.axvline(flipper_length)
plt.title('Flipper Length By Species')
st.pyplot(ax)