# -*- encoding=utf8 -*-
__author__ = "Lenovo"


from airtest.core.api import *
from airtest.core.settings import Settings as ST 

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)



#获取屏幕大小的方法
# print("获取屏幕大小：",poco.get_screen_size())
width, height = device().get_current_resolution()
# 校准滑动的起点和终点
start_pt2 = (width *0.9,height / 2)
end_pt2 = (width *0.1,height / 2)

for i in range(2):
 swipe(start_pt2 , end_pt2,1000)
 sleep(1)  # 等待设备的响应

touch(Template(r"tpl1623985495845.png", record_pos=(0.121, -0.007), resolution=(1079, 2340)))

# touch (Template(r"tpl1624001190965.png", record_pos=(0.386, -0.925), resolution=(1079, 2340)))
sleep(0.5)

# assert_exists(Template(r"tpl1624026313531.png")
dou_exist = poco("com.douban.frodo:id/skip")

if  (dou_exist.exists()):
  dou_exist.click()
# sleep(0.5)
else:
  wait(Template(r"tpl1623986098899.png", record_pos=(-0.378, -0.825), resolution=(1079, 2340)))
  touch(Template(r"tpl1623986098899.png", record_pos=(-0.378, -0.825), resolution=(1079, 2340)))
wait(Template(r"tpl1624000769955.png", record_pos=(0.012, 0.905), resolution=(1079, 2340)))
poco("android.widget.LinearLayout").offspring("com.douban.frodo:id/main_container").offspring("android.widget.LinearLayout").child("android.widget.RelativeLayout")[2].offspring("com.douban.frodo:id/mIcon").click()



touch(Template(r"tpl1623986157126.png", record_pos=(-0.374, -0.669), resolution=(1079, 2340)))

sleep(0.3)
swipe(Template(r"tpl1623986272516.png", record_pos=(-0.005, 0.098), resolution=(1079, 2340)), vector=[0.0019, -0.1692])                                                    