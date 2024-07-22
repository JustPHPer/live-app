import re

fileUrl = '/Users/shenchong/Downloads/iptv.m3u8'
with open(fileUrl, 'rb') as f:
    content = f.read().decode('utf-8')

pattern = re.compile(r'group-title="(.*)" tvg-id="(.*)" .*\n(.*)')
list = pattern.findall(content)
# print(list)

newList = {}
for item in list:
    if item[0] in newList:
        newList[item[0]].append({"name": item[1], "url": item[2]})
    else:
        newList[item[0]] = [{"name": item[1], "url": item[2]}]
liveStr = ""
for newItem in newList:
    value = newList[newItem]
    liveStr += newItem + ",#genre#\n"
    for item in value:
        liveStr += item['name'] + "," + item['url'] + "\n"

fileUrl2 = '/Users/shenchong/Documents/workspace/live-app/live.txt'
with open(fileUrl2, 'a') as file:
    file.write(liveStr)
