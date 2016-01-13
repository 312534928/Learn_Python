# 员工人数分配
# 商店ABC
# 每个商店获得员工时的收益情况如下
# dict{'A':[0,3,7,9,12,13],'B':[0,5,10,11,11,11],'C':[0,4,6,11,12,12]}
# 总共有可分配员工5人
# 求最大收益的分配方案

# 状态变量sk，对第k个商店分配员工时，可分配的员工数量
# 决策变量d[k][sk],对第k个商店在sk状态下分配的员工数量
# 顺序解法
def Plan(v, d, K, S):
    '''
    :param v: 商店收益表
    :param d: 决策变量
    :param K: 商店数
    :param S: 员工数量
    :return: 第K阶段分配S人的最大收益
    '''
    f = [[0 for col in range(S + 1)] for row in range(K + 1)]  # 二维数组初始化
    for i in range(S + 1):
        f[0][i] = 0  # 边界初始化
    for k in range(1, K + 1):
        for s in range(S + 1):
            maxf = 0
            for x in range(s + 1):
                if (v[k - 1][x] + f[k - 1][s - x] > maxf):
                    maxf = v[k - 1][x] + f[k - 1][s - x]
                    d[k][s] = x
            f[k][s] = maxf
    print("最优配置盈利：", f[K][S])
    return f[K][S]


def disPlan(d, K, S):
    s = S
    for k in range(1, K + 1)[::-1]:
        print(" %c 商店分配 %d 人" % (chr(ord('C') + k - 3), d[k][s]))
        s = s - d[k][s]


# v = dict(A=[0, 3, 7, 9, 12, 13], B=[0, 5, 10, 11, 11, 11], C=[0, 4, 6, 11, 12, 12])
v = [[0, 3, 7, 9, 12, 13], [0, 5, 10, 11, 11, 11], [0, 4, 6, 11, 12, 12]]
K = len(v)
S = 5
d = [[0 for col in range(S + 1)] for row in range(len(v) + 1)]
Plan(v, d, K, S)
disPlan(d, K, S)
