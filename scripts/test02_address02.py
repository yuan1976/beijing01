import sys
import os

from tool.get_log import GetLog

sys.path.append(os.getcwd())
import pytest
from tool.read_yaml import read_yaml
from page.page_in import PageIn
from tool.get_driver import GetDriver

# def get_data(key):
#     arrs = []
#     if key == "add":
#         data = read_yaml("address.yaml").get("add_address")
#         arrs.append(tuple(data.values()))
#         return arrs
#     else:
#         data = read_yaml("address.yaml").get("update_address")
#         arrs.append(tuple(data.values()))
#         return arrs

log = GetLog.get_log()

def get_data(key):
    arrs = []
    data = read_yaml("address.yaml").get(key)
    arrs.append(tuple(data.values()))
    return arrs


class TestAddress:
    # 初始化
    def setup_class(self):
        # 获取 PageAddress
        self.address = PageIn().page_get_pageaddress()
        # 获取PageLogin 并且登录成功
        PageIn().page_get_pagelogin().page_login_address()
        # 点击 地址管理
        self.address.page_click_manage()

    # 结束
    def teardown_class(self):
        # 关闭driver对象
        GetDriver.quit_driver()

    # 测试新增地址方法
    @pytest.mark.parametrize("name, phone, address, code, province, city, area", get_data("add_address"))
    def test01_add_address(self,name, phone, address, code, province, city, area):
        # 调用地址管理新增业务方法
        self.address.page_address(name, phone, address, code, province, city, area)
        # 组合收件人 和电话
        expect = name+"  "+phone
        try:
             # 断言
            assert expect in self.address.page_get_name_iphone()
        except Exception as e:
            # 截图
            self.address.base_get_img()
            # 写日志
            log.error(e)
            # 抛异常
            raise


    # 测试更新地址方法
    @pytest.mark.parametrize("name, phone, address, code, province, city, area", get_data("update_address"))
    def test02_update_address(self,name, phone, address, code, province, city, area):
        # 调用更新业务方法
        self.address.page_update_address(name, phone, address, code, province, city, area)
        # 组合收件人 和电话
        expect = name+"  "+phone
        try:
            # 断言
            assert expect in self.address.page_get_name_iphone()
        except Exception as e:
            # 截图
            self.address.base_get_img()
            # 写日志
            log.error(e)
            # 抛异常
            raise

    # 删除地址
    def test03_delete_address(self):
        # 调用删除地址业务方法
        self.address.page_delete_address()
        try:
            # 断言 是否删除干净
            assert self.address.page_address_is_exists()
        except Exception as e:
            # 截图
            self.address.base_get_img()
            # 写日志
            log.error(e)
            # 抛异常
            raise