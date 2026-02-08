# Numpy

可以使用该`array`函数从普通的 Python 列表或元组创建数组。

`array`将序列的序列转换为二维数组，将序列的序列的序列转换为三维数组，依此类推。

```
>>>b = np.array([(1.5, 2, 3), (4, 5, 6)])
>>>b
array([[1.5, 2. , 3. ],
       [4. , 5. , 6. ]])
```



```
c = np.array([[1, 2], [3, 4]], dtype=complex)
```

该函数`zeros`创建一个全为零的数组，该函数 `ones`创建一个全为一的数组，该函数`empty` 创建一个初始内容随机且取决于内存状态的数组。默认情况下，所创建数组的数据类型为 `dtype` `float64`

NumPy 提供了一个`arange`类似于 Python 内置函数的函数`range`，但它返回的是一个数组。

打印数组时，NumPy 的显示方式与嵌套列表类似，但布局如下：

- 最后一个轴是从左到右打印的。
- 倒数第二轴是从上到下印刷的。
- 其余部分也从上到下打印，每一部分之间用空行隔开。

然后，一维数组打印为行，二维数组打印为矩阵，三维数组打印为矩阵列表。

NumPy 数组中的乘积运算符`*`是逐元素运算的。矩阵乘法可以使用`@`运算符

许多一元计算，都是作为ndarray类进行,可以通过·axis参数指定：

```
a.sum()
b.sum(axis=0)     # sum of each column
b.min(axis=1)     # min of each row
```

**多维**数组每个轴可以有一个索引。这些索引以元组的形式给出，并用逗号分隔

例：三维：（块索引，行索引，列索引）

假设b是四维，b[i]和b[i, ...]一样，均为b[i, :, :, :]

**对多维数组进行迭代**是相对于第一个轴进行的,如果想要对数组中的每个元素执行操作，可以使用该`flat`属性

```
for element in b.flat:
    print(element)
```

可以使用各种命令来改变数组的形状。请注意，以下三个命令都会返回一个修改后的数组，但**不会改变原始数组**：

`a.ravel() `:展平为一维数组

`a.reshape(x, y)`:改变现形状

`a.T`：转置

最右边的索引“变化最快”

如果在重塑操作中指定了某个尺寸`-1`，则其他尺寸将自动计算

`column_stack((a, b))`:将一维数组作为列堆叠成一个二维数组

<img src="https://dyins-storage-01.oss-cn-guangzhou.aliyuncs.com/202602081330164.png" alt="image-20260208133007967" style="zoom:40%;float:left" />

对于维度超过两个的数组， [`hstack`](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack)会沿着其第二个轴堆叠，[`vstack`](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack)沿着其第一个轴堆叠，并且[`concatenate`](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate) 允许使用可选参数指定连接应该沿着哪个轴进行。

`np.r_[x, y]` ：按行（垂直）拼接

`np.c_[x, y]`  :  按列（水平）拼接

函数[`hsplit`](https://numpy.org/doc/stable/reference/generated/numpy.hsplit.html#numpy.hsplit)，您可以沿水平轴分割数组，既可以指定要返回的等形状数组的数量，也可以指定分割发生的列数

`np.hsplit(a, 3）`:分成三个数组

`np.hsplit(a, (3, 4))`:在第三列和第四列**后**分

简单赋值不会复制对象或其数据。

`b = a`:只是给a起了个别名叫b

<img src="https://dyins-storage-01.oss-cn-guangzhou.aliyuncs.com/202602081405862.png" alt="image-20260208140540795" style="zoom:50%;float:left" />

查看或潜复制：

`c = a.view()`:创建了一个新的数组对象，该对象会查看相同的数据。

<img src="C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20260208140413879.png" alt="image-20260208140413879" style="zoom:50%;float:left" />

深度复制：
<img src="https://dyins-storage-01.oss-cn-guangzhou.aliyuncs.com/202602081407500.png" alt="image-20260208140757443" style="zoom:50%;float:left" />







利用del 释放内存

<img src="C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20260208141221948.png" alt="image-20260208141221948" style="zoom:50%;float:left" />

(如果直接`b = a[:100]`,b和a共享内存，无法del)

高级索引：

<img src="https://dyins-storage-01.oss-cn-guangzhou.aliyuncs.com/202602081444294.png" alt="image-20260208144440207" style="zoom:50%;float:left" />

当索引数组`a`是多维的，单个索引数组引用`a`的第一维

布尔索引：

<img src="https://dyins-storage-01.oss-cn-guangzhou.aliyuncs.com/202602081452245.png" alt="image-20260208145238160" style="zoom:50%;float:left" />

ix_()函数：将输入的一维数组转换为可以进行**广播**运算的多维网格结构

使用`newaxis`索引运算符添加一个新轴



