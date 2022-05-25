from os import times
import os
import datetime

"""
参考サイト
https://note.com/financedog/n/n08a01a502a5b#7172ae1e-448e-4d28-bd79-fa34af53243b
https://qiita.com/ume1126/items/c1be49cc9ad5553ecc78
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
    fname='weather' + d1 + '.csv'
    move='move '+ fname + ' ./weather_daily'
    os.system(move)
    os.system('git add .')
    #今日の日付とメッセージを結合させてcommit
    gm='git commit -m auto:'+ d1
    os.system(gm)
    os.system('git push origin w1')
    print('finish')

#実際に呼び出されるのはこの関数
def main():
    work()

if __name__=='__main__':
    main()