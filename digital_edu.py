#створи тут свій індивідуальний проект!
import pandas as pd

df = pd.read_csv("train.csv")

df.drop(["id","city","bdate","graduation","last_seen","occupation_name","career_start","career_end"],axis=1,inplace= True)

def mean_occup_type(study):
        if study == "university":
           return 0
        return 1

def mean_langs(lang):
    if not (";" in lang):
        return 1
    range = 1
    for i in lang:
        if i == ";":
            range+=1
    return range
    
def change_education_status(string):
    if string == "Undergraduate applicant":
        return 1
    if string == "Student (Bachelor's)":
        return 2
    if string == "Alumnus (Bachelor's)":
        return 3
    if string == "Student (Specialist)":
        return 4
    if string == "Student (Master's)":
        return 5
    if string == "Alumnus (Specialist)":
        return 6
    if string == "Alumnus (Master's)":
        return 7
    if string == "Candidate of Sciences":
        return 8
    if string == "PhD":
        return 9
        
      
df["occupation_type"] = df["occupation_type"].apply(mean_occup_type)
df["education_status"] = df["education_status"].apply(change_education_status)
df["langs"] = df["langs"].apply(mean_langs)
df["education_form"].fillna("Full-time", inplace= True)
df[pd.get_dummies(df["education_form"]).columns] = pd.get_dummies(df["education_form"], dtype = int)
df.drop(["education_form"],axis=1,inplace= True)

df["has_mobile"] = df["has_mobile"].apply(int)
df["followers_count"] = df["followers_count"].apply(int)
#df["relation"] = df["relation"].apply(int)

df[["relation 0","relation 1","relation 2","relation 3","relation 4","relation 5","relation 6","relation 7","relation 8"]] = pd.get_dummies(df["relation"], dtype = int)
#df.drop(["relation"],axis=1,inplace= True)

print(df.head(20))
#print(df["relation"].value_counts())
#df.info()