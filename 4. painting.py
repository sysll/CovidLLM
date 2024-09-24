"""
临床结果
Feature: 年龄, Importance: 171            英文:Age
Feature: 血_淋巴细胞(%), Importance: 139     英文：Percentage of lymphocytes (LYMPH%)
Feature: 血_纤维蛋白原, Importance: 116   英文： Fibrinogen (FIB)
Feature: 血_超敏C反应蛋白, Importance: 107 英文：Hypersensitive C-reactive protein (hs-CRP)
Feature: 血_乳酸脱氢酶, Importance: 97    英文：Lactic dehydrogenase (LDH)

严重性
Feature: 血_尿酸, Importance: 121      英文：Urea
Feature: 血_乳酸脱氢酶, Importance: 101   英文：Lactic dehydrogenase (LDH)
Feature: 血_碳酸氢根, Importance: 101    英文：Bicarbonate (HCO)
Feature: 血_D-D二聚体定量, Importance: 98 英文：D-Dimer
Feature: 血_平均RBC体积, Importance: 94  英文：Red cell volume distribution width CV (RDW CV)


临床结果 85
Feature: 血_淋巴细胞(%), Importance: 0.27679065293383154
Feature: 血_超敏C反应蛋白, Importance: 0.16186797559017344
Feature: 血_中性粒细胞(%), Importance: 0.11593425140062472
Feature: 高血压(0=无，1=有), Importance: 0.1024182130533688
Feature: 年龄, Importance: 0.045672265531105656

严重程度 69
Feature: 血_D-D二聚体定量, Importance: 0.5048168738823775
Feature: 血_淋巴细胞(%), Importance: 0.11966163637898966
Feature: 血_肌酐, Importance: 0.06044686319382675
Feature: 血_白蛋白, Importance: 0.04534682987483522
Feature: 血_直接胆红素, Importance: 0.03804266931537721
['血_淋巴细胞(%)', '年龄', '血_超敏C反应蛋白', '血_中性粒细胞(%)', '高血压(0=无，1=有)', '血_D-D二聚体定量',
'血_肌酐', '血_白蛋白', '血_直接胆红素']

LYMPH% Age hs-CRP Neu% HBP D-Dimer Cr ALB BC
"""
import matplotlib.pyplot as plt
import numpy as np
clinic_feature_list = ['LYMPH%', 'hs-CRP', 'Neu%', 'HBP', 'Age']
clinic_importance_list = [0.27679, 0.16186, 0.11593, 0.10241, 0.04567]

severe_feature_list = ['D-Dimer', 'LYMPH%', 'Cr', 'ALB', 'BC']
severe_importance_list = [0.50481, 0.1196, 0.060446, 0.04534, 0.03804]


# Set up the figure and axis
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Plotting clinic features
ax[0].bar(clinic_feature_list, clinic_importance_list, color='#adc3e4')
ax[0].set_title('(a) Clinical Feature Importance', fontsize=21)
ax[0].set_xlabel('Features', fontsize=17)
ax[0].set_ylabel('Importance', fontsize=17)
ax[0].set_ylim(0, 0.7)


# Plotting severe features
ax[1].bar(severe_feature_list, severe_importance_list, color='#f9c2b9')
ax[1].set_title('(b) Severe Feature Importance', fontsize=21)
ax[1].set_xlabel('Features', fontsize=17)
ax[1].set_ylabel('Importance', fontsize=17)
ax[1].set_ylim(0, 0.7)

plt.tight_layout()
plt.show()















# import pandas as pd
# import numpy as np
# severe_map = {'重型': 1, '轻型': 0}
# clinic_map = {'死亡': 1, '出院': 0}
# df = pd.read_excel("feature selection train dataset.xlsx")
#
# A = np.array(df['严重程度（最终）'].map(severe_map))
# B = np.array(df['临床结局 '].map(clinic_map))
#
# feature_list = ['年龄', '血_淋巴细胞(%)', '血_纤维蛋白原','血_超敏C反应蛋白', '血_乳酸脱氢酶',
#                 '血_尿酸', '血_碳酸氢根', '血_D-D二聚体定量', '血_平均RBC体积']
#
# help_prompt = []
# for i in feature_list:
#     coefficient_severe = np.corrcoef(A, np.array(df[i]))[0, 1]
#     # print(f"特征{i}和疾病严重程度的相关性: {coefficient_severe}")
#
#     coefficient_clinic = np.corrcoef(B, np.array(df[i]))[0, 1]
#     # print(f"特征{i}和临床结局的相关性是: {coefficient_clinic}")
#
#     if coefficient_clinic > 0:
#         help_prompt.append(f"{i} correlates positively with clinical outcomes.")
#
# result = " ".join(help_prompt)
# print(result)
#
# """
# Age, FIB, hs-CRP, LDH, HCO, D-Dimer, RDW_CV correlate positively with clinical outcomes
# """


