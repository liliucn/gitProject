"""
Project Name : exp4
File Name    : my_DBSCAN.py
Author       : Chen Chunhan
Student ID   : 04194041
Major & Class: Big Data 1902
Date         : 2021-11-10 Wed.
"""
import copy
import random

import numpy as np


class my_DBSCAN:
    """
    基于NumPy实现DBSCAN算法
    """

    def __init__(self, dataset, eps, min_pts):
        self.dataset = dataset
        self.eps = eps
        self.min_pts = min_pts

    def dist(self, xi, xj):
        """
        计算两个样本点之间的欧氏距离
        :param xi: 样本点1
        :param xj: 样本点2
        :return: 两个样本点之间的欧氏距离
        """
        return np.sqrt((np.power((xi[0] - xj[0]), 2) + np.power((xi[1] - xj[1]), 2)))

    def eps_neighborhood(self, j):
        """
        确定样本的ε-邻域
        :param j: 样本索引
        :return: 样本的ε-邻域
        """
        neighborhood = set()
        for i in range(self.dataset.shape[0]):
            if self.dist(self.dataset[i], self.dataset[j]) <= self.eps:
                neighborhood.add(i)
        return neighborhood

    def DBSCAN(self):
        """
        DBSCAN聚类
        :return: DBSCAN聚类后的簇划分
        """
        k = -1                                                # 初始化聚类簇数
        cluster = [-1 for _ in range(len(self.dataset))]
        omega = []                                            # 初始化核心对象集合为空
        N_eps = []
        gamma = set([i for i in range(len(self.dataset))])    # 初始化未访问集合
        for i in range(len(self.dataset)):
            N_eps.append(self.eps_neighborhood(i))            # 确定样本的epsilon邻域
            if len(N_eps[-1]) >= self.min_pts:
                omega.append(i)
        omega = set(omega)
        while len(omega) > 0:
            gamma_old = copy.deepcopy(gamma)                  # 记录当前未访问样本集合
            j = random.choice(list(omega))
            k += 1
            Q = [j]                                           # 初始化队列
            gamma.remove(j)                                   # j已被访问，移出gamma集合
            while len(Q) > 0:
                q = Q[0]                                      # 取队首
                Q.remove(q)
                if len(N_eps[q]) >= self.min_pts:
                    delta = N_eps[q] & gamma
                    for i in range(len(delta)):
                        Q.append(list(delta)[i])
                        gamma -= delta
            Ck = gamma_old - gamma
            for i in range(len(Ck)):
                cluster[list(Ck)[i]] = k
            omega -= Ck
        return cluster


# test
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from sklearn import datasets

    X1, y1 = datasets.make_circles(n_samples=2000, factor=.6, noise=.02)
    X2, y2 = datasets.make_blobs(n_samples=400, n_features=2, centers=[[1.2, 1.2]], cluster_std=[[.1]], random_state=9)
    X = np.concatenate((X1, X2))
    plt.figure()
    plt.scatter(X[:, 0], X[:, 1])
    plt.savefig('./raw_data.png')
    plt.show()

    eps = 0.08
    min_pts = 10
    C = my_DBSCAN(X, eps, min_pts).DBSCAN()
    plt.figure()
    plt.scatter(X[:, 0], X[:, 1], c=C)
    plt.savefig('./result.png')
    plt.show()
