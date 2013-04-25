# -*- coding: utf-8 -*-

import random

# サンプル数
NUM = 1000

# 扇形の内側に入った数
inside = 0
for i in range(NUM):
    x = random.random()
    y = random.random()

    # 点の中心からの距離を計算
    if x*x+y*y <= 1:
        inside += 1

# 浮動小数点に型変換するの忘れずに
pai = 4*float(inside)/NUM
print pai

