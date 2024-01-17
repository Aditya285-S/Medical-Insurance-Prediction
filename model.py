import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score
import joblib

ins_dataset=pd.read_csv("insurance.csv")


ins_dataset['sex']=ins_dataset['sex'].map({'male':0 , 'female':1})
ins_dataset['smoker']=ins_dataset['smoker'].map({'yes':0 , 'no':1})
ins_dataset['region']=ins_dataset['region'].map({'southwest':1 , 'southeast':2 , 'northwest':3 , "northeast":4})


X = ins_dataset.drop(['charges'],axis=1)
y = ins_dataset['charges']


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)


gr = GradientBoostingRegressor()
gr.fit(X_train,y_train)


train_predictions = gr.predict(X_train)
training_accuracy = r2_score(train_predictions, y_train)
print('Accuracy on Training data:', training_accuracy * 100, "%")


test_predictions = gr.predict(X_test)
test_accuracy = r2_score(test_predictions, y_test)
print('Accuracy on Test data:', test_accuracy * 100, "%")


joblib.dump(gr,'GR_model')
model = joblib.load('GR_model')