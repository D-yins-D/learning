class Book:
    total_books = 0  # 类变量：所有书的总数

    def __init__(self, title, author, count = 1):
        self.title = title
        self.author = author
        Book.total_books += count
        # 私有属性
        self.__total_stock = count
        self.__current_stock = count

    def get_current_stock(self):
        return self.__current_stock

    def get_total_stock(self):
        return self.__total_stock

    def set_current_stock(self, count):
        self.__current_stock = count

    def set_total_stock(self, count):
        self.__total_stock = count

    def borrow(self):
        pass

    def return_book(self):
        if self.__current_stock < self.__total_stock:
            self.__current_stock += 1
            print(f"已归还《{self.title}》，当前可用库存：{self.__current_stock}")
        else:
            print(f"《{self.title}》库存已满，无需归还。")

    def display(self):
        return f"《{self.title}》 | 作者：{self.author} | 库存：{self.__current_stock}/{self.__total_stock}"

class NormalBook(Book):
    def borrow(self):
        current = self.get_current_stock()
        if current <= 0:
            # 抛出异常
            raise ValueError(f"库存不足，《{self.title}》已经全部借出。")
        self.set_current_stock(current - 1)
        print(f"成功借出《{self.title}》，剩余{self.get_current_stock()}本")


class ReferenceBook(Book):
    def borrow(self):
        # 不能借，抛出异常
        print(f"【禁止外借】《{self.title}》为馆内参考书，请在阅览室阅读。")


class Library:
    def __init__(self, name):
        self.name = name
        self.bookshelf = []

    # 展示所有详细信息
    def show_bookshelf(self):
        current_total = 0
        print(f"{self.name}库存详情")
        for book in self.bookshelf:
            print(book.display())
            current_total +=book.get_current_stock()
        print(f"总库存：{Book.total_books}本   目前剩余：{current_total}本")

    # 查询
    def query(self, keyword):
        result = []
        for book in self.bookshelf:
            if keyword == book.title or keyword == book.author:
                result.append(book)
        return result

    # 打印查询
    def show_query(self, keyword):
        try:
            result = self.query(keyword)
            if not result:
                raise NameError(f"没有找到匹配{keyword}的结果")
            print(f"找到了，结果如下：")
            final_result = list(map(lambda book: book.display(), result))
            print(*final_result, sep="\n")
        except NameError as e:
            print(f"{e}")

    # 借书
    def borrow_book(self, title):
        try:
            result = self.query(title)
            if not result:
                raise NameError(f"没有找到《{title}》，无法借出")
            result[0].borrow()
        except (NameError, ValueError) as e:
            print(f"{e}")

    # 还书
    def return_book(self, title):
        try:
            result = self.query(title)
            if result:
                result[0].return_book()
            else:
                raise NameError(f"没有找到《{title}》，无法完成还书操作")
        except (ValueError, NameError) as e:
            print(f"{e}")

    # 删除
    def remove_book(self, title):
        result = self.query(title)
        try:
            if not result:
                raise NameError(f"没有找到《{title}》，无法完成删除操作")
            self.bookshelf.remove(result[0])
            Book.total_books -= result[0].get_total_stock()
            print(f"已经删除了《{title}》相关书籍")
        except NameError as e:
            print(f"{e}")

    # 更新
    def update_book(self, title, author, add_count, book_type):
        result = self.query(title)
        if result:
            result[0].set_current_stock(add_count + result[0].get_current_stock())
            result[0].set_total_stock(add_count + result[0].get_total_stock())
            Book.total_books += add_count
            print(f"已为现有的《{title}》追加库存")
        else:
            if book_type == "1":
                new_book = NormalBook(title, author, add_count)
                print(f"发现新书，作为【NormalBook】类型录入")
            else:
                new_book = ReferenceBook(title, author, add_count)
                print(f"发现新书，作为【ReferenceBook】类型录入")
            self.bookshelf.append(new_book)

    # 存盘
    def saving(self):
        with open("library.txt", "w", encoding="utf-8") as f:
            for book in self.bookshelf:
                line = f"{book.title},{book.author},{book.get_total_stock()},{book.get_current_stock()},{book.__class__.__name__}\n"
                f.write(line)
        print("数据已成功同步到本地文件")

    # 读盘
    def loading(self):
        try:
            with open("library.txt", "r", encoding="utf-8") as f:
                self.bookshelf = []
                Book.total_books = 0

                for line in f:
                    data = line.strip().split(",")
                    if len(data) < 5: continue
                    title, author, total, current, b_type = data[0], data[1], int(data[2]), int(data[3]), data[4]
                    if b_type == "NormalBook":
                        new_book = NormalBook(title, author, total)
                    else:
                        new_book = ReferenceBook(title, author, total)
                    new_book.set_current_stock(current)
                    self.bookshelf.append(new_book)
            print("历史数据加载成功！")
        except FileNotFoundError:
            print("未发现历史数据，开启全新库。")


def main():
    lib = Library("图书库存管理系统")
    lib.loading()

    # lib.add_book(NormalBook("西游记", "吴承恩", 2))
    # lib.add_book(NormalBook("三国杀", "未知", 3))
    # lib.add_book(ReferenceBook("工具书1", "国家级作者1", 3))

    while True:
        print(f"------{lib.name}------")
        print("1-录入/更新\n2-查询\n3-展示\n4-借书\n5-还书\n6-删除\n0-退出")
        choice = input("请输入你的选择：")
        if choice == "1":
            try:
                t = input("请输入书名：")
                a = input("请输入作者：")
                c = int(input("请输入数量："))
                type_code = input("请输入类型：1.普通书（可外借）  2.参考书（不可外借）")
                lib.update_book(t, a, c, type_code)
                lib.saving()
            except ValueError:
                print("数量必须是数字，请重试")

        elif choice == "2":
            lib.show_query(input("请输入要查询的书名："))

        elif choice == "3":
            lib.show_bookshelf()

        elif choice == "4":
            lib.borrow_book(input("请输入要借的书名："))
            lib.saving()

        elif choice == "5":
            lib.return_book(input("请输入要还的书名："))
            lib.saving()

        elif choice == "6":
            lib.remove_book(input("请输入要删除的书名："))
            lib.saving()

        elif choice == "0":
            print(f"退出{lib.name}")
            lib.saving()
            break

        else:
            print("无效选择")

main()

