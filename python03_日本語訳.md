# Data Quest — Pythonコレクションをマスターする

> **概要:** データエンジニアとしてデジタル世界を冒険しよう！ゲームデータを構築・処理しながら、Pythonの強力なデータ構造をマスターします。
>
> **バージョン:** 3.0

---

## 目次

- [第I章 まえがき](#第i章-まえがき)
- [第II章 AI利用に関する指示](#第ii章-ai利用に関する指示)
- [第III章 はじめに](#第iii章-はじめに)
- [第IV章 共通ルール](#第iv章-共通ルール)
- [第V章 演習0: Command Quest](#第v章-演習0-command-quest)
- [第VI章 演習1: Score Cruncher](#第vi章-演習1-score-cruncher)
- [第VII章 演習2: Position Tracker](#第vii章-演習2-position-tracker)
- [第VIII章 演習3: Achievement Hunter](#第viii章-演習3-achievement-hunter)
- [第IX章 演習4: Inventory Master](#第ix章-演習4-inventory-master)
- [第X章 演習5: Stream Wizard](#第x章-演習5-stream-wizard)
- [第XI章 演習6: Data Alchemist](#第xi章-演習6-data-alchemist)
- [第XII章 提出方法](#第xii章-提出方法)

---

## 第I章 まえがき

Twitterの初期の成長期において、スケーリングとは単にサーバーを増やすことではありませんでした。それは、巨大なスケールにおいて突然重要になる小さな設計判断を修正することでした。何度も現れたパターンの一つは、シンプルで扱いやすく、小規模なトラフィックでは全く問題のない「逐次的なデータ構造（リストや配列など）」を使っていたことです。その後、ユーザー数が爆発的に増加しました。

「これはすでに存在するか？」といった、かつてはマイクロ秒で済んでいた操作が、毎秒何百万回も実行されるようになり、静かにパフォーマンスのボトルネックへと変わっていきました。論理的には何も間違っていません。コードはきれいで正しかったのです。しかし、間違ったコンテナを選んだことで、線形時間の処理が本番環境での頭痛の種になってしまいました。ハッシュベースの構造に差し替えると、この問題は魔法のように解決することがよくありました。

これは、**大規模な環境では、あなたのデータ構造こそがアルゴリズムである**ということを思い出させてくれる良い教訓です。

---

## 第II章 AI利用に関する指示

### ● 背景

学習の過程で、AIはさまざまなタスクを手助けしてくれます。AIツールのさまざまな能力と、それらがどのようにあなたの作業を支援できるかを探求する時間を取りましょう。ただし、常に慎重に向き合い、結果を批判的に評価してください。コード、ドキュメント、アイデア、技術的な説明のいずれであっても、自分の質問が適切だったか、生成された内容が正確かどうかを完全に確信することはできません。仲間（peers）は、ミスや盲点を避けるための貴重なリソースです。

### ● 主なメッセージ

- 繰り返しの多い、退屈なタスクを減らすためにAIを使う。
- 将来のキャリアに役立つプロンプト作成スキル（コーディング・非コーディングの両方）を磨く。
- AIシステムの仕組みを学び、よくあるリスク・バイアス・倫理的問題を予測し回避できるようにする。
- 仲間と協力しながら、技術スキルとパワースキル（対人スキル）の両方を伸ばし続ける。
- 自分が完全に理解し、責任を持てるAI生成コンテンツだけを使う。

### ● 学習者のルール

- AIツールを探求し、その仕組みを理解する時間を取るべきです。そうすることで倫理的に使い、潜在的なバイアスを減らせます。
- プロンプトを書く前に自分の問題についてよく考えるべきです。これにより、正確な語彙を使って、より明確で詳細で的確なプロンプトを書けるようになります。
- AIが生成したものは、体系的にチェック・レビュー・疑問視・テストする習慣を身につけるべきです。
- 常に仲間のレビューを求めるべきです。自分だけの検証に頼らないこと。

### ● このフェーズで得られる成果

- 汎用的なプロンプト作成スキルと、特定分野向けのプロンプト作成スキルの両方を身につける。
- AIツールを効果的に使い、生産性を向上させる。
- 計算論的思考、問題解決能力、適応力、協働力をさらに強化する。

### ● コメントと例

- 試験や評価など、本当の理解を示さなければならない場面に定期的に遭遇します。準備を怠らず、技術スキルと対人スキルの両方を磨き続けましょう。
- 自分の推論を説明したり仲間と議論したりすると、理解の抜け漏れが見えてくることがよくあります。仲間との学び合いを優先しましょう。
- AIツールはあなた固有の文脈を欠いていることが多く、一般的な回答になりがちです。同じ環境を共有する仲間は、より的確で正確な洞察を与えてくれます。
- AIが「最も可能性の高い答え」を生成しがちなのに対し、仲間は別の視点や価値あるニュアンスを提供してくれます。品質のチェックポイントとして彼らを頼りましょう。

> **✓ 良い実践例:**
> AIに「ソート関数をどうテストすればいい？」と尋ねる。いくつかアイデアをもらう。それを試し、結果を仲間とレビューする。一緒にアプローチを洗練させる。

> **✗ 悪い実践例:**
> AIに関数全体を書かせ、プロジェクトにコピペする。ピア評価のとき、それが何をするのか・なぜそうなのかを説明できない。信頼を失い、プロジェクトに不合格になる。

> **✓ 良い実践例:**
> パーサーの設計をAIに手伝ってもらう。その後、ロジックを仲間と一緒に追っていく。2つのバグを見つけ、一緒に書き直す。より良く、よりきれいで、完全に理解できたものになる。

> **✗ 悪い実践例:**
> プロジェクトの重要な部分のコードをCopilotに生成させる。コンパイルは通るが、パイプをどう処理しているか説明できない。評価のとき、根拠を示せず、プロジェクトに不合格になる。

---

## 第III章 はじめに

おかえりなさい、デジタル世界へ。データエンジニアよ！

Pythonの基礎をたどる旅は、あなたを十分に鍛え上げました。デジタルな庭を動かす基本的な構文をマスターし、現実のシステムをモデル化する堅牢なクラス階層を構築し、優雅な例外処理で予期せぬ事態に対処する方法を学びました。さあ、データエンジニアリングの核心に挑む準備ができました。すなわち、**コレクションとデータ構造**です。これらをゲーム環境の中で探求していきます。

想像してみてください。1980年、パックマンのゲーム状態全体（すべてのドット、ゴーストの位置、スコア）は、わずか16KBのRAMに収まっていました。プログラマーたちは効率の魔術師でなければならなかったのです！彼らは、データを整理することが単にメモリを節約するだけでなく、ゲームの魔法を解き放つことであると発見しました。現代に早送りすると、Fortniteは1,000万人以上の同時接続プレイヤーを処理し、各プレイヤーが毎秒何千ものデータポイントを生成しています。原理は同じ、遊び場がより大きくなっただけです！

Pythonのコレクション型は、さまざまなユースケース向けに設計されており、それぞれに固有の特徴があります。

- **リスト (lists)**: 順序付き、インデックス付き、拡張可能
- **タプル (tuples)**: 順序付き、変更不可（イミュータブル）、ハッシュ可能
- **集合 (sets)**: ユニークな要素の順序なしコレクション
- **辞書 (dictionaries)**: キーと値のペア

これらに加えて、**ジェネレータ (generators)** と **内包表記 (comprehensions)** があり、強力な構文と振る舞いをもたらします。

このクエストでは、ゲーム分析プラットフォームを支えるコンポーネントを構築します。各演習で新しいデータ型が解放され、最後にはデータエンジニアのようにPythonのコレクションを自在に操れるようになります！

> ℹ️ **このプロジェクト以降、演習で適切に紹介された時点で、新しいPythonのデータ構造とそれに関連するすべてのクラスメソッドを使えるようになります。**

---

## 第IV章 共通ルール

### IV.1 一般ルール

- プロジェクトは **Python 3.10 以降** で書くこと。
- プロジェクトは **flake8** のコーディング規約に準拠すること。
- すべての関数・メソッドに型ヒント（type hints）を付けること。`mypy` で確認すること。
- 関数はクラッシュを避けるため、例外を優雅に処理すること。
- このプロジェクトではコマンドライン引数へのアクセスが必要です。`import` の仕組みを通じて `sys` モジュールを使います。importについては将来のプロジェクトで詳しく扱います。
- **ファイルI/O操作は一切許可されません。** すべてのデータはメモリ上、またはコマンドライン引数を通じて処理すること。
- コレクションの利用パターンを明確に示すことに集中すること。
- 各データ構造について、基本的な操作と応用的なテクニックの両方を示すこと。

> ℹ️ **以下の標準型は、関連するすべてのメソッドおよびコンストラクタとともに使用が許可されます: `str`, `int`, `float`。**

### IV.2 追加のガイドライン

- 作業は指定されたGitリポジトリに提出すること。
- このリポジトリ内のコンテンツのみが評価対象となります。

---

## 第V章 演習0: Command Quest

| 項目 | 内容 |
|------|------|
| 演習 | Exercise 0 |
| 名称 | ft_command_quest |
| ディレクトリ | `ex0/` |
| 提出ファイル | `ft_command_quest.py` |
| 許可されるもの | `import sys`, `sys.argv`, `len()`, `print()` |

**ようこそ、データ冒険者よ！** すべての壮大なクエストは、自分の道具を理解することから始まります。デジタル世界では、プログラムは外の世界から指示を受け取る必要があります。あなたの最初のミッションは、プログラムがユーザーからメッセージを受け取る方法を発見することです！

さあ、**リスト**を導入する時が来ました。自分でリストを作る前に、すでに存在するリストを操作してみましょう。すなわち、`sys` モジュールを通じて利用できるコマンドライン引数です。その構造はC言語のものと似ています。文字列の配列です。リストの要素にアクセスし、操作する方法を探求しましょう。

受け取ったコマンドライン引数のデータを表示するシンプルなスクリプトを作成してください。以下の例を模倣しましょう。

```
$> python3 ft_command_quest.py
=== Command Quest ===
Program name: ft_command_quest.py
No arguments provided!
Total arguments: 1

$> python3 ft_command_quest.py hello world 42
=== Command Quest ===
Program name: ft_command_quest.py
Arguments received: 3
Argument 1: hello
Argument 2: world
Argument 3: 42
Total arguments: 4

$> python3 ft_command_quest.py "Data Quest"
=== Command Quest ===
Program name: ft_command_quest.py
Arguments received: 1
Argument 1: Data Quest
Total arguments: 2
```

> 💡 スクリプトの先頭で `import sys` を使うだけで `sys.argv` リストにアクセスできます。

> ℹ️ プログラム名を引数と一緒に再表示しないようにする方法は複数あります。評価の際に代替案を議論できるよう準備しておきましょう。

---

## 第VI章 演習1: Score Cruncher

| 項目 | 内容 |
|------|------|
| 演習 | Exercise 1 |
| 名称 | ft_score_analytics |
| ディレクトリ | `ex1/` |
| 提出ファイル | `ft_score_analytics.py` |
| 許可されるもの | `import sys`, `sys.argv`, `len()`, `sum()`, `max()`, `min()`, `print()` |

**ミッション説明:** コマンドでのやり取りをマスターしたので、次はデータのクリーンアップの時間です！コマンドを送ってくるユーザーは人間であり、ミスをすることがあります。

この演習では、スコアを格納するために**リスト**を使い、不正な入力（例: 数値でない値をユーザーが与えた場合）を優雅に処理するために **try/except ブロック** を使う必要があります。

ゲームのスコアをコマンドライン引数として受け取ります。やるべきことは以下の通りです。

- コマンドライン引数を処理する
- さまざまなエラーケース（引数なし、数値でない値）を適切なメッセージで処理する
- スコアを格納・整理するための新しい**リスト**を作成する
- ゲームプレイヤーが喜ぶような基本統計を計算する（個数、合計、平均、最大、最小、範囲）
- ゲーム仲間に自慢できるくらいカッコいい出力にする（再び例を模倣してよい）
- 有効な入力と無効な入力の両方がコマンドラインで与えられた場合、無効なものは破棄し、残った有効な入力で処理を進める（有効なものが残らない場合を除く）

```
$> python3 ft_score_analytics.py 1500 2300 1800 2100 1950
=== Player Score Analytics ===
Scores processed: [1500, 2300, 1800, 2100, 1950]
Total players: 5
Total score: 9650
Average score: 1930.0
High score: 2300
Low score: 1500
Score range: 800

$> python3 ft_score_analytics.py
=== Player Score Analytics ===
No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...

$> python3 ft_score_analytics.py ab ac
=== Player Score Analytics ===
Invalid parameter: 'ab'
Invalid parameter: 'ac'
No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...
```

---

## 第VII章 演習2: Position Tracker

| 項目 | 内容 |
|------|------|
| 演習 | Exercise 2 |
| 名称 | ft_coordinate_system |
| ディレクトリ | `ex2/` |
| 提出ファイル | `ft_coordinate_system.py` |
| 許可されるもの | `import math`, `math.sqrt()`, `input()`, `round()`, `print()` |

**レベルアップ！** 3D座標をマスターする時間です！ゲームで特定の場所にテレポートしたことを覚えていますか？あるいは3D空間内の2点間の距離を求める必要があったことは？まさにそれを作ります！

この演習では、3D座標 (x, y, z) を格納するために**タプル**を使う必要があります。

まず、`get_player_pos()` という関数を書きます。この関数は:

- `x,y,z` という形式で新しいプレイヤーの座標をユーザーに尋ねる
- 不正な入力を処理する
- 有効な座標が与えられるまで再試行する
- プレイヤーの現在の3D座標を含むタプルを返す

次に、あなたのコードは以下を行います。

- 1つ目の座標セットを取得する
- タプルを表示し、続いて各座標を個別に表示する
- 3Dの中心 (0, 0, 0) までの距離を計算する（下記参照）
- 2つ目の座標セットを取得する
- 2つ目と1つ目の座標セット間の距離を計算する

**距離の公式:** 2つの3D点間の距離を計算するには、ユークリッド距離の公式を使います。

$$\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}$$

点 (x1, y1, z1) と (x2, y2, z2) について、距離は `math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)` です。これはピタゴラスの定理を3Dに拡張したものにすぎません！

```
$> python3 ft_coordinate_system.py
=== Game Coordinate System ===
Get a first set of coordinates
Enter new coordinates as floats in format 'x,y,z': hello world
Invalid syntax
Enter new coordinates as floats in format 'x,y,z': 1.0 , 2.5, 3.0
Got a first tuple: (1.0, 2.5, 3.0)
It includes: X=1.0, Y=2.5, Z=3.0
Distance to center: 4.0311

Get a second set of coordinates
Enter new coordinates as floats in format 'x,y,z': 4,abc,5
Error on parameter 'abc': could not convert string to float: 'abc'
Enter new coordinates as floats in format 'x,y,z': 4,5,6
Distance between the 2 sets of coordinates: 4.9244
```

> 💡 `math.sqrt()` を使うには、スクリプトの先頭で `import math` を使うだけです。

> ℹ️ タプルは石に刻まれたデータのようなものです。一度作成されると、変更されません。

---

## 第VIII章 演習3: Achievement Hunter

| 項目 | 内容 |
|------|------|
| 演習 | Exercise 3 |
| 名称 | ft_achievement_tracker |
| ディレクトリ | `ex3/` |
| 提出ファイル | `ft_achievement_tracker.py` |
| 許可されるもの | `len()`, `print()`, `import random`, `random.*`, `set()`, `set.union()`, `set.intersection()`, `set.difference()` |

**実績解除！** 史上最高に格好いい実績システムを作る時間です！レアな実績を解除したときの満足感、知っていますよね？今度はそれらすべてを追跡するシステムを作るのです！

この演習では、ユニークな実績を格納するために**集合（set）**を使い、プレイヤー間の実績コレクションを分析するために集合演算（和集合、積集合、差集合）を行う必要があります。

`gen_player_achievements()` という関数を作成します。この関数は、実績の大きな固定リストを使い、プレイヤーにランダムに集合を割り当てます。ランダムな個数の実績を選び、その個数分の実績をリストから選んで集合を構築し、返します。

次に、あなたのコードは以下を行います。

- 最低4人の異なるプレイヤーの実績集合を生成する
- 全プレイヤー間のユニークな実績をすべて把握する
- 全プレイヤーが共有している実績を見つける
- 各プレイヤーについて、他の誰も持っていない実績を特定する
- 各プレイヤーについて、全実績を揃えるために不足している実績を列挙する

```
$> python3 ft_achievement_tracker.py
=== Achievement Tracker System ===
Player Alice: {'Crafting Genius', 'World Savior', 'Master Explorer', 'Collector Supreme', 'Untouchable', 'Boss Slayer'}
Player Bob: {'Crafting Genius', 'Strategist', 'World Savior', 'Master Explorer', 'Unstoppable', 'Collector Supreme', 'Untouchable'}
Player Charlie: {'Strategist', 'Speed Runner', 'Survivor', 'Master Explorer', 'Treasure Hunter', 'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind'}
Player Dylan: {'Strategist', 'Speed Runner', 'Unstoppable', 'Untouchable', 'Boss Slayer'}

All distinct achievements: {'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner', 'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable', 'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind', 'Boss Slayer'}

Common achievements: {'Untouchable'}

Only Alice has: set()
Only Bob has: set()
Only Charlie has: {'Survivor', 'Treasure Hunter', 'First Steps', 'Sharp Mind'}
Only Dylan has: set()

Alice is missing: {'Strategist', 'Speed Runner', 'Survivor', 'Treasure Hunter', 'Unstoppable', 'Hidden Path Finder', 'First Steps', 'Sharp Mind'}
Bob is missing: {'Speed Runner', 'Survivor', 'Treasure Hunter', 'Hidden Path Finder', 'First Steps', 'Sharp Mind', 'Boss Slayer'}
Charlie is missing: {'Crafting Genius', 'World Savior', 'Hidden Path Finder', 'Unstoppable', 'Boss Slayer'}
Dylan is missing: {'Crafting Genius', 'World Savior', 'Survivor', 'Master Explorer', 'Treasure Hunter', 'Hidden Path Finder', 'First Steps', 'Collector Supreme', 'Sharp Mind'}
```

> 💡 実績の総数と、各プレイヤーが取得する個数を調整して、要求されるすべての集合が空にならない可能性が高くなるようにしましょう。ところで、Pythonは空集合をどのように表示するでしょうか？そしてそれはなぜでしょうか？

---

## 第IX章 演習4: Inventory Master

| 項目 | 内容 |
|------|------|
| 演習 | Exercise 4 |
| 名称 | ft_inventory_system |
| ディレクトリ | `ex4/` |
| 提出ファイル | `ft_inventory_system.py` |
| 許可されるもの | `import sys`, `sys.argv`, `len()`, `print()`, `sum()`, `list()`, `round()`, `dict.keys()`, `dict.values()`, `dict.update()` |

**戦利品の時間だ！** RPGでインベントリを整理したことを覚えていますか？あの伝説の剣を持っているか確認したことは？究極のインベントリシステムを作る時間です！

この演習では、インベントリのデータを格納するために**辞書（dictionary）**を使う必要があります。

あなたのコードはまず、コマンドライン引数を解析してインベントリシステムを埋めます。各引数は `<item_name>:<quantity>` という形式に従う必要があります。無効な引数（構文が不正、重複した引数）はエラーメッセージとともに破棄し、有効なものを辞書に入れます。辞書内の `<quantity>` の値は、後で計算を行えるように `int` として格納します。

インベントリに対して操作を行いましょう。

- インベントリを表示する
- インベントリに含まれる全アイテムのリストを作成して表示する
- インベントリ内の全アイテムの合計数量を計算して出力する
- 各アイテムがインベントリ内で占める数量の割合（パーセント）を表示する
- 最も多いアイテムと最も少ないアイテムを報告する（同数の場合はコマンドラインで先に来たものを選ぶ）
- 最後に、新しいアイテムをインベントリに追加して、再度表示する

```
$> python3 ft_inventory_system.py sword:1 potion:5 shield:2 armor:3 helmet:1 sword:2 hello key:value
=== Inventory System Analysis ===
Redundant item 'sword' - discarding
Error - invalid parameter 'hello'
Quantity error for 'key': invalid literal for int() with base 10: 'value'
Got inventory: {'sword': 1, 'potion': 5, 'shield': 2, 'armor': 3, 'helmet': 1}
Item list: ['sword', 'potion', 'shield', 'armor', 'helmet']
Total quantity of the 5 items: 12
Item sword represents 8.3%
Item potion represents 41.7%
Item shield represents 16.7%
Item armor represents 25.0%
Item helmet represents 8.3%
Item most abundant: potion with quantity 5
Item least abundant: sword with quantity 1
Updated inventory: {'sword': 1, 'potion': 5, 'shield': 2, 'armor': 3, 'helmet': 1, 'magic_item': 1}
```

> 💡 ゲームの始まりでは、インベントリはたいてい空っぽですよね ;)

---

## 第X章 演習5: Stream Wizard

| 項目 | 内容 |
|------|------|
| 演習 | Exercise 5 |
| 名称 | ft_data_stream |
| ディレクトリ | `ex5/` |
| 提出ファイル | `ft_data_stream.py` |
| 許可されるもの | `next()`, `range()`, `len()`, `print()`, `import typing`, `typing.Generator`, `import random`, `random.*` |

**魔法の時間だ！** ゲームがクラッシュせずに何百万ものイベントを処理する仕組みを不思議に思ったことはありませんか？Pythonのメモリ節約の超能力、**ジェネレータ**の世界へようこそ！

この演習では、データストリームをその場で生成するために、`yield` キーワードを使った**ジェネレータ**を使う必要があります。すべてをメモリに格納するのではなく、必要に応じて値を生成するジェネレータ関数を実装しなければなりません。

`gen_event()` という無限ジェネレータ関数を作成します。これはプレイヤーのリストからランダムに名前を選び、アクションのリストからランダムにアクションを選びます。このジェネレータに対して `next()` が呼ばれるたびに、新しいイベントをタプル `(name, action)` として返します。

スクリプトのメイン部分で、1000回ループし、`gen_event()` から得た1000件のイベントをすべて表示します。

次に、再び `gen_event()` で生成した10個のタプルのリストを作成します。

最後に、`consume_event` という新しいジェネレータ関数を作成します。これは先ほど作成したリストを受け取り、その要素の1つをランダムに選び、リストから削除し、それをyieldします。これをリストが空になるまで繰り返します。このジェネレータは `for .. in ..` 構文の中で直接使われなければなりません。

```
$> python3 ft_data_stream.py
=== Game Data Stream Processor ===
Event 0: Player bob did action run
Event 1: Player alice did action eat
Event 2: Player bob did action sleep
Event 3: Player bob did action grab
Event 4: Player dylan did action run
Event 5: Player bob did action move
Event 6: Player alice did action move
Event 7: Player dylan did action move
Event 8: Player alice did action climb
Event 9: Player bob did action sleep
Event 10: Player bob did action run
Event 11: Player bob did action swim
Event 12: Player dylan did action swim
Event 13: Player charlie did action sleep
Event 14: Player charlie did action sleep
[...]
Event 992: Player dylan did action eat
Event 993: Player alice did action sleep
Event 994: Player charlie did action move
Event 995: Player charlie did action climb
Event 996: Player bob did action release
Event 997: Player bob did action grab
Event 998: Player bob did action move
Event 999: Player alice did action move

Built list of 10 events: [('charlie', 'move'), ('dylan', 'grab'), ('alice', 'use'), ('alice', 'use'), ('charlie', 'swim'), ('bob', 'run'), ('charlie', 'move'), ('dylan', 'climb'), ('alice', 'use'), ('bob', 'release')]

Got event from list: ('charlie', 'swim')
Remains in list: [('charlie', 'move'), ('dylan', 'grab'), ('alice', 'use'), ('alice', 'use'), ('bob', 'run'), ('charlie', 'move'), ('dylan', 'climb'), ('alice', 'use'), ('bob', 'release')]
（以下、リストが空になるまで「ランダムに1件取り出し → 残りを表示」が繰り返される）
...
Got event from list: ('dylan', 'grab')
Remains in list: []
```

---

## 第XI章 演習6: Data Alchemist

| 項目 | 内容 |
|------|------|
| 演習 | Exercise 6 |
| 名称 | ft_data_alchemist |
| ディレクトリ | `ex6/` |
| 提出ファイル | `ft_data_alchemist.py` |
| 許可されるもの | `import random`, `random.*`, `print()`, `len()`, `sum()`, `round()` |

**ラスボスの時間だ！** あなたはすべてのデータ構造をマスターしました。今こそ、それらをエレガントな凝縮された形で発見する時です！ここであなたは真のデータ錬金術師（Data Alchemist）になります！

この演習では、データを効率的に変換・フィルタリングするために、**リスト内包表記**と**辞書内包表記**を使う必要があります。これらはデータ処理のためのPythonの基本機能です。

プレイヤー名のリストを作成します。一部は先頭が大文字、一部はそうでないものにします。2つのリスト内包表記を作ります。1つ目はすべての名前を先頭大文字（capitalize）にした新しいリストを作り、2つ目は元のリストから先頭が大文字の名前だけを集めた新しいリストを作ります。

次に、この「すべて先頭大文字にしたプレイヤー名のリスト」から辞書を作成します。名前がキーになり、値は定められた範囲でランダムに生成されたスコアになります。もちろん、内包表記でこの辞書を構築します。続いて、平均より高いスコアだけを集めた2つ目の辞書を、同じく内包表記で作成します。

```
$> python3 ft_data_alchemist.py
=== Game Data Alchemist ===
Initial list of players: ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']
New list with all names capitalized: ['Alice', 'Bob', 'Charlie', 'Dylan', 'Emma', 'Gregory', 'John', 'Kevin', 'Liam']
New list of capitalized names only: ['Alice', 'Charlie', 'Emma', 'Gregory', 'Liam']
Score dict: {'Alice': 263, 'Bob': 666, 'Charlie': 907, 'Dylan': 170, 'Emma': 568, 'Gregory': 446, 'John': 90, 'Kevin': 527, 'Liam': 54}
Score average is 410.11
High scores: {'Bob': 666, 'Charlie': 907, 'Emma': 568, 'Gregory': 446, 'Kevin': 527}
```

> ℹ️ 集合（set）に対しても内包表記を使うことができます。

> ⚠️ 各内包表記は1行で書くべきです（行の長さ制限を超える場合を除く）。

---

## 第XII章 提出方法

いつものように、課題をGitリポジトリに提出してください。評価（defense）の際には、リポジトリ内の作業のみが評価対象となります。ファイル名が正しいかどうか、念のため二重に確認しておきましょう。

> ℹ️ 評価の際には、データ構造の選択理由を説明したり、コレクション操作を実演したり、分析システムに新しい機能を追加するよう求められることがあります。各データ構造の背後にある原理を確実に理解しておきましょう。

> ⚠️ このプロジェクトの課題で要求されたファイルのみを提出してください。Pythonのコレクション型とデータ処理技法の習熟を明確に示す、クリーンでよくドキュメント化されたコードを書くことに集中しましょう。
