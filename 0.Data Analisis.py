import pandas as pd
from all_utils import division_X
df = pd.read_excel(r'D:\Users\ASUS\Desktop\用于统计.xlsx')
df2 = division_X(df)
print(f"人数有{len(df2)}人")


print(f"血清数量有{df.shape[0]}个")


average = df['年龄'].mean()
print(f"年龄的平均值是{average}，其最大值是{df['年龄'].max()}，最小值是{df['年龄'].min()}，标准差是{df['年龄'].std()}")


# 使用value_counts()方法统计每种类型的人数
type_counts = df['严重程度（最终）'].value_counts()
heavy_count = type_counts.get('重型', 0)  # 如果'重型'不存在，则返回0
light_count = type_counts.get('轻型', 0)  # 如果'轻型'不存在，则返回0
print(f"重型的人数有{heavy_count}人，轻型的人数有{light_count}人")


# 使用value_counts()方法统计每种类型的人数
type_counts = df['临床结局 '].value_counts()
heavy_count = type_counts.get('死亡', 0)  # 如果'重型'不存在，则返回0
light_count = type_counts.get('出院', 0)  # 如果'轻型'不存在，则返回0
print(f"死亡的人数有{heavy_count}人，出院的人数有{light_count}人")


# 使用value_counts()方法统计每种类型的人数
type_counts = df['性别'].value_counts()
heavy_count = type_counts.get('男', 0)  # 如果'重型'不存在，则返回0
light_count = type_counts.get('女', 0)  # 如果'轻型'不存在，则返回0
print(f"男生的人数有{heavy_count}人，女生的人数有{light_count}人")