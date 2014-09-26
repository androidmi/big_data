import sys
import json
reload(sys)
sys.setdefaultencoding( "utf-8" )
coding="utf-8"
name = []
month = []
uv_data = {}
uv_count = 0
lineCount = 0
dataCount = 0
for line in open("mms_upload_data"):
    lineCount += 1
    data = line.split(" -> ")
    frist = data[0].split("\t")
    f_date = frist[0]
    f_short = frist[1]
    # month
    f_date_month = f_date.split("-")[1]
    # second data
    second = data[1].split("\t")
    s_name = second[0]
    if (f_date_month not in month):
        month.append(f_date_month)
    if (s_name not in name):
        name.append(s_name)
    s_uv = int(second[1])
    if (uv_data.has_key(s_name)):
        uv_count = uv_count + s_uv
        dataCount += 1
        uv_data[s_name] = uv_count
    else:
        uv_count = s_uv
        uv_data[s_name] = uv_count
        dataCount = 0
    s_pv = second[2]
    s_arg_pv = second[3]
day = 0
for key in uv_data:
    day += 1
    print key + ":PV:" + str(uv_data[key])
print str(lineCount) +" all " + str(lineCount / day) + " data line in " + str(day) + "days"
