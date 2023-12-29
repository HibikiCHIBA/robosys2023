# Robosys2023
![test](https://github.com/HibikiCHIBA/robosys2023/actions/workflows/test.yml/badge.svg)

千葉工業大学 上田隆一先生の講義 ロボットシステム学 2023年度版の内容に沿って作成した課題の提出用リポジトリ

# Install
インストールは, 下記コマンドのようにインストールしたいGithubページのURLを挿入することで開始される. インストールが終了したら, robosys2023ディレクトリへ移動し, 内部ファイルが正しくインストールされているかを確認すること. 
```
$ git clone https://github.com/HibikiCHIBA/robosys2023.git
$ cd robosys2023
$ ls
LICENSE  README.md  plus  test.bash
```

# Plus
1, -2, 3, -4, …, といった数列から標準入力値(自然数)で指定した数列の整数までの総和を計算する. 例えば標準入力値が, 1, 2, 3, 4, …, であった場合, 出力は, 1, -1, 2, -2, …, となる. 

# Environment
* Ubuntu 20.04.4 LTS
* python 3.8.10

(上記環境にてテスト済み)


# Demo
実行例を示す. 例として標準入力が5と6の場合の実行コマンドが下記の通りである. 
```
$ seq 5 | ./plus  
3
$ seq 6 | ./plus  
-3
```

# License
* このソフトウェアパッケージは, [3条項BSDライセンス](https://opensource.org/license/bsd-3-clause/)の下, 再配布および使用が許可されています. 
* このパッケージのコードは，上田隆一先生の[スライド](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
* © 2023 Hibiki Chiba
