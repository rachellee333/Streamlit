import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

penguin_df = pd.read_csv('penguin_ml.csv')
print('penguin_df.head()')
print(penguin_df.head())
penguin_df.dropna(inplace=True)
output = penguin_df['species']
features = penguin_df[['island', 'bill_length_mm', 'bill_depth_mm',
                      'flipper_length_mm', 'body_mass_g', 'sex']]
features = pd.get_dummies(features)
print('Here are our output variables')
print(output.head())
# print(output)
print('Here are our feature variables')
print(features.head())
output, uniques = pd.factorize(output)
x_train, x_test, y_train, y_test = train_test_split(
  features, output, test_size=.8
)
rfc = RandomForestClassifier(random_state=15)
rfc.fit(x_train.values, y_train)
y_pred = rfc.predict(x_test.values)
score = accuracy_score(y_pred, y_test)
print('Our accuracy score for this model is {}'.format(score))
rf_pickle = open('random_forest_penguin.pickle', 'wb')
pickle.dump(rfc, rf_pickle)
rf_pickle.close()
output_pickle = open('output_penguin.pickle', 'wb')
pickle.dump(uniques, output_pickle)
output_pickle.close()

# https://github.com/rachellee333/Streamlit/blob/f74f3739981435b67e23937d334ca72a066f28b2/streamlit_apps/penguin_ml/random_forest_penguin.pickle