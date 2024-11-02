# JPMC Company Relationship Analysis Tool
from scipy.cluster.hierarchy import linkage, fcluster 
Z = linkage(X, method = 'average')

fig = plt.figure(figsize = (10,5))
dn = dendrogram(Z)
plt.title("Average Linkage Dendrogram")
plt.xlabel('Prices')
plt.ylabel('Distance')
plt.show()
