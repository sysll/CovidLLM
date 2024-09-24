import numpy as np
import pandas as pd
def division_X(df):
    # dataFrame和list之间相互转换
    data = df.values.tolist()

    list_new = []
    list_short = []
    for i in range(0, len(data) - 1):
        # 如果i和i+1的ID相同,那就将该条样本添加到list_short中
        if data[i][0] == data[i + 1][0]:
            list_short.append(data[i])
        # 否则将list_short添加到list_new中,并且重置list_short(便于存下一个ID病人的信息)
        else:
            list_short.append(data[i])
            list_new.append(list_short)
            list_short = []

        if i == len(data) - 2:
            list_short.append(data[i + 1])
            list_new.append(list_short)

    return list_new



def delet_and_replace(list_new):


        # 替换缺失值为相同 ID 的其他值的平均数
        for group in list_new:
            for n in range(len(group[0]) - 1):
                values = [x[n + 1] for x in group]
                mean_value = np.nanmean(values)  # 使用 np.nanmean() 计算平均值，忽略 NaN 值
                for i in range(len(group)):
                    if np.isnan(group[i][n + 1]):
                        group[i][n + 1] = mean_value
        return list_new



def Get_prompt(English_subject, Chinese_subject, df):
    all_stu_score_string = []
    for i in range(df.shape[0]):  # 读取contnet部分
        a_score_string = []
        a_score_string.append(
            'As an experienced clinical medicine expert, predict COVID-19 '
            'severity (severe/mild) and predict clinical outcome (survive/death) based on serum report. '
            'The serum report is as follows: ')
        score = []
        for j in Chinese_subject:
            mid = df[j][i]
            score.append(mid)

        for j in range(0, len(Chinese_subject)):
            if not np.isnan(score[j]):
                if j == 8:
                    a_score_string.append(f"{English_subject[j]}: {score[j]}. ")
                else:
                    a_score_string.append(f"{English_subject[j]}: {score[j]}, ")
            else:
                if j == 8:
                    a_score_string.append(f"{English_subject[j]}'s value is missing. ")
                else:
                    a_score_string.append(f"{English_subject[j]}'s value is missing, ")

        result = ''.join(a_score_string)
        all_stu_score_string.append(result)
    return all_stu_score_string