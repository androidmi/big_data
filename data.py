import json
import sys
"""sms public data"""
reload(sys)
sys.setdefaultencoding( "utf-8" )
has_logo_file = open("has_logo.txt", "w")
# data in server
spider = []
all_spider_count = 0
no_logo_file = open("no_logo.txt", "w")
for line in open("sample.json"):
    all_spider_count = all_spider_count + 1
    j = json.loads(line)
    number = j['phone'][0]['number']
    logourl = ""
    if ("logourl" in j):
        logourl = j['logourl']
    name = j['name']
    if logourl == "":
        spider.append(number + "|" + name)
        no_logo_file.write(number + "|" + name + "\n")
    else:
        has_logo_file.write(number + "|" + name + "\n")
has_logo_file.close()
print " spdier data count :" + str(len(spider))
# local data in yhds
local = []
for line in open("sms_public_number.db"):
    data = line.split("|")
    number = data[0]
    name = data[1]
    local.append(number + "|" + str(name))
#print local
#print spider
for litem in local:
    for sitem in spider:
        if litem == sitem:
            print sitem
#has logo data
has_logo = []
for line in open("logo"):
    data = line.split("|")
    number = data[1]
    name = data[0]
    has_logo.append(number + "|" + str(name))

#has logo but no input
has_log_no_input = []
for litem in local:
    for hitem in has_logo:
        #same number
        if litem.split("|")[0] ==  hitem.split("|")[0]:
            print 1









