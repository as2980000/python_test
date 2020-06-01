#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
功能說明:重新命名指定路徑下所有檔案

'''
import os
import re
from os import listdir
from os.path import isfile ,isdir ,join
import pathlib
mypath="D:\\rename\\"

files=listdir(mypath)

#列出目錄下所有檔案迴圈開始
for f in files:
  #取得檔案完整路徑
  fullpath = join(mypath,f)

  if isfile(fullpath):
      #取得檔案副檔名
      file_extention=pathlib.Path(f).suffix
      print(file_extention)
      print("file :",f)
      file_name=str(f)
      #如果檔名符合regular expression
      if( re.search("[a-zA-Z]{3,5}-[0-9]+", file_name)) :
        reg_ar=re.findall("[a-zA-Z]{3,5}-[0-9]+",file_name)
        reg_name=reg_ar[0]
        print(f"{file_name} rename to {reg_name} ?")
        #使用者輸入是否重新命名
        is_reg_rename = input("reame ok?")
        if is_reg_rename=="Y" or is_reg_rename=="y":
          rename_full_path=join(mypath,reg_name)+file_extention
          try:
            #依照變數reg_name重新命名
            os.rename(fullpath,rename_full_path)
          except:
              print("rename fail")
              continue
          print(f"rename to {rename_full_path}")
          continue
      #使用者輸入是否重新命名
      is_rename =input("rename file?")
      if is_rename=="Y" or is_rename=="y" :
          rename=input("rename to?")
          rename_full_path=join(mypath,rename)+file_extention
          try:
            os.rename(fullpath,rename_full_path)
            print(f"rename to {rename_full_path}")
          except:
              print("rename fail")
  elif isdir(fullpath):
      print("directory:",f)
#列出目錄下所有檔案迴圈結束
