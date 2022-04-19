import numpy as np
import pandas as pd
from sklearn.datasets import load_iris #鸢尾花数据集
from sklearn.datasets import load_wine #红酒数据集
from sklearn.datasets import load_boston #波士顿数据集
from sklearn.datasets import load_breast_cancer #乳腺癌数据集
from sklearn.tree import DecisionTreeClassifier # 分类树
from sklearn.tree import DecisionTreeRegressor  # 回归树
from sklearn import tree
import sklearn

import graphviz
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split #训练集、测试集 划分
from sklearn.model_selection import GridSearchCV #网格搜索
from sklearn.model_selection import cross_val_score #交叉验证

from sklearn.ensemble import RandomForestClassifier #随机森林-分类算法
from sklearn.ensemble import RandomForestRegressor #随机森林-回归算法
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler #数据归一化
# preprocessing包：几乎包含所有数据预处理的内容；
# impute包：填充缺失值专用；
# feature_selection：包含特征选择的各种方法的实践
# decomposition：包含降维算法



# 决策树-分类树1
def DecisionTreeClassifier1():
    #region 获取数据集 红酒数据集
    wine = load_wine()
    # print(wine.data.shape,wine.target)
    df =pd.concat([pd.DataFrame(wine.data),pd.DataFrame(wine.target)],axis=1)
    # print(df.head(),wine.feature_names,wine.target_names)
    #endregion 获取数据集

    #region 划分数据集
    Xtrain, Xtest, Ytrain, Ytest = train_test_split(wine.data, wine.target, test_size=0.3)
    # print(Xtrain.shape, Xtest.shape)
    #endregion 划分数据集

    #region 建模
    #region 较简单建模
    # clf = DecisionTreeClassifier(criterion='entropy')
    # clf = clf.fit(Xtrain, Ytrain)
    # score = clf.score(Xtest, Ytest)
    #
    # # apply返回每个测试样本所在的叶子节点的索引
    # applyT=clf.apply(Xtest)
    #
    # # predict返回每个测试样本的分类/回归结果
    # predictT=clf.predict(Xtest)

    # print(score,applyT,predictT)

    #endregion

    #region 剪枝参数 调参-优化模型
    test = []
    for i in range(10):
        clf = tree.DecisionTreeClassifier(max_depth=i + 1
                                          , criterion="entropy"
                                          , random_state=30
                                          , splitter="random"
                                          )
        clf = clf.fit(Xtrain, Ytrain)
        score = clf.score(Xtest, Ytest)
        test.append(score)
    plt.plot(range(1, 11), test, color="red", label="max_depth")
    plt.legend()
    plt.show()
    #endregion
    #endregion

    #region 可视化
    feature_name = ['酒精', '苹果酸', '灰', '灰的碱性', '镁', '总酚', '类黄酮', '非黄烷类酚类', '花青素', '颜色强度','色调','od280 / od315稀释葡萄酒','脯氨酸']
    dot_data = tree.export_graphviz(clf
                                    , out_file=None
                                    , feature_names=feature_name
                                    , class_names=["琴酒", "雪莉", "贝尔摩德"]
                                    , filled=True
                                    , rounded=True
                                    )
    graph = graphviz.Source(dot_data,encoding='utf-8')
    graph.view()
    #endregion

# 决策树-分类树1
def DecisionTreeClassifier2():
    data=pd.read_csv('files/Taitanicdata/data.csv')
    print(data.head(),data.info(),data.describe()) #描述性统计

    #删除分类型变量
    data.drop(["Cabin", "Name", "Ticket"], inplace=True, axis=1)  #删除Name Cabin Ticket列
    data['Age']=data['Age'].fillna(data['Age'].mean()) #用平均值 填充年龄的空值
    data=data.dropna()

    #二分类转为数值 #将男女转为0,1  新增列
    # print(data.head())
    # data['Sex2']=(data['Sex']=='male').astype('int') #第一种
    # data['Sex3']=data['Sex'].copy()
    data['Sex'] = (data['Sex'] == 'male').astype(np.int)
    # data["Sex3"]=(data["Sex3"]=="male").astype('int')#第二种

    #三分类转为数值
    labels=data["Embarked"].unique().tolist()
    # data["Embark1"]=data["Embarked"].copy()
    data["Embarked"]=data["Embarked"].apply(lambda x:labels.index(x))
    print(labels)
    # print(data['Embark1'].unique())

    # 以survived划分x,y数据集
    x =data.iloc[:,data.columns != 'Survived']
    y =data.iloc[:,data.columns == 'Survived']

    Xtrain,Xtest,Ytrain,Ytest=train_test_split(x,y,test_size=0.3)
    # 修正测试集和训练集的索引
    for i in [Xtrain,Xtest,Ytrain,Ytest]:
        i.index = range(i.shape[0])
    print('mmm')
    clf = DecisionTreeClassifier(random_state=25)
    clf = clf.fit(Xtrain, Ytrain)
    score = clf.score(Xtest, Ytest)
    score2 = cross_val_score(clf,x, y, cv=10).mean()
    print(score2)

    tr = []
    te = []
    for i in range(10):
        clf = DecisionTreeClassifier(random_state=25
                                     , max_depth=i + 1
                                     , criterion="entropy"
                                     )
        clf = clf.fit(Xtrain, Ytrain)
        score_tr = clf.score(Xtrain, Ytrain)
        score_te = cross_val_score(clf, x, y, cv=10).mean()
        tr.append(score_tr)
        te.append(score_te)
    print(max(te))
    plt.plot(range(1, 11), tr, color="red", label="train")
    plt.plot(range(1, 11), te, color="blue", label="test")
    plt.xticks(range(1, 11))
    plt.legend()
    plt.show()

# 决策树-回归树1
def DecisionTreeRegressor1():
    boston=load_boston()
    regressor=DecisionTreeRegressor(random_state=0)
    cross_val_score(regressor, boston.data, boston.target, cv=10,
                    scoring="neg_mean_squared_error")
# 随机森林-分类算法
def RandomForestClassifier1():
    wine=load_wine()
    print(wine.data,wine.target)
    Xtrain,Xtest,Ytrain,Ytest=train_test_split(wine.data,wine.target,test_size=0.3)

    #region 没有交叉验证的情况下，决策树和随机森林的比较结果
    #决策树-分类树
    clf=DecisionTreeClassifier(random_state=20)
    clf=clf.fit(Xtrain,Ytrain)
    score_c=clf.score(Xtest,Ytest)

    # 随机森林-分类树
    rfc=RandomForestClassifier(random_state=20)
    rfc=rfc.fit(Xtrain,Ytrain)
    score_r=rfc.score(Xtest,Ytest)
    print('决策树-分类树：',score_c,' 随机森林-分类算法：',score_r)
    #endregion

    # region 有交叉验证的情况下，决策树和随机森林的比较结果；只有一次交叉验证
    # 交叉验证- 随机森林  n_estimators：森林中树木的数量，即基评估器的数量; 值越大越慢，准确率越高，模型越可靠
    rfc = RandomForestClassifier(n_estimators=25)
    rfc_s = cross_val_score(rfc, wine.data, wine.target, cv=10)
    # 交叉验证- 决策树
    clf = DecisionTreeClassifier()
    clf_s = cross_val_score(clf, wine.data, wine.target, cv=10)

    plt.plot(range(1, 11), rfc_s, label="RandomForest")
    plt.plot(range(1, 11), clf_s, label="Decision Tree")
    plt.legend()
    plt.show()
    #endregion

    #region 有交叉验证的情况下，决策树和随机森林的比较结果；有十次交叉验证
    rfc_l = []
    clf_l = []
    #n_estimators：森林中树木的数量，即基评估器的数量; 值越大越慢，准确率越高，模型越可靠
    for i in range(10):
        rfc = RandomForestClassifier(n_estimators=25)
        rfc_s = cross_val_score(rfc, wine.data, wine.target, cv=10).mean()
        rfc_l.append(rfc_s)

        clf = DecisionTreeClassifier()
        clf_s = cross_val_score(clf, wine.data, wine.target, cv=10).mean()
        clf_l.append(clf_s)
    plt.plot(range(1, 11), rfc_l, label="Random Forest")
    plt.plot(range(1, 11), clf_l, label="Decision Tree")
    plt.legend()
    plt.show()
    #endregion

    #region  n_estimators：200，就会变得很慢了 【测试 n_estimators这个参数】
    # superpa = []
    # for i in range(200):
    #     rfc = RandomForestClassifier(n_estimators=i + 1, n_jobs=-1)
    #     rfc_s = cross_val_score(rfc,wine.data, wine.target, cv=10).mean()
    #     superpa.append(rfc_s)
    # print(max(superpa), superpa.index(max(superpa)))
    # plt.figure(figsize=[20, 5])
    # plt.plot(range(1, 201), superpa)
    # plt.show()
    #endregion

    #region 1、random_state  当random_state固定时，随机森林中生成是一组固定的树，但每棵树依然是不一致的，
    # 这是用”随机挑选特征进行分枝“的方法得到的随机性
    rfc = RandomForestClassifier(n_estimators=20, random_state=2)
    rfc = rfc.fit(Xtrain, Ytrain)
    # 随机森林的重要属性之一：estimators，查看森林中树的状况
    print(rfc.estimators_[0].random_state)
    for i in range(len(rfc.estimators_)):
        print(rfc.estimators_[i].random_state)
    #endregion

    #region 2、bootstrap参数默认True，代表采用这种有放回的随机抽样技术
    rfc = RandomForestClassifier(n_estimators=25, oob_score=True)
    rfc = rfc.fit(wine.data, wine.target)
    print(rfc.oob_score_)
    #endregion

def RandomForestRegressor1():
    boston = load_boston()
    #如果不填写scoring = "neg_mean_squared_error"，
    # 交叉验证默认的模型衡量指标是R平方，因此交叉验证的结果可能有正也可能有负。
    # 而如果写上scoring，则衡量标准是负MSE，交叉验证的结果只可能为负。
    regressor = RandomForestRegressor(n_estimators=100, random_state=0)
    cross_val_score(regressor, boston.data, boston.target, cv=10
                    , scoring="neg_mean_squared_error")
    print(sorted(sklearn.metrics.SCORERS.keys()))

def RandomForestRegressor2():
    dataset = load_boston()
    print(dataset.data.shape) # 共506*13=6578个数据
    X_full, y_full = dataset.data, dataset.target
    n_samples = X_full.shape[0]
    n_features = X_full.shape[1]
    '''填充缺失值的逻辑：
    #首先确定我们希望放入的缺失数据的比例，在这里我们假设是50%，那总共就要有3289个数据缺失
    #所有数据要随机遍布在数据集的各行各列当中，而一个缺失的数据会需要一个行索引和一个列索引
    #如果能够创造一个数组，包含3289个分布在0~506中间的行索引，和3289个分布在0~13之间的列索引，那我们就可以利用索引来为数据中的任意3289个位置赋空值
    #然后我们用0，均值和随机森林来填写这些缺失值，然后查看回归的结果如何
    #missing_samples = rng.choice(dataset.data.shape[0],n_missing_samples,replace=False)
    #我们现在采样了3289个数据，远远超过我们的样本量506，所以我们使用随机抽取的函数randint。
        但如果我们需要的数据量小于我们的样本量506，那我们可以采用np.random.choice来抽样，
        choice会随机抽取不重复的随机数，因此可以帮助我们让数据更加分散，确保数据不会集中在一些行中
    '''
    rng = np.random.RandomState(0)
    missing_rate = 0.5
    # np.floor向下取整，返回.0格式的浮点数
    n_missing_samples = int(np.floor(n_samples * n_features * missing_rate))

    missing_features = rng.randint(0, n_features, n_missing_samples)
    missing_samples = rng.randint(0, n_samples, n_missing_samples)

    X_missing = X_full.copy()
    y_missing = y_full.copy()

    X_missing[missing_samples, missing_features] = np.nan
    # 转换成DataFrame是为了后续方便各种操作，numpy对矩阵的运算速度快到拯救人生，但是在索引等功能上却不如pandas来得好用
    X_missing = pd.DataFrame(X_missing)


    ''' 用 0 和 均值  填充缺失值'''
    # 使用均值进行填补
    imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
    X_missing_mean = imp_mean.fit_transform(X_missing)
    # 使用0进行填补
    imp_0 = SimpleImputer(missing_values=np.nan, strategy="constant", fill_value=0)
    X_missing_0 = imp_0.fit_transform(X_missing)

    ''' 用随机森林填补缺失值 '''
    X_missing_reg = X_missing.copy()
    sortindex = np.argsort(X_missing_reg.isnull().sum(axis=0)).values
    for i in sortindex:
        # 构建我们的新特征矩阵和新标签
        df = X_missing_reg
        fillc = df.iloc[:, i]
        df = pd.concat([df.iloc[:, df.columns != i], pd.DataFrame(y_full)],axis=1)
        # 在新特征矩阵中，对含有缺失值的列，进行0的填补     
        df_0 =SimpleImputer(missing_values=np.nan,strategy='constant',fill_value=0).fit_transform(df)
        # 找出我们的训练集和测试集
        Ytrain = fillc[fillc.notnull()]
        Ytest = fillc[fillc.isnull()]
        Xtrain = df_0[Ytrain.index,:]
        Xtest = df_0[Ytest.index, :]
        rfc = RandomForestRegressor(n_estimators=100)
        rfc = rfc.fit(Xtrain, Ytrain)
        Ypredict = rfc.predict(Xtest)
        # 将填补好的特征返回到我们的原始的特征矩阵中
        X_missing_reg.loc[X_missing_reg.iloc[:, i].isnull(), i] =Ypredict
    # 对所有数据进行建模，取得MSE结果
    X = [X_full, X_missing_mean, X_missing_0, X_missing_reg]
    mse = []
    std = []
    for x in X:
        estimator = RandomForestRegressor(random_state=0, n_estimators=100)
        scores = cross_val_score(estimator, x, y_full, scoring='neg_mean_squared_error', cv=5).mean()
        mse.append(scores * -1)

def RandomForestRegressor3():
    data = load_breast_cancer()
    rfc = RandomForestClassifier(n_estimators=100, random_state=90)
    score_pre = cross_val_score(rfc, data.data, data.target, cv=10).mean()
    print(score_pre)
    scorel = []
    for i in range(0, 200, 10):
        rfc = RandomForestClassifier(n_estimators=i + 1,
                                      n_jobs=-1,
                                      random_state=90)
        score = cross_val_score(rfc, data.data, data.target, cv=10).mean()
        scorel.append(score)
    print(max(scorel), (scorel.index(max(scorel)) * 10) + 1)
    plt.figure(figsize=[20, 5])
    plt.plot(range(1, 201, 10), scorel)
    plt.show()

def DataTreat():
    data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]
    pd.DataFrame(data)
    # 实现归一化
    scaler=MinMaxScaler() #实例化
    scaler=scaler.fit(data)
    result=scaler.transform(data)
    print(result)

    result2=scaler.fit_transform(data)
    scaler.inverse_transform(result2)

    data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]
    scaler = MinMaxScaler(feature_range=[5, 10])
    result = scaler.fit_transform(data)
    print(result)

#主方法
def main():
    DecisionTreeClassifier1()  #1、决策树-分类树 红酒数据集,有树的可视化,以及 模型估化可视化 【这个乱码】
    # DecisionTreeClassifier2()  #2、决策树-分类树  泰坦尼克号幸存者的预测
    # DecisionTreeRegressor1()   #3、 决策树-回归树
    # RandomForestClassifier1()  #4、随机森林-分类算法  比较决策树和随机森林的分类结果
    # RandomForestRegressor1()   #5、随机森林-回归算法
    # RandomForestRegressor2()   #5、随机森林-回归算法 用于填充 缺失值
    # RandomForestRegressor3()   #5、随机森林-回归算法 乳腺癌案例
    # DataTreat()# 6、数据预处理
main()