#%%
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm



# 지역별 인구수 시설 현황

## 데이터 로드

import pandas as pd
import numpy as np

ks_pub_df = pd.read_csv(r'.\data\KS_AREA_ACCTO_PUBLIC_ALSFC_SUPPLY_STTUS_INFO_202205.csv')
ks_pub_df.tail()

ks_pub_df.columns

## 데이터 전처리 및 분할

ks_pub_df1 = ks_pub_df.drop(['CTPRVN_CD','SIGNGU_CD'], axis=1) # 필요없는 컬럼 지우기

ks_pub_df1.info()

df_2020 = ks_pub_df1.iloc[:1145,:]
df_2021 = ks_pub_df1.iloc[1145:3893,:]
df_2022 = ks_pub_df1.iloc[3893:,:]

cityname = ks_pub_df1.CTPRVN_NM.unique().tolist()

c_pvalue_2020 = []
c_fvalue_2020 = []

for i in cityname:
    city = df_2020[df_2020['CTPRVN_NM'] == i]
    i_pvalue = sum(city['SIGNGU_ACCTO_POPLTN_CO'].values)
    i_fvalue = sum(city['SIGNGU_ACCTO_FCLTY_CO'].values)
    
    c_pvalue_2020.append(i_pvalue)
    c_fvalue_2020.append(i_fvalue)

c_pvalue_2021 = []
c_fvalue_2021 = []

for i in cityname:
    city = df_2021[df_2021['CTPRVN_NM'] == i]
    i_pvalue = sum(city['SIGNGU_ACCTO_POPLTN_CO'].values)
    i_fvalue = sum(city['SIGNGU_ACCTO_FCLTY_CO'].values)
    
    c_pvalue_2021.append(i_pvalue)
    c_fvalue_2021.append(i_fvalue)

c_pvalue_2022 = []
c_fvalue_2022 = []

for i in cityname:
    city = df_2022[df_2022['CTPRVN_NM'] == i]
    i_pvalue = sum(city['SIGNGU_ACCTO_POPLTN_CO'].values)
    i_fvalue = sum(city['SIGNGU_ACCTO_FCLTY_CO'].values)
    
    c_pvalue_2022.append(i_pvalue)
    c_fvalue_2022.append(i_fvalue)

# 연도별 인당 시설수 구하기

pf2020 = []

for i in range(len(c_fvalue_2020)):
    v = np.round(c_fvalue_2020[i]/c_pvalue_2020[i],5)
    pf2020.append(v)
    
pf2021 = []

for i in range(len(c_fvalue_2021)):
    v = np.round(c_fvalue_2021[i]/c_pvalue_2021[i],5)
    pf2021.append(v)
    
pf2022 = []

for i in range(len(c_fvalue_2022)):
    v = np.round(c_fvalue_2022[i]/c_pvalue_2022[i],5)
    pf2022.append(v)

c_pvalue_2020 = pd.Series(c_pvalue_2020)
c_fvalue_2020 = pd.Series(c_fvalue_2020)
pf2020 = pd.Series(pf2020)

tdf_2020 = pd.concat((c_pvalue_2020,c_fvalue_2020,pf2020),axis = 1)
tdf_2020 = tdf_2020.transpose()
tdf_2020.columns = cityname
tdf_2020.index = ['시설 사용 총 인구수', '총 시설 수', '인구 당 시설 수']
tdf_2020

c_pvalue_2021 = pd.Series(c_pvalue_2021)
c_fvalue_2021 = pd.Series(c_fvalue_2021)
pf2021 = pd.Series(pf2021)

tdf_2021 = pd.concat((c_pvalue_2021,c_fvalue_2021,pf2021),axis = 1)
tdf_2021 = tdf_2021.transpose()
tdf_2021.columns = cityname
tdf_2021.index = ['시설 사용 총 인구수', '총 시설 수', '인구 당 시설 수']
tdf_2021

c_pvalue_2022 = pd.Series(c_pvalue_2022)
c_fvalue_2022 = pd.Series(c_fvalue_2022)
pf2022 = pd.Series(pf2022)

tdf_2022 = pd.concat((c_pvalue_2022,c_fvalue_2022,pf2022),axis = 1)
tdf_2022 = tdf_2022.transpose()
tdf_2022.columns = cityname
tdf_2022.index = ['시설 사용 총 인구수', '총 시설 수', '인구 당 시설 수']
tdf_2022

## 시각화

import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
import warnings
warnings.filterwarnings('ignore')
plt.rcParams['axes.unicode_minus'] = False

### 2020년도

column_name = tdf_2020.columns

sns.set_theme(style="whitegrid")
plt.figure(figsize=(13, 5))
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.xticks(rotation = -45)
sns.barplot(x=column_name, y=tdf_2020.iloc[0])

sns.set_theme(style="whitegrid")
plt.figure(figsize=(13, 5))
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.xticks(rotation = -45)
sns.barplot(x=column_name, y=tdf_2020.iloc[1])

sns.set_theme(style="whitegrid")
plt.figure(figsize=(13, 5))
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.xticks(rotation = -45)
sns.barplot(x=column_name, y=tdf_2020.iloc[2])

### 2021년도

column_name = tdf_2021.columns

sns.set_theme(style="whitegrid")
plt.figure(figsize=(13, 5))
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.xticks(rotation = -45)
sns.barplot(x=column_name, y=tdf_2021.iloc[0])

sns.set_theme(style="whitegrid")
plt.figure(figsize=(13, 5))
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.xticks(rotation = -45)
sns.barplot(x=column_name, y=tdf_2021.iloc[1])

sns.set_theme(style="whitegrid")
plt.figure(figsize=(13, 5))
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.xticks(rotation = -45)
sns.barplot(x=column_name, y=tdf_2021.iloc[2])

### 2022년도

column_name = tdf_2022.columns

sns.set_theme(style="whitegrid")
plt.figure(figsize=(13, 5))
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.xticks(rotation = -45)
sns.barplot(x=column_name, y=tdf_2022.iloc[0])

sns.set_theme(style="whitegrid")
plt.figure(figsize=(13, 5))
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.xticks(rotation = -45)
sns.barplot(x=column_name, y=tdf_2022.iloc[1])

sns.set_theme(style="whitegrid")
plt.figure(figsize=(13, 5))
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.xticks(rotation = -45)
sns.barplot(x=column_name, y=tdf_2022.iloc[2])

# 지역별 동호회 빈도

## 데이터 로드

ksa_df = pd.read_csv(r'.\data\KS_AREA_ACCTO_SPORTS_CLUB_CRSTAT_INFO_202205.csv')
ksa_df.head()

ksa_df.info()

## 데이터 전처리

ksa_df1 = ksa_df.drop(['CLUB_NM','FOND_DE'],axis = 1)

CTP = ksa_df1['CTPRVN_NM'].value_counts()
CTP.index

kk_df = ksa_df1[ksa_df1['CTPRVN_NM'] == CTP.index[0]].reset_index(drop=True)
seoul_df = ksa_df1[ksa_df1['CTPRVN_NM'] == CTP.index[1]].reset_index(drop=True)
kj_df = ksa_df1[ksa_df1['CTPRVN_NM'] == CTP.index[2]].reset_index(drop=True)
dg_df = ksa_df1[ksa_df1['CTPRVN_NM'] == CTP.index[3]].reset_index(drop=True)
kb_df = ksa_df1[ksa_df1['CTPRVN_NM'] == CTP.index[4]].reset_index(drop=True)
cb_df = ksa_df1[ksa_df1['CTPRVN_NM'] == CTP.index[5]].reset_index(drop=True)
kw_df = ksa_df1[ksa_df1['CTPRVN_NM'] == CTP.index[6]].reset_index(drop=True)
jj_df = ksa_df1[ksa_df1['CTPRVN_NM'] == CTP.index[7]].reset_index(drop=True)
ic_df = ksa_df1[ksa_df1['CTPRVN_NM'] == CTP.index[8]].reset_index(drop=True)
bs_df = ksa_df1[ksa_df1['CTPRVN_NM'] == CTP.index[9]].reset_index(drop=True)
kn_df = ksa_df1[ksa_df1['CTPRVN_NM'] == CTP.index[10]].reset_index(drop=True)
us_df = ksa_df1[ksa_df1['CTPRVN_NM'] == CTP.index[11]].reset_index(drop=True)
jb_df = ksa_df1[ksa_df1['CTPRVN_NM'] == CTP.index[12]].reset_index(drop=True)
jn_df = ksa_df1[ksa_df1['CTPRVN_NM'] == CTP.index[13]].reset_index(drop=True)
cn_df = ksa_df1[ksa_df1['CTPRVN_NM'] == CTP.index[14]].reset_index(drop=True)
dj_df = ksa_df1[ksa_df1['CTPRVN_NM'] == CTP.index[15]].reset_index(drop=True)
sj_df = ksa_df1[ksa_df1['CTPRVN_NM'] == CTP.index[16]].reset_index(drop=True)

kk_item = kk_df['ITEM_NM'].value_counts()
seoul_item = seoul_df['ITEM_NM'].value_counts()
kj_item = kj_df['ITEM_NM'].value_counts()
dg_item = dg_df['ITEM_NM'].value_counts()
kb_item = kb_df['ITEM_NM'].value_counts()
cb_item = cb_df['ITEM_NM'].value_counts()
kw_item = kw_df['ITEM_NM'].value_counts()
jj_item = jj_df['ITEM_NM'].value_counts()
ic_item = ic_df['ITEM_NM'].value_counts()
bs_item = bs_df['ITEM_NM'].value_counts()
kn_item = kn_df['ITEM_NM'].value_counts()
us_item = us_df['ITEM_NM'].value_counts()
jb_item = jb_df['ITEM_NM'].value_counts()
jn_item = jn_df['ITEM_NM'].value_counts()
cn_item = cn_df['ITEM_NM'].value_counts()
dj_item = dj_df['ITEM_NM'].value_counts()
sj_item = sj_df['ITEM_NM'].value_counts()

df = pd.concat([jj_item, kb_item, kn_item, cn_item, jb_item, kk_item, dg_item, kj_item, us_item, jn_item, bs_item, seoul_item, sj_item, cb_item, kw_item, ic_item, dj_item], axis = 1)
df

df.columns = ksa_df1['CTPRVN_NM'].unique()

### 데이터 결측치 제거

df.fillna('0', inplace=True)

df = df.astype(int)

df

df.index

df.sort_values(by='대전광역시', ascending = False)

df.columns

df.iloc[:,1].sort_values(ascending=False)

## 시각화

import seaborn as sns

plt.style.use("fivethirtyeight")
plt.figure(figsize=(30, 10))
sns.barplot(x=df.index, y=df.iloc[:,0].values)
plt.title("제주도 동호회 빈도", size=20)
plt.xlabel("종목", fontsize=17)
plt.ylabel("동호회 빈도수", fontsize=17)
plt.xticks(rotation = -45)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()

plt.style.use("fivethirtyeight")
plt.figure(figsize=(30, 10))
sns.barplot(x=df.index, y=df.iloc[:,1].values)
plt.title("경상북도 동호회 빈도", size=20)
plt.xlabel("종목", fontsize=17)
plt.ylabel("동호회 빈도수", fontsize=17)
plt.xticks(rotation = -45)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()

plt.style.use("fivethirtyeight")
plt.figure(figsize=(30, 10))
sns.barplot(x=df.index, y=df.iloc[:,2].values)
plt.title("경상남도 동호회 빈도", size=20)
plt.xlabel("종목", fontsize=17)
plt.ylabel("동호회 빈도수", fontsize=17)
plt.xticks(rotation = -45)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()

plt.style.use("fivethirtyeight")
plt.figure(figsize=(30, 10))
sns.barplot(x=df.index, y=df.iloc[:,3].values)
plt.title("충청남도 동호회 빈도", size=20)
plt.xlabel("종목", fontsize=17)
plt.ylabel("동호회 빈도수", fontsize=17)
plt.xticks(rotation = -45)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()

plt.style.use("fivethirtyeight")
plt.figure(figsize=(30, 10))
sns.barplot(x=df.index, y=df.iloc[:,4].values)
plt.title("전라북도 동호회 빈도", size=20)
plt.xlabel("종목", fontsize=17)
plt.ylabel("동호회 빈도수", fontsize=17)
plt.xticks(rotation = -45)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()

plt.style.use("fivethirtyeight")
plt.figure(figsize=(30, 10))
sns.barplot(x=df.index, y=df.iloc[:,5].values)
plt.title("경기도 동호회 빈도", size=20)
plt.xlabel("종목", fontsize=17)
plt.ylabel("동호회 빈도수", fontsize=17)
plt.xticks(rotation = -45)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()

plt.style.use("fivethirtyeight")
plt.figure(figsize=(30, 10))
sns.barplot(x=df.index, y=df.iloc[:,6].values)
plt.title("대구광역시 동호회 빈도", size=20)
plt.xlabel("종목", fontsize=17)
plt.ylabel("동호회 빈도수", fontsize=17)
plt.xticks(rotation = -45)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()

plt.style.use("fivethirtyeight")
plt.figure(figsize=(30, 10))
sns.barplot(x=df.index, y=df.iloc[:,7].values)
plt.title("광주광역시 동호회 빈도", size=20)
plt.xlabel("종목", fontsize=17)
plt.ylabel("동호회 빈도수", fontsize=17)
plt.xticks(rotation = -45)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()

plt.style.use("fivethirtyeight")
plt.figure(figsize=(30, 10))
sns.barplot(x=df.index, y=df.iloc[:,8].values)
plt.title("울산광역시 동호회 빈도", size=20)
plt.xlabel("종목", fontsize=17)
plt.ylabel("동호회 빈도수", fontsize=17)
plt.xticks(rotation = -45)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()

plt.style.use("fivethirtyeight")
plt.figure(figsize=(30, 10))
sns.barplot(x=df.index, y=df.iloc[:,9].values)
plt.title("전라남도 동호회 빈도", size=20)
plt.xlabel("종목", fontsize=17)
plt.ylabel("동호회 빈도수", fontsize=17)
plt.xticks(rotation = -45)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()

plt.style.use("fivethirtyeight")
plt.figure(figsize=(30, 10))
sns.barplot(x=df.index, y=df.iloc[:,10].values)
plt.title("부산광역시 동호회 빈도", size=20)
plt.xlabel("종목", fontsize=17)
plt.ylabel("동호회 빈도수", fontsize=17)
plt.xticks(rotation = -45)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()

plt.style.use("fivethirtyeight")
plt.figure(figsize=(30, 10))
sns.barplot(x=df.index, y=df.iloc[:,11].values)
plt.title("서울특별시 동호회 빈도", size=20)
plt.xlabel("종목", fontsize=17)
plt.ylabel("동호회 빈도수", fontsize=17)
plt.xticks(rotation = -45)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()

plt.style.use("fivethirtyeight")
plt.figure(figsize=(30, 10))
sns.barplot(x=df.index, y=df.iloc[:,12].values)
plt.title("세종특별자치시 동호회 빈도", size=20)
plt.xlabel("종목", fontsize=17)
plt.ylabel("동호회 빈도수", fontsize=17)
plt.xticks(rotation = -45)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()

plt.style.use("fivethirtyeight")
plt.figure(figsize=(30, 10))
sns.barplot(x=df.index, y=df.iloc[:,13].values)
plt.title("충청북도 동호회 빈도", size=20)
plt.xlabel("종목", fontsize=17)
plt.ylabel("동호회 빈도수", fontsize=17)
plt.xticks(rotation = -45)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()

plt.style.use("fivethirtyeight")
plt.figure(figsize=(30, 10))
sns.barplot(x=df.index, y=df.iloc[:,14].values)
plt.title("강원도 동호회 빈도", size=20)
plt.xlabel("종목", fontsize=17)
plt.ylabel("동호회 빈도수", fontsize=17)
plt.xticks(rotation = -45)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()

plt.style.use("fivethirtyeight")
plt.figure(figsize=(30, 10))
sns.barplot(x=df.index, y=df.iloc[:,15].values)
plt.title("인천광역시 동호회 빈도", size=20)
plt.xlabel("종목", fontsize=17)
plt.ylabel("동호회 빈도수", fontsize=17)
plt.xticks(rotation = -45)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()

plt.style.use("fivethirtyeight")
plt.figure(figsize=(30, 10))
sns.barplot(x=df.index, y=df.iloc[:,16].values)
plt.title("대전광역시 동호회 빈도", size=20)
plt.xlabel("종목", fontsize=17)
plt.ylabel("동호회 빈도수", fontsize=17)
plt.xticks(rotation = -45)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()

# 공공체육시설

import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


## 데이터 로드

df = pd.read_csv(r".\data\KS_WNTY_PHSTRN_FCLTY_STTUS_202205.csv")
df.head()

df.isna().sum()

## 데이터 전처리

df1 = df.copy()
df1 = df[['FACI_NM','FMNG_CP_NM','FMNG_CPB_NM','FACI_ROAD_ADDR1']]

df1

### 결측치 처리

df1.isna().sum()

df1["FACI_ROAD_ADDR1"].fillna('없음', inplace=True)

df1.isna().sum()

df1

df1['FMNG_CP_NM'].isna().sum()

l = df1['FMNG_CP_NM'].isna().values.tolist()

for i in range(len(l)):
    if l[i]==True:
        df1.FMNG_CP_NM[i] = df1.FACI_ROAD_ADDR1[i].split(" ")[0]

df1['FMNG_CP_NM'].value_counts()

total_df = df1[['FMNG_CP_NM']]

### 중복된 데이터 처리

total_df['FMNG_CP_NM'].replace('서울','서울특별시',inplace=True)
total_df['FMNG_CP_NM'].replace('서울시','서울특별시',inplace=True)
total_df['FMNG_CP_NM'].replace('광주','경기도',inplace=True)
total_df['FMNG_CP_NM'].replace('광주시','경기도',inplace=True)
total_df['FMNG_CP_NM'].replace('부산','부산광역시',inplace=True)
total_df['FMNG_CP_NM'].replace('부산시','부산광역시',inplace=True)
total_df['FMNG_CP_NM'].replace('경남','경상남도',inplace=True)
total_df['FMNG_CP_NM'].replace('경북','경상북도',inplace=True)
total_df['FMNG_CP_NM'].replace('전남','전라남도',inplace=True)
total_df['FMNG_CP_NM'].replace('전북','전라북도',inplace=True)
total_df['FMNG_CP_NM'].replace('경기','경기도',inplace=True)
total_df['FMNG_CP_NM'].replace('강원','강원도',inplace=True)
total_df['FMNG_CP_NM'].replace('대전','대전광역시',inplace=True)
total_df['FMNG_CP_NM'].replace('대전시','대전광역시',inplace=True)
total_df['FMNG_CP_NM'].replace('울산','울산광역시',inplace=True)
total_df['FMNG_CP_NM'].replace('울산시','울산광역시',inplace=True)
total_df['FMNG_CP_NM'].replace('인천','인천광역시',inplace=True)
total_df['FMNG_CP_NM'].replace('인천시','인천광역시',inplace=True)
total_df['FMNG_CP_NM'].replace('제주시','제주특별자치도',inplace=True)
total_df['FMNG_CP_NM'].replace('서귀포시','제주특별자치도',inplace=True)
total_df['FMNG_CP_NM'].replace('충남','충청남도',inplace=True)
total_df['FMNG_CP_NM'].replace('충북','충청북도',inplace=True)

total_df['FMNG_CP_NM'].value_counts()

### 불필요 데이터 제거

dfresult = total_df[~total_df['FMNG_CP_NM'].str.contains("로", na=False, case=False)]
dfresult = dfresult[~dfresult['FMNG_CP_NM'].str.contains("1", na=False, case=False)]
dfresult = dfresult[~dfresult['FMNG_CP_NM'].str.contains("2", na=False, case=False)]
dfresult = dfresult[~dfresult['FMNG_CP_NM'].str.contains("3", na=False, case=False)]
dfresult = dfresult[~dfresult['FMNG_CP_NM'].str.contains("4", na=False, case=False)]
dfresult = dfresult[~dfresult['FMNG_CP_NM'].str.contains("5", na=False, case=False)]
dfresult = dfresult[~dfresult['FMNG_CP_NM'].str.contains("6", na=False, case=False)]
dfresult = dfresult[~dfresult['FMNG_CP_NM'].str.contains("7", na=False, case=False)]
dfresult = dfresult[~dfresult['FMNG_CP_NM'].str.contains("8", na=False, case=False)]
dfresult = dfresult[~dfresult['FMNG_CP_NM'].str.contains("9", na=False, case=False)]
dfresult = dfresult[~dfresult['FMNG_CP_NM'].str.contains("0", na=False, case=False)]
dfresult = dfresult[~dfresult['FMNG_CP_NM'].str.contains("면", na=False, case=False)]
dfresult = dfresult[~dfresult['FMNG_CP_NM'].str.contains("읍", na=False, case=False)]
dfresult = dfresult[~dfresult['FMNG_CP_NM'].str.contains("리", na=False, case=False)]
dfresult = dfresult[~dfresult['FMNG_CP_NM'].str.contains("동", na=False, case=False)]
dfresult = dfresult[~dfresult['FMNG_CP_NM'].str.contains("길", na=False, case=False)]
dfresult = dfresult[~dfresult['FMNG_CP_NM'].str.contains("군", na=False, case=False)]

dfresult['FMNG_CP_NM'].value_counts()

## 시각화는 태블로로

# 공공기관 스포츠강좌

## 데이터 로드

lec = pd.read_csv(r'.\data\KS_OLPARKSPORTSCENTER_REGI_CLASS_INFO_202205.csv')

## 데이터 전처리

lec.head(3)

lec.columns

lec.columns = ['Sports', 'Center', 'Lesson', 'Start', 'End', 'Period', 'Member']
lec.head(3)

lec.info()

lec.isna().sum()

lec['Sports'].unique()

### Sports 중복데이터 정리

lec.loc[lec.Sports.str.contains('축구'), 'Sports'] = '축구'
lec.loc[lec.Sports.str.contains('수영'), 'Sports'] = '수영'
lec.loc[lec.Sports.str.contains('댄스'), 'Sports'] = '댄스 스포츠'
lec.loc[lec.Sports.str.contains('농구'), 'Sports'] = '농구'
lec.loc[lec.Sports.str.contains('탁구'), 'Sports'] = '탁구'
lec.loc[lec.Sports.str.contains('골프'), 'Sports'] = '골프'
lec.loc[lec.Sports.str.contains('음악'), 'Sports'] = '노래교실'
lec.loc[lec.Sports.str.contains('노래'), 'Sports'] = '노래교실'
lec.loc[lec.Sports.str.contains('팝송'), 'Sports'] = '노래교실'
lec.loc[lec.Sports.str.contains('가요'), 'Sports'] = '노래교실'
lec.loc[lec.Sports.str.contains('스쿼시'), 'Sports'] = '스쿼시'
lec.loc[lec.Sports.str.contains('다이어트'), 'Sports'] = '다이어트'
lec.loc[lec.Sports.str.contains('복싱'), 'Sports'] = '복싱'
lec.loc[lec.Sports.str.contains('바디'), 'Sports'] = '보디빌딩(헬스)'
lec.loc[lec.Sports.str.contains('헬스'), 'Sports'] = '보디빌딩(헬스)'
lec.loc[lec.Sports.str.contains('필라테스'), 'Sports'] = '필라테스'
lec.loc[lec.Sports.str.contains('요가'), 'Sports'] = '요가'
lec.loc[lec.Sports.str.contains('아쿠아'), 'Sports'] = '아쿠아 스포츠'



lec['Sports'].unique()

### 연도 관련 컬럼 재정렬

#### End 컬럼에서 2010년대 데이터 정리

d = lec['End'].str.contains('201')
lec1 = lec[~d]
lec1['End'].unique()

#### Start 컬럼에서 2010년대 데이터 정리

d1 = lec['Start'].str.contains('201')
lec1 = lec1[~d1]
lec1['Start'].unique()

d2 = lec['Start'].str.contains('200')
lec1 = lec1[~d2]
lec1.Start.unique()

d2 = lec['End'].str.contains('200')
lec1 = lec1[~d2]
lec1.Start.unique()

lec1.reset_index(drop=True, inplace=True)
lec1

lec1.Sports.nunique()

lec.Center.value_counts()

## 시각화

plt.rcParams['figure.figsize'] = (13, 11)
plt.style.use("fivethirtyeight")
ax = sns.countplot(y='Sports', data=lec1, order = lec1['Sports'].value_counts().index)
plt.xlabel('')
plt.ylabel('스포츠')
plt.tight_layout()

### 상위 15개 종목

sports15 = ['수영','보디빌딩(헬스)', '아쿠아 액티비티', '축구', '테니스', '배드민턴', '탁구',
            '필라테스', '골프', '스케이트', '(온라인)점핑트램폴린', '댄스 스포츠', '요가', '농구', '악기교실']

lec15 = lec1[lec1.Sports.apply(lambda x: True if x in sports15 else False)].reset_index(drop=True)

lec15['Sports'].value_counts()

# TOP 15
plt.style.use("fivethirtyeight")
plt.rcParams['figure.figsize'] = (10, 8)
ax = sns.countplot(y='Sports', data=lec15, order = lec15['Sports'].value_counts().index)
plt.xlabel('')
plt.ylabel('스포츠')
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.tight_layout()

lec1.head(3)

### 연도별 정리 (20 / 21 / 22)

lec15['Start'] = lec15['Start'].apply(lambda x: x[0:4])
lec15['End'] = lec15['End'].apply(lambda x: x[0:4])
lec15.head(3)

lec2020 = lec1[lec1['Start'].str.contains('2020')]
lec2020.shape[0]

lec2021 = lec1[lec1['Start'].str.contains('2021')]
lec2021.shape[0]

lec2022 = lec1[lec1['Start'].str.contains('2022')]
lec2022.shape[0]

plt.figure(figsize=(16,8))
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

# 2020
plt.subplot(1,3,1)
ax = sns.countplot(y='Sports', data=lec2020, order = lec2020['Sports'].value_counts().index)
plt.title('2020', fontsize=15)
plt.xlabel('')
plt.ylabel('스포츠')

# 2021
plt.subplot(1,3,2)
ax = sns.countplot(y='Sports', data=lec2021, order = lec2021['Sports'].value_counts().index)
plt.title('2021', fontsize=15)
plt.xlabel('')
plt.ylabel('스포츠')

# 2022
plt.subplot(1,3,3)
ax = sns.countplot(y='Sports', data=lec2022, order = lec2022['Sports'].value_counts().index)
plt.title('2022', fontsize=15)
plt.xlabel('')
plt.ylabel('스포츠')

plt.tight_layout()
plt.show()

### 연도별 TOP15

lec2020_15 = lec2020['Sports'].value_counts().to_frame().reset_index().iloc[:15, :]
lec2021_15 = lec2021['Sports'].value_counts().to_frame().reset_index().iloc[:15, :]
lec2022_15 = lec2022['Sports'].value_counts().to_frame().reset_index().iloc[:15, :]

lec2020_15.columns = ['Sports', 'Counts']
lec2021_15.columns = ['Sports', 'Counts']
lec2022_15.columns = ['Sports', 'Counts']

lec2021_15

plt.figure(figsize=(16,8))
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

# 2022
plt.subplot(1,3,1)
ax = sns.barplot(data=lec2020_15, x='Counts', y='Sports')
plt.title('2020', fontsize=15)
plt.xlabel('')
plt.ylabel('스포츠')

# 2021
plt.subplot(1,3,2)
ax = sns.barplot(data=lec2021_15, x='Counts', y='Sports')
plt.title('2021', fontsize=15)
plt.xlabel('')
plt.ylabel('스포츠')

# 2022
plt.subplot(1,3,3)
ax = sns.barplot(data=lec2022_15, x='Counts', y='Sports')
plt.title('2022', fontsize=15)
plt.xlabel('')
plt.ylabel('스포츠')

plt.tight_layout()
plt.show()

### 연도별 TOP10

lec2020_10 = lec2020['Sports'].value_counts().to_frame().reset_index().iloc[:10, :]
lec2021_10 = lec2021['Sports'].value_counts().to_frame().reset_index().iloc[:10, :]
lec2022_10 = lec2022['Sports'].value_counts().to_frame().reset_index().iloc[:10, :]
lec2020_10.columns = ['Sports', 'Counts']
lec2021_10.columns = ['Sports', 'Counts']
lec2022_10.columns = ['Sports', 'Counts']

plt.figure(figsize=(16,8))
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

# 2022
plt.subplot(1,3,1)
ax = sns.barplot(data=lec2020_10, x='Counts', y='Sports')
plt.title('2020', fontsize=15)
plt.xlabel('')
plt.ylabel('스포츠')

# 2021
plt.subplot(1,3,2)
ax = sns.barplot(data=lec2021_10, x='Counts', y='Sports')
plt.title('2021', fontsize=15)
plt.xlabel('')
plt.ylabel('스포츠')

# 2022
plt.subplot(1,3,3)
ax = sns.barplot(data=lec2022_10, x='Counts', y='Sports')
plt.title('2022', fontsize=15)
plt.xlabel('')
plt.ylabel('스포츠')

plt.tight_layout()
plt.show()

# 자격증 취득 빈도 분석

## 데이터 로드

data = pd.read_csv(r".\data\KS_PTDRCTOR_PSEXAM_INFO_202205.csv")
data.head()

data.info()

data.isnull().sum()

## 데이터 재정의

# - QF_GRADE_NM: 자격등급명
# - QF_ITM_NM: 자격종목명
# - AQ_DT: 자격취득일자
# - STAR_EFC_YY
# - ADD1: 지역

add1 = data["ADD1"].values.tolist()
df = data.dropna(axis=1)
df["ADD1"] = add1
df.head()

df = df.iloc[:, 1:]
df.head()

## 시각화

#자격증명 확인
grade = df["QF_GRADE_NM"].value_counts()
grade

### 지역별 자격증 빈도분석

plt.figure(figsize=(10, 15))
sns.barplot(x=grade.values, y=grade.index)
plt.title("지역별 체육지도자 자격증 취득 현황", size=20)
plt.xlabel("Count", fontsize=17)
plt.ylabel("자격증명", fontsize=17)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

### 종목별 빈도분석

#종목별 확인
items = df["QF_ITM_NM"].value_counts()
items

plt.figure(figsize=(10, 15))
sns.barplot(x=items.values[:20], y=items.index[:20])
plt.title("종목별 체육지도자 자격증 취득 현황 Top20", size=20)
plt.xlabel("Count", fontsize=17)
plt.ylabel("종목", fontsize=17)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()

### 연도별 취득자격증 변화율

df.head()

#일자 확인
df["AQ_DT"] = pd.to_datetime(df["AQ_DT"], format="%Y%m%d")
df.head()

df["연도"] = df["AQ_DT"].dt.year

crt_df = pd.crosstab(df["연도"], df["QF_GRADE_NM"])
crt_df.head()
# pd.crosstab(df["AQ_DT"], df["QF_GRADE_NM"]).plot(kind="line")

plt.figure(figsize=(20, 10))
sns.lineplot(data=crt_df)
plt.title("연도별 체육지도사 자격증 취득 현황", size=20)
plt.ylabel("Count", fontsize=17)
plt.xlabel("연도", fontsize=17)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()

### 연도별 체육지도사 자격증 취득 현황(지역별)

df.head()

ct_loc = pd.crosstab(df["연도"], df["ADD1"])
ct_loc.head()

plt.figure(figsize=(20, 10))
sns.lineplot(data=ct_loc, label=None)
plt.legend().remove()


df["ADD1"] = df["ADD1"].str.replace(" ", "")
replace_dict = {"서울": "서울특별시",
 "경기": "경기도",
 "부산": "부산광역시",
 "경남": "경상남도",
 "경북": "경상북도",
 "대구": "대구광역시",
 "충북": "충청북도",
 "전북": "전라북도",
 "충남": "충청남도",
 "인천": "인천광역시",
 "전남": "전라남도",
 "광주": "광주광역시",
 "대전": "대전광역시",
 "강원": "강원도",
 "제주": "제주특별자치도",
 "울산": "울산광역시",
 "강동": "서울특별시",
 "구리": "경기도",
 "수원": "경기도",
 "서울시": "서울특별시",
 "광진": "서울특별시",
 "부산시": "부산광역시",
 "순천": "전라남도",
 "부천": "경기도",
 "청주": "충청북도",
 "제주도": "제주특별자치도",
 "남양": "전라남도",
 "용인": "경기도" 
 }

df["ADD1"] = df["ADD1"].replace(replace_dict)
df["ADD1"] = df["ADD1"].replace("", "서울특별시")
df["ADD1"].value_counts()

#위도 경도 구하기
from geopy.geocoders import Nominatim

def geocoding(address):
    geolocoder = Nominatim(user_agent = 'South Korea', timeout=None)
    geo = geolocoder.geocode(address)
    crd = {"lat": str(geo.latitude), "lng": str(geo.longitude)}

    return crd

# crd = geocoding("전남")
print(geocoding("서울특별시"))
print(geocoding("경기도"))
print(geocoding("전라남도"))
# print(crd['lat'])
# print(crd['lng'])

df.head()

geo_df = list = []
for i in df["ADD1"].unique():
  geo_dict = geocoding(i)
  geo_df.append(pd.DataFrame(geo_dict, index=[i]))

total_geo_df = pd.concat(geo_df)
total_geo_df.head()

#데이터프레임 합치기
df = df.merge(total_geo_df, left_on="ADD1", right_on=total_geo_df.index, how="outer")
df.head()

### 태블로 시각화를 위해 지역이름 재정의

df.to_csv("지역별_체육지도자자격증_취득현황.csv")

#지역 전처리
df["ADD1"] = df["ADD1"].str.replace(" ", "")
df["ADD1"] = df["ADD1"].replace({"경상남도": "경남",
                                 "강동": "서울",
                                 "구리": "경기",
                                 "충청북도": "충북",
                                 "수원": "경기",
                                 "전라북도": "전북",
                                 "서울시": "서울",
                                 "광진": "서울",
                                 "청주": "충남",
                                 "부산시": "경남",
                                 "제주도": "제주",
                                 "경상북도": "경북",
                                 "전라남도": "전남",
                                 "남양": "전남",
                                 "용인": "경기",
                                 "순천": "전남",
                                 "부천": "경기"})
print(df["ADD1"].value_counts())

# 국민 체력현황 분석

import os
import numpy as np
import pandas as pd
#%%
## 데이터 로드

parent = ".\data\국민체력측정 현황 데이터"

data = []
for p in os.listdir(parent):
  path = os.path.join(parent, p)
  data.append(pd.read_csv(path, parse_dates=["TEST_YMD"]))

df = pd.concat(data, axis=0)
print(df.shape)
df.head()

df["CERT_GBN"].value_counts()

## 데이터 전처리

#참가증, 1등급, 2등급, 3등급인 사람들만 추출
# cond1 = df["CERT_GBN"] == "참가증"
cond2 = df["CERT_GBN"] == "1등급"
cond3 = df["CERT_GBN"] == "2등급"
cond4 = df["CERT_GBN"] == "3등급"

df = df[(cond2)|(cond3)|(cond4)]
print(df.shape)
# df = df[(cond1 or cond2 or cond3 or cond4)]
# print(df.shape)

df.head()

df["yaer"] = df["TEST_YMD"].dt.year
df.head()

gbn_ct = pd.crosstab(df["yaer"], df["CERT_GBN"])
gbn_ct

year_list = [2017, 2018, 2019, 2020, 2021]
for i in year_list:
  print((gbn_ct.loc[i,:] /gbn_ct.loc[i,:].sum()*100).round(1))
# print("2017년 1등급": 10762 / gbn_ct.loc[2017, :].sum()

## 시각화

gbn_ct = pd.crosstab(df["yaer"], df["CERT_GBN"])

plt.figure(figsize=(20, 10))
sns.lineplot(data=gbn_ct)
plt.title("연도별 체력측정현황", size=20)
plt.xlabel("Year", fontsize=17)
plt.ylabel("Count", fontsize=17)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.legend(loc=1, prop={'size':20})
plt.show()

# end of file
# %%
