=======================================
Python入門 Part1 (プログラミングの基礎)
=======================================

このテキストは， `Python Scientific Lecture Notes の日本語翻訳 <http://www.ike-dyn.ritsumei.ac.jp/~uchida/scipy-lecture-notes/index.html>`_ から，
特に重要度が高いと考えるものを抜粋して作成してある．
より詳細な内容が知りたくなったら，
原著を参照することをおすすめする．

:参考サイト1: `NumPy and Scipy Documentation <http://docs.scipy.org/doc/>`_
:参考サイト2: `The Matplotlib API <http://matplotlib.org/api/index.html>`_

Python入門
==========

-------
iPython
-------

コマンドラインから

::

    $ ipython

と打ち込むと，インタラクティブシェルが立ち上がる．

.. sourcecode:: ipython

    In [1]: print "Hello world"
    Hello world

このように，プロンプトから直接コマンドを入力しても良いし，

.. sourcecode:: ipython

    In [2]: run example.py

このようにして，スクリプトを実行することもできる．

他にも

* **ls**, **pwd**, **cd** が使える
* **whos** を使うと，メモリ上の変数を一覧できる
* **Tab 補完** を使えば，関数名，ファイル名，オブジェクト名，メソッドなど，ありとあらゆる補完ができる
* **up キー** でコマンド履歴を遡る

といった拡張機能があり，標準のインタラクティブシェルより便利である．

+------------------+-------------------------------------------------------+
| who              | show contents of workspace                            |
+------------------+-------------------------------------------------------+
| who int          | show integers in workspace                            |
+------------------+-------------------------------------------------------+
| whos             | show details of workspace contents                    |
+------------------+-------------------------------------------------------+
| whos int         | show details of integers in workspace                 |
+------------------+-------------------------------------------------------+
| psearch msg*     | search for objects in the workspace starting with msg |
+------------------+-------------------------------------------------------+
| psearch msg* int | restrict search to just integers                      |
+------------------+-------------------------------------------------------+
| reset            | delete all variables from workspace                   |
+------------------+-------------------------------------------------------+
| del var1,var2    | delete specific variable(s) from workspace            |
+------------------+-------------------------------------------------------+

------------------
とりあえず慣れよう
------------------

下の例のように，上から順番にコードを打ち込んでみよう．

.. sourcecode:: ipython

    In [1]: a = 3

    In [2]: b = 2 * a

    In [3]: type(b)
    Out[3]: int

    In [4]: a * b
    Out[4]: 18

    In [5]: b = 'hello'

    In [6]: type(b)
    Out[6]: str

    In [7]: b + b
    Out[7]: 'hellohello'

    In [8]: 2 * b
    Out[8]: 'hellohello'

基本的な型
==========

C言語など他の言語と同じようにPythonにも変数型がある．
しかし，C言語と違ってあまり明示的に型を扱わないので，注意が必要でもある．

------
数値型
------

はじめは，整数型と浮動小数点型に注意していれば十分．

整数で数値を入力すると，整数での割り算になり，期待した答えにならない．

.. sourcecode:: ipython

    In [1]: 3 / 2
    Out[1]: 1

    In [2]: a = 3
    In [3]: b = 2
    In [4]: a / b
    Out[4]: 1

したがって，明示的に浮動小数点を使う必要がある．

.. sourcecode:: ipython

    In [5]: 3 / 2.0
    Out[5]: 1.5

    In [6]: a / float(b)
    Out[6]: 1.5

.. Note::

    気になる変数が出てきたら，type()を使って確認してみるとよい．

------
リスト
------

リストは順序つきのオブジェクトの集まり．
要素となるオブジェクトは異なる型を取ることができる．

.. sourcecode:: ipython

    In [1]: I = range(10)

    In [2]: type(I)
    Out[2]: list

    In [3]: print I
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    In [4]: I[2]
    Out[4]: 2

    In [5]: I[-1]
    Out[5]: 9

    In [6]: I[-2]
    Out[6]: 8

.. Note::

    リストのインデックスは **0** から始まり，最後の要素は **リストの長さ-1** になる．
    MATLABと違うので注意が必要．

**スライス**

スライスを使うと，リストの要素をまとめて取得できる

.. sourcecode:: ipython

    In [7]: I[1:3]
    Out[7]: [1, 2]

    In [8]: I[1:10:3]
    Out[8]: [1, 4, 7]

.. Note::

    **スライス構文** ： `l[start:stop:stride]`

**引数の省略**

.. sourcecode:: ipython

    In [9]: I[3:]
    Out[9]: [3, 4, 5, 6, 7, 8, 9]

    In [10]: I[:3]
    Out[10]: [0, 1, 2]

    In [11]: I[::2]
    Out[11]: [0, 2, 4, 6, 8]

    In [12]: I = I[:-2]
    In [12]: I
    Out[13]: [0, 1, 2, 3, 4, 5, 6, 7]

**値の変更**

.. sourcecode:: ipython

    In [14]: I[0] = 112
    In [15]: I
    Out[15]: [112, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    In [16]: I[3:5] = [99, 25]
    In [17]: I
    Out[17]: [112, 1, 2, 99, 25, 5, 6, 7, 8, 9]

.. Note::

    同じ型を持つ数値データの集まりを扱うには, :mod:`numpy` モジュールが
    提供する ``array`` 型を使う方が **より効率的** ．
    NumPy の配列は固定サイズのメモリ上のかたまり．
    Numpy の配列を使うと，要素が規則正しく並んでおり，
    Python のループではなく配列操作用の C 関数によって操作されるため，
    要素に対する演算を速く行なうことができる．

**リスト型のメソッド**

.. sourcecode:: ipython

    In [1]: I = [1, 2, 3, 4, 5]

    In [2]: I.append(6)
    In [3]: I
    Out[3]: [1, 2, 3, 4, 5, 6]

    In [4]: I.pop()
    Out[4]: 6
    In [5]: I
    Out[5]: [1, 2, 3, 4, 5]

    In [6]: I.extend([6, 7])
    In [7]: I
    Out[7]: [1, 2, 3, 4, 5, 6, 7]

.. Note::

    オブジェクトが持つメソッド一覧を知りたいときには，
    オブジェクト変数の後に '**.**' （ピリオド）を打って **tab 補完** するとよい．

**その他の操作**

.. sourcecode:: ipython

    In [8]: r = I[::-1]
    In [9]: r
    Out[9]: [5, 4, 3, 2, 1]

    In [10]: r + I
    Out[10]: [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]

    In [11]: 2*r
    Out[11]: [5, 4, 3, 2, 1, 5, 4, 3, 2, 1]

    In [12]: r.sort()
    In [13]: r
    Out[13]: [1, 2, 3, 4, 5]

------
文字列
------

文字列型は，シングル，ダブル，トリプルクオーテーションで囲んで宣言する．

.. sourcecode:: ipython

    In [1]: s = 'Hello, how are you?'
    In [2]: s
    Out[2]: 'Hello, how are you?'

    In [3]: s = "Hi, what's up"
    In [4]: s
    Out[4]: "Hi, what's up"

    In [5]: s = '''Hello,
       ...: how are you'''
    In [6]: s
    Out[6]: 'Hello,\nhow are you'

    In [7]: s = """Hi,
       ...: what's up"""
    In [8]: s
    Out[8]: "Hi,\nwhat's up"

.. Note::

    改行文字は \\n で tab 文字は \\t ．

リストと同じようにインデックスでアクセス可能．ただし，リストと違って文字の変更はできない．

.. sourcecode:: ipython

    In [1]: s = 'Hello, how are you?'

    In [2]: s[6:]
    Out[2]: ' how are you?'

    In [3]: s[::-1]
    Out[3]: '?uoy era woh ,olleH'

    In [4]: s[::2]
    Out[4]: 'Hlo o r o?'

メソッドを使って，単語に分割したりもできる．

.. sourcecode:: ipython

    In [5]: t = s.split()
    In [6]: t
    Out[6]: ['Hello,', 'how', 'are', 'you?']

----
辞書
----

辞書は キー (key) を値 (value) に対応づけする効率よいテーブルです．
リストとは異なり，順序づけられていない．

.. sourcecode:: ipython

    In [1]: tel = {'taro': 5752, 'hanako': 5578}
    In [2]: tel['ichiro'] = 5915

    In [3]: tel
    Out[3]: {'hanako': 5578, 'ichiro': 5915, 'taro': 5752}

    In [4]: tel['taro']
    Out[4]: 5752

    In [5]: tel.keys()
    Out[5]: ['hanako', 'taro', 'ichiro']

    In [6]: tel.values()
    Out[6]: [5578, 5752, 5915]

制御フロー
==========

------------
if/elif/else
------------

ソースコード：

:download:`ex_if.py <./py/01/ex_if.py>`

.. literalinclude:: py/01/ex_if.py

実行結果：

.. sourcecode:: ipython

    In [1]: run ex_if.py
    Obvious!
    A lot

---------
for/range
---------

ソースコード：

:download:`ex_for.py <./py/01/ex_for.py>`

.. literalinclude:: py/01/ex_for.py

実行結果：

.. sourcecode:: ipython

    In [2]: run ex_for.py
    0
    1
    2
    3
    Python is cool
    Python is powerful
    Python is readable

--------------------
while/break/continue
--------------------

ソースコード：

:download:`ex_while.py <./py/01/ex_while.py>`

.. literalinclude:: py/01/ex_while.py

実行結果：

.. sourcecode:: ipython

    In [3]: run ex_while.py
    The count is: 0
    The count is: 1
    The count is: 2
    The count is: 3
    The count is: 4
    The count is: 5
    I need to break now
    Good bye!
    1.0
    0.5
    0.25

.. Note::

    **改行しない print 出力** ： print した後に，改行したくないときは ',' を入れる．

------
条件式
------

**==** ：論理的に等価かどうか調べる：

.. sourcecode:: ipython

    In [1]: 1 == 1.
    Out[1]: True

**is** ：同一性を調べる：2つのオブジェクトが同じオブジェクトかどうか

.. sourcecode:: ipython

    In [2]: 1 is 1.
    Out[2]: False

    In [3]: a = 1

    In [4]: b = 1

    In [5]: a is b
    Out[5]: True

----------------------------
その他の制御ループテクニック
----------------------------

ソースコード：

:download:`ex_adv_loop.py <./py/01/ex_adv_loop.py>`

.. literalinclude:: py/01/ex_adv_loop.py

実行結果：

.. sourcecode:: ipython

    In [1]: run ex_adv_loop.py
    ['Hello', 'how', 'are', 'you?']
    Hello
    how
    are
    you?
    0 cool
    1 powerful
    2 readable
    0 cool
    1 powerful
    2 readable
    Key: a has value: 1
    Key: c has value: 1j
    Key: b has value: 1.2

------------
もっと詳しく
------------

`ココ <http://docs.python.jp/2/tutorial/datastructures.html>`_ のページを参照のこと．

関数の定義
==========

ソースコード：

:download:`ex_func.py <./py/01/ex_func.py>`

.. literalinclude:: py/01/ex_func.py

実行結果：

.. sourcecode:: ipython

    In [1]: run ex_func
    4

入出力
======



演習
====

------
ソート
------

数字のリストを引数で渡すと，昇順に並べ替えた結果を返す関数を作成せよ．
リストには，中身をソートする関数があるが，ここでは練習のため手作りしてみる．

.. image:: images/sort.jpg
    :width: 600 px
    :align: center

------------
円周率の計算
------------

モンテカルロ法を用いて円周率を計算せよ．
サンプル数を減らしたり増やしたりすると，計算結果がどのように変化するか確かめよ．

.. image:: images/calc_pi.jpg
    :width: 600 px
    :align: center

宿題
====

次回の授業までに，下記のうち，いずれか2つのプログラムを作成すること．

-------------------
組み合わせnCrの計算
-------------------

組み合わせの計算をする．

.. image:: images/ncr.jpg
    :width: 600 px
    :align: center

--------
素数判定
--------

入力された数字が素数かを判定する．

.. image:: images/prime.jpg
    :width: 600 px
    :align: center

.. Note::
    データの入力には raw_input() を用いる．
    平方根の計算には， import math をして math.sqrt() のように計算する．

--------------
正規乱数の発生
--------------

正規分布にしたがう乱数を発生する．

.. image:: images/randn.jpg
    :width: 600 px
    :align: center

