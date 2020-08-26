#pip install xlrd
#pip install pyttsx3
import pandas as pd
import sklearn
import pyttsx3
################### Fucking starts ############################
print("****** Kindly ENTER 'Online file' - 1 or 'Local Directory File- 2' !! ")
engine = pyttsx3.init()
engine.setProperty("rate",150)
text = "Hey,User, Enter 1 if your file is Offline or in Local Machine or Enter 2 if your File is Online"
engine.say(text)
# play the speech
engine.runAndWait()
# Data collecting form link
data_link = input("Enter the file directory path :")
file_type = data_link[-3:]
#File Format identification
dtype_dict = {'csv':'Comma Separated File','lsx':'Excel File','tsv':'Tab Separated File','psv':'Pipe Separated File'}
for i in dtype_dict.keys():
    if i == file_type:
        print('The dataset type is : '+ dtype_dict[i])
# Data Importing
if file_type =="csv":
    data = pd.read_csv(data_link)
elif file_type == "psv":
    data = pd.read_csv(data_link,sep='|')
elif file_type == "lsx":
    data = pd.read_excel(data_link)
else :
    print('Sorry Bitch !! Only csv,psv,excel files are allowed !')

print(data.head())
# Data Analytics
class data_analytics:
    def __init__(self,data):
        self.data = data
        print('1) Dimension of the dataset is      :',data.shape)
        print('2) Number of Columns in the dataset :',data.shape[1])
        print('3) Number of Rows in the dataset    :',data.shape[0])
        numerical_features = [f for f in data.columns if data[f].dtypes!='O']
        print('4) Count of Numerical Features      :',len(numerical_features))
        cat_features = [c for c in data.columns if data[c].dtypes=='O']
        print('5) Count of Categorical Features    :',len(cat_features))
    def missing_values(self,data):
        print('6.1) Total Missing Values in the dataset:',(data.isnull().sum().sum()))
        print('6.2) Percentage of Total Missing Values :',(data.isnull().sum().sum()/(data.shape[0]*data.shape[1]))*100)
        print('6.3) Missing Values Estimation          :')
        for i in data.columns:
            if data[i].isna().sum()>0:
                print(' >> The Column ',i,' has '+ str(data[i].isna().sum()) + ' missing values')
              
text2 = "Here is a basic analytics report of the Dataset"
engine.say(text2)
engine.runAndWait()
analytics = data_analytics(data)
#print(analytics)
print(analytics.missing_values(data))
# Data Insights
lst = []
for feature in data.columns:
    lst.append(feature)
print('7) These are the following features or Columns in the Dataset :')
print(lst)
def text_analysis(feature):
    if len(data[feature].value_counts()) < data.shape[0]:
        engine.say('Enter the range you want to print top and bottom repeated values:')
        engine.runAndWait()
        n = int(input('Enter the range to print the most repeated Data :'))
        a= data[feature].value_counts().head(n)
        b= data[feature].value_counts().tail(n)
        print(a)
        print(b)
        
def feature_analysis():
    text3 = "Hey, Do u want to understand what's in your data ? Just enter the column you want to Analyze !"
    engine.say(text3)
    engine.runAndWait()
    feature = input('Enter the feature/column name :')
    if feature in data.columns:
        if data[feature].dtypes == 'O':
            text_analysis(feature)
        else:
            print(f'{feature} has maximum value of {data[feature].max()}')
            print(f'{feature} has a minimum value of {data[feature].min()}')
            text_4 = f" The {feature} has maximum value of {data[feature].max()} and minimum value of {data[feature].min()}. here is the list of most repeated values and least repeated values"
            engine.say(text_4)
            engine.runAndWait()
            print('Most repeated values:')
            print(data[feature].value_counts().head(5))
            print('Least repeated values:')
            print(data[feature].value_counts().tail(5))
            
print(feature_analysis())
text_5 = "Do you want to do the same for other column ? Type 'yes' if u want to or 'no' if u want to skip and go to next features !"
engine.say(text_5)
engine.runAndWait()
query_1 = input(" Enter 'yes' or 'no' !")
query_1v = query_1.lower()
query_1v = 'yes'
while query_1v == 'no':
    print(feature_analysis)
#Classifier or regressor
# **************** Conditions for Classification *******************
# Target variable Analysis
colname = input('Enter the Target feature name :')
a = len(data[colname].value_counts())
#lst1 = []
#if a == 2:
 #   for i in data[colname].value_counts():

  #      lst1.append(i)
   #     count_1 = sum(data[colname]==lst[0])
    #    count_2 = sum(data[colname]==lst[1])
     #   if (count_1 / count_2) >= 2 or (count_2 / count_1) >= 2:
      #      print('This is an Imbalanced Dataset')
       # elif (count_1 / count_2) == 1:
        #    print('This is a perfectly Balanced Dataset')
        #else:
            #print('This is a Balanced Dataset')
if colname in data.columns:
    if a == 2 and data[colname].dtypes == 'int64':
        print('This is a BINARY CLASSIFICATION problem !!')
        out_bc = "This Dataset holds for a Binary Classification Problem. Go on to build a Binary Classifier !"
        engine.say(out_bc)
        engine.runAndWait()
    elif (a==1 or a==0) and a/data.shape[0] >= 0.8:
        print('Not enough data to day whether it is a classification or regression.')
        out_nc = "Oh My God ! This is impossible to find whether is Classification or regression problem statement"
        engine.say(out_nc)
        engine.runAndWait()
    elif a > 2 and a <= 10:
        print('This is a MULTI-CLASS CLASSIFICATION problem ')
        out_mc = "This Dataset holds for a Multi class Classification Problem. Go on to build a Multi class Classifier !"
        engine.say(out_mc)
        engine.runAndWait()
    else:
        print('This is regression problem statement')
        out_reg="This is a regression problem statement. Go onto build a Regression Models to fit the data."
        engine.say(out_reg)
        engine.runAndWait()        
# Enter features to drop for training the model


