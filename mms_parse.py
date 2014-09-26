import sys
import json
reload(sys)
sys.setdefaultencoding( "utf-8" )
coding="utf-8"
name = {}
month = []
date = []
month_data = {}
uv_count = 0
lineCount = 0
dataCount = 0
flag = False
for line in open("mms_upload_data"):
    lineCount += 1
    data = line.split(" -> ")
    frist = data[0].split("\t")
    f_date = frist[0]
    f_short = frist[1]
    #month
    f_date_month = f_date.split("-")[1]
    # second data
    second = data[1].split("\t")
    s_name = second[0]
    s_uv = int(second[1])
    s_pv = second[2]
    s_arg_pv = second[3]
    if (name.has_key(s_name+"\t"+f_short)):
        name.get(s_name+"\t"+f_short).append(s_uv)
    else:
        name[s_name+"\t"+f_short] = []
        name.get(s_name+"\t"+f_short).append(s_uv)
    if (f_date not in date):
        date.append(f_date) 
        
for key in name:
    print key + "\t" + str(name[key])
print str(date)
