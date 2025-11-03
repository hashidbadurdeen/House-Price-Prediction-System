import pickle
import pandas as pd
import sklearn
from sklearn.ensemble._forest import ForestClassifier,ForestRegressor

cols = ['LotArea', 'Street', 'BldgType', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd', 'CentralAir', 'MoSold', 'YrSold']
model = pickle.load(open('C:/Users/hashi/Downloads/HousePrice.pkl', 'rb'))
df = pd.DataFrame(columns=cols)
df['LotArea'] = [str(input("Please Enter the value for Lot size in square feet = "))]
df['Street'] = [str(input("Please Enter the value for Type of road access to property= "))]
df['BldgType'] = [str(input("Please Enter the value for Type of dwelling = "))]
df['OverallQual'] = [str(input("Please Enter the value for overall material and finish of the house =  "))]
df['OverallCond'] = [str(input("Please Enter the value for overall condition of the house = "))]
df['YearBuilt'] = [str(input("Please Enter the value for Original construction date = "))]
df['YearRemodAdd'] = [str(input("Please Enter the value for Remodel date = "))]
df['CentralAir'] = [str(input("Please Enter the value for Central air conditioning = "))]
df['MoSold'] = [str(input("Please Enter the value for Month Sold (MM) = "))]
df['YrSold'] = [str(input("Please Enter the value for Year Sold (YYYY) = "))]
pred = model.predict(df)
label = ''
if(pred):
    label = "House Price is Predicted", pred
else:
    label = "Nothing Exist"
print("The predictions for data set is: {}".format(label))

input()



