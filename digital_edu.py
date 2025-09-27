#створи тут свій індивідуальний проект!
import pandas as pd

df = pd.read_csv("train.csv")

df.drop(["id","city","bdate","graduation","last_seen","occupation_name","career_start","career_end"],axis=1,inplace= True)

def mean_occup_type(study):
        if study == "university":
           return 0
        return 1

def mean_langs(lang):
    if lang == ";":
         return 0
    return 2
      
df["occupation_type"] = df["occupation_type"].apply(mean_occup_type)
df["langs"] = df["langs"].apply(mean_langs)
df["education_form"].fillna("Full-time", inplace= True)
df[pd.get_dummies(df["education_form"]).columns] = pd.get_dummies(df["education_form"], dtype = int)
df.drop(["education_form"],axis=1,inplace= True)
df["has_mobile"] = df["has_mobile"].apply(int)
df["followers_count"] = df["followers_count"].apply(int)
df["relation"] = df["relation"].apply(int)

#df.info()
print(df.head(20))