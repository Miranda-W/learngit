import json
import demjson
import numpy as np
import pandas as pd

raw_data = pd.read_csv("doctor_detail(1).csv",encoding="utf8")

department_series=raw_data['department']
hospitalname=[]
departmentname=[]

for tmp_department_list in department_series:
    tmp_department_json = demjson.decode(tmp_department_list)
    if len(tmp_department_json) == 0:
        tmp_department_json=[{'hospital':{'name':'NAN','url':'NAN'},'department':'NAN'}]
        
    for tmp_department in tmp_department_json:
            
            # print(tmp_department['hospital'])
            hospital = tmp_department['hospital']
            department=tmp_department['department']
            
            hospital_name = hospital['name']
            hospital_url = hospital['url']
            # print(hospital_name)
            # print(hospital_url)
            hospitalname.append(hospital_name)
            departmentname.append(department)
dname=pd.Series(departmentname)
name=pd.Series(hospitalname)

list_c=list(raw_data.index)
data.insert(7,'hospital_name',name)
data.insert(8,'count',list_c)
data.insert(9,'department_name',dname)

data_01=data.groupby(['hospital_name','position'])['count'].count().sort_values(ascending=False).unstack()
data_02=pd.DataFrame(data.groupby('hospital_name')['department_name'].count())
data_03=pd.merge(data_01,data_02,how='left',on='hospital_name')

writer=pd.ExcelWriter('doctor_data3.xlsx')
data_03.to_excel(writer,'hosptial_name_count',float_format='%.5f')
writer.save()


