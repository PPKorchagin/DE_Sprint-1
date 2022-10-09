import pandas as pd
import json

# df=pd.read_json("./files/res.json")

# df.to_csv("./files/res.csv")
# pd.set_option('display.max_rows', None)

df = pd.read_csv("./files/filtered_res.csv")

# Таблица замен
repl = [
    ["data-инженер", "data engineer"],
    ['\(.*\)', ''],
    ["[Рр]азработчик", "developer"],
    ["Developer", "developer"],
    ["[Сс]тарший\ +", ""],
    ["[иИ]нженер", "engineer"],
    ["[Jj]unior\ +", ""],
    ["[Mm]iddle\ +", ""],
    ["[Гг]лавный\ +", ""],
    ["[Мм]ладший\ +", ""],
    ["^.*devops.*$", "devops"],
    ["^.*[Dd][Bb][Aa]", "dba"],
    ["^.*database.*$", "dba"],
    ["^.*python.*$", "python"],
    ["^.*java.*$", "java"],
    ["^.*php.*$", "java"],
    ["^(.*\ )?etl(\ .*)?$", "etl"],
    ["^(.*\ )?[Bb][Ii]([\ -].*)?$", "bi"],
    ["^(.*\ )?[Ss][Rr][Ee]([\ \/].*)?$", "devops"],
    ["^.*[Сс]истемный администратор.*$", "system administrator"],
    ["^.*system administrator.*$", "system administrator"],
    ["^.*technical support.*$", "system administrator"],
    ["^.*[Ss][Rr][Ee][\ -].*$", "devops"],
    ["engineer по данным *", "data engineer"],
    ["^.*data[\ -]?engineer.*", "data engineer"],
    ["qa automation engineer", "qa engineer"],
    ["dev/?ops engineer", "devops"],
    ["^(.*\ )?devops\ .*$", "devops"],
    ["^.*engineer ?- ?программист.*$", "engineer"],
    ["^.*project engineer.*$", "engineer"],
    ["^.*ведущий engineer.*$", "engineer"],
    ["^.*системный engineer.*$", "system administrator"],
    ["^.*data sciencist.*$", "data science"],
    ["^.*data scientist.*$", "data science"],
    ["^.*data science.*$", "data science"],
    ["^.*data analy.*$", "data analytics"],
    ["^.*аналитик данных.*$", "data analytics"],
    ["^(.*\ )?[Qq][Aa][\ -].*$", "qa"],
    ["^.*рекрутер.*$", "recruiter"],
    ["^.*recruter.*$", "recruiter"],
    ["^.*recruiter.*$", "recruiter"],
    ["^.*ml engineer.*$", "ml engineer"],
    ["^.*machine learning.*$", "ml engineer"],
    ["^.*net/c#.*$", "c#"],
    ["^.*c#.*$", "c#"],
    ["^.*[CcСс]\+\+.*$", "c++"],
    ["^.*[Cc]pp.*$", "c++"],
    ["^.*sysops.*$", "sysops"],
    ["^(.*\ )?[Gg][Oo](\ .*)?$", "golang"],
    ["^(.*\ )?[Ii][Oo][Ss](\ .*)?$", "ios"],
    ["^(.*\ )?[Mm][Aa][Cc][Oo][Ss](\ .*)?$", "macos"],
    ["^(.*\ )?[Gg][Oo]lang(\ .*)?$", "golang"],
    ["^(.*\ )?full[\ -]?stack(\ .*)?$", "fullstack"],
    ["^(.*\ )?fullstack(\ .*)?$", "fullstack"],
    ["^(.*\ )?backend(\ .*)?$", "fullstack"],
    ["^(.*\ )?back-end(\ .*)?$", "fullstack"],
    ["^(.*\ )?лидер направления(\ .*)?$", "teamlead"],
    ["^(.*\ )?team[\ -]?lead(\ .*)?$", "teamlead"],
    ["^(.*\ )?[Aa]ndroid(\ .*)?$", "android"],
    ["^(.*\ )?sales(\ .*)?$", "sales"],
    ["^(.*\ )?отдела? продаж(\ .*)?$", "sales"],
    ["^(.*\ )?pre[\ -]?sale(\ .*)?$", "sales"],
    ["^(.*\ )?[Mm][Ll][\ -]?ops(\ .*)?$", "mlops"],
    ["^(.*\ )?engineer.*поддержки(\ .*)?$", "engineer"],
    ["^(.*\ )?project manager(\ .*)?$", "pm"],
    ["^(.*\ )?руководитель.*проект(.*)?$", "pm"],
    ["^(.*\ )?manager(.*)?$", "manager"],
    ["^(.*\ )?менеджер(.*)?$", "manager"],
    ["^(.*\ )?network engineer(.*)?$", "network engineer"],
    ["^(.*\ )?ruby(.*)?$", "ruby"],
    ["^(.*\ )?\.net(.*)?$", ".net"],
    ["^(.*\ )?front[\ -]?end(.*)?$", "frontend"],
    ["^(.*\ )?kotlin(.*)?$", "kotlin"],
    ["^.*security operations.*$", "secops"],
    ["^.*bi-.*$", "bi"],
    ["^.*sql.*$", "dba"],
    ["^.*operations specialist.*$", "devops"],
    ["^.*test automation.*$", "qa"],
    ["^.*тестирован.*$", "qa"],
    ["^.*test engineer.*$", "qa"],
    ["^.*engineer данных .*", "data engineer"],
    ["^.*архитектор.*", "architect"],
    ["^.*engineer-оператор.*", "system administrator"],
    ["^.*technical services.*", "system administrator"],
    ["^.*[Ii][Tt] engineer .*", "system administrator"],
    ["^.*systems? engineer.*", "system administrator"],
    ["^.*site reliability engineer .*", "devops"],
    ["^.*linux.*", "linux"],
    ["^.*elk.*", "elk"],
    ["^.*машинн.*обучен.*", "ml"],
    ["^.*ui\/ux.*", "ui/ux"],
    ["^.*баз\ данн.*", "dba"],
    ["сетевой", "network"],
    ["^.*network engineer.*$", "network engineer"],
    ["^.*hadoop.*$", "hadoop"],
    ["^.*computer vision .*$", "cv"],
    ["^(.*\ )?бд(\ .*)?$", "dba"],
    ["^(.*\ )?nlp(\ .*)?$", "nlp"],

    ["\ *\[.*\]\ *", ""]
]

# Избавляемся от текстов в скобках
df["name"] = df["name"].str.lower()
df["name"] = df["name"].str.strip()
for r in repl:
    df["name"].replace(r[0], r[1], inplace=True, regex=True)

uniq = df["name"]

filt = df["name"].value_counts()

cnts = df.groupby("name")["id"].transform("nunique").rename('counts')
wcnts = df[cnts > 10]

print(wcnts.groupby("name")[["salary_from", "salary_to"]].mean())
print(wcnts.groupby("name")[["salary_from", "salary_to"]].median())

print(wcnts.groupby("area")[["salary_from", "salary_to"]].median().sort_values("salary_to"))
print(wcnts.groupby("area")[["salary_from", "salary_to"]].mean().sort_values("salary_to"))

# Самая оплачиваемая группа из средних (и менее оплачиваемая):
print(wcnts.groupby("name")[["salary_to"]].mean().dropna().sort_values("salary_to").head(1))
print(wcnts.groupby("name")[["salary_to"]].mean().dropna().sort_values("salary_to").tail(1))

# Какое процентное соотношение каждого региона по вакансиям от всех вакансий?
print((100 * wcnts.groupby("area")["id"].count() / wcnts["id"].count()).sort_values())

corr_df = df[["experience", "salary_from"]]


#Корелляция
corr_df["experience_n"]=corr_df["experience"].map({
    "noExperience": 0,
    "between1And3": 1,
    "between3And6": 3,
    "moreThan6": 6
})


#Количество уникальных вакансий
print(df["name"].nunique())


#Какие 10 наиболее часто встречающихся должностей?
print(df.groupby("name")["id"].nunique().sort_values(ascending=False)[:10])
