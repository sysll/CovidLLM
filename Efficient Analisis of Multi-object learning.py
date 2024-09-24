# import json
# import matplotlib.pyplot as plt
#
# plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 使用微软雅黑字体
# plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
# # 读取txt文件中的内容
# file_path = 'generated_predictions.txt'  # 请替换为你的文件路径
#
# bar = [0]*8
#
# with open(file_path, 'r', encoding='utf-8') as file:
#     data_list = file.readlines()  # 读取所有行数据
#     for line in data_list:
#         try:
#             json_obj = json.loads(line.strip())  # 解析每行的JSON对象
#             predict_str = json_obj['predict']
#             if(predict_str == "mild and survive"):
#                 bar[0] = bar[0]+1
#             elif(predict_str == "mild and death"):
#                 bar[1] = bar[1] + 1
#             elif (predict_str == "severe and survive"):
#                 bar[2] = bar[2] + 1
#             elif (predict_str == "severe and death"):
#                 bar[3] = bar[3] + 1
#             else:
#                 print("有问题")
#
#         except json.JSONDecodeError:
#             print("JSON解析错误")
#
#
#
#
# with open(file_path, 'r', encoding='utf-8') as file:
#     data_list = file.readlines()  # 读取所有行数据
#     for line in data_list:
#         try:
#             json_obj = json.loads(line.strip())  # 解析每行的JSON对象
#             predict_str = json_obj['labels']
#             if (predict_str == "mild and survive"):
#                 bar[4] = bar[4] + 1
#             elif (predict_str == "mild and death"):
#                 bar[5] = bar[5] + 1
#             elif (predict_str == "severe and survive"):
#                 bar[6] = bar[6] + 1
#             elif (predict_str == "severe and death"):
#                 bar[7] = bar[7] + 1
#             else:
#                 print("有问题")
#         except json.JSONDecodeError:
#             print("JSON解析错误")
#
#
#
# print(bar)


def mapp(predict_str):
    if(predict_str == "mild and survive"):
            return 0
    elif(predict_str == "mild and death"):
            return 1
    elif (predict_str == "severe and survive"):
            return 2
    elif (predict_str == "severe and death"):
            return 3
    else:
        print("有问题")


import json
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 使用微软雅黑字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
# 读取txt文件中的内容
file_path = '../generated_predictions.txt'  # 请替换为你的文件路径

predict = []
with open(file_path, 'r', encoding='utf-8') as file:
    data_list = file.readlines()  # 读取所有行数据
    for line in data_list:
        try:
            json_obj = json.loads(line.strip())  # 解析每行的JSON对象
            predict_str = json_obj['predict']
            predict.append(predict_str)
        except json.JSONDecodeError:
            print("JSON解析错误")

predict = list(map(mapp, predict))

label = []
with open(file_path, 'r', encoding='utf-8') as file:
    data_list = file.readlines()  # 读取所有行数据
    for line in data_list:
        try:
            json_obj = json.loads(line.strip())  # 解析每行的JSON对象
            predict_str = json_obj['labels']
            label.append(predict_str)
        except json.JSONDecodeError:
            print("JSON解析错误")
label = list(map(mapp, label))


from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
# 假设的标签和预测值
y_true = label  # 实际标签
y_pred = predict  # 预测值
print(y_true)

# # 计算准确率
# accuracy = accuracy_score(y_true, y_pred)
# print(f"Accuracy: {accuracy:.4f}")
#
# # 计算混淆矩阵
# cm = confusion_matrix(y_true, y_pred)
# print("Confusion Matrix:")
# print(cm)
#
# # 绘制混淆矩阵
# disp = ConfusionMatrixDisplay(confusion_matrix=cm,
#                               display_labels=["Class 0", "Class 1"])
# disp.plot(cmap='Blues')
# plt.show()