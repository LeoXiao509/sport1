import requests
import pandas as pd
from bs4 import BeautifulSoup

# 指定要抓取的网页URL
url = 'https://wgynl.pixnet.net/blog/post/2292844-world-gym-%E4%B8%96%E7%95%8C%E5%81%A5%E8%BA%AB%E4%BF%B1%E6%A8%82%E9%83%A8-%E5%85%A8%E5%8F%B0'  # 替换为实际的URL

# 发送HTTP GET请求
response = requests.get(url)

# 解析网页内容
soup = BeautifulSoup(response.content, 'html.parser')
    
# 查找所有表格元素
tables = soup.find_all('table')

    
if not tables:
    print("沒有任何表格")
else:
    table = tables[0]
    
    # 删除 <tbody> 中的第一个 <td> 元素
    
    if table:
       first_td = table.find('tr')
       if first_td:
           first_td.decompose()
    if table:
       Second_td = table.find('tr')
       if Second_td:
           Second_td.decompose()

    df = pd.read_html(str(table))[0]

    # 合并第0列和第1列的内容，并放在第0列
    df[0] = df[0].astype(str) + ' ' + df[1].astype(str)
    
    # 删除原来的第1列、第3列
    df.drop(columns=[1], inplace=True)
    df.drop(columns=[3], inplace=True)

    df[1] = df[2].astype(str)
    df.drop(columns=[2], inplace=True)
    
    print(df)
    
    html_table = df.to_html(index=False)
    
    with open('分店.html', 'w', encoding='utf-8') as f:
       f.write(html_table)