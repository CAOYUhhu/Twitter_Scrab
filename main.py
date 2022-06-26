import json
from time import sleep, strftime, localtime, time

import TwitterScraper
import StoredData
import SetJSRun

def main():
    TS = TwitterScraper.TwitterScraper()
    accountpage = 'https://twitter.com/new_nft_alert/'
    target_route = r'D:\token\0 My Libraries\9.AutoMint\AutoMint_JS_Subscribe_AND_Mint_withPY'
    bat_name = r'\监测土狗Mint情况.bat'
    addr_matrix=[]
    while True:
        try:
            (project, addr) = TS.tweetget(accountpage)
            if StoredData.is_included(addr, addr_matrix):
                print('not updated...', strftime('%Y-%m-%d %H:%M:%S', localtime(time())))
            else:
                addr_matrix.append(addr)
                addr_json = {'addrs':[{'addr': addr},{'NFTname': project}]}
                json_route = target_route + r'\addr.json'
                with open(json_route, 'w') as fw:
                    json.dump(addr_json, fw)
                SetJSRun.runbat(target_route, bat_name)
        except:
            print('no free mint contract', strftime('%Y-%m-%d %H:%M:%S', localtime(time())))
        sleep(5)

if __name__ == '__main__':
    main()
