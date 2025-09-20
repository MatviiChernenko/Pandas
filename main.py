import pandas as pd

df = pd.read_csv("titanic.csv")

df.drop(["PassengerId","Name","Ticket","Fare","Cabin"],axis=1,inplace= True)

age1 = df[df["Pclass"] == 1]["Age"].mean()
age2 = df[df["Pclass"] == 2]["Age"].mean()
age3 = df[df["Pclass"] == 3]["Age"].mean()

def mean_age(string):
    if pd.isnull(string["Age"]):
        if string["Pclass"] == 1:
            return age1
        if string["Pclass"] == 2:
            return age2
        if string["Pclass"] == 3:
            return age3
    else:
        return string["Age"]
      
def mean_age(string):
    if pd.isnull(string["Age"]):
        if string["Pclass"] == 1:
            return age1
        if string["Pclass"] == 2:
            return age2
        if string["Pclass"] == 3:
            return age3
    else:
        return string["Age"]

def mean_gender(gender):
       if gender == "male":
           return 0
       if gender == "female":
           return 1
       else:
           return gender["Gender"]      

df["Age"] = df.apply(mean_age,axis=1)
df["Gender"] = df["Gender"].apply(mean_gender)
df[pd.get_dummies(df["Embarked"]).columns] = pd.get_dummies(df["Embarked"], dtype = int)
df.drop(["Embarked"],axis=1,inplace= True)

#df.info()
print(df.head(20))
#print(df["Pclass"].value_counts())