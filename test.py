
###分词
import pkuseg
#pkuseg.test('data.csv', 'cuted_withAttri.txt', postag=True, nthread=1)
pkuseg.test('data.csv', 'cuted.txt', postag=False, nthread=1)


###情感分析
'''
from classifiers import DictClassifier
classify=DictClassifier()
classify.analysis_file('cuted.txt', 'senti.csv', encoding="utf-8", print_show=True, start=0, end=-1)


###可视化

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
crime=pd.read_csv(r'senti.csv')
fig,ax=plt.subplots()
ax.hist(crime['0'],bins=100,histtype="stepfilled",alpha=1,label="Score")
ax.legend()
ax.set_xticks(np.arange(-7,17,1))
ax.set_xlim(-7,17)
ax.set_yticks(np.arange(0,3001,300))
plt.savefig('pic.png')
plt.show()
'''