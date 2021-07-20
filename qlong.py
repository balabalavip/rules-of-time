import requests
import json
f = open(r'../config/auth.json', 'r')
f = f.read()
f = json.loads(f)
f = f['token']
headers = {
    'Origin': 'http://fiddle.jshell.net',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*',
    'Referer': 'http://fiddle.jshell.net/_display/',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Authorization': 'Bearer '+f
}


def cronslist():
    r = requests.get(
        'http://localhost:5700/api/crons?searchValue=&t=1626666655292', headers=headers).text
    cronlist = json.loads(r)
    for i in cronlist['data']:
        crname = i['name']
        crcommand = i['command']
        crschedule = i['schedule']
        crid = i['_id']
        if crschedule == '0 6 * * *':
            print(crname, crcommand, crschedule, crid)
            data = {"name": crname, "command": crcommand,
                    "schedule": '0 */8 * * *', "_id": crid}
            re = requests.put(
                'http://localhost:5700/api/crons?t=1626666655292', headers=headers, data=data).text
            print(re)
    print('更新完成')


cronslist()
