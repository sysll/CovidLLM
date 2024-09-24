from all_utils import division_X
import pandas as pd
from sklearn.model_selection import train_test_split
def del_columns(data):
    t = int(0.9 * data.shape[0])
    data = data.dropna(thresh=t, axis=1)
    return data

def del_rows(data):
    t = int(0.5 * data.shape[1])    #这个t是
    data = data.dropna(thresh=t)  # 保留至少有50%非空的行
    return data

def list_to_dataframe(list_new):
    # 将list_new转换为DataFrame
    df = pd.DataFrame([item for sublist in list_new for item in sublist])
    return df

# 设定随机种子为5
seed = 8
df = pd.read_excel(r'D:\Users\ASUS\Desktop\原始数据 - 副本.xlsx')

#丢掉一些无用
df = df.drop(['首发症状','临床症状','样本ID','核酸-汇总','呼吸频率(RR)','动脉血氧分压（PaO2)','氧饱和度%（SpO2)',
              '吸氧流量（面罩或鼻导管）L/min','FiO2(%)', '发病天数'],axis = 1)
df = df.drop(['发病日期', '入院时间', '出院/死亡时间', '检测日期', 'N_IgG', '是否进入ICU', 'S1_IgG'], axis=1)


# 去掉存在部分''临床结局', '严重程度（最终）''缺失的行
df = df.dropna(axis=0, subset=['严重程度（最终）'], inplace=False)
df = df.dropna(axis=0, subset=['临床结局 '], inplace=False)

# 字符型变成数值型
df['严重程度（最终）'] = df['严重程度（最终）'].replace({
    '轻型': '轻型',
    '危重型': '重型',
    '重型': '重型',
    '无症状感染者': '轻型'
})


# # 输出缺失值
print('数据大小:', df.shape)

df = del_rows(df)
print('行处理后,数据大小:', df.shape)
df = del_columns(df)
print('列处理后,数据大小:', df.shape)


#因为这两列数据里面有int，有float，把他们都变成float。并且排除不是数值的数，把他变成NAN
df['血_RBC分布宽度CV'] = pd.to_numeric(df['血_RBC分布宽度CV'], errors='coerce')
df['血_RBC分布宽度SD'] = pd.to_numeric(df['血_RBC分布宽度SD'], errors='coerce')
df['血_嗜碱细胞(%)'] = pd.to_numeric(df['血_嗜碱细胞(%)'], errors='coerce')
df['血_嗜碱细胞(#)'] = pd.to_numeric(df['血_嗜碱细胞(#)'], errors='coerce')
df['血_血小板计数'] = pd.to_numeric(df['血_血小板计数'], errors='coerce')
df['血_中性粒细胞(%)'] = pd.to_numeric(df['血_中性粒细胞(%)'], errors='coerce')
df['血_中性粒细胞(#)'] = pd.to_numeric(df['血_中性粒细胞(#)'], errors='coerce')
df['血_单核细胞(%)'] = pd.to_numeric(df['血_单核细胞(%)'], errors='coerce')
df['血_淋巴细胞(%)'] = pd.to_numeric(df['血_淋巴细胞(%)'], errors='coerce')
df['血_淋巴细胞(#)'] = pd.to_numeric(df['血_淋巴细胞(#)'], errors='coerce')



df2 = division_X(df)
print("行处理和列处理后的患者数： "+str(len(df2)))



#因为split是随机抽取，抽的是乱的。所以要从新排一些顺序
train_temp, test_temp = train_test_split(df2, test_size=0.3, random_state=seed)
train_temp = sorted(train_temp, key=lambda x: x[0][0], reverse=False)
test_temp = sorted(test_temp, key=lambda x: x[0][0], reverse=False)



train2 = []
for i in train_temp:
    for j in i:
        train2.append(j)

import random
random.shuffle(train2)
train = pd.DataFrame(train2, columns=df.columns)
train = train.fillna(train.mean())
train.to_excel(
    ".\\feature selection train dataset.xlsx",
    engine="openpyxl")



test2 = []
for i in test_temp:
    for j in i:
        test2.append(j)

random.shuffle(test2)
test = pd.DataFrame(test2, columns=df.columns)
test = test.fillna(test.mean())
test.to_excel(
    ".\\feature selection test dataset.xlsx",
    engine="openpyxl")