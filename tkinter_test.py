#!/usr/bin/python
# -*- coding: UTF-8 -*-

from tkinter import *
def gui_start():
    init_windows = Tk()
    init_windows.title("文本处理工具")
    init_windows.geometry('1068x680+10+10') # 前两个表示的是窗口的大小，后两个表示的是弹出时的默认位置
    init_windows['bg'] = 'pink'
    init_windows.attributes('-alpha',0.8)
    init_data_label = Label(init_windows,text="待处理数据")
    init_data_label.grid(row=0,column=0)
    init_data_label1 = Label(init_windows, text="输出结果")
    init_data_label1.grid(row=0, column=10)
    init_data_text = Text(init_windows, width=67, height=35)
    init_data_text.grid(row=1,column=0, rowspan=10, columnspan=10)
    result_data_text = Text(init_windows, width=70,height=49)
    result_data_text.grid(row=1, column=12, rowspan=15, columnspan=10)
    md5_butthon = Button(init_windows, text='字符串转MD5', bg='lightblue',width = 10, command=str)
    md5_butthon.grid(row=1, column=11)
    init_windows.mainloop()



gui_start()