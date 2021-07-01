---
marp: true
theme: osc21do
paginate: true
---

<!-- _class: title-->
<!-- _paginate: false -->

# Pythonではじめる今風な型プログラミング

## 6/25(Sat), OSC2021 Online/Hokkaido

---

<!-- _class: agenda -->

# 今日話すこと

1. そもそも: 型ヒントとは
2. 型ヒント入門編: 小さく始める
    1. 関数の戻り値・引数
    2. 標準で使える組み込み型
3. 少し発展編: typingモジュール
    1. Genarator, Callable, TypeVar, Genarics, etc...
4. 最近のアップデート・新機能を以前のバージョンでも使うには

---

<!-- class: content -->

# 自己紹介

- 名前: Peacock / 高井 陽一
    - [Twitter](https://twitter.com/peacock0803sz/) / [GitHub](https://github.com/peacock0803sz/) / [Facebook](https://www.facebook.com/peacock0803sz): `peacock0803sz`
- [CMSコミュニケーションズ](https://cmscom.jp)でWebなPythonを書いている
- [PyCon JP Association](https://www.pycon.jp)関係の活動
    - PyCon JP [2020](https://pycon.jp/2020), [2021](https://2021.pycon.jp)スタッフ
    - [PyCon JP TV](https://tv.pycon.jp)ディレクター

---

# 自己紹介（続き）

- OSCは2019 Tokyo/Fallから
- 2020はちょこちょこスタッフやってたりしてました
- パブリックな場所で話すのが初めてなのでどうかお手柔らかに:pray:
    - Zoom発表さみしいのでリアクションたくさんもらえると嬉しいです
    - Twitter実況も歓迎(あとで見に行きます
- 資料はSpeakerDeckにアップロード済みです

---

# Motivationとこの発表のゴール

---

<!-- _class: subtitle -->
<!-- _paginate: false -->

# Let's begin!

---

# そもそも: 型ヒントとは

- 3.5まで完全な動的型付け言語だったPythonに、型を導入しようという話
- あくまで「ヒント」でありコメント
    - 実行時に評価はされず、TypeSciptのようにコンパイルエラーも出ない

```py
def greet(name: str) -> str:
    return "Hello, " + name
```

![w:960px](images/CleanShot%202021-06-12%20at%2014.37.59.png)

---

<!-- _class: subtitle -->
<!-- _paginate: false -->


# 型ヒント入門編: 小さく始める

## 最初から頑張って書くのはつらいので小さく始める

---

# まずは関数の引数・戻り値から

- 全部に書こうとしなくていい
    - JavaやCみたいに全部書く必要はない
- 基本的に型をつけるときは名前の後ろに`:`を書いて型
- 関数の戻り値は`->`を使う

```py
def greet(name: str) -> str:
    return "Hello, " + name
```

---

# 何が嬉しいのか?

- エディタで参照したときに型がわかる
- 間違ったものを渡そうとしたときに怒ってくれる

![h:250px](images/CleanShot%202021-06-12%20at%2014.37.59.png)
![h:200px](images/CleanShot%202021-06-12%20at%2015.41.54.png)

---

# 何もimportしなくていい組み込み型

- `bool`, `bytes`, `float`, `int`, `str`: 何もしなくても使える
- `None`: 何も返さない関数に使う
- `dict`, `frozenset`, `list`, `set`, `tuple`
    - Collectionsは中の型を`[]`で書ける
        - 3.9以降のみ
        - 3.7, 3.8は`from __future__ import annotaions`(後述)を書く
        - 3.6は`typing`(次項)から大文字始まりのものをimportする
    - ex: `list[str]`, `dict[str, int]`
    - refs: [python.jpでの紹介記事](https://www.python.jp/pages/python3.9.html#%E7%B5%84%E3%81%BF%E8%BE%BC%E3%81%BFGeneric%E5%9E%8B)、[公式ドキュメント(英語)](https://docs.python.org/ja/3.9/whatsnew/3.9.html#type-hinting-generics-in-standard-collections)

---

# (3.9から非推奨) typingモジュールからimportする

- Generics系は3.9までは`from typing import ...`を書いていた
    - コレクション、プロトコル関係など
- 3.9からは後述する書き方になって、非推奨に

---

# Any

- あらゆる型のインスタンスを保持できる
- 使わないに越したことはない
    - 必要なときには`typing`からimportして使う

```py
from typing import Any

unknown_variable: Any
```

---

<!-- _class: subtitle -->
<!-- _paginate: false -->

# 少し発展編: Generics型

---

# 合併型(Union)

`Union`: 合併型。3.10以降は`|`で表せる
例:文字列と整数をどっちも受け入れる関数
```py
from __future__ import annoations  # 3.7 - 3.9は必要
def normalize_year(year: int | str) -> int:
    if isinstance(year, int): return year  # ここではyearは数値
    # これ以降ではyearは文字列
    if year.startswith("昭和"): return int(year[2:]) + 1925
    elif year.startswith("平成"): return int(year[2:]) + 1988
    elif year.startswith("令和"): return int(year[2:]) + 2018
    else: raise ValueError('unsupported style')
```
```py
from typing import Union  # for 3.6
def normalize_year(year: Union[int, str]) -> int: pass
```

---

# Optional型

- nullable, NoneとのUnionと等価
    - Unionと同じように振る舞ってくれる
- 関数の戻り値とかに使うと伝播してしまうので、使い方は**要注意**

```py
from typing import Optional
age: Optional[int]
age = 17
age = None  # これも有効
age: int | None  # 3.9以降ならこれでもいい
```

---

# Callable(呼び出し可能オブジェクト)

デコレーター関数など、関数を引数に取る関数を書くときに使える
```py
from collections.abc import Callable  # 3.9以降
from fuctools import wraps
from typing import Callable  # 3.8以前
def validate(func: Callable) -> Callable[..., Callable | tuple[Response, Literal[400]]]:
    @wraps(func)
    def wrapper(*args, **kw) -> Callable | tuple[Response, Literal[400]]:
        try:
            j = request.json
            if j is None: raise BadRequest
        except BadRequest:
            return jsonify({"data": [], "errors": {"message": ERROR_MESSAGE, "code": 400}}), 400
        return func(*args, **kw)
    return wrapper
```

---

<!-- _class: subtitle -->
<!-- _paginate: false -->

# 最近のアップデート・新機能を以前のバージョンでも使うには

---

# 最近のアップデート事情

https://www.python.org/downloads/

| バージョン | ステータス   | 初回リリース| EOS        | PEP |
| ---------- | ------------ | ----------- | ---------- | --- |
|        3.9 | バグ修正     | 2020-10-05  | 2025-10    | 596 |
|        3.8 | バグ修正     | 2019-10-14  | 2024-10    | 569 |
|        3.7 | セキュリティ | 2018-06-27  | 2023-06-27 | 537 |
|        3.6 | セキュリティ | 2016-12-23  | 2021-12-23 | 494 |

---

# `__future__` モジュール: (dunder future) とは

- 後方互換性のために存在している
- 破壊的変更がいつ導入されて、必須になったかが書かれている
- typingの他にも3.xの機能を2.xでも呼び出すときなどに使っていた
    - ex) `print_func`, `unicode_literals` etc ...
- refs: 公式ドキュメント[\_\_future\_\_](https://docs.python.org/ja/3/library/__future__.html), [future statement](https://docs.python.org/ja/3/reference/simple_stmts.html#future)

---

<!-- _class: subtitle -->
<!-- _paginate: false -->

# 3.9, 3.10で使えるようになった(る)typing関連の新機能たち

---

# 3.9から: 標準Collections型のGenerics

- Generics型定義(`[]`を使って中の型を書ける)のimport元が変わった
- 3.8までは`typing`からだったけど、分散した
- `list`, `tuple`, `dict`などの`__builtins__`なら何もせずに小文字始まりにする
- `collections`系(deque, defaultdict)などは`collections`から
- iterable, callableなどプロトコル関係は`collections.abc`から
- 正規表現は`re` 
- コンテキスト関連は`contextlib`

---

# 3.10から: Union型演算子

- 前述した合併型(Union)が演算子として使える
- `isinstance()`で聞くときにも使える
- TypeSciptなどがこの記法なのでより直感的
- 3.10の他のtyping関連の新機能は複雑なのでは紹介しない
    - 引数仕様変数、明示的型エイリアス、ユーザー定義型ガード
    - See also: [What's New In Python 3.10](https://docs.python.org/ja/3.10/whatsnew/3.10.html#new-features-related-to-type-hints)

---

# まとめ

- 小さいところから、こつこつと
    - 関数の返値、戻り値からやるのがおすすめ
- ここ1,2年で注目が高まってきて、アップデートも速い分野
- 書いていて気持ちいい、素敵なPythonライフ?を!
