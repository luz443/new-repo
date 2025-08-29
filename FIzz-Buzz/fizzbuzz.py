"""
Fizz-Buzz游戏最终版本
"""
import only
import ranging


def explain():
    """游戏说明"""
    choice_explain = input(
        '输入"yes"或"y"查看游戏说明，其余任意键跳过：\n> ').strip().lower()
    if choice_explain in ("yes", "y"):
        print("\n----游戏说明----")
        print(
            "1.此游戏有单独模式、范围模式、自定义模式共三种模式\n2.单独模式可以输入任意数字\n3.范围模式可以计算范围内的整数\n4.自定义模式可以自定义输出内容")


def choice_made():
    """选择模式"""
    choice_input = input('输入"单独"或"范围"或"自定义"选择模式：\n> ').strip()
    return choice_input


def continue_choice():
    """是否继续游戏"""
    choice_continue = input('\n是否继续游玩？（输入"quit"或"q"退出，输入任意字符继续）\n> ')
    return choice_continue.strip().lower()


def main():
    """主函数"""
    print("欢迎来到FizzBuzz游戏！")
    print("需要查看游戏说明吗？")
    explain()
    print("----开始游戏----")
    while True:
        print("请选择一个模式")
        decision_made = choice_made()
        if decision_made == "单独":
            only.main_only()
        elif decision_made == "范围":
            ranging.main_range()
        elif decision_made == "自定义":
            print("自定义模式正在开发中，敬请期待！")
        else:
            print("请输入正确的模式名！")
            continue
        then_choice = continue_choice()
        if then_choice in ("quit", "q"):
            print("感谢游玩，再见！")
            print("-"*20)
            break
        print("----继续游戏----")


if __name__ == "__main__":
    main()
