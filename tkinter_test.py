#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter import *
import time
import hashlib

LOG_LINE_NUM = 0


class MY_GUI():
    def __init__(self, init_windows_name):
        self.init_windows_name = init_windows_name

    def set_init_windows(self):
        self.init_windows_name.title('文本转换工具')
        self.init_windows_name.geometry('1068x680+10+10')  # 前两个表示的是窗口的大小，后两个表示的是弹出时的默认位置
        # self.init_windows_name['bg'] = 'white'
        # self.init_windows_name.attributes('-alpha', 0.9)
        self.init_data_label = Label(self.init_windows_name, text="待处理数据")
        self.init_data_label.grid(row=0, column=0)

        self.init_data_label1 = Label(self.init_windows_name, text="输出结果")
        self.init_data_label1.grid(row=0, column=12)

        self.log_label = Label(self.init_windows_name, text='日志')
        self.log_label.grid(row=12, column=0)

        self.init_data_text = Text(self.init_windows_name, width=67, height=35)   # 数据输入框
        self.init_data_text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.init_data_text_scroll_y = Scrollbar(self.init_windows_name)
        self.init_data_text_scroll_y.config(command=self.init_data_text.yview)
        self.init_data_text.config(yscrollcommand=self.init_data_text_scroll_y.set)
        self.init_data_text_scroll_y.grid(row=1, column=10, rowspan=10, sticky=NS)

        self.init_data_text_scroll_x = Scrollbar(self.init_windows_name, orient=HORIZONTAL)
        self.init_data_text_scroll_x.config(command=self.init_data_text.xview)
        self.init_data_text.config(xscrollcommand=self.init_data_text_scroll_x.set)
        self.init_data_text_scroll_x.grid(row=11, column=0, columnspan=10, sticky=EW)



        self.result_data_text = Text(self.init_windows_name, width=70, height=49)  # 数据输出框
        self.result_data_text.grid(row=1, column=12, rowspan=15, columnspan=10)
        self.init_data_text_scroll_y = Scrollbar(self.init_windows_name)
        self.init_data_text_scroll_y.config(command=self.result_data_text.yview)
        self.init_data_text.config(yscrollcommand=self.init_data_text_scroll_y.set)
        self.init_data_text_scroll_y.grid(row=1, column=24, rowspan=15, sticky=NS)

        self.log_data_text = Text(self.init_windows_name, width=67, height=9)
        self.log_data_text.grid(row=13, column=0, rowspan=4, columnspan=10)

        md5_butthon = Button(self.init_windows_name, text='字符串转MD5', width=10, command=self
                             .str_trans_to_md5)
        md5_butthon.grid(row=1, column=11)

    def str_trans_to_md5(self):
        src = self.init_data_text.get(1.0, END).strip().replace("\n", "").encode()
        # print("src =",src)
        if src:
            try:
                myMd5 = hashlib.md5()
                myMd5.update(src)
                myMd5_Digest = myMd5.hexdigest()
                print(myMd5_Digest)
                # 输出到界面
                self.result_data_text.delete(1.0, END)
                self.result_data_text.insert(1.0, myMd5_Digest)
                self.write_log_to_Text("INFO:str_trans_to_md5 success")
            except:
                self.result_data_text.delete(1.0, END)
                self.result_data_text.insert(1.0, "字符串转MD5失败")
        else:
            self.write_log_to_Text("ERROR:str_trans_to_md5 failed")

    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return current_time

    def write_log_to_Text(self, logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) + " " + str(logmsg) + "\n"
        if LOG_LINE_NUM <= 7:
            self.log_data_text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_text.delete(1.0, 2.0)
            self.log_data_text.insert(END, logmsg_in)
        self.log_data_text.focus_force()


def gui_start():
    init_windows = Tk()
    gui = MY_GUI(init_windows)
    gui.set_init_windows()
    init_windows.mainloop()


gui_start()
