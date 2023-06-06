import time
import os

# 定义函数以开始计时和触发提醒
def focus_timer(minutes):
    # 将分钟转换为秒
    seconds = minutes * 60 
    # 计时循环
    while seconds > 0:
        # 显示剩余时间（分钟：秒）
        print(f"Remaining Time: {seconds//60}:{seconds%60:02d}")
        # 每隔1秒减少1秒
        time.sleep(1)
        seconds -= 1

    # 提示时间到了
    os.system('say "Time is up!"')

if __name__ == '__main__':
    # 设置要专注的时间
    minutes = 25
    # 开始计时
    focus_timer(minutes)
