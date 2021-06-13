# Covid-19Visualization

数据大屏展示项目

这是一个基于echarts和flask的可视化项目。完成于2021.6.13

技术栈：
html  ajax  JavaScript

python：requests flask

实现流程：

1. 数据来源：腾讯实时疫情 https://news.qq.com/zt2020/page/feiyan.htm#/
具体数据在：
   https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5
   https://view.inews.qq.com/g2/getOnsInfo?name=disease_other
通过reques爬虫获取数据，保存至本地数据库。

2. 前端页面设计  
通过css设计出网页的布局和分块。echarts工作原理为用图表填充html元素块，所以需要提前为他分配好大小。
jquery + ajax技术实现实时数据更新
官网下载echarts的js文件，找到需要的示例对代码进行修改


3. 后端部分设计
utils.py 与数据库交互
flask的基本运用
