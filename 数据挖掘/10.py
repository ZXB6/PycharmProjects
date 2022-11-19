import pandas as pd
Data=pd.read_excel(".xlsx")
X=Data.iloc[:,1:]
R=X.corr()

from sklearn.decomposition import PCA
pca = PCA(n_component=0.95)
pca.fit(X)
Y=pca.transfrom(X)
tzxl=pca.components_
tz=pca.explained_variance_
gxl=pca.explained_variance_ratio_
Y00=sum(X[0,:]*tzxl[0,:])
Y01=sum(X[1,:]*tzxl[0,:])
Y02=sum(X[2,:]*tzxl[0,:])
Y03=sum(X[3,:]*tzxl[0,:])
