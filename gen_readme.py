#! /usr/bin/python3
# 
import os
from urllib.parse import quote

n=0

with open('README.md','w',encoding="utf-8") as f:
    f.write('''# 剪报--保存一些看到的有用文章

( 使用singlefile保存网页 )

''')
    for i in os.listdir("./"):
        if i[-4:]=='html':
            n+=1
            f.write(f"+ [{i[:-5]}](https://ouyen.github.io/saved_html/{quote(i)})\n\n")


os.system('git add *')
os.system('git commit -m "%s"'%str(n))
os.system('git push -u origin master')