import time
import requests
from bs4 import BeautifulSoup
#import pymysql

headers = {
    'User-Agent':' 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }
for i in range(1, 2):
    # time.sleep(1)

    url = 'http://www.tianqihoubao.com/aqi/qingdao-2018' + str("%02d" % i) + '.html'
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    tr = soup.find_all('tr')

    for j in tr[1:]:
        td = j.find_all('td')
        Date = td[0].get_text().strip()
        Quality_grade = td[1].get_text().strip()
        AQI = td[2].get_text().strip()
        AQI_rank = td[3].get_text().strip()
        PM = td[4].get_text()
        with open('air_qingdao_2018.csv', 'a+', encoding='utf-8-sig') as f:
            f.write(Date + ',' + Quality_grade + ',' + AQI + ',' + AQI_rank + ',' + PM + '\n')


        # try:
        #     db = pymysql.connect(
        #         host='39.108.234.115',
        #         user='root',
        #         password='123456',
        #         port=3306,
        #         db='spiders'
        #     )
        #     cursor = db.cursor()
        #     cursor.execute("INSERT INTO tianqi2(data,quality_grade,AQI,AQI_rank,PM) VALUES ('"+Date+"','"+Quality_grade+"','"+AQI+"','"+AQI_rank+"','"+PM+"')")
        #     print('************** 数据保存成功 **************')
        #     db.commit()
        #     cursor.close()
        # except Exception as e:
        #     print(e)
        #     print('*************!!!! 保存失败!!!! **************')
        #     db.rollback()
        #     db.close()
