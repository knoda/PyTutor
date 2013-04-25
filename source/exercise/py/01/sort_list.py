# -*- coding: utf-8 -*-

import random

# ソート関数の定義
def sort(x):
    # リスト全体をトレースする
    for i in range(len(x)):
        # 基準となる値，インデックスを保持
        min_a = x[i]
        ind = i
        # それよりも小さな値がないか調べる
        for j in range(i+1,len(x)):
            if min_a > x[j]:
                min_a = x[j]
                ind = j
        # 値を入れ替える
        t = x[i]
        x[i] = x[ind]
        x[ind] = t

x = []
for i in range(10):
    x.append(random.randint(10,100))

# ソート前のリスト
print x

# Python の引数は参照渡しなので，引数が書きかわる
sort(x)

# ソート後のリスト
print x

