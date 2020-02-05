### Project: 2020Wuhan@Github/Ginchung
## File: Guangxi.py
## Run with 'python Guangxi.py'

# object 'sdct'
# Function: stores the info from official message
# Key: YYYY-MM-DD-HH
import sys

province='guangxi'

if sys.argv[-1]=='u':
    print('Loading Update News...')
    import requests
    from bs4 import BeautifulSoup
    r=requests.get('http://wsjkw.gxzf.gov.cn/zhuantiqu/ncov/ncovyqtb/')
    r.encoding='gb2312'
    soup = BeautifulSoup(r.text,'lxml')
    txtlst=soup.select('.lxwmbox_newtxt')
    if len(txtlst)==0:
        print('List of NewsBox is empty. Exit. ')
        exit()
    for i in txtlst[0].select('li'):
        dct=i.a.attrs
        href,title=dct['href'],dct['title']
        if '新型冠状病毒感染的肺炎疫情情况' not in title:
            continue
        print(href)
        rnew=requests.get(href)
        rnew.encoding='gb2312'
        soup = BeautifulSoup(rnew.text,'lxml')
        Sign=[False,False,False] 
        for s in soup.select('.news_show_conter')[0].contents:
            s=s.string
            if s==None:
                continue
            if '目前' in s:
                Sign[0]=True
            if Sign[0] and '累计' in s:
                Sign[1]=True
            if Sign[1] and '中' in s:
                Sign[2]=True
            if Sign[2]:
                print(title)
                substr=s[s.index('中')+1:s.index('。')]
                print(substr)
                break
    exit()
            
print('Run "python %s.py u" to load updated data. '%province)
sdct={}
sdct['2020-01-24-00']='柳州市2例、桂林市2例、梧州市1例、北海市6例、百色市1例、河池市1例'
sdct['2020-01-25-00']='柳州市3例、桂林市6例、梧州市1例、北海市6例、百色市1例、河池市3例、玉林市1例、防城港市2例'
sdct['2020-01-26-00']='南宁市1例、柳州市4例、桂林市11例、梧州市2例、北海市7例、防城港市2例、玉林市1例、百色市2例、河池市3例'
sdct['2020-01-27-00']='南宁市5例、柳州市6例、桂林市14例、梧州市2例、北海市9例、防城港市3例、玉林市2例、百色市2例、河池市3例'
sdct['2020-01-28-00']='南宁市5例、柳州市6例、桂林市15例、梧州市4例、北海市11例、防城港市3例、玉林市2例、百色市2例、河池市3例'
sdct['2020-01-29-00']='南宁7例、柳州6例、桂林16例、梧州4例、北海13例、防城港5例、玉林2例、百色2例、河池3例'
sdct['2020-01-30-00']='南宁15例、柳州10例、桂林18例、梧州4例、北海15例、防城港5例、玉林2例、百色2例、河池5例、钦州1例、贺州1例'
sdct['2020-01-31-00']='南宁市16例、柳州市12例、桂林市21例、梧州市5例、北海市23例、防城港市8例、钦州1例、玉林市5例、百色市2例、河池市6例、贺州市1例；累计出院病例中：梧州市1例、防城港市1例'
sdct['2020-02-01-00']='南宁市16例、柳州市12例、桂林市23例、梧州市5例、北海市23例、防城港市8例、钦州市2例、贵港市4例、玉林市7例、百色市2例、贺州市3例、河池市6例；累计出院病例中：梧州市1例、防城港市1例'
sdct['2020-02-02-00']='南宁市22例、柳州市14例、桂林市24例、梧州市5例、北海市26例、防城港市9例、钦州市2例、贵港市5例、玉林市8例、百色市2例、贺州市4例、河池市6例；累计出院病例中：梧州1例、防城港1例'
sdct['2020-02-03-00']='南宁市27例、柳州市15例、桂林市24例、梧州市5例、北海市27例、防城港市11例、钦州市3例、贵港市5例、玉林市8例、百色市2例、贺州市4例、河池市8例；累计出院病例中：桂林4例、梧州2例、防城港1例'
sdct['2020-02-04-00']='南宁市28例、柳州市17例、桂林市26例、梧州市5例、北海市29例、防城港市13例、钦州市4例、贵港市5例、玉林市8例、百色市2例、贺州市4例、河池市9例'
sdct['2020-02-05-00']=''
sdct['2020-02-06-00']=''

city=[]
latest='2020-02-04-00'
for i in sdct[latest].split('、'):
    city.append(i[:2])

print('city of %s: '%province,city,'\n')    
print('number of infected cities now: ',len(city))

Table={}
for k,v in zip(sdct.keys(),sdct.values()):
    if len(v)<5:
        continue
    s=['0']*len(city)
    for i in v.split('、'):
        tmp=''
        for t in i:
            if t.isdigit():
                tmp+=t
            #tmp=int(tmp)
            s[city.index(i[:2])]=tmp
        Table[k]=s
    print(s)

### Output
print(province,',',','.join(city))
for date,out in zip(Table.keys(),Table.values()):
    print(date,',',','.join(out))
