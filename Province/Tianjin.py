### Project: 2020Wuhan@Github/Ginchung
## File: tianjin.py
## Run with 'python tianjin.py'

# object 'sdct'
# Function: stores the info from official message
# Key: YYYY-MM-DD-HH

province='tianjin'

sdct={}
sdct['2020-01-26-00']='和平区1例，南开区1例，河东区3例，河北区2例，西青区1例，滨海新区1例，外地来津1例'
sdct['2020-01-27-00']='河北区5例、河东区2例、南开区2例、西青区1例、和平区1例、滨海新区1例、外地来津2例'
sdct['2020-01-28-00']='河北区7例、河东区5例、南开区2例、西青区1例、和平区1例、滨海新区1例、红桥区1例、河西区3例、外地来津2例'
sdct['2020-01-29-00']='河北区7例、河东区5例、河西区3例、南开区2例、西青区2例、和平区1例、红桥区1例、滨海新区1例、外地来津2例'
sdct['2020-01-30-00']='河北区7例、河东区5例、河西区3例、南开区2例、西青区2例、和平区2例、红桥区1例、滨海新区1例、外地来津4例'
sdct['2020-01-31-00']='河北区8例、河东区5例、河西区3例、和平区3例、南开区2例、西青区2例、红桥区2例、滨海新区2例、外地来津4例'
sdct['2020-02-01-00']='河北区8例、河东区5例、河西区3例、和平区3例、南开区2例、西青区2例、红桥区2例、滨海新区2例、宁河区1例，外地来津4例'
sdct['2020-02-02-00']='河北区9例、河东区6例、河西区3例、和平区3例、宝坻区3例、东丽区3例、南开区2例、西青区2例、红桥区2例、宁河区2例、滨海新区2例、外地来津4例'
sdct['2020-02-03-00']='河北区9例、河东区9例、宝坻区5例、和平区4例、河西区3例、东丽区3例、宁河区3例、南开区2例、西青区2例、红桥区2例、滨海新区2例、外地来津4例'
sdct['2020-02-04-00']='宝坻区11例、河东区9例、河北区9例、和平区5例、宁河区4例、河西区3例、南开区3例、东丽区3例、西青区3例、红桥区2例、滨海新区2例、外地来津6例'
sdct['2020-02-05-00']='宝坻区13例、河东区10例、河北区10例、和平区6例、宁河区4例、河西区4例、南开区3例、东丽区3例、西青区3例、红桥区2例、滨海新区2例、津南区1例、外地来津6例'
sdct['2020-02-06-00']=''

city=[]
latest='2020-02-05-00'
for i in sdct[latest].split('、'):
    city.append(i[:2])

print('city of %s: '%province,city,'\n')    
print('number of infected cities now: ',len(city))

Table={}
for k,v in zip(sdct.keys(),sdct.values()):
    if len(v)<5:
        continue
    s=['0']*len(city)
    v=v.replace('，','、')
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
