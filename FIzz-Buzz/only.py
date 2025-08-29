"""
这是一个介绍
"""


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
    while True:
        user = input("请输入你的数字：")
        if not user:
            print("输入不能为空！请重新输入！")
            continue
        try:
            user_input = float(user)
            if user_input.is_integer():
                return int(user_input)
            return user_input
        except ValueError:
            print("请输入一个数字！")


def main_only():
    """主函数"""
    print("欢迎来到FizzBuzz游戏（单独模式）！")
    while True:
        number = get_user_input()
        result = fizz_buzz(number)
        print(f"输入的数字为 {number}，其结果为 {result}")
        continue_choice = input(
            "\n是否继续游玩该模式？（输入\"quit\"或\"q\"退出，其余任意键继续）：\n> ").strip().lower()
        if continue_choice in ("quit", "q"):
            print("感谢游玩本模式，再见！")
            print("-"*20)
            break
        print("-"*20)
        print("继续游戏！")


if __name__ == "__main__":
    main_only()
