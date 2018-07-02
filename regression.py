import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.cross_validation import train_test_split
from sklearn.datasets import load_boston

boston = load_boston()
DfX=pd.DataFrame(boston.data,columns=boston.feature_names)
DfY=pd.DataFrame(boston.target)
DfX.describe()
reg=linear_model.LinearRegression()
xTrain,xTest,yTrain,yTest=train_test_split(DfX,DfY,train_size=0.2,random_state=4)
reg.fit(xTrain,yTrain)
a=reg.predict(xTest)
print(boston)