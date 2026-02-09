# pandas

`Series`函数：

```
pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
```

<img src="https://dyins-storage-01.oss-cn-guangzhou.aliyuncs.com/202602091325305.png" alt="image-20260209132504174" style="zoom:67%;float:left" />

一些常用函数示例：

```
import pandas as pd
# 创建 Series
data = [1, 2, 3, 4, 5, 6]
index = ['a', 'b', 'c', 'd', 'e', 'f']
s = pd.Series(data, index=index)
# 获取索引
index = s.index
# 获取值数组
values = s.values
# 获取描述统计信息
stats = s.describe()
# 获取最大值和最小值的索引
max_index = s.idxmax()
min_index = s.idxmin()
# 其他属性和方法
print(s.dtype)   # 数据类型
print(s.shape)   # 形状
print(s.size)    # 元素个数
print(s.head())  # 前几个元素，默认是前 5 个
print(s.tail())  # 后几个元素，默认是后 5 个
print(s.sum())   # 求和
print(s.mean())  # 平均值
print(s.std())   # 标准差
print(s.min())   # 最小值
print(s.max())   # 最大值
s = s.astype('float64')  # 将 Series 中的所有元素转换为 float64 类型
s_doubled = s.map(lambda x: x * 2)  # 使用 map 函数将每个元素加倍
cumsum_s = s.cumsum()  # 计算累计和
 s.isnull()  # 查找缺失值（这里没有缺失值，所以返回的全是 False）
sorted_s = s.sort_values()  # 排序
```

```
s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
value = s[2]  # 获取索引为2的值
subset = s[1:4]  # 获取索引为1到3的值
value = s['b']  # 获取索引为'b'的值
print(s['a':'c'])  # 返回索引标签 'a' 到 'c' 之间的元素
print(s[:3])  # 返回前三个元素
s['a'] = 10  # 将索引标签 'a' 对应的元素修改为 10
s['e'] = 5  # 在 Series 中添加一个新的元素，索引标签为 'e'
del s['a']  # 删除索引标签 'a' 对应的元素
s_dropped = s.drop(['b'])  # 返回一个删除了索引标签 'b' 的新 Series
filtered_series = series[series > 2]  # 选择大于2的元素
```

`DataFrame`:

```
pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
```

使用 **loc** 属性返回指定行的数据,返回结果其实就是一个 Pandas Series 数据;

也可以返回多行数据，使用 **[[ ... ]]** 格式，**...** 为各行的索引，以逗号隔开,此时返回结果其实就是一个 Pandas DataFrame 数据。也可以使用 **loc** 属性返回指定索引对应到某一行。

```
import pandas as pd
# 创建 DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)
# 查看 DataFrame 的基本信息
print(df.info())
# 按年龄排序
df_sorted = df.sort_values(by='Age', ascending=False)
print(df_sorted)
# 选择指定列
print(df[['Name', 'Age']])
# 按索引选择行
print(df.iloc[1:3])  # 选择第二到第三行（按位置）
# 按标签选择行
print(df.loc[1:2])  # 选择第二到第三行（按标签）
# 计算分组统计（按城市分组，计算平均年龄）
print(df.groupby('City')['Age'].mean())
# 处理缺失值（填充缺失值）
df['Age'] = df['Age'].fillna(30)
# 导出为 CSV 文件
df.to_csv('output.csv', index=False)
# 使用concat添加新行
new_row = pd.DataFrame([[4, 7]], columns=['A', 'B'])  # 创建一个只包含新行的DataFrame
df = pd.concat([df, new_row], ignore_index=True)  # 将新行添加到原始DataFrame
```

```
# 纵向合并
pd.concat([df1, df2], ignore_index=True)
# 横向合并
pd.merge(df1, df2, on='Column1')
```

## csv

`pd.read_csv()`：从csv文件读取数据并加载为DataFrame

<img src="https://dyins-storage-01.oss-cn-guangzhou.aliyuncs.com/202602091423544.png" alt="image-20260209142306401" style="zoom:60%;float:left" />

`DataFrame.to_csv()`：将 DataFrame 写入到 CSV 文件

<img src="https://dyins-storage-01.oss-cn-guangzhou.aliyuncs.com/202602091424506.png" alt="image-20260209142449364" style="zoom:60%;float:left" />

**to_string()** 用于返回 DataFrame 类型的数据，如果不使用该函数，则输出结果为数据的前面 5 行和末尾 5 行，

## 数据清洗

### 空字段数据

`isnull()`:判断各个单元格是否为空，Pandas 把 n/a 和 NA 当作空数据，na 不是空数据

`dropna()`:删除包括空字段的行

```
DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
```

<img src="https://dyins-storage-01.oss-cn-guangzhou.aliyuncs.com/202602091542260.png" alt="image-20260209154244118" style="zoom:80%;float:left" />

`fillna()`：替换空字段

```
df['PID'].fillna(12345, inplace = True)  # 使用 12345 替换 PID 为空数据：
```

`mean()`:均值    `median()`:中位数值   `mode（）`：众数

替换空单元格的常用方法是计算列的均值、中位数值或众数。

### 格式错误数据

格式化日期**to_datetime(x, format = 'mixed')**

`df['Date'] = pd.to_datetime(df['Date'], format='mixed')`

<img src="https://dyins-storage-01.oss-cn-guangzhou.aliyuncs.com/202602091555065.png" alt="image-20260209155545963" style="zoom:50%;float:left" />

`df.astype()`:转换数据类型

### 错误数据

例子：`df.loc[2, 'age'] = 30 # 修改第2行age列的数据`

`drop(x)`:删除第x行

### 重复数据

`duplicated()`:如果对应的数据是重复的，会返回 True，否则返回 False。

`drop_duplicates()`:删除重复数据

### 类别编码

`pd.get_dummies()`:将每个类别转换为一个新的二进制特征（独热编码）

### 标准化和归一化

`StandardScaler()`:将数据转换为均值为0，标准差为1的分布。

`MinMaxScaler()`:将数据缩放到指定的范围（如 [0, 1]）

## 常用函数

![image-20260209163601832](https://dyins-storage-01.oss-cn-guangzhou.aliyuncs.com/202602091636943.png)

![image-20260209163547528](https://dyins-storage-01.oss-cn-guangzhou.aliyuncs.com/202602091635677.png)

![image-20260209163626213](https://dyins-storage-01.oss-cn-guangzhou.aliyuncs.com/202602091636356.png)

![image-20260209163759922](https://dyins-storage-01.oss-cn-guangzhou.aliyuncs.com/202602091638058.png)

![image-20260209163845523](https://dyins-storage-01.oss-cn-guangzhou.aliyuncs.com/202602091638618.png)

![image-20260209163915965](https://dyins-storage-01.oss-cn-guangzhou.aliyuncs.com/202602091639084.png)

![image-20260209163932109](https://dyins-storage-01.oss-cn-guangzhou.aliyuncs.com/202602091639225.png)

## 相关性

### corr()

计算数据集中每列之间的关系(method,min_periods都是可选的):

```
df.corr(method='pearson', min_periods=1)
```

返回一个相关系数矩阵，矩阵的行和列对应数据框的列名，矩阵的元素是对应列之间的相关系数

相关性矩阵是一个对称矩阵，矩阵中的每个值表示两个变量之间的相关系数。

### 相关性矩阵

可以通过 corr() 方法直接计算 DataFrame 中所有变量的相关性矩阵。

### 可视化

#### 1.基本的 `plot()` 方法:

| **参数**  | **说明**                                                     |
| :-------- | :----------------------------------------------------------- |
| `kind`    | 图表类型，支持 `'line'`, `'bar'`, `'barh'`, `'hist'`, `'box'`, `'kde'`, `'density'`, `'area'`, `'pie'` 等类型 |
| `x`       | 设置 x 轴的数据列                                            |
| `y`       | 设置 y 轴的数据列                                            |
| `title`   | 图表的标题                                                   |
| `xlabel`  | x 轴的标签                                                   |
| `ylabel`  | y 轴的标签                                                   |
| `color`   | 设置图表的颜色                                               |
| `figsize` | 设置图表的大小（宽, 高）                                     |
| `legend`  | 是否显示图例                                                 |

#### 2. 常用图表类型

| **图表类型**   | **描述**                                             | **常用用法**                                  |
| :------------- | :--------------------------------------------------- | :-------------------------------------------- |
| **折线图**     | 用于显示随时间变化的数据趋势                         | `df.plot(kind='line')`                        |
| **柱状图**     | 用于显示类别之间的比较数据                           | `df.plot(kind='bar')`                         |
| **水平柱状图** | 与柱状图类似，但柱子是水平的                         | `df.plot(kind='barh')`                        |
| **直方图**     | 用于显示数据的分布（频率分布）                       | `df.plot(kind='hist')`                        |
| **散点图**     | 用于显示两个数值变量之间的关系                       | `df.plot(kind='scatter', x='col1', y='col2')` |
| **箱线图**     | 用于显示数据的分布、异常值及四分位数                 | `df.plot(kind='box')`                         |
| **密度图**     | 用于显示数据的密度分布                               | `df.plot(kind='kde')`                         |
| **饼图**       | 用于显示各部分占总体的比例                           | `df.plot(kind='pie')`                         |
| **区域图**     | 用于显示累计数值的图表（类似于折线图，但填充了颜色） | `df.plot(kind='area')`                        |