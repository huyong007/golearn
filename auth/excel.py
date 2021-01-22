from os import sep
import pandas as pd

# 极为重要 重要 一般
data = pd.read_csv("./auths.txt", sep=',')
# data.to_excel("./output/excel.xls", index=False,sheet_name='权限列表')

arrs = []
for auth in data:
    if '消息' in auth or '乘客' in auth:
        item = [auth, '极度重要']
        arrs.append(item)
    elif '司机' in auth or '用户' in auth:
        item = [auth, '重要']
        arrs.append(item)
    else:
        item = [auth, '一般']
        arrs.append(item)

demo_df = pd.DataFrame(arrs, columns=['权限名称', '权限重要程度'])

def style_color(df, colors):
    """
    
    :param df: pd.DataFrame
    :param colors: 字典  内容是 {标题:颜色}
    :return: 
    """
    return df.style.apply(style_apply, colors=colors)


def style_apply(series, colors, back_ground=''):
    """
    :param series: 传过来的数据是DataFramt中的一列   类型为pd.Series
    :param colors: 内容是字典  其中key 为标题名   value 为颜色
    :param back_ground: 北京颜色
    :return:
    """
    series_name = series.name[0]
    a = list()
    # 为了给每一个单元格上色
    for col in series:
        # 其中 col 为pd.DataFrame 中的 一个小单元格   大家可以根据不同需求为单元格设置不同的颜色
        # 获取什么一级标题获取什么颜色
        if series_name in colors:
            for title_name in colors:
                if title_name == series_name:
                    back_ground = 'background-color: ' + colors[title_name]
                    # '; border-left-color: #080808'
        a.append(back_ground)
    return a


style_df = style_color(demo_df, {"一般": '#1C1C1C', "极为重要": '#00EEEE', "重要": '#1A1A1A'})

with pd.ExcelWriter('df_style.xlsx', engine='openpyxl') as writer:
    #注意： 二级标题的to_excel index 不能为False
    style_df.to_excel(writer, sheet_name='sheet_name')

