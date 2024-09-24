import numpy as np
import pandas as pd
import lightgbm as lgb
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
# 创建示例数据
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
train_path = "feature selection train dataset.xlsx"
test_path = "feature selection test dataset.xlsx"

df_train = pd.read_excel(train_path)
df_test = pd.read_excel(test_path)

mapping = {'重型': 0, '轻型': 1}


mapp = {'男':1, '女':0}
df_train['性别'] = df_train['性别'].map(mapp)
X_train = df_train.drop(['临床结局 ', '严重程度（最终）'], axis=1)
y_train = df_train['严重程度（最终）'].replace(mapping)
y_train = np.where(y_train == 1.0, 1, 0).astype(int)


df_test['性别'] = df_test['性别'].map(mapp)
X_test = df_test.drop(['临床结局 ', '严重程度（最终）'], axis=1)
y_test = df_test['严重程度（最终）'].replace(mapping)
y_test = np.where(y_test == 1.0, 1, 0).astype(int)


from sklearn.ensemble import GradientBoostingClassifier
clf = GradientBoostingClassifier(n_estimators=100, learning_rate=0.01, max_depth=3, random_state=2024)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)


#打印特征以及其重要性权重
feature_importances = clf.feature_importances_
feature_names = X_train.columns

# 将特征及其重要性组合成元组，并按重要性排序
sorted_features = sorted(zip(feature_names, feature_importances), key=lambda x: x[1], reverse=True)

# 打印排序后的特征及其重要性
for name, importance in sorted_features:
    print(f"Feature: {name}, Importance: {importance}")






# 绘制混淆矩阵
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                              display_labels=['出院', '死亡'])
disp.plot(cmap='Blues')
plt.title('Confusion Matrix')
plt.show()


accuracy = accuracy_score(y_test, y_pred)
print("准确率:", accuracy)

from sklearn.metrics import classification_report
report = classification_report(y_test, y_pred)
print(report)