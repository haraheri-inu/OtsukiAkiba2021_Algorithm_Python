# -*- coding: utf-8 -*-
"""code5.1_DP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ayN2KFtNRj6dPYJyz6jppyBdywdJSL2J

# 5 設計技法(3)：動的計画法
## 5.2 動的計画法の例題
問題: https://atcoder.jp/contests/dp/tasks/dp_a

入力の形式は以下を想定する。

入力1として足場の数を受けとり、入力2として各$h_1, \ldots , h_N$をスペース区切りで受けとる。
"""

def dp_frog():
    # 足場長
    N = int(input())
    # 足場の高さ
    H = list(map(int, input().split()))
    # dp[k]は足場kまでの最短経路
    dp = [0]
    dp.append(abs(H[0]-H[1]))
    for i in range(2, N):
        min_root = min(dp[i-2]+abs(H[i-2]-H[i]), dp[i-1]+abs(H[i-1]-H[i]))
        dp.append(min_root)
    return print(f"各コスト:{dp}\n最終コスト:{dp[-1]}")

# test
dp_frog()