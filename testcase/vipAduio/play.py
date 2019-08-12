#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from time import sleep
import tool.swipe as swipe
import tool.isElement as isElements
import tool.back as back

# 大咖播放页

# 原条目
def wiki_detail(self):
    print("原条目")
    self.driver.find_element_by_id('tv_wiki_play_detail_wiki_web').click()
    sleep(5)
    print("进入该音频对应的条目详情页")


# 点击头像，进入大咖教师主页
def fragment_circle_img(self):
    print("大咖教师头像")
    title = self.driver.find_element_by_id('tv_wiki_play_fragment_name').text
    self.driver.find_element_by_id('iv_wiki_play_fragment_circle_img').click()
    sleep(5)
    # 判断是否进入大咖教师页面
    # name=self.driver.find_element_by_id('').text
    # if name==title:
    #     print("进入的是大咖教师主页列表")
    # else:
    #     print("未进入大咖教师主页列表")


# 暂停/播放
def wiki_play(self):
    print("播放页的播放状态")
    self.driver.find_element_by_id('iv_wiki_play_detail_play').click()


# 拖动进度条


# 大咖头像、文稿页面切换
def play_manuscripts(self):
    # 左滑页面
    screen = swipe.get_size(self)
    self.driver.swipe(screen[0] * 0.75, screen[1] * 0.5, screen[0] * 0.05, screen[1] * 0.5, 6000)
    sleep(5)
    flag = isElements.find_Element(self, 'id', 'wiki_play_detail_pager')
    if flag:
        print("切换到文稿")
        # 判断该音频是否有文稿
        line = isElements.find_Element(self, 'id', 'rl_wiki_play_detail_lineWaveVoiceView')
        if line:
            print("暂无文稿")
        else:
            print("该音频有文稿，滑动查看文稿")
            self.driver.swipe(50 * 0.5, 180 * 0.75, 500 * 0.5, 700, 6000)
            sleep(5)
        # 切换到大咖头像页
        screen1 = swipe.get_size(self)
        self.driver.swipe(screen1[0] * 0.05, screen1[1] * 0.5, screen1[0] * 0.75, screen1[1] * 0.5, 6000)
        # 判断是否切换成功
        play = isElements.find_Element(self, 'id', 'iv_wiki_play_detail_play')
        if play:
            print("切换到了大咖头像页")
        else:
            print("未切换")
    else:
        print("未切换到文稿")


# 上一首/下一首
def play_prev_next(self):
    # 获取当前音频在列表中的序号

    num = self.driver.find_element_by_id('tv_wiki_play_detail_play_list').text
    num = int(num.split('/')[0])
    print("num:", num)
    self.driver.find_element_by_id('iv_wiki_play_detail_prev').click()
    sleep(5)
    prev = int(self.driver.find_element_by_id('tv_wiki_play_detail_play_list').text.split('/')[0])
    print("prev:", prev)
    if num == prev:
        print("没有上一首")
    else:
        if num == prev + 1:
            print("切换到上一首成功")
        else:
            print("切换到上一首失败")
    sleep(5)

    # 下一首

    num1 = self.driver.find_element_by_id('tv_wiki_play_detail_play_list').text
    num1 = int(num1.split('/')[0])
    print("num1:", num1)
    self.driver.find_element_by_id('iv_wiki_play_detail_next').click()
    sleep(5)
    self.driver.find_element_by_id('iv_wiki_play_detail_play').click()
    next = int(self.driver.find_element_by_id('tv_wiki_play_detail_play_list').text.split('/')[0])
    print("next:", next)
    if num1 == next:
        print("没有上一首")
    else:
        if num == next - 1:
            print("切换到下一首成功")
        else:
            print("切换到下一首失败")
    sleep(5)


# 定时
def play_set_time(self):
    self.driver.find_element_by_id('tv_wiki_play_detail_set_time').click()
    sleep(5)
    #选择播完当前音频
    self.driver.find_elements_by_id('recycler_popu_wiki_detail_set_time')[0].find_elements_by_class_name('android.widget.RelativeLayout')[1].click()
    sleep(5)
    text=self.driver.find_element_by_id('tv_wiki_play_detail_set_time').text
    print("text:",text)
    if text=='本节完':
        print("定时选择的是【播完当前音频】")
    else:
        print("定时选择的是【播放当前音频】，但播放页显示的文案不正确")

    #选择15分钟
    self.driver.find_element_by_id('tv_wiki_play_detail_set_time').click()
    self.driver.find_elements_by_id('recycler_popu_wiki_detail_set_time')[0].find_elements_by_class_name('android.widget.RelativeLayout')[2].click()
    sleep(5)
    text_15 = self.driver.find_element_by_id('com.mbalib.android.wiki:id/tv_wiki_play_detail_set_time').text
    text_15s=text_15.split(':')
    if int(text_15s[0])*60+int(text_15s[1]) < 900:
        print("定时选择的是【15分钟】")
    else:
        print("定时选择的是【15分钟】，但播放页显示的文案不正确")

    #选择30分钟
    self.driver.find_element_by_id('tv_wiki_play_detail_set_time').click()
    self.driver.find_elements_by_id('recycler_popu_wiki_detail_set_time')[0].find_elements_by_class_name(
        'android.widget.RelativeLayout')[3].click()
    sleep(5)
    text_30 = self.driver.find_element_by_id('com.mbalib.android.wiki:id/tv_wiki_play_detail_set_time').text
    text_30s = text_30.split(':')
    if int(text_30s[0]) * 60 + int(text_30s[1]) < 1800:
        print("定时选择的是【30分钟】")
    else:
        print("定时选择的是【30分钟】，但播放页显示的文案不正确")

    #选择60分钟
    self.driver.find_element_by_id('tv_wiki_play_detail_set_time').click()
    self.driver.find_elements_by_id('recycler_popu_wiki_detail_set_time')[0].find_elements_by_class_name(
        'android.widget.RelativeLayout')[4].click()
    sleep(5)
    text_60 = self.driver.find_element_by_id('com.mbalib.android.wiki:id/tv_wiki_play_detail_set_time').text
    text_60s = text_60.split(':')
    if int(text_60s[0]) * 60 + int(text_60s[1]) < 3600:
        print("定时选择的是【60分钟】")
    else:
        print("定时选择的是【60分钟】，但播放页显示的文案不正确")

    # 选择不开启
    self.driver.find_element_by_id('tv_wiki_play_detail_set_time').click()
    self.driver.find_elements_by_id('recycler_popu_wiki_detail_set_time')[0].find_elements_by_class_name('android.widget.RelativeLayout')[0].click()
    sleep(5)
    textNoOpen = self.driver.find_element_by_id('com.mbalib.android.wiki:id/tv_wiki_play_detail_set_time').text
    if textNoOpen=="定时":
        print("定时选择的是【不开启】")
    else:
        print("定时选择的是【不开启】，但播放页显示的文案不正确")

#定时为播完当前音频
def set_time_NowPlay(self):
    self.driver.find_element_by_id('tv_wiki_play_detail_set_time').click()
    sleep(5)
    # 选择播完当前音频
    self.driver.find_elements_by_id('recycler_popu_wiki_detail_set_time')[0].find_elements_by_class_name(
        'android.widget.RelativeLayout')[1].click()
    sleep(5)
    text = self.driver.find_element_by_id('tv_wiki_play_detail_set_time').text
    print("text:", text)
    if text == '本节完':
        print("定时选择的是【播完当前音频】")
        #获取当前音频的时长
        self.driver.find_element_by_id('tv_wiki_play_detail_play_list').click()
        sleep(5)
        list = self.driver.find_elements_by_id('recycler_popu_wiki_detail_list')[0].find_elements_by_class_name("android.widget.LinearLayout")
        times = list[0].find_element_by_id('tv_item_wiki_detail_list_time').text.split(':')
        time=(int(times[0])+int(times[1]))*1000
        #关闭播放列表弹窗
        self.driver.find_element_by_id('tv_popu_wiki_play_detail_list_close').click()
        #点击播放
        self.driver.find_element_by_id('iv_wiki_play_detail_play').click()
        sleep(time)
        t=self.driver.find_element_by_id('tv_wiki_play_detail_set_time').text
        if t=="定时":
            print("定时结束")
        else:
            print("未播完")

    else:
        print("定时选择的是【播放当前音频】，但播放页显示的文案不正确")

# 下载,type  0为马上开通   1为取消
def play_download(self, isVip, type):
    print("离线下载")
    self.driver.find_element_by_id('tv_wiki_play_detail_download').click()
    sleep(5)
    if isVip:
        # 判断是否在【下载管理】列表
        print("vip用户")
    else:
        print("不是vip用户")
        text = self.driver.find_element_by_id('textView3').text
        if text == "大咖VIP可下载语音":
            print("触发弹窗：大咖vip可下载语音")
            if type == 0:
                print("跳转到开通页")
                self.driver.find_element_by_id('tvSignUp').click()
                sleep(5)
                title = self.driver.find_element_by_id('tvTitle').text
                if title == "大咖讲百科VIP":
                    print("跳转到开通vip页")
                else:
                    print("未跳转到开通vip页")
            else:
                print("取消")
                self.driver.find_element_by_id('tvCancel').click()
        else:
            print("弹窗提示不正确")


# 分享
def share_paly(self):
    print("分享到微信")
    self.driver.find_element_by_id('tv_wiki_play_detail_share').click()
    sleep(5)


# 播放列表-切换音频
def play_list(self, isVip):
    print("播放列表")
    self.driver.find_element_by_id('tv_wiki_play_detail_play_list').click()
    sleep(5)
    flag = isElements.find_Element(self, 'id', 'recycler_popu_wiki_detail_list')
    if flag:
        print("播放列表弹窗")
        # 切换音频
        list = self.driver.find_elements_by_id('recycler_popu_wiki_detail_list')[0].find_elements_by_class_name("android.widget.LinearLayout")
        title = list[1].find_element_by_id('tv_item_wiki_detail_list_title').text[1:]
        title = title[1:]
        print("title:",title)
        list[1].click()
        isVipPanel = isElements.find_Element(self, 'id', 'bg')
        sleep(5)
        if isVipPanel:
            print("触发开通vip弹窗提示")
            # 点击关闭
            self.driver.find_element_by_id('ivCancel').click()
            sleep(5)
        else:
            print("未触发开通vip弹窗提示")
            # 判断进入的是否为播放页
            #sleep(5)
            #self.driver.find_element_by_id('iv_wiki_play_detail_back').click()
            #self.driver.find_element_by_id('iv_play_state').click()
            # playTitle=self.driver.find_element_by_id('tv_title').text
            # print("playTitle:", playTitle)
            # if title==playTitle:
            #     print("切换音频成功")
            # else:
            #     print("切换音频未成功")
    else:
        print("未显示出播放列表弹窗")


# 播放列表-关闭
def play_list_off(self):
    print("播放列表")
    self.driver.find_element_by_id('tv_wiki_play_detail_play_list').click()
    sleep(5)
    flag = isElements.find_Element(self, 'id', 'recycler_popu_wiki_detail_list')
    if flag:
        print("播放列表弹窗")
        # 关闭播放列表
        self.driver.find_element_by_id('tv_popu_wiki_play_detail_list_close').click()
        sleep(5)
        # 判断是否关闭了弹窗
        play = isElements.find_Element(self, 'id', 'iv_wiki_play_detail_play')
        if play:
            print("关闭列表弹窗成功")
        else:
            print("未返回到播放页")
    else:
        print("未显示出播放列表弹窗")
