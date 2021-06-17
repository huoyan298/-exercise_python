# -*- encoding=utf8 -*-
__author__ = "Lenovo"

from airtest.core.api import *


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebFirefox
# driver = WebFirefox()
driver =  WebFirefox()
driver.implicitly_wait(20)

auto_setup(__file__)