from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn import preprocessing
import numpy as np
import umap.umap_ as umap

def perform_PCA(X: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    scaler = preprocessing.StandardScaler()
    X = scaler.fit_transform(X)

    pca = PCA(n_components=2)
    pca.fit(X)  # Learn the projection matrix
    Z = pca.transform(X) # Project the given data with the learnt projection matrix
    
    PC1, PC2 = pca.components_ # Since n_components = 2
    PCs = np.vstack((PC1.reshape(1, -1), PC2.reshape(1, -1))) # Rows refer to each PC; Columns refer to each data attribute
    return Z, PCs

def perform_TSNE(X: np.ndarray, perplexity: int = 5) -> np.ndarray:
    scaler = preprocessing.StandardScaler()
    X = scaler.fit_transform(X) #standardized_data

    tsne = TSNE(n_components=2, random_state = 0, perplexity=perplexity)
    Z = tsne.fit_transform(X)
    return Z

def perform_UMAP(X: np.ndarray, target: np.ndarray) -> np.ndarray:
    reducer = umap.UMAP(n_neighbors=13, min_dist=0.1, n_components=2)
    Z = reducer.fit_transform(X)
    return Z