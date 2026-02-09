import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:\ziliao\CSV file\housing.csv")

# 读取数据
print("数据预览前5行：")
print(df.head().to_string())
print("数据基本信息：")
print(df.info())
print("数值列统计描述：")
print(df.describe())

# 替换空字段
print("处理前空字段数量:")
print(df.isnull().sum())
median_bedrooms = df["total_bedrooms"].median()
df["total_bedrooms"] = df["total_bedrooms"].fillna(median_bedrooms)
print("处理后空字段数量:")
print(df.isnull().sum())

# 处理重复数据
duplicated_sum = df.duplicated().sum()
print(f"处理前重复行数量：{duplicated_sum}")
if duplicated_sum > 0:
    df = df.drop_duplicates()
print(f"处理后重复行数量：{df.duplicated().sum()}")

# 相关性分析
correlation_matrix = df.corr(numeric_only=True)
corr_price = correlation_matrix["median_house_value"].sort_values(ascending = False)
print("与房价的相关性（从高到低）：")
print(corr_price)

# 可视化相关性

corr_price.plot(kind = "bar", y = "与‘median_house_value'的相关性", figsize = (12, 8))
plt.show()