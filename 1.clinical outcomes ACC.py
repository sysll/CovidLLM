import json
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 使用微软雅黑字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
# 读取txt文件中的内容
file_path = './generated_predictions.txt'  # 请替换为你的文件路径
star_levels = []  # 用于保存星级信息的数组


with open(file_path, 'r', encoding='utf-8') as file:
    data_list = file.readlines()  # 读取所有行数据
    for line in data_list:
        try:
            json_obj = json.loads(line.strip())  # 解析每行的JSON对象
            predict_str = json_obj['predict']
            split_label = predict_str.split()
            star_levels.append(split_label[2])
        except json.JSONDecodeError:
            print("JSON解析错误")

predic_list = [0 if star == 'survive' else 1 for star in star_levels]


star_levels = []  # 用于保存星级信息的数组
with open(file_path, 'r', encoding='utf-8') as file:
    data_list = file.readlines()  # 读取所有行数据
    for line in data_list:
        try:
            json_obj = json.loads(line.strip())  # 解析每行的JSON对象
            predict_str = json_obj['labels']
            split_label = predict_str.split()
            star_levels.append(split_label[2])
        except json.JSONDecodeError:
            print("JSON解析错误")


label_list = [0 if star == 'survive' else 1 for star in star_levels]



from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# 假设的标签和预测值
y_true = label_list  # 实际标签
y_pred = predic_list  # 预测值


# 计算准确率
accuracy = accuracy_score(y_true, y_pred)
print(f"Accuracy: {accuracy:.4f}")

cm = confusion_matrix(y_true, y_pred)
total = np.sum(cm)
cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
annot_kws = {"fontsize": 27, "ha": "center", "va": "center"}
plt.figure(figsize=(5.4, 5.2))
sns.heatmap(cm_normalized, annot=True, fmt=".2%", cmap='Blues', vmin=0, vmax=1,
            annot_kws=annot_kws, cbar=False, linecolor='black', linewidths=1)
plt.xticks(np.arange(cm.shape[1]) + 0.5, fontsize=14)  # 根据你的类别数量调整
plt.yticks(np.arange(cm.shape[0]) + 0.5, fontsize=14)  # 根据你的类别数量调整
plt.xlabel('Predicted Label', fontsize=18)
plt.ylabel('True Label', fontsize=18)
plt.title('(e) Ours', fontsize=18)
plt.savefig('.\\大模型混淆矩阵\\A5.pdf')  # 注意文件路径中的斜杠
plt.show()

from sklearn.metrics import classification_report
report = classification_report(y_true, y_pred, digits=4)
print(report)