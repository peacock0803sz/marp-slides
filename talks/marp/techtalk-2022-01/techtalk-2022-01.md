---
marp: true
theme: simple
paginate: true
---

<!-- _class: title -->
<!-- _paginate: false -->

# Gitの運用について

## CMScom Techtalk 2022-01, Yoichi TAKAI

---

# この発表の動機・モチベーション

GitのBranch運用やCommit粒度などについてOSSやコミュニティで色んな意見を見聞きすることがあったので、社内全体でも考えたいと考えた

## 前提

- Gitを使った一通りの開発・運用ができる

---

# 今日話すこと(Gitについて)

- Branch model
- Commitの粒度
- PRのmerge method

---

# GitのBranch modelとは

- Branchを複数運用して開発していると、最新の開発用Branchと運用しているBranchがわからなくなる
- master(main), develop, feature/xxx, bugfix/yyyなどとルールを決めておく
    - 開発用Branchがいくつも並行して動いていても運用しているBranchを見失いにくい

---

# GitのBranch model(flow)にはいくつか種類がある

今回はGit flow, GitHub flowの2種類を紹介する

## 共通していること

意味単位の区切りに`/`を使用する

---

# Git flow

![w:1080px](https://image.itmedia.co.jp/ait/articles/1708/01/at-it-git-15-001.jpg)

---

# GitHub flow

![w:1440px](https://image.itmedia.co.jp/ait/articles/1708/01/l_at-it-git-15-009.jpg)

---

# Commitの粒度について

- いきなり巨大なCommitを入れると後から分割したくなった時に大変
- 小さなCommitをいくつも並べて後から結合(merge)や並び換え(rebase/revert)をする方が手間が少ない

---

<https://twitter.com/t_wada/status/1466610043756101634>

> Gitのコミット粒度はまずConventional Commitsで種類が混ざりにくいようにしつつ、「小さいコミットを後からくっつけたり並べ替えたりする方が、大きいコミットを後から分割するよりもずっと簡単なので、迷ったら細かくコミットして後から見直せばいいよ」とよく言っています
> <https://conventionalcommits.org/ja/v1.0.0/>

(Conventional Commitsについては割愛)

---

# (GitHubなどの)Gitホスティングサービス上でのPRをMergeするやり方(Method)

いくつかPRをMergeする方法がある。代表的なものを3つ挙げると

- Create a merge commit `git merge --no-ff`
- Rebase and merge `git merge --ff`
- Squash and merge `git merge --squash`

どんな時にどのMethodですべきか? を考えたい(各Methodの解説へ)

---

# Create a merge commit `git merge --no-ff`

![h:720px](https://camo.qiitausercontent.com/034f69638cb0185d6860ace0b0e33eb0fb99c8b1/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e616d617a6f6e6177732e636f6d2f302f38363638342f30623030316233352d333531302d316362312d303435632d3732613030326539663166642e706e67)

---

# Rebase and merge `git merge --ff`

![h:720px](https://camo.qiitausercontent.com/0d30f32a5be0f36928d6ef78dc0fdd32de46fbd0/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e616d617a6f6e6177732e636f6d2f302f38363638342f37633232353165312d386333632d356661332d646232332d6463303330626261653866612e706e67)

---

# Squash and merge `git merge --squash`

![h:720px](https://camo.qiitausercontent.com/8fb83e2a003f6ec203ad85ac0e81db757723b333/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e616d617a6f6e6177732e636f6d2f302f38363638342f65303761666334632d663839372d646264642d386635362d3130653861333134353064652e706e67)

---

# まとめ

- Branch modelと運用
    - master(main), develop, feature/xxx, bugfix/yyyなど
    - 区切りには`/`を使用する
- Commitの粒度
    - 最初は意味のある最小単位ごとに分けるのがよい

---

- PRのmerge method
    - Create a merge commit `git merge --no-ff`
        - 履歴が全部保存される。Merge前のBranchはそのまま
    - Rebase and merge `git merge --ff`
        - 履歴が1本になるが、Commit履歴はそのまま
    - Squash and merge `git merge --squash`
        - Commitを纏めて1つにすることができる

---

# 参考記事など

- <https://atmarkit.itmedia.co.jp/ait/articles/1708/01/news015.html>
- <https://qiita.com/ko-he-8/items/94e872f2154829c868df>
