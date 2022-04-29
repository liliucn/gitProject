import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine #红酒数据集
from sklearn.datasets import load_iris #鸢尾花数据集
from sklearn.datasets import load_breast_cancer #乳腺癌数据集

from sklearn.tree import DecisionTreeClassifier #分类树
from sklearn.tree import DecisionTreeRegressor #回归树
from sklearn import tree #树
import sklearn #机器学习 sklearn库

import graphviz #画树的库

from sklearn.model_selection import train_test_split#训练集，测试集划分
from sklearn.model_selection import GridSearchCV #网格搜索
from sklearn.model_selection import cross_val_score #交叉验证


#决策树-分类树
def DecisionTreeClassifier_one():
    # 1、加载数据集
    wine=load_wine()
    df=pd.concat([pd.DataFrame(wine.data),pd.DataFrame(wine.target)],axis=1)
    print(df.head())

    # 2、划分数据集
    x_train, x_test, y_train, y_test=train_test_split(wine.data,wine.target,test_size=0.3)

    # 3、建模
    clf=DecisionTreeClassifier(criterion='entropy',random_state=1) # A：实例化
    clf=clf.fit(x_train,y_train) # B：fit 训练
    score=clf.score(x_test,y_test) # C：评估
    # print(score)

    #apply 返回每个测试样本所在的叶子节点的索引
    applyT=clf.apply(x_test)
    # print(applyT)

    #predict 返回每个测试样本的分类/回归结果
    predictT=clf.predict(x_test)
    print(predictT)

    #剪树参数 调参-优化模型
    test=[]
    for i in range(10):
        clf=tree.DecisionTreeClassifier(max_depth=i+1
                                        ,criterion='entropy'
                                        ,random_state=30
                                        ,splitter='random')
        clf=clf.fit(x_train,y_train)
        score=clf.score(x_test,y_test)
        test.append(score)

    #可视化查看调参的结果
    plt.plot(range(1,11),test,color='red',label='max_depth')
    plt.legend()
    plt.show()

    #画树
    #特征名称
    feature_name = ['酒精', '苹果酸', '灰', '灰的碱性', '镁', '总酚', '类黄酮', '非黄烷类酚类', '花青素', '颜色强度','色调','od280 / od315稀释葡萄酒','脯氨酸']
    dot_data=tree.export_graphviz(clf
                                  ,out_file=None
                                  ,feature_names=feature_name
                                  ,class_names=['琴酒','雪莉','贝尔摩德']
                                  ,filled=True
                                  ,rounded=True
                                  )
    graph=graphviz.Source(dot_data,encoding='gbk')
    graph.view()
def main():
    DecisionTreeClassifier_one()
main()


