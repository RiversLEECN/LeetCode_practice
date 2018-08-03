#coding=utf-8

#写一个函数，change,更改资料
def change(change_obj,type1):   #，change_obl,是用于定位用户；type1，用于定位修改内容，可以是‘name,age,tel’
    file2=open('d:\\user.txt','r')
    line2=file2.readlines()
    print("文本中读取出的line2:",line2)
    print('type(line2):',type(line2))
    print()
    count_j=0
    count_h=0
    for j in line2:      #j是列表中的一个元素，为字符串类型，包含姓名、年龄、电话
        count_j+=1       #判断更改的位置，和后续更新数据位置作对比用的
        if change_obj in j:  #判断输入的用户名是否在这个字符串内，在的话，就定位正确了
    #将j这个字符串进行拆分，直到拆为列表！！！！
            new_obj=input('请输入更新后的%s-->：'%type1)
            j=j.strip('\n') #去掉字符串末尾的换行符
            print('上一行的type(j):',type(j))
            print()
            print('去掉换行符之后：',j)
            print('上一行的type(j):',type(j))
            print()
            j=j.split('\t') #先按照空格拆分
            print('去掉table之后：',j)    #j是一个列表
            print('上一行的type(j)：',type(j))
            print()
            if type1=='name':
                j[0]=new_obj   #将j这个列表中的第一个元素，即姓名，进行替换
            elif type1=='age':
                j[1]=new_obj  #将j这个列表中的第二个元素，即年龄，进行替换
            elif type1=='tel':
                j[2]=new_obj  #将j这个列表中的第三个元素，即电话，进行替换
            print('J:',j)
            print('上一行的type(j)：',type(j))
            print()
            k='%s\t%s\t%s\n'%(j[0],j[1],j[2]) #将列表转换为字符串才能写入,字符串拼接啊！！
            #现将替换后的列表j，需要写进文档里面
            print("K:",k)
            print('上一行的type(k)：',type(k))
            print()
            file2.close()
            file3=open('d:\\user.txt','w')
            for h in line2:
                count_h+=1       
                if count_h ==count_j:  #定位到这个位置的数据需要更新
                    file3.write(k)
                else:
                    file3.write(h)
            file3.close()
            print('该用户的%s更新完成！'%type1)

# change('n2','name') 调试函数专用



print('--------------------欢迎进入管理员界面---------------')
opt=int(input('请输入\'数字\'选择您要进行的操作：1.新增用户 2.修改用户 3.删除用户 \n请输入数字-->：'))
if opt==1:
#新增用户
    file=open('d:\\user.txt','a')
    name=str(input('请输入新增用户名-->：'))
    age=str(input('请输入新增用户的年龄-->：'))
    tel=str(input('请输入新增用户的电话-->：'))
    adduser='\n%s\t%s\t%s'%(name,age,tel)  #这个组成一个字符串的方式，有点意思哦！！
    file.write(adduser)
    file.close()
    print('已经完成用户新增！')

if opt==2:
#修改用户
    ch_name=input('请输入需要修改资料的用户名-->：')
    ch_type=input('请输入将对该用户哪些标签内容进行修改,name或者age或者tel-->:')
    change(ch_name, ch_type) # 调用函数

if opt==3:
 #删除用户
    del_user=input('请输入需要删除的用户名-->：')
    with open('d:\\user.txt','r') as g:
        y1=g.readlines()
    with open('d:\\user.txt','w') as g2:
        for s in y1:
            if del_user in s:
                continue
            g2.write(s)
        g2.close()
        print('已经删除%s用户!'%del_user) 





