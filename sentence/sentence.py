"""在字符串中找到出现频率最高的字符"""
from pprint import pprint
import json
HISTORY_FILE = 'history.json'


def load_history():
    """加载历史"""
    try:
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            history = json.load(f)
        print("正在加载历史")
    except FileNotFoundError:
        print("暂无历史记录，将创建新的历史记录文件")
        history = []
    except json.JSONDecodeError:
        print("历史记录文件损坏，将创建新的历史记录文件")
        history = []
    return history


def get_sentence():
    """获取用户输入"""
    while True:
        sentence = input("请输入一句话：").lower().replace(" ", "").strip(".,!?;:'\"")
        if not sentence:
            print("输入不能为空，请重新输入！")
            continue
        return sentence


def save_history(history, sentence, char_frequency_sorted):
    """保存历史"""
    while True:
        user_choice = input("是否保存历史？（输入\"y\"或\"n\"）：\n> ").strip().lower()
        if user_choice == "y":
            point = {
                'sentence': sentence,
                'most_frequent': char_frequency_sorted[0][0] if char_frequency_sorted else None}
            history.append(point)
            print("保存成功！")
            try:
                with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
                    json.dump(history, f, ensure_ascii=False, indent=4)
                print("历史记录已保存")
            except IOError as e:
                print(f'保存历史记录时出错: {e}')
            return history
        elif user_choice == "n":
            print("取消保存！")
            return history
        else:
            print("输入错误！请重新输入！")


def input_history(history):
    """输出历史"""
    if not history:
        print("\n暂无历史记录！")
        return
    print("\n历史记录：")
    pprint(history, width=20)


def get_frequency(sentence):
    """统计字符出现的频率"""
    char_frequency = {}
    for char in sentence:
        char_frequency[char] = char_frequency.get(char, 0) + 1
    return char_frequency


def sorted_frequency(char_frequency):
    """按频率排序"""
    char_frequency_sorted = sorted(
        char_frequency.items(),
        key=lambda x: x[1],
        reverse=True)
    return char_frequency_sorted


def input_most_frequent_char(char_frequency_sorted):
    """输入出现频率最高的字符"""
    print("出现频率最高的字符是：", char_frequency_sorted[0][0])


def complete_list(char_frequency_sorted):
    """输出完整的字符频率列表"""
    print("完整的字符频率列表：")
    pprint(char_frequency_sorted, width=100)


def print_menu(history):
    """菜单信息"""
    while True:
        print("""
输入“游戏说明”以查看游戏说明
输入“开始游戏”以开始游戏
输入“退出”以退出游戏
输入“历史”以查看历史记录""")
        choice_menu = input("\n> ").strip()
        if choice_menu == "游戏说明":
            print("""
    1. 输入一句话，程序会统计每个字符出现的频率。
    2. 程序会告诉你出现频率最高的字符。
    3. 你还可以选择查看完整的字符频率列表。
                """)
        elif choice_menu == "退出":
            print("欢迎下次再来！")
            exit()
        elif choice_menu == "开始游戏":
            print("开始游戏！")
            break
        elif choice_menu == "历史":
            input_history(history)
            continue
        elif not choice_menu:
            print("选项不能为空！请输入选项！")
        else:
            print("请输入正确的选项！")


def choice_menu_user(char_frequency_sorted):
    """选择输出方式"""
    while True:
        choice_input = input("""请选择操作：
    输入“1”查看出现频率最高的字符
    输入“2”查看完整的字符频率列表
    > """).strip()
        if choice_input == "1":
            input_most_frequent_char(char_frequency_sorted)
            return
        elif choice_input == "2":
            complete_list(char_frequency_sorted)
            return
        else:
            print("请输入正确的选项！")


def main():
    """主函数"""
    print("欢迎来到字符频率统计工具！")
    history = load_history()
    while True:
        print("-" * 30)
        print_menu(history)
        sentence_input = get_sentence()
        char_frequency_input = get_frequency(sentence_input)
        char_frequency_sorted_input = sorted_frequency(
            char_frequency_input)
        choice_menu_user(char_frequency_sorted_input)
        history = save_history(
            history, sentence_input, char_frequency_sorted_input)
        while True:
            cont = input("是否继续使用？(y/n)：> ").strip().lower()
            if cont == "n":
                print("感谢使用字符频率统计工具！")
                print("-" * 30)
                exit()
            if cont == "y":
                break
            else:
                print("输入错误！请重新输入！")


if __name__ == '__main__':
    main()
