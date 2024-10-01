import tkinter as tk
from tkinter import *
from tkinter import messagebox
from calculate import calculate
import collection
import data_object
from PIL import Image, ImageTk




class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.window_width = 1200
        self.window_height = 900
        self.set_main_window()# 设置主窗口
        # 设置全局变量
        """
        ImageTk.PhotoImage对象都是在add_collections方法中创建的局部变量
        当该方法返回时，这些局部变量将被销毁并释放内存
        因此需要创建全局变量来存储图片对象
        """
        self.images = {}  # 全局存储图像对象
        self.load_all_images()
        
        # 创建一级界面
        self.frame1 = Frame(self,bg="red")# 伤害计算界面
        self.frame2 = Frame(self,bg="green")# 干员图鉴界面
        self.frame3 = Frame(self,bg="blue")# 敌方图鉴界面
        self.frame4 = Frame(self,bg="darkblue")# 藏品图鉴界面
        self.frame5 = Frame(self,bg="orange")# 暂定界面
        self.first_frame = None# 一级界面状态
        
        # 创建二级界面
        self.DMG1_frame = Frame(self.frame1,bg="yellow")# 物理伤害界面
        self.DMG2_frame = Frame(self.frame1,bg="purple")# 法术伤害界面
        self.DMG3_frame = Frame(self.frame1,bg="grey")# 真实伤害界面
        self.second_frame = None# 二级界面状态

        #创建三级界面
        self.DMG1_calculate_frame = Frame(bg="#236B8E",padx=26,pady=5)# 物理伤害计算界面
        self.DMG2_calculate_frame = Frame(bg="#4F2F4F",padx=26,pady=5)# 法术伤害计算界面
        self.DMG3_calculate_frame = Frame(bg="#D9D9F3",padx=26,pady=5)# 真实伤害计算界面
        self.third_calculate_frame = None# 三级界面状态
        self.select_collections_frame = Canvas(bg="green")
        self.collections_canvas = Canvas(bg="white")# 藏品界面
        self.show_DMG1_calculate_frame_flag = True
        self.show_DMG2_calculate_frame_flag = True
        self.show_DMG3_calculate_frame_flag = True
        self.show_DMG_collections_frame_flag = True

        # 布局一级界面
        self.show_all_frame1()
        # 布局二级界面
        self.show_all_DMG1_frame()
        # 布局三级界面
        self.show_all_DMG1_calculate_frame()

    # 设置主窗口大小和位置
    def set_main_window(self):
        self.title("明日方舟伤害计算器demo")# 程序名称
        # self.iconbitmap('../icon/icon.ico')# 程序图标
        x_offset = (self.winfo_screenwidth() - self.window_width) // 2 # 窗口居中
        y_offset = (self.winfo_screenheight() - self.window_height) // 2
        self.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, x_offset, y_offset))# 设置窗口大小和出现位置
        self.minsize(self.window_width,self.window_height)# 设置最小窗口
        self.resizable(1,1)# 不可调整窗口大小

    # 设置一级界面frame大小
    def set_window_size(self,frame):
        frame.grid_propagate(False)# 禁止框架自适应大小
        frame.config(width=self.window_width, height=self.window_height)

    # 隐藏frame内容
    def clean_frame(self,state_frame,click_frame):
        print("当前界面：{}".format(state_frame))
        print("点击界面：{}".format(click_frame))
        if state_frame != click_frame and state_frame != None:
            print("即将隐藏界面:{}".format(state_frame))
            state_frame.grid_forget()

    # 布置总导航栏组件
    def navigation_widgets(self, frame):  
        frame.config(highlightbackground="red", highlightthickness=2)
        for i in range(5):  # 设置列数量
            frame.columnconfigure(i, weight=1, minsize=100)
        buttons = ["伤害计算", "干员图鉴", "敌方图鉴", "藏品图鉴", "暂定"]
        commands = [self.show_all_frame1, self.show_all_frame2, self.show_all_frame3, self.show_all_frame4, self.show_all_frame5]
        for index, text in enumerate(buttons):
            Button(frame, text=text, command=commands[index]).grid(row=0, column=index, sticky="ew")

    # 布置伤害计算导航栏组件
    def set_DMG_navigation_wigets(self,frame):
        frame.config(highlightbackground="red", highlightthickness=2)
        for i in range(3):  # 设置列数量
            frame.columnconfigure(i, weight=1)
        buttons = ["物理伤害", "法术伤害", "真实伤害"]
        commands = [self.show_all_DMG1_frame, self.show_all_DMG2_frame, self.show_all_DMG3_frame]
        for index, text in enumerate(buttons):
            Button(frame, text=text, command=commands[index]).grid(row=0, column=index, sticky="ew")

    # 加载图片并转换为Tkinter PhotoImage对象
    def load_image(self,path):
        open_img = Image.open(path)
        img = ImageTk.PhotoImage(open_img)
        return img
    
    # 加载所有图片
    def load_all_images(self):
        for index, item in data_object.data.items():
            img_path = item['img_path']
            self.images[index] = self.load_image(img_path)
    
    # 一级界面
    def show_all_frame1(self):
        self.show_frame1()
        self.navigation_widgets(self.frame1)

    def show_all_frame2(self):
        self.show_frame2()
        self.navigation_widgets(self.frame2)

    def show_all_frame3(self):
        self.show_frame3()
        self.navigation_widgets(self.frame3)

    def show_all_frame4(self):
        self.show_frame4()
        self.navigation_widgets(self.frame4)

    def show_all_frame5(self):
        self.show_frame5()
        self.navigation_widgets(self.frame5)

    # 布局伤害计算界面
    def show_frame1(self):
        # 更改self.first_frame状态
        self.clean_frame(self.first_frame,self.frame1)
        self.first_frame = self.frame1

        print("切换到 frame1")
        self.set_window_size(self.frame1)# 设置frame1大小
        self.frame1.rowconfigure(1, weight=1)# 设置frame1第2行权重,如果有空余空间则占满
        self.frame1.columnconfigure(0, weight=1)# 设置frame1第1列权重,如果有空余空间则占满
        self.frame1.grid(row=0, column=0, sticky="nsew")

    # 布局干员图鉴界面
    def show_frame2(self):
        self.clean_frame(self.first_frame,self.frame2)
        self.first_frame = self.frame2

        print("切换到 frame2")
        self.set_window_size(self.frame2)
        self.frame2.grid(row=0, column=0, sticky="nsew")

    # 布局敌方图鉴界面
    def show_frame3(self):
        self.clean_frame(self.first_frame,self.frame3)
        self.first_frame = self.frame3

        print("切换到 frame3")
        self.set_window_size(self.frame3)
        self.frame3.grid(row=1, column=0, sticky="nsew")
        
    # 布局藏品图鉴界面
    def show_frame4(self):
        self.clean_frame(self.first_frame,self.frame4)
        self.first_frame = self.frame4

        print("切换到 frame4")
        self.set_window_size(self.frame4)
        self.frame4.grid(row=1, column=0, sticky="nsew")

    # 布局暂定
    def show_frame5(self):
        self.clean_frame(self.first_frame,self.frame5)
        self.first_frame = self.frame5

        print("切换到 frame5")
        self.set_window_size(self.frame5)
        self.frame5.grid(row=1, column=0, sticky="nsew")

    # 二级界面
    def show_all_DMG1_frame(self):
        self.show_DMG1_frame()
        self.set_DMG_navigation_wigets(self.DMG1_frame)
    
    def show_all_DMG2_frame(self):
        self.show_DMG2_frame()
        self.set_DMG_navigation_wigets(self.DMG2_frame)

    def show_all_DMG3_frame(self):
        self.show_DMG3_frame()
        self.set_DMG_navigation_wigets(self.DMG3_frame)
    

    # 布局物理伤害界面
    def show_DMG1_frame(self):
        # 更改self.second_frame状态
        self.clean_frame(self.second_frame,self.DMG1_frame)
        self.second_frame = self.DMG1_frame

        print("切换到物理伤害界面")
        # 使第一行占满整个剩余空间
        self.DMG1_frame.grid_rowconfigure(1,weight=1)
        # 布置DMG1_frame界面
        self.DMG1_frame.grid(row=1, column=0, sticky="nsew",columnspan=5)
        # 展示物理伤害计算界面
        self.show_DMG1_calculate_frame()
        # 展示藏品界面
        self.show_DMG1_collections_frame()

    # 布局法术伤害界面
    def show_DMG2_frame(self):
        self.clean_frame(self.second_frame,self.DMG2_frame)
        self.second_frame = self.DMG2_frame

        print("切换到法术伤害界面")
        self.DMG2_frame.grid_rowconfigure(1,weight=1)
        self.DMG2_frame.grid(row=1, column=0, sticky="nsew",columnspan=5)
        self.show_DMG2_calculate_frame()
        self.show_DMG2_collections_frame()

    # 布局真实伤害界面
    def show_DMG3_frame(self):
        self.clean_frame(self.second_frame,self.DMG3_frame)
        self.second_frame = self.DMG3_frame

        print("切换到真实伤害界面")
        self.DMG3_frame.grid_rowconfigure(1,weight=1)
        self.DMG3_frame.grid(row=1, column=0, sticky="nsew",columnspan=5)
        self.show_DMG3_calculate_frame()
        self.show_DMG3_collections_frame()

    # 三级界面
    def show_all_DMG1_calculate_frame(self):
        self.show_DMG1_calculate_frame()
        self.show_DMG1_collections_frame()

    def show_all_DMG2_calculate_frame(self):
        self.show_DMG2_calculate_frame()
        self.show_DMG2_collections_frame()

    def show_all_DMG3_calculate_frame(self):
        self.show_DMG3_calculate_frame()
        self.show_DMG3_collections_frame()

    # 伤害计算界面
    # 物理伤害计算界面
    def show_DMG1_calculate_frame(self):
        self.clean_frame(self.third_calculate_frame,self.DMG1_calculate_frame)
        # 更改self.third_calculate_frame状态
        self.third_calculate_frame = self.DMG1_calculate_frame

        # 布局DMG_calculate_frame
        self.DMG1_calculate_frame.config(highlightbackground="black", highlightthickness=2)
        self.DMG1_calculate_frame.columnconfigure(0, weight=0)
        self.DMG1_calculate_frame.columnconfigure(1, weight=0)
        # 设置组件不随内容自动调整大小
        self.DMG1_calculate_frame.grid_propagate(False)
        self.DMG1_calculate_frame.grid(row=1, column=0, sticky="nsew", in_=self.DMG1_frame)# 从其他(法术伤害计算)界面回来时重新布局，row和column缺失时不会显示self.DMG1_calculate_frame
        print("展示物理伤害计算界面")
        # 放置按钮文本等框架
        if self.show_DMG1_calculate_frame_flag:
            self.show_DMG1_calculate_frame_flag = False
            Button(self.DMG1_calculate_frame,text="开始计算",command=lambda: load_data()).grid(row=15,column=0,columnspan=2)
            # 显示计算结果
            Label(self.DMG1_calculate_frame,text="DPH:", width=20).grid(row=16,column=0)
            # 设置DPH默认文本
            DPH = tk.StringVar(value="未计算")
            DPH_label = Label(self.DMG1_calculate_frame, textvariable=DPH)
            DPH_label.grid(row=16, column=1, sticky='ew', padx=5, pady=5)

            # 创建属性文本
            tag_names = ['基础攻击力', '攻击力增加倍率', '最终加算攻击力', '技能伤害倍率', '固定减防', '百分比减防', '无视防御力', '无视百分百防御力', '增伤', '易伤', '敌方基础防御力', '敌方防御力增加', '敌方防御力增加倍率', '敌方百分比减伤']
            var_names = ['ATK', 'ATK_Inc_Mult', 'Fin_ATK_Add', 'Skill_Dmg_Mult', 'Dec_DEF', 'Prec_Dec_DEF', 'Ign_DEF', 'Ign_Mul_DEF', 'Dmg_Inc', 'Vul', 'Emy_DEF', 'Emy_DEF_Add', 'Emy_DEF_Inc_Mult', 'Emy_Perc_Dmg_Red']
            tags = {}
            for index, name in enumerate(tag_names):
                tags[name] = Label(self.DMG1_calculate_frame,text=tag_names[index], width=20)
                tags[name].grid(row=index, column=0, sticky="ew", padx=5, pady=5)
            # 创建储存数据的变量和输入数据的文本框 两者绑定
            # 物理：我方属性(共10条) 敌方属性(共4条) 法术：我方属性(共10条) 敌方属性(共4条) 真实：我方属性(共6条)
            vars = {}
            entries = {}
            for index, name in enumerate(var_names):
                if name != "Skill_Dmg_Mult":
                    vars[name] = DoubleVar()
                else:
                    vars[name] = DoubleVar(value=1.0)
                entries[name] = Entry(self.DMG1_calculate_frame, textvariable=vars[name],width=10)
                entries[name].grid(row=index, column=1, padx=5, pady=5, sticky='ew')
        # 创建字典储存数据
        def load_data():
            dic = {}
            dic["Phy_Dmg_Inc"] = 0
            dic["Phy_Vul"] = 0
            dic["ATK_Mult"] = 0
            for name in entries:
                try:
                    if entries[name].get() == "":
                        dic[name] = 0
                    else:
                        dic[name] = float(entries[name].get())
                except ValueError:
                    messagebox.showerror("错误", "请输入数字")
                    break

            total_ATK_Inc_Mult = sum(item["ATK_Inc_Mult"] for item in collection.ATKCollections.all_collections)# 获取勾选中藏品所有ATK_Inc_Mult的值
            total_Dmg_Inc = sum(item["Dmg_Inc"] for item in collection.ATKCollections.all_collections)# 获取勾选中藏品所有Dmg_Inc的值
            total_Phy_Dmg_Inc = sum(item["Phy_Dmg_Inc"] for item in collection.ATKCollections.all_collections)# 获取勾选中藏品所有Phy_Dmg_Inc的值
            total_Prec_Dec_DEF = sum(item["Prec_Dec_DEF"] for item in collection.ATKCollections.all_collections)# 获取勾选中藏品所有Prec_Dec_DEF的值
            total_Vul = sum(item["Vul"] for item in collection.ATKCollections.all_collections)# 获取勾选中藏品所有Vul的值
            total_Phy_Vul = sum(item["Phy_Vul"] for item in collection.ATKCollections.all_collections)# 获取勾选中藏品所有Phy_Vul的值
            total_ATK_Mult = sum(item["ATK_Mult"] for item in collection.ATKCollections.all_collections)# 获取勾选中藏品所有ATK_Mult的值
            total_Prec_Dec_DEF = sum(item["Prec_Dec_DEF"] for item in collection.ATKCollections.all_collections)# 获取勾选中藏品所有Prec_Dec_DEF的值
            print(dic)
            # 将勾选的藏品属性添加至计算公式
            dic['ATK_Inc_Mult'] += total_ATK_Inc_Mult
            dic['Dmg_Inc'] += total_Dmg_Inc
            dic['Phy_Dmg_Inc'] += total_Phy_Dmg_Inc
            dic['Vul'] += total_Vul
            dic['Phy_Vul'] += total_Phy_Vul
            dic['ATK_Mult'] += total_ATK_Mult
            dic['Prec_Dec_DEF'] += total_Prec_Dec_DEF

            print(dic)
            print(collection.ATKCollections.all_collections)
            result = calculate.phyDmg(dic)
            # 更新DPH文本
            DPH.set(result)

    # 法术伤害计算界面
    def show_DMG2_calculate_frame(self):
        self.clean_frame(self.third_calculate_frame,self.DMG1_calculate_frame)
        # 更改self.third_calculate_frame状态
        self.third_calculate_frame = self.DMG2_calculate_frame

        # 布局DMG_calculate_frame
        self.DMG2_calculate_frame.config(highlightbackground="black", highlightthickness=2)
        self.DMG2_calculate_frame.columnconfigure(0, weight=0)
        self.DMG2_calculate_frame.columnconfigure(1, weight=0)
        # 设置组件不随内容自动调整大小
        self.DMG2_calculate_frame.grid_propagate(False)
        self.DMG2_calculate_frame.grid(row=1, column=0, sticky="nsew", in_=self.DMG2_frame)# 从其他(法术伤害计算)界面回来时重新布局，row和column缺失时不会显示self.DMG1_calculate_frame
        print("展示物理伤害计算界面")
        if self.show_DMG2_calculate_frame_flag:
            self.show_DMG2_calculate_frame_flag = False
            Button(self.DMG2_calculate_frame,text="开始计算",command=lambda: load_data()).grid(row=15,column=0,columnspan=2)
            # 显示计算结果
            Label(self.DMG2_calculate_frame,text="DPH:", width=20).grid(row=16,column=0)
            # 设置DPH默认文本
            DPH = tk.StringVar(value="未计算")
            DPH_label = Label(self.DMG2_calculate_frame, textvariable=DPH)
            DPH_label.grid(row=16, column=1, sticky='ew', padx=5, pady=5)

            # 创建属性文本
            tag_names = ['基础攻击力', '攻击力增加倍率', '最终加算攻击力', '技能伤害倍率', '固定减法抗', '百分百减法抗', '无视法抗', '增伤', '易伤', '法术脆弱', '敌方基础法抗', '敌方法抗提升', '敌方法抗增加倍率', '敌方百分比减伤']
            var_names = ['ATK', 'ATK_Inc_Mult', 'Fin_ATK_Add', 'Skill_Dmg_Mult', 'Prec_Dec_DEF', 'Ign_DEF', 'Ign_Mul_DEF', 'Dmg_Inc', 'Vul', 'Spell_Vul', 'Emy_Spell_RES', 'Emy_Spell_RES_Add', 'Emy_Spell_RES_Inc_Mult', 'Emy_Perc_Dmg_Red']
            tags = {}
            for index, name in enumerate(tag_names):
                tags[name] = Label(self.DMG2_calculate_frame,text=tag_names[index], width=20)
                tags[name].grid(row=index, column=0, sticky="ew", padx=5, pady=5)
            # 创建储存数据的变量和输入数据的文本框 两者绑定
            # 物理：我方属性(共10条) 敌方属性(共4条) 法术：我方属性(共10条) 敌方属性(共4条) 真实：我方属性(共6条)
            vars = {}
            entries = {}
            for index, name in enumerate(var_names):
                if name != "Skill_Dmg_Mult":
                    vars[name] = DoubleVar()
                else:
                    vars[name] = DoubleVar(value=1.0)
                entries[name] = Entry(self.DMG2_calculate_frame, textvariable=vars[name],width=10)
                entries[name].grid(row=index, column=1, padx=5, pady=5, sticky='ew')
        # 创建字典储存数据
        def load_data():
            dic = {}
            dic["ATK_Mult"] = 0
            dic['Spell_Dmg_Inc'] = 0
            dic['Dec_Spell_RES'] = 0
            dic['Prec_Dec_Spell_RES'] = 0
            dic['Ign_Spell_RES'] = 0

            for name in entries:
                try:
                    if entries[name].get() == "":
                        dic[name] = 0
                    else:
                        dic[name] = float(entries[name].get())
                except ValueError:
                    messagebox.showerror("错误", "请输入数字")
                    break

            total_ATK_Inc_Mult = sum(item["ATK_Inc_Mult"] for item in collection.ATKCollections.all_collections)# 获取勾选中藏品所有ATK_Inc_Mult的值
            total_Dmg_Inc = sum(item["Dmg_Inc"] for item in collection.ATKCollections.all_collections)# 获取勾选中藏品所有Dmg_Inc的值
            total_Spell_Dmg_Inc = sum(item["Spell_Dmg_Inc"] for item in collection.ATKCollections.all_collections)# 获取勾选中藏品所有Phy_Dmg_Inc的值
            total_Vul = sum(item["Vul"] for item in collection.ATKCollections.all_collections)# 获取勾选中藏品所有Vul的值
            total_Spell_Vul = sum(item["Spell_Vul"] for item in collection.ATKCollections.all_collections)# 获取勾选中藏品所有Phy_Vul的值
            total_ATK_Mult = sum(item["ATK_Mult"] for item in collection.ATKCollections.all_collections)# 获取勾选中藏品所有ATK_Mult的值
            total_Dec_Spell_RES = sum(item["Dec_Spell_RES"] for item in collection.ATKCollections.all_collections)# 获取勾选中藏品所有Dec_Spell_RES的值
            total_Prec_Dec_Spell_RES = sum(item["Prec_Dec_Spell_RES"] for item in collection.ATKCollections.all_collections)# 获取勾选中藏品所有Prec_Dec_DEF的值
            total_Ign_Spell_RES = sum(item["Ign_Spell_RES"] for item in collection.ATKCollections.all_collections)# 获取勾选中藏品所有Ign_Spell_RES的值
            print(dic)
            print(collection.ATKCollections.all_collections)
            # 将勾选的藏品属性添加至计算公式
            dic['ATK_Inc_Mult'] += total_ATK_Inc_Mult
            dic['Dmg_Inc'] += total_Dmg_Inc
            dic['Spell_Dmg_Inc'] += total_Spell_Dmg_Inc
            dic['Vul'] += total_Vul
            dic['Spell_Vul'] += total_Spell_Vul
            dic['ATK_Mult'] += total_ATK_Mult
            dic['Dec_Spell_RES'] += total_Dec_Spell_RES
            dic['Prec_Dec_Spell_RES'] += total_Prec_Dec_Spell_RES
            dic['Ign_Spell_RES'] += total_Ign_Spell_RES
            result = calculate.speDmg(dic)
            # 更新DPH文本
            DPH.set(result)



    # 真实伤害计算界面
    def show_DMG3_calculate_frame(self):
        self.clean_frame(self.third_calculate_frame,self.DMG1_calculate_frame)
        # 更改self.third_calculate_frame状态
        self.third_calculate_frame = self.DMG3_calculate_frame

        # 布局DMG_calculate_frame
        self.DMG3_calculate_frame.config(highlightbackground="black", highlightthickness=2)
        self.DMG3_calculate_frame.columnconfigure(0, weight=0)
        self.DMG3_calculate_frame.columnconfigure(1, weight=0)
        # 设置组件不随内容自动调整大小
        self.DMG3_calculate_frame.grid_propagate(False)
        self.DMG3_calculate_frame.grid(row=1, column=0, sticky="nsew", in_=self.DMG3_frame)# 从其他(法术伤害计算)界面回来时重新布局，row和column缺失时不会显示self.DMG1_calculate_frame
        print("展示物理伤害计算界面")
        if self.show_DMG3_calculate_frame_flag:
            self.show_DMG3_calculate_frame_flag = False
            Button(self.DMG3_calculate_frame,text="开始计算",command=lambda: load_data()).grid(row=15,column=0,columnspan=2)
            # 显示计算结果
            Label(self.DMG3_calculate_frame,text="DPH:", width=20).grid(row=16,column=0)
            # 设置DPH默认文本
            DPH = tk.StringVar(value="未计算")
            DPH_label = Label(self.DMG3_calculate_frame, textvariable=DPH)
            DPH_label.grid(row=16, column=1, sticky='ew', padx=5, pady=5)

            # 创建属性文本
            tag_names = ['基础攻击力', '攻击力增加倍率', '最终加算攻击力', '技能伤害倍率', '增伤', '易伤']
            var_names = ['ATK', 'ATK_Inc_Mult', 'Fin_ATK_Add', 'Skill_Dmg_Mult', 'Dmg_Inc', 'Vul']
            tags = {}
            tags = {}
            for index, name in enumerate(tag_names):
                tags[name] = Label(self.DMG3_calculate_frame,text=tag_names[index], width=20)
                tags[name].grid(row=index, column=0, sticky="ew", padx=5, pady=5)
            # 创建储存数据的变量和输入数据的文本框 两者绑定
            # 物理：我方属性(共10条) 敌方属性(共4条) 法术：我方属性(共10条) 敌方属性(共4条) 真实：我方属性(共6条)
            vars = {}
            entries = {}
            for index, name in enumerate(var_names):
                if name != "Skill_Dmg_Mult":
                    vars[name] = DoubleVar()
                else:
                    vars[name] = DoubleVar(value=1.0)
                entries[name] = Entry(self.DMG3_calculate_frame, textvariable=vars[name],width=10)
                entries[name].grid(row=index, column=1, padx=5, pady=5, sticky='ew')

        # 创建字典储存数据
        def load_data():
            dic = {}
            dic["ATK_Mult"] = 0
            dic["True_Dmg_Inc"] = 0

            for name in entries:
                try:
                    if entries[name].get() == "":
                        dic[name] = 0
                    else:
                        dic[name] = float(entries[name].get())
                except ValueError:
                    messagebox.showerror("错误", "请输入数字")
                    break
            
            total_ATK_Inc_Mult = sum(item["ATK_Inc_Mult"] for item in collection.ATKCollections.all_collections)# 获取勾选中藏 品所有ATK_Inc_Mult的值
            total_ATK_Mult = sum(item["ATK_Mult"] for item in collection.ATKCollections.all_collections)
            total_Dmg_Inc = sum(item["Dmg_Inc"] for item in collection.ATKCollections.all_collections)
            total_True_Dmg_Inc = sum(item["True_Dmg_Inc"] for item in collection.ATKCollections.all_collections)
            total_Vul = sum(item["Vul"] for item in collection.ATKCollections.all_collections)
            dic['ATK_Inc_Mult'] += total_ATK_Inc_Mult
            dic['ATK_Mult'] += total_ATK_Mult
            dic['Dmg_Inc'] += total_Dmg_Inc
            dic['True_Dmg_Inc'] += total_True_Dmg_Inc
            dic['Vul'] += total_Vul

            result = calculate.trueDmg(dic)
            # 更新DPH文本
            DPH.set(result)

    # 伤害计算藏品界面
    def show_DMG1_collections_frame(self):
        """
        把父容器third_calculate_frame传给子容器in_=
        使变换二级界面时self.DMG_collections_frame界面不变
        """
        self.collections_canvas.config(highlightbackground="pink", highlightthickness=2)
        self.collections_canvas.grid(row=1, column=1, columnspan=2, sticky="nsew", in_=self.DMG1_frame)
        self.collections_canvas.grid_propagate(False)
        print("展示伤害计算通用藏品界面")
        self.collections_canvas.columnconfigure(0, weight=1)
        self.collections_canvas.rowconfigure(0, weight=1)

        if self.show_DMG_collections_frame_flag:
            self.show_DMG_collections_frame_flag = False
            self.init_collections()

    def show_DMG2_collections_frame(self):
        self.collections_canvas.config(highlightbackground="pink", highlightthickness=2)
        self.collections_canvas.grid(row=1, column=1, columnspan=2, sticky="nsew", in_=self.DMG2_frame)
        # self.collections_canvas.grid_propagate(False)
        print("展示伤害计算通用藏品界面")
        self.collections_canvas.columnconfigure(0, weight=1)
        self.collections_canvas.rowconfigure(0, weight=1)

    def show_DMG3_collections_frame(self):
        self.collections_canvas.config(highlightbackground="pink", highlightthickness=2)
        self.collections_canvas.grid(row=1, column=1, columnspan=2, sticky="nsew", in_=self.DMG3_frame)
        self.collections_canvas.grid_propagate(False)
        print("展示伤害计算通用藏品界面")
        self.collections_canvas.columnconfigure(0, weight=1)
        self.collections_canvas.rowconfigure(0, weight=1)

    def init_collections(self):
        # 创建垂直滚动条
        y_scrollbar = Scrollbar(self.collections_canvas, orient=VERTICAL, command=self.collections_canvas.yview)
        y_scrollbar.grid(row=0, column=5, sticky="ns")
        self.collections_canvas.configure(yscrollcommand=y_scrollbar.set)

        # 创建一个frame来容纳Checkbutton
        inner_frame = tk.Frame(self.collections_canvas)

        for index, item in data_object.data.items():
            title = ['ID:'+str(index)+'\nNo.'+str(item['No'])+'\n'+str(item['Name'])]
            print(title)
            
            checkbox_var = BooleanVar()
            # 创建并布局复选框
            checkbox = tk.Checkbutton(inner_frame, text=title[0], image=self.images[index], compound="bottom", bg="gray", padx=45, pady=10, variable=checkbox_var, command=lambda var=checkbox_var, idx=index: checkbutton_action(var, idx))

            # Tooltip功能
            tooltip = ToolTip(checkbox, item["text"])
            print(checkbox_var.get())
            checkbox.grid(row=index // 4, column=index % 4, sticky="nesw")
            # 使鼠标在复选框上时滚动鼠标滚轮控制self.canvas的滚动
            checkbox.bind("<Configure>", lambda event: self.collections_canvas.configure(scrollregion=self.collections_canvas.bbox("all")))
            # 绑定鼠标滚轮事件
            checkbox.bind("<MouseWheel>", lambda event: self.collections_canvas.yview_scroll(-1 * (event.delta // 120), "units"))
            # 绑定frame的大小改变事件来更新canvas的滚动区域
        
        # 使鼠标在inner_frame上时滚动鼠标滚轮控制self.canvas的滚动
        inner_frame.bind("<Configure>", lambda event: self.collections_canvas.configure(scrollregion=self.collections_canvas.bbox("all")))
        # 绑定鼠标滚轮事件
        inner_frame.bind("<MouseWheel>", lambda event: self.collections_canvas.yview_scroll(-1 * (event.delta // 120), "units"))
        # 将内部框架添加到canvas上
        self.collections_canvas.create_window((0, 0), window=inner_frame, anchor="nw")
        # 设置canvas的滚动区域
        self.collections_canvas.configure(scrollregion=self.collections_canvas.bbox("all"))

        def checkbutton_action(checkbox_var, idx):
            status = checkbox_var.get()
            print(status)
            if status:
                collection.ATKCollections(idx)
                print("当前选中藏品:{}".format(collection.ATKCollections.all_collections))
                print("选中")
            else:
                collection.ATKCollections.all_collections = [item for item in collection.ATKCollections.all_collections if item['Id'] != idx]
                print("取消后当前选中藏品:{}".format(collection.ATKCollections.all_collections))
                print("取消选中")
        
class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 0
        y += self.widget.winfo_rooty() + 190

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")

        label = tk.Label(self.tooltip, text=self.text, background="#ffffe0", relief="solid", borderwidth=1)
        label.pack(ipadx=1)

    def hide_tooltip(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

            
if __name__ == '__main__':
    app = App()
    app.mainloop()