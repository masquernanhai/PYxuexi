# 列表：增加.append(),delete(),list(),pop(index)
import pandas as pd


def list():
    a=[]
    for i in range(1,100):
        a.append(i)
    print(a)
    print(len(a))
    for j in a:
        if j%2==0:
            a.remove(j)
    print(a)

def dict():
    b={}
    for i in range(0,100):
        b[i]=i*i/2
    c={}
    b.update({"大林":"帅哥"})
    print(b)
# 元组没有重复值，不能被修改
def yuanzu():
    a=(1,2,3,4,5)

datafirst=read_csv("路径",encodings="utf-8")
datafirst.isnull().sum()  #空值相加
ditafirst["shijian"].value_counts().sum()  #同类几个，总共几个
datafirst.duplicates().value_counts() #完全相同的行分别有几个
datefirst.drop(datafirst[datafirst.shijian=="--"].index) #删除 index为行指引，columns为列指引
datafirst.dropna(axis=0)  #删除有空值的行
datafirst.dropna(subset=['列标签'],inplace=True) #找到列标签，找到其中空值，删掉行
datafirst=pd.DataFrame('dalin'=[1,2,3,4,5],'dahai'=[1,2,3,4,5,6])
print(datafirst.describe())

datafirst.head(10)  #展示前10行
datafirst.drop_duplicates(['列1','列2'])  #删除列1和列2同时相同的行
datafirst.loc[3:4,['mountains','height']] #取第四行和第五行的mountains列和height列

allsum=datafirst['列1'].value_counts().sum()
set_option('display.max_rows',None)
allrecent=datafirst['列1']
allrecent=allrecent.reset_index(drop=True)#重新拍一次索引
present=[],absent=[]
for i in range(len(allrecent)):
    data=allrecent[i][:4]
    if data>=2019:
       present.append(data)
    if data<2019:
        absent.append(data)
present_plt=len(present)
absent_plt=len(absent)
x=[present_plt,absent_plt]

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['FangSong']
plt.title('大林帅气程度比')
plt.pie(x,lables=['真帅','特别帅'],autopct='%0.2f%%')
plt.show()
plt.close()

datafirst_course_id=DataFrame(datafirst['lie1'].value_counts) #转化为dataframe,并使课程名称为行索引
y=datafirst_course_id['course_id'][:20]
plt.title('用户课程选择情况')
plt.barh(datafirst_course_id.index,y)
plt.rcParams['font.sans-serif']='SimHei'
plt.show()
plt.close()

plt.scatter(datafirst['course'],datafirst['course_id'])#散点图

if __name__=='__main__':
    # list()
    dict()




Datathird=Datathird.drop(Datathird[Datathird.login_place=='英国'].index)

