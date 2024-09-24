import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import seaborn as sns
import lightgbm as lgb
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
# 创建示例数据
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
train_path = "traditional train dataset.xlsx"
test_path = "traditional test dataset.xlsx"

df_train = pd.read_excel(train_path)
df_test = pd.read_excel(test_path)

mapping = {'死亡': 1, '出院': 0}
feature = ['血_乳酸脱氢酶', '血_超敏C反应蛋白', '血_尿素', '血_中性粒细胞(%)', '血_中性粒细胞(#)', '血_LDH*0.9',
           '血_D-D二聚体定量', '血_凝血酶原活动度', '血_淋巴细胞(%)', '血_白蛋白', '血_白细胞计数']

mapp = {'男':1, '女':0}
df_train['性别'] = df_train['性别'].map(mapp)
X_train = df_train[feature]
y_train = df_train['临床结局 '].replace(mapping)
y_train = np.where(y_train == 1.0, 1, 0).astype(int)

df_test['性别'] = df_test['性别'].map(mapp)
X_test = df_test[feature]
y_test = df_test['临床结局 '].replace(mapping)
y_test = np.where(y_test == 1.0, 1, 0).astype(int)


from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100, random_state=2024)


clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# 绘制混淆矩阵
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
cm = confusion_matrix(y_test, y_pred)
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
plt.title('(c) RandomForest', fontsize=18)
plt.savefig('.\\confusion matrice\\A3.pdf')  # 注意文件路径中的斜杠
plt.show()



accuracy = accuracy_score(y_test, y_pred)
print("准确率:", accuracy)

from sklearn.metrics import classification_report
report = classification_report(y_test, y_pred, digits = 4)
print(report)