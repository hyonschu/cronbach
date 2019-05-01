def Cronbach(corr_matrix, drops=None, corr_func='pearson', raw_data=1):
	'''
	Takes a pandas dataframe and returns Cronbach's alpha
	
	`corr_matrix` is a pandas dataframe. np.array would also work (maybe)
	`drops` allows to compare alpha with missing features to check consistency
	`corr_func` can be any function of pd.DataFrame.corr() ie 'pearson, 'kendall'
	`raw_data` when == 1 means the dataframe is raw responses. 0 means correlations are already applied

	returns Cronbach's alpha as float
	'''

	import numpy as np
	if raw_data == 1:
	if drops:
	    corr_matrix = corr_matrix.drop(drops, axis=1).corr(corr_func)
	else: 
	    corr_matrix = corr_matrix.corr(corr_func)
	else: pass
	corr_matrix = np.array(corr_matrix)
	x,y = corr_matrix.shape
	m = np.tril_indices(n=x, k=-1, m=y)
	#      (k*avg(r))	   	 / (1 + (k -1) * avg(r))
	return (x*corr_matrix[m].mean()) / (1+ (x-1) * corr_matrix[m].mean())    
