# 合併排序演算法
def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    if right:
        result += right
    return result


def divide(test):
    if len(test) <= 1:
        return test
    mid = len(test)//2
    left = test[:mid]
    right = test[mid:]

    left = divide(left)
    right = divide(right)
    return merge(left, right)

def main():
    a = eval(input("請輸入一串列:"))
    print(divide(a))


main()
