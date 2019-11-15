#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author:Se7en
#@Time:2019/11/16 2:45
PwdTempaltList = []
FuzzResultLlist = []
#获取Fuzz密码的模板，每行为一条放进PwdList列表中
def GetPwdTemplat():
    with open('rule','r',encoding='utf-8') as Frule:
        FruleLines = Frule.readlines()
        for FruleLine in FruleLines:
            PwdTempaltList.append(FruleLine.strip())
    Frule.close()
#输出最后的字典结果到当前目录下的password.txt文件
def OutPutFile(FuzzResultLlist):
    with open('password.txt','w',encoding='utf-8') as Fpassword:
        for FuzzResultWord in FuzzResultLlist:
            Fpassword.write(FuzzResultWord+'\n')
    Fpassword.close()

if __name__ == '__main__':
    banner = """
  ________ ___       __________ ________                                  
  ___  __ \__ |     / /___  __ \___  __/____  ___________________ ________
  __  /_/ /__ | /| / / __  / / /__  /_  _  / / /___  /___  /_  _ \__  ___/
  _  ____/ __ |/ |/ /  _  /_/ / _  __/  / /_/ / __  /___  /_/  __/_  /    
  /_/      ____/|__/   /_____/  /_/     \__,_/  _____/_____/\___/ /_/      

                                                                 _by Se7en
                                                                       """ 
    print(banner)
    KeyWords = input("Please input the keywords e.g.[username,domain,numbers,...]:")
    KeyWordsList = KeyWords.split(",")
    GetPwdTemplat()
    #遍历列表，将密码模板的内容替换为列表里的关键字
    for KeyWord in KeyWordsList:
        for PwdTempalWord in PwdTempaltList:
            FuzzResultWord = PwdTempalWord.replace('%username%',KeyWord)
            if FuzzResultWord not in FuzzResultLlist:
                FuzzResultLlist.append(FuzzResultWord)
    #最后输出所有Fuzz出的密码至password.txta
    OutPutFile(FuzzResultLlist)
    print("Enjoy your password.txt!")