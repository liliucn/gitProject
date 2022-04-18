import pycaret
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import warnings
from pycaret.regression import *
from pycaret.datasets import get_data
warnings.simplefilter("ignore")

#
# 次要- 【[Pytorch-从一团乱麻到入门]：3、模型效果评估指标：ROC、AUC、precision、recall】https://blog.csdn.net/qq_40815731/article/details/122948106?spm=1001.2101.3001.6650.9&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-9.pc_relevant_paycolumn_v3&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-9.pc_relevant_paycolumn_v3&utm_relevant_index=17
# 次要-使用Python+Pycaret进行异常检测(附代码演练)：https://blog.csdn.net/woshicver/article/details/118742153?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164844319516781685378091%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=164844319516781685378091&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-6-118742153.142^v5^pc_search_result_cache,143^v6^control&utm_term=python+pycaret&spm=1018.2226.3001.4187
# 重要-pycaret的具体使用流程：https://blog.csdn.net/qq_43627540/article/details/107667298?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.topblog&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.topblog&utm_relevant_index=2
# 重要-超参数：https://zhuanlan.zhihu.com/p/234509605
# 重要-聚类后效果：https://blog.csdn.net/u014556057/article/details/81286608?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164845822116781685362002%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=164845822116781685362002&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-4-81286608.142^v5^pc_search_result_cache,143^v6^control&utm_term=python+%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0+%E8%81%9A%E7%B1%BB%E5%8F%AF%E8%A7%86%E5%8C%96&spm=1018.2226.3001.4187
# 重要-经典模型实践：https://blog.csdn.net/weixin_44436319/article/details/123044521?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164845245916782246423766%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fcode.%2522%257D&request_id=164845245916782246423766&biz_id=&utm_medium=distribute.pc_search_result.none-task-code-2~code~first_rank_ecpm_v1~code_v1-1-123044521-2.nonecase&utm_term=python%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0+%E8%B6%85%E5%8F%82%E6%95%B0
# 重要-ROC曲线：https://blog.csdn.net/m0_47256162/article/details/118566843?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164845232816782094817628%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fcode.%2522%257D&request_id=164845232816782094817628&biz_id=&utm_medium=distribute.pc_search_result.none-task-code-2~code~first_rank_ecpm_v1~code_v1-2-118566843-0.nonecase&utm_term=python%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0roc%E6%9B%B2%E7%BA%BF
all_datasets = pd.read_csv('pycaret-master/datasets/index.csv')
# print(all_datasets.head())
df = pd.read_csv('pycaret-master/datasets/anomaly.csv')
exp1 = setup(df, target = 'Class variable')
# print(df.head())

# print(df.describe())
# print(df.info())

plt.rcParams["figure.figsize"] = (10, 8)
sns.swarmplot(x="variable", y="value", data=pd.melt(df))
plt.show()


