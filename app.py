import tkinter as tk

from storage.excel import save_to_excel
from twitter.api import get_tweets


def fetch_tweets():
    username = username_entry.get()
    year = year_var.get()
    month = month_var.get()
    tweets = get_tweets(username, year, month)
    filepath = save_to_excel(tweets, username, year, month)
    result_label.config(text=f"文件已保存至: {filepath}")


# 创建窗口
root = tk.Tk()
root.title("Twitter Monthly Tweet Exporter")
root.geometry('400x200')  # 设置窗口尺寸

# 添加输入字段
tk.Label(root, text="Twitter 用户名:").pack(pady=10)  # pady增加垂直外边距
username_entry = tk.Entry(root, width=30)
username_entry.pack()

# 年份和月份的下拉选择
year_var = tk.StringVar(root)
month_var = tk.StringVar(root)
year_var.set('2024')  # 默认值
month_var.set('4')  # 默认值

# 创建年份和月份的选择列表
years = [str(year) for year in range(2006, 2031)]
months = [str(month) for month in range(1, 13)]

year_menu = tk.OptionMenu(root, year_var, *years)
month_menu = tk.OptionMenu(root, month_var, *months)
tk.Label(root, text="选择年份:").pack(pady=5)
year_menu.pack()
tk.Label(root, text="选择月份:").pack(pady=5)
month_menu.pack()

# 添加按钮和结果标签
fetch_button = tk.Button(root, text="获取推文", command=fetch_tweets)
fetch_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
