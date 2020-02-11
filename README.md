# 中国nCoV-2019疫情发展的城市分辨率数据
## City-resolution statistics of nCov-2019, China

此项目是基于各省卫生健康委员会（简称“卫健委”）每日发布的中国各城市疫情数据汇总（暂不包含港澳台）。
继而能够为后续建模分析、统计学习、人工智能算法提供基础数据。

### 项目特色 Project Features
- 非爬虫数据，直接从卫健委官方数据获得 Official statistics(NHC of each province), **NOT From Web crawlers!**
- 各城市的数据，不只是各省 City-resolution! 
- 只囊括准确的确诊感染数 Just need to include the infected stats
- 按照官方隔日发布数据更新 Daily updated

### 项目的目标
根据各省卫健委发布数据，每日更新各城市的感染情况数据（目前只需要确诊病例）。

### 目前项目状况 Project Status
Province|Lastest File Date|Status|Comment|Auto Scripts?
:-|-:|-:|-:|-:
[Guangdong](Province/Guangdong.py)|2020-02-02-00|Tracked:white_check_mark:
[Beijing](Province/Beijing.py)|2020-02-05-00|Tracked:white_check_mark:
[Tianjin](Province/Tianjin.py)|2020-02-05-00|Tracked:white_check_mark:
[Anhui](Province/Anhui.py)|2020-02-05-00|Tracked:white_check_mark:
[Guangxi](Province/Guangxi.py)|2020-02-05-00|Tracked:white_check_mark:||:zap:
[Chongqing](Province/Chongqing.py)|2020-02-03-12|Stopped|Recent posts are pics|:zap:
Shanghai|None|Stopped|All posts are pics
其它各省级行政区|TO DO|

### 如何为此项目贡献？
感谢开源精神。
欢迎各位朋友们拉取项目，从最远未更新的数据开始更新，合并分支。
- 未添加的省区，按照模版[Template](Province/Template.py)进行添加；
- 对已在Province文件夹中有的省市，若是文件未更新，请一起进行对应的Python代码更新。


### 推荐外部项目 Recommend Projects
由于本项目人手不足，更新有延迟。因此，对于数据要求不是特别严格的用户（不要求包含全部历史数据），推荐几个在Github上维护较为及时的项目，以便大家使用数据库。

项目名称|特点|缺点
-|-|-
[2019新型冠状病毒疫情时间序列数据仓库](https://github.com/BlankerL/DXY-2019-nCoV-Data)|此项目通过爬取“丁香园”网站获得具体数据，爬取的是丁香园的历史数据，保存为[csv文件](https://github.com/BlankerL/DXY-2019-nCoV-Data/blob/master/csv/DXYArea.csv)，便于机器读取。|数据最早记录来自2020-01-24，而本项目最早日期为2020-01-21，见[Province/Beijing.py](Province/Beijing.py)文件

### 数据来源
感谢[各省卫健委官方网站](Source/webSource.csv)的数据发布

### 引用格式
引用本项目的格式：
```
原始数据来自国家卫生健康委员会、各省卫生健康委员会。
引用数据来自2020Wuhan@github/ginchung项目的汇总。
```

### 数据输出样式
进入Province文件夹，运行脚本：
```
cd Province;
python <省行政区名>.py
```

输出如：
```
beijing , 东城,西城,朝阳,海淀,丰台,石景,门头,房山,通州,顺义,昌平,大兴,怀柔,外地
2020-01-21-18 , 0,1,0,2,1,0,0,0,1,0,2,2,0,1
2020-01-22-18 , 0,2,1,2,1,1,0,0,1,0,2,2,0,2
2020-01-24-00 , 0,3,3,3,2,1,0,0,2,1,2,2,0,7
...
2020-02-01-00 , 3,17,27,35,12,3,1,0,13,2,12,19,1,11
2020-02-01-12 , 3,17,28,39,16,3,1,2,13,2,12,20,1,11
2020-02-02-00 , 3,17,35,41,16,4,1,2,13,6,12,21,1,11
```
 
