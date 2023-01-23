import pandas as pd
from pyecharts.charts import Timeline, Bar
from pyecharts import options as opts

# data1=pd.read_excel(r'D:\data_analyse\data\非洲通讯产品销售数据.xlsx',sheet_name=0)
# data1_country=data1.groupby('国家')[['销售额','利润']].sum()
# data1_country.reset_index(inplace=True)
# print(data1_country)
# # data1_country['国家']=data1_country['国家'].astype('str')
# # data1_country['销售额']=data1_country['销售额'].astype('int')
# # data1_country['利润']=data1_country['利润'].astype('int')
# # print(type(list(data1_country['国家'].values)))
# # print(type(list(data1_country['销售额'].values)))
#
# c=(
#     Bar()
#     .add_xaxis([str(i) for i in data1_country['国家'].values])
#     .add_yaxis('销售额',[int(value) for value in data1_country['销售额'].values])
#     .add_yaxis('利润',[int(value) for value in data1_country['销售额'].values])
#     .set_global_opts(
#         title_opts=opts.TitleOpts(title='各国销售额和利润')
#     )
# )
# c.render("各国销售和利润情况.html")
#     i=0
#     for year in range(2017,2020):
#         lists = []
#         temp = datain
#         for j in range(i,len(temp),4):
#             lists.append({"name":namelist[j],"value":temp[j]})
#         i+=1
#         dataout[year] = lists
#     print(dataout[2018])
        # temp=datain
        # for i in range(len(temp)):

            # if year in dataout.keys():
            #     dataout[year][i]={"name":namelist[i],"value":temp[i]}
            # else:
            #     dataout[year] = {"name":namelist[i],"value":temp[i]}
# 第三版：
data1=pd.read_excel(r'D:\data_analyse\data\非洲通讯产品销售数据.xlsx',sheet_name=0)
data1['日期']=data1['日期'].astype('str')
data1['年份']=[x[:4] for x in data1['日期']]
data1['年份']=data1['年份'].astype('int')
print(data1)
data1=pd.DataFrame(data1)
data1_country=data1.groupby(['国家','年份'])[['销售额','利润']].sum()
data1_country.reset_index(inplace=True)
def countrysales(datain):
    dataout = {}
    for year in range(data1_country['年份'].min(), data1_country['年份'].max()+1):
        dataout[year] = []
        for i in range(len(datain[datain['年份']==year])):
            y=datain[datain['年份']==year]
            y.reset_index(inplace=True)
            dataout[year].append({'name':y['国家'][i],'value':y['销售额'][i]})
    return dataout
def countrylubric(datain):
    dataout = {}
    for year in range(data1_country['年份'].min(), data1_country['年份'].max()+1):
        dataout[year] = []
        for i in range(len(datain[datain['年份']==year])):
            y=datain[datain['年份']==year]
            y.reset_index(inplace=True)
            dataout[year].append({'name':y['国家'][i],'value':y['利润'][i]})
    return dataout
country_sales=countrysales(data1_country)
country_lubric=countrylubric(data1_country)
x=list(data1_country[data1_country['年份']==2017]['国家'].values)
def country_overlap_chart(year:int) -> Bar:
    bar=(
        Bar()
        .add_xaxis(xaxis_data=x,
                   )
        .add_yaxis(
            series_name='销售额',
            y_axis=country_sales[year],
            is_selected=True,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name='利润',
            y_axis=country_lubric[year],
            is_selected=True,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                name='国家名称',
                name_gap=10,
                name_rotate=45,
                name_textstyle_opts=opts.TextStyleOpts(
                    color='green',
                    font_size=20,


                )

            ),
            title_opts=opts.TitleOpts(
                title="{}各国销售额和利润情况".format(year),subtitle="作者王大林真帅"
            ),
            tooltip_opts=opts.TooltipOpts(
                is_show=True, trigger="axis", axis_pointer_type="shadow"
            ),
        )

    )
    return bar
timeline=Timeline()

for y in range(data1_country['年份'].min(), data1_country['年份'].max()+1):
    timeline.add(country_overlap_chart(year=y), time_point=str(y))
timeline.add_schema(is_auto_play=True,play_interval=1000)
timeline.render('各国销售额和利润情况.html')



