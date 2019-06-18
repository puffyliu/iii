# 2. 產生一個class名為Stack，有一個成員變數為一串列(用以存放資料)；
# 有兩個成員方法push()和pop()，分別用來放資料和取資料。
# 產生一個exception class名為StackEmptyError，用來處理Stack空的狀況。
# 提示：Stack以先進後出(First In Last Out)的方式存取資料。
# 寫一個class繼承Exception，push要給值，pop不用
class Stack:
    def __init__(self, list1):
        self.list1 = list1

    def push(self, data):
        self.list1.append(data)

    def pop(self):
        self.list1.pop()

    def __str__(self):
        return "list1 = {}".format(self.list1)

class StackEmptyError(Exception):
    pass


def main():
    try:
        s = Stack([])
        while True:
            n = int(input("請選擇要(1)push還是(2)pop:"))
            if n == 1:
                while True:
                    push_value = eval(input("請輸入要push的值:"))
                    if push_value != 'none':
                        s.push(push_value)
                    else:
                        break
            elif n == 2:
                if len(s.list1) == 0:
                    raise StackEmptyError
                else:
                    s.pop()
                    continue
            else:
                break
    except StackEmptyError:
        print("stack為空時不可pop!")
    except:
        print("就是有錯啦!")
    finally:
        print(s)

main()