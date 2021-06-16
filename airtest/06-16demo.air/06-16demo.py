# -*- encoding=utf8 -*-
__author__ = "huoyanyang"

from airtest.core.api import *
from airtest.core.settings import Settings as ST     
ST.CVSTRATEGY = ["tpl", "sift","brisk"]

auto_setup(__file__)
touch(Template(r"tpl1623846274479.png", threshold=0.5999999999999999, rgb=False, target_pos=4, record_pos=(-0.105, -0.293), resolution=(1079, 2340)))
touch(Template(r"tpl1623846675198.png", record_pos=(0.006, -0.148), resolution=(1079, 2340)))
wait(Template(r"tpl1623851905998.png", record_pos=(0.025, -0.621), resolution=(1079, 2340)))

dev =device()
dev.minitouch.swipe_along([[257, 1384],[528, 1384],[532, 1659],[528, 1937],[806, 1937]])