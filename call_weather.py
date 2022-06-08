from os import times
import os
import datetime



#今日の日付を文字列に変換する
today=datetime.date.today()
d1=today.strftime("%y-%m-%d")

#この関数でweather.pyを呼び出す
def work():
    import weather
    weather.main()
    print("running")

def git():
    #gitを操作してpushまでやる
    """
    参考サイト
    https://noitalog.tokyo/python-git-push/
    """
    os.system('git add .')
    #今日の日付とメッセージを結合させてcommit
    gm='git commit -m auto:'+ d1
    os.system(gm)
    os.system('git push origin w2')
    print('finish')

#実際に呼び出されるのはこの関数
def main():
    work(d1)
    git(d1)

if __name__=='__main__':
    main()