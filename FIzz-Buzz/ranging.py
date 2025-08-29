"""
这是一个介绍
"""
import math


def range_fb(start, end):
    """对指定范围内的数字使用Fizz和Buzz输出"""
    results = []
    start_int = math.ceil(start)
    end_int = math.floor(end)
    if start_int > end_int:
        results.append("范围内没有整数！")
    else:
        for i in range(start_int, end_int+1):
            results.append(f"输入的数字为 {i},结果为 {fizz_buzz(i)}")
    return results


def fizz_buzz(n):
    """实现FizzBuzz函数"""

    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    return n


def get_user_input():
    """获取用户输入"""
    start = None
    while True:
        if start is None:
            start_input = input("请输入一个起始数字：")
            if not start_input:
                print("输入不能为空！请重新输入！")
                continue
            try:
                start = float(start_input)
            except ValueError:
                print("请输入一个有效的数字！")
                continue
        end_input = input("请输入一个结束数字：")
        if not end_input:
            print("输入不能为空！请重新输入！")
            continue
        try:
            end = float(end_input)
        except ValueError:
            print("请输入一个数字！")
            continue
        if start > end:
            print("起始数字必须不大于结束数字！请重新输入！")
            choice = input(
                '是否需要重新输入start值？（输入“yes”/“y”重新输入，按任意键将重新输入end值！)\n> ').lower().strip()
            if choice in ("yes", "y"):
                start = None
                continue
            continue
        start_display = pretty_print(start)
        end_display = pretty_print(end)
        decision = input(
            f'是否确认输入的范围是 [{start_display}, {end_display}] ？（输入“yes”/“y”确认，其余任意键重新输入end值！)\n> ').lower().strip()
        if decision in ("yes", "y"):
            print(f"范围 [{start_display}, {end_display}] 确认！")
            return start_display, end_display
        else:
            start = None


def pretty_print(num: float) -> int | float:
    """去掉多余的.0数字"""
    if isinstance(num, float) and num.is_integer():
        return int(num)
    return num


def main_range():
    """主函数"""
    print("---欢迎来到FizzBuzz游戏（范围模式）---")
    while True:
        start, end = get_user_input()
        result_line = range_fb(start, end)
        print(f"---计算范围 [{start}, {end}] 内的结果---")
        for line in result_line:
            print(line)
        continue_choice = input(
            "\n是否继续？（输入\"quit\"或\"q\"退出，其余任意键继续）：\n> ").strip().lower()
        if continue_choice in ("quit", "q"):
            print("感谢游玩本模式，再见！")
            print("-"*20)
            break
        print("-"*20)
        print("继续游戏！")


if __name__ == "__main__":
    main_range()
