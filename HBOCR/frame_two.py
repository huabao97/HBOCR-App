# -*- coding:utf8 -*-
import tkinter as tk
from tkinter import ttk 
from tkinter.constants import BOTH, CENTER, E, END, LEFT, NE, NW, RIGHT, W,  X, Y
import json
import baiduocr
import tencentocr

class Frametwoset():
    def __init__(self,frametwo,table_value,win):
        self.master = frametwo
        self.table_value = table_value
        self.root = win
        self.__UI()

    def __UI(self):
        self.frametwo_button = tk.Frame(self.master,width=800,height=75,bg='AliceBlue')
        self.frametwo_button.pack(fill=X)
        self.frametwo_result = tk.Frame(self.master,width=800,height=300,bg='AliceBlue')
        self.frametwo_result.pack(fill=BOTH,expand=True)
        self.frametwo_button.columnconfigure(0, weight = 1)
        self.frametwo_button.columnconfigure(1, weight = 1)
        self.frametwo_conbobox1 = ttk.Combobox(self.frametwo_button,width=12,state='readonly',justify='center')
        self.frametwo_conbobox1['value'] = ('百度表格识别','腾讯表格识别')
        self.frametwo_conbobox1.current(self.table_value)
        self.frametwo_conbobox1.bind("<<ComboboxSelected>>",self.table_ocrsetting)
        self.frametwo_conbobox1.grid(row=0, column=0, padx=100, pady=15,)
        self.frametwo_button2 = tk.Button(self.frametwo_button,width=15,height=2,text='截图识别',relief='groove',bg='Azure',activebackground='Azure',command=self.frametwotable_button)
        self.frametwo_button2.grid(row=0, column=1, padx=100, pady=10,)
        
        self.frametwo_tableresult = tk.Text(self.frametwo_result,width=3,height=3,bd=0)
        self.frametwo_tableresult.pack(padx=30,pady=30,fill=BOTH,expand=True)

    def table_ocrsetting(self,event):
        tableopenaiton = ('百度表格识别','腾讯表格识别')
        table_index = tableopenaiton.index(self.frametwo_conbobox1.get())
        with open('api.json', 'r') as f:
            data = json.load(f)
        data['table'] = table_index
        with open('api.json', 'w') as f:
            json.dump(data, f)

    def frametwotable_button(self):
        with open('api.json', 'r') as f:
            tabledata = json.load(f)
        tableocrdata = int(tabledata['table'])
        self.frametwo_tableresult.delete('1.0','end')
        if tableocrdata == 0:
            self.root.iconify()
            ocrresult = baiduocr.baidu_table()
            self.root.deiconify()
            self.frametwo_tableresult.insert(END,ocrresult)
        elif tableocrdata == 1:
            self.root.iconify()
            ocrresult = tencentocr.tencent_table()
            self.root.deiconify()
            self.frametwo_tableresult.insert(END,ocrresult)
        else:
            ocrresult = 'error'
            self.frametwo_tableresult.insert(END,ocrresult)
