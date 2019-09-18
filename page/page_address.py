from time import sleep

import page
from base.base import Base


class PageAddress(Base):
    # 点击 地址管理
    def page_click_manage(self):
        self.base_click(page.address_manage)

    # 点击 新增地址
    def page_click_new_address(self):
        self.base_click(page.address_new_address)
        # self.base_click_text("新增地址")

    # 输入 收件人
    def page_input_recipients(self, name):
        self.base_input(page.address_receipt_name, name)

    # 输入 手机号
    def page_input_phone(self, phone):
        self.base_input(page.address_add_phone, phone)

    # 点击 所在地区
    def page_click_area(self, province, city, area):
        # 点击 所在区域
        self.base_click(page.address_area)
        sleep(1)
        # 选择 省/直辖市
        self.base_click_text(province)
        # 选择 市
        sleep(1)
        self.base_click_text(city)
        # 选择 区
        sleep(1)
        self.base_click_text(area)

    # 输入 详细地址
    def page_input_detail_address(self, address):
        self.base_input(page.address_detail_address, address)

    # 输入 邮编
    def page_input_postcode(self, code):
        self.base_input(page.address_post_code, code)

    # 设为 默认地址
    def page_click_default_address(self):
        self.base_click(page.address_default_address)

    # 点击保存
    def page_click_save(self):
        self.base_click(page.address_save)

    # 获取所有的收件人 姓名 电话
    def page_get_name_iphone(self):
        # 必须返回
        return self.base_get_list_text(page.address_name_phone)

    # 点击编辑
    def page_click_edit(self):
        self.base_click_text("编辑")

    # 点击修改
    def page_click_modify(self):
        self.base_get_texts_click("修改")

    # 点击删除
    def page_click_delete(self):
        self.base_get_texts_click("删除")

    # 确认删除
    def page_delete_ok(self):
        self.base_click(page.address_delete_ok)

    # 删除业务方法
    def page_delete_address(self):
        # 获取地址列表中所有的收件人和电话
        el = self.base_get_list_text(page.address_name_phone)
        for i in range(len(el)):
            # 点击编辑
            self.page_click_edit()
            # 点击删除
            self.page_click_delete()
            # 确认删除
            self.page_delete_ok()

    # 断言 地址是否删除干净
    def page_address_is_exists(self):
        try:
            # 查找收件人列表
            self.base_finds(page.address_name_phone, timeout=2)
            # 找到了，说明删除地址失败
            return False
        except:
            # 异常，未找到，说明：删除地址成功
            return True


    # 输入更新地址
    def page_input_address(self, name, phone, address, code, province, city, area):
        self.page_input_recipients(name)
        self.page_input_phone(phone)
        self.page_click_area(province, city, area)
        self.page_input_detail_address(address)
        self.page_input_postcode(code)

    # 更新地址业务方法
    def page_update_address(self, name, phone, address, code, province, city, area):
        sleep(2)
        self.page_click_edit()
        self.page_click_modify()
        sleep(2)
        self.page_input_address(name, phone, address, code, province, city, area)
        self.page_click_save()

    # 组合业务方法
    def page_address(self, name, phone, address, code, province, city, area):
        self.page_click_new_address()
        self.page_input_recipients(name)
        self.page_input_phone(phone)
        self.page_click_area(province, city, area)
        self.page_input_detail_address(address)
        self.page_input_postcode(code)
        self.page_click_default_address()
        self.page_click_save()