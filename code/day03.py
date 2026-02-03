oldnew = " Agent:007_Bond; Coords:(40,74); Items:gun,money,gun;Mission:2025-RESCUE-X "
oldnew = oldnew.replace(" ","")   # 去除空格
oldnew = oldnew.split(";")  # 分割字符串信息
# 提取特工代号
agent = oldnew[0].split(":")[1]
# 利用Set对装备去重
items = set(oldnew[2].split(":")[1].split(","))
items = list(set(items))
# 利用Slicing获取核心任务
mission = oldnew[3].split(":")[1]
mission = mission[5:-2]
# 利用Tuple获取坐标
coords = oldnew[1].split(":")[1]
coords = coords.strip("()")
x, y = coords.split(",")
coords = (int(x), int(y))
# 利用Dict归档
dicts = {"特工代号": agent,
        "坐标": coords,
        "装备": items,
        "核心任务": mission
        }
print("情报档案：\n", dicts)

