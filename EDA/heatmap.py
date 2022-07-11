
import pandas  as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
%matplotlib inline

plt.rcParams['figure.figsize'] = [8,5]
plt.rcParams['font.size'] =14
plt.rcParams['font.weight']= 'bold'
plt.style.use('seaborn-whitegrid')

#Loading the Dataset
df = pd.read_csv('./dataset/Fish.csv')

# correlation plot
corr = df.corr()
sns.heatmap(corr, cmap = 'Wistia', annot= True);
