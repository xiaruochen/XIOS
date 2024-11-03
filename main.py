import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('第一个窗口')       # 设置窗口的标题
window.geometry('200x100')     # 设置窗口的大小





#--------------
password = open('password.txt')

#打开password.txt
pc = open('pc.txt')
list1 = open('list.txt')
list = list1.readlines()
list1.close()
#打开pc.txt
while True:
    name_entry = input("User>")           # 创建用户名输入框
    pwd_entry = input("password>")
        #获取用户输入
    if (name_entry == password.read() and pwd_entry == pc.read()):
        #密码正确
        print('密码正确 SQL【2.0.0】')
        messagebox.showinfo(title='友情提示', message="密码正确 SQL【2.0.0】")
        break
        #密码错误
    else :
        print('密码错误 用户错误 ERROR 【',name_entry,'and',pwd_entry,'】')
        messagebox.showinfo(title='友情提示', message="密码错误 SQL【2.0.0】")
import os
d = open('激活文件.txt')
d = d.read()
if (d == '26V4U3-375W61-TQ7DHS-487FFN-SX85D-0LEEU-ZAW5Q-S2Z8A-6JYUS-ADWYJ-RZ' or "XXXXX-XXXXX-XXXXX-XXXXX-XXXXX-XXXXX-XXXXX-XXXXX-XXXXX"):
    print('welcome to sql!')
else:
    print("加载失败，你未激活")
    input('bye!!!')
    exit()
a = "mysql;"
while (a != 'exit'):
    try:
        a = input('sql>')
        if (a == '' or a == ' ' or a == '  '):    
            pass
        elif ('append namespace();' in a) :
            list.append(input('list>'))
            f = open('list.txt','w')
            for i in list:
                f.writelines(str(i+"\n"))
            f.close()
        elif ('del namespace();' in a) :
            del list[int(input('list>'))]
            f = open('list.txt','w')
            for i in list:
                f.writelines(str(i+"\n"))
            f.close()
        elif ('mysql;' in a) :
           print("6.6.6版本")
        elif ('show file;' in a) :
            for i in list:
                print(i)
        elif ('show file this;' in a) :
            print(list)
        elif ('insert namespace();' in a) :
            o = input('list>')
            while o:
                
                o = input('list>')
                list.append(o) 
                f = open('list.txt','w')
                for i in list:
                    f.writelines(str(i+'\n'))
                f.close()
            list.pop()
            f = open('list.txt','w')
            for i in list:
                f.writelines(str(i+"\n"))
            f.close()
        elif 'password namespace();' in a:
            cmd = open("password.txt","w+")
            cmd.write(input(">>>"))
            if cmd:
                print("加载成功")
            else:
                print("加载失败")
        elif 'pc namespace();' in a:
            cmd = open("pc.txt","w")
            cmd.write(input(">>>"))
            if cmd:
                print("加载成功")
            else:
                print("加载失败")
        else :
            print('错误  ERROR 【',a,'】')
        
    except Exception as e:
        print('ERORR',e)
print('bye!')
