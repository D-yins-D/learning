raw_data = ["85", "92", "ERROR", "105", "78", "WARNING", "99", "120"]
# 清洗与过滤函数
def cleaned(data):
    clean_data = []
    # 跳过非数字项
    for x in data:
        try:
            num = float(x)
            clean_data.append(num)
        except ValueError:
            continue
    # 仅保留≥80 数值
    filtered = [num for num in clean_data if num>=80]
    return filtered

# 归一化
def guiyi(data):
    gui_list = []
    max_data = max(data)
    for num in data:
        gui_num = num / max_data
        if gui_num > 1.0:
            status = "核心过载"
        else:
            status = "运转正常"
        gui_list.append({num: status})
    print(gui_list)

cleaned = cleaned(raw_data)
guiyi(cleaned)