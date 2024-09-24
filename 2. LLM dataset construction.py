import numpy as np
import pandas as pd
from all_utils import Get_prompt
df = pd.read_excel("第一号训练数据.xlsx")
severe_map = {'重型':'severe', '轻型': 'mild'}
clinic_map = {'死亡':'death', '出院': 'survive'}
df['临床结局 '] = df['临床结局 '].map(clinic_map)
df['严重程度（最终）'] = df['严重程度（最终）'].map(severe_map)

English_subject = [ "LYMPH%", "Age", "hs-CRP", "Neu%", "HBP", "D-Dimer", "Cr",  "ALB",  "BC" ]
Chinese_subject = ['血_淋巴细胞(%)', '年龄', '血_超敏C反应蛋白', '血_中性粒细胞(%)', '高血压(0=无，1=有)', '血_D-D二聚体定量',
'血_肌酐', '血_白蛋白', '血_直接胆红素']

all_stu_score_string = Get_prompt(English_subject, Chinese_subject, df)

all_label = []
label = []
for i in range(df.shape[0]):
    remark1 = df['严重程度（最终）'][i]
    label.append(remark1)
    label.append(" and ")

    remark2 = df['临床结局 '][i]
    label.append(remark2)

    result = "".join(label)
    all_label.append(result)
    label = []


import json
for i in range(df.shape[0]):  # 假设用户要输入两组内容
    content = all_stu_score_string[i]
    summary = all_label[i]

    # 构造单个产品的JSON对象
    product = {
        "content": content,
        "summary": summary
    }

    # 将单个产品的JSON对象转换为字符串并写入文件
    with open('.\\大语言模型数据集\\train.json','a', encoding='utf-8') as jsonl_file:
        jsonl_file.write(json.dumps(product, ensure_ascii=False) + '\n')

print("数据已按JSON Lines格式保存到products_info.jsonl文件中。")











#下面是构建测试集
import numpy as np
import pandas as pd
df = pd.read_excel("第一号测试数据.xlsx")
df['临床结局 '] = df['临床结局 '].map(clinic_map)
df['严重程度（最终）'] = df['严重程度（最终）'].map(severe_map)

English_subject = [ "LYMPH%", "Age", "hs-CRP", "Neu%", "HBP", "D-Dimer", "Cr",  "ALB",  "BC" ]
Chinese_subject = ['血_淋巴细胞(%)', '年龄', '血_超敏C反应蛋白', '血_中性粒细胞(%)', '高血压(0=无，1=有)', '血_D-D二聚体定量',
'血_肌酐', '血_白蛋白', '血_直接胆红素']
all_stu_score_string = Get_prompt(English_subject, Chinese_subject, df)



all_label = []
label = []
for i in range(df.shape[0]):
    remark1 = df['严重程度（最终）'][i]
    label.append(remark1)

    label.append(" and ")

    remark2 = df['临床结局 '][i]
    label.append(remark2)

    result = "".join(label)
    all_label.append(result)
    label = []



import json
for i in range(df.shape[0]):  # 假设用户要输入两组内容
    content = all_stu_score_string[i]
    summary = all_label[i]

    # 构造单个产品的JSON对象
    product = {
        "content": content,
        "summary": summary
    }

    # 将单个产品的JSON对象转换为字符串并写入文件
    with open('.\\大语言模型数据集\\dev.json','a', encoding='utf-8') as jsonl_file:
        jsonl_file.write(json.dumps(product, ensure_ascii=False) + '\n')

print("数据已按JSON Lines格式保存到products_info.jsonl文件中。")