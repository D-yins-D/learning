# 导入数据处理包
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.close('all')

# 显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号

# 导入数据集
df = pd.read_csv("D:\\ziliao\\CSV file\\Titanic\\train.csv")

# 查看数据结构
print(df.head().to_string())
print(df.info())
print(df.describe())

# 数据预处理
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# 数据分析
# 乘客总体存活率
n = df["Survived"].value_counts()
print(n)
plt.pie(n, autopct="%.2f%%", labels = ["死亡", "存活"])
plt.title("总体生还率")
plt.show()

# 不同性别生还率
sex_count = df.groupby("Sex")["Survived"].value_counts()
print(sex_count)
plt.subplot(1, 2, 1).pie(sex_count["female"], autopct = "%.2f%%", labels = ["存活", "死亡"])
plt.title("女性生还率")
plt.subplot(1, 2, 2).pie(sex_count["male"], autopct = "%.2f%%", labels = ["存活", "死亡"])
plt.title("男性生还率")
plt.suptitle("不同性别生还率")
plt.show()

# 不同年龄段生还率
age_range = ["0-10", "11-20", "21-30", "31-40", "41-50", "51-60", "61+"]
bins = [0, 10, 20, 30, 40, 50, 60, 100]
df["Age_group"] = pd.cut(df["Age"], bins, labels=age_range)
age_survival_rate = df.groupby("Age_group")["Survived"].mean()
print(age_survival_rate)
plt.bar(x = age_range, height = age_survival_rate)
plt.title("各年龄段生还率")
plt.show()

# 登船港口与生还率关系
embarked_count = df.groupby("Embarked")["Survived"].value_counts().sort_index()
print(embarked_count)
plt.subplot(1, 3, 1).pie(embarked_count["C"], autopct = "%.2f%%", labels = ["死亡", "存活"])
plt.title("瑟堡乘客生还率")
plt.subplot(1, 3, 2).pie(embarked_count["S"], autopct = "%.2f%%", labels = ["死亡", "存活"])
plt.title("南安普顿乘客生还率")
plt.subplot(1, 3, 3).pie(embarked_count["Q"], autopct = "%.2f%%", labels = ["死亡", "存活"])
plt.title("皇后镇乘客生还率")
plt.suptitle("不同登港口生还率")
plt.show()

# 不同舱位与生还率关系
pclass_count = df.groupby("Pclass")["Survived"].value_counts().sort_index()
print(pclass_count)
plt.subplot(1, 3, 1).pie(pclass_count[1], autopct = "%.2f%%", labels = ["死亡", "存活"])
plt.title("一等舱乘客生还率")
plt.subplot(1, 3, 2).pie(pclass_count[2], autopct = "%.2f%%", labels = ["死亡", "存活"])
plt.title("二等舱乘客生还率")
plt.subplot(1, 3, 3).pie(pclass_count[3], autopct = "%.2f%%", labels = ["死亡", "存活"])
plt.title("三等舱乘客生还率")
plt.suptitle("不同舱位生还率")
plt.show()

# 不同港口乘客的舱位关系
embarked_pclass_count = df.groupby("Embarked")["Pclass"].value_counts().sort_index()
print(embarked_pclass_count)
plt.subplot(1, 3, 1).pie(embarked_pclass_count["C"], autopct = "%.2f%%", labels =["一等舱", "二等舱", "三等舱"])
plt.title("瑟堡舱位分布")
plt.subplot(1, 3, 2).pie(embarked_pclass_count["S"], autopct = "%.2f%%", labels =["一等舱", "二等舱", "三等舱"])
plt.title("南安普顿舱位分布")
plt.subplot(1, 3, 3).pie(embarked_pclass_count["Q"], autopct = "%.2f%%", labels =["一等舱", "二等舱", "三等舱"])
plt.title("皇后镇舱位分布")
plt.suptitle("不同港口乘客的舱位关系")
plt.show()

# 不同票价生还率
plt.scatter(df[df["Survived"]==0]["Fare"],df[df["Survived"]==0]["Survived"], c = "blue", label = "死亡", s = 10)
plt.scatter(df[df["Survived"]==1]["Fare"],df[df["Survived"]==1]["Survived"], c = "red", label = "生还", s = 10)
plt.xlabel("票价")
plt.ylabel("是否生还 0-否 1-是")
plt.title("票价与生还情况")
plt.legend()
plt.grid(True)
plt.show()