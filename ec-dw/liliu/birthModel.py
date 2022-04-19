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
def DecisionTreeClassifier1():
    # 1、加载数据集
    wine=load_wine()
    df=pd.concat([pd.DataFrame(wine.data),pd.DataFrame(wine.target)],axis=1)
    print(df.head())

    # 2、划分数据集
    X_train, X_test, y_train, y_test=train_test_split(wine.data,wine.target,test_size=0.3)

    # 3、建模
    clf=DecisionTreeClassifier(criterion='entropy')
    clf=clf.fit(X_train,X_test)
    score=clf.score(X_test,y_test)
def main():
    DecisionTreeClassifier1()
main()


