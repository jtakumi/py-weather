import schedule
import time
import datetime
import os

"""
参考サイト
https://note.com/financedog/n/n08a01a502a5b#7172ae1e-448e-4d28-bd79-fa34af53243b
"""

#この関数でweather.pyを呼び出す
def work():
    import weather
    weather.main()
    print("running")
    #今日の日付を文字列に変換する
    today=datetime.date.today()
    d1=today.strftime("%y-%m-%d")
    #gitを操作してpushまでやる
    """
    参考サイト
    https://noitalog.tokyo/python-git-push/
    """
    os.system('git add .')
    #今日の日付とメッセージを結合させてcommit
    gm='git commit -m auto:'+ d1
    os.system(gm)
    os.system('git push origin w1')
    print('finish')

def main():
    work()

#AM9:00実行
schedule.every().day.at("9:00").do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
