# Create a function to divide yr_build column into a 20 years interval
def gp_yr_built(x):
    '''
    signature:     gp_yr_built(x=int)
    docstring      classify year into category by grouping them in 20-year interval
    parameters:    x: element from pandas series
    return:        single int
    '''
    if x >= 1900 and x < 1921:
        return 5
    elif x >= 1921 and x < 1941:
        return 4
    elif x >= 1961 and x < 1981:
        return 3
    elif x >= 1981 and x < 2001:
        return 2
    else:
        return 1

# Highlight pair-wise correlation that has a value tht is greater than 0.75
def color_true_red(val):
    '''
    signature:    color_true_red(val=bool)
    docstring:    evaluate parameter value and return a string with color name
    parameters:   take in a single boolean valueb
    returns:      string
    '''
    color = 'red' if val > 0 else 'black'
    return 'color: %s' % color

# Extract the p-value that are less than 0.05 from the summary and use them to subset our features
def refine_xcols(summary):
    '''
    signature:    refine_x_cols(summary= (ols model results))
    docstring:    create a dataframe based on the 2nd section of model.summary object.
                  evaluate the p-value, if greater then 0.05 add them to the dataframe.
                  capture the number of features before and after the p-value evaluation.
    parameters:   take in the regression model object
    returns:      2 int and 1 str.  Number of count of features before and after the
                  process of elimination and the feature list.
    '''
    import pandas as pd
    # Grab the section where p-value is stored in the model.summary()
    p_table = summary.tables[1]
    # Unstack the data in the section and create a dataframe
    p_table = pd.DataFrame(p_table.data)
    # Use first row as the dataframe columns
    p_table.columns = p_table.iloc[0,:]
    p_table = p_table.drop(0)
    p_table = p_table.set_index(p_table.columns[0])
    bef_cols = len(p_table['P>|t|'])
    p_table['P>|t|'] = p_table['P>|t|'].astype(float)
    x_cols = list(p_table[p_table['P>|t|'] < 0.05].index)
    if 'Intercept' in x_cols:
        x_cols.remove('Intercept')
    aft_cols = len(x_cols)
    
    return bef_cols, aft_cols, x_cols

# Calculate Variance Inflation Factor
def cal_vif(dataframe, xcol, variance_inflation_factor):
    '''
    signature:     cal_vif(dataframe=object, xcol=list, variance_inflation_factor=obj)
    docstring:     using statsmodel VIF function to calculate feature multicollinearity.
                   return a list of features with their assocated VIF values.
    parameters:    dataframe: Dataframe object
    xcol: a list of strings object
    variance_inflation_factor: statsmodels.stats.outliers_influence.variance_inflation_factor object
    returns:       list of tuple        
    '''
    
    X = dataframe[xcol]
    vif = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    
    return xcol, vif

# Create a function to eliminate VIF greater than 5, excluding sqft_living feature
def rem_large_vif(xcol, vif, cutoff, np):
    '''
    signature:    rem_large_vif(xcol=list, vif=floats, cutoff=int, np=numpy).
    doctring:     evaluate list of values in vif results and eliminate entries greater than 5.
                  return a list of feature names.
    parameters:   x_cols: list of features used for old model.
                  vif: result set from the vif function.
    cutoff: criterior for removing VIF
    np: numpy object
    return:       list of string.
    '''
    
    for i , j in list(zip(xcol, vif)):
        # Evaluate feature-vif pair 
        if (j > cutoff and i != 'sqft_living') or (j == 'inf' and i != 'sqft_living') or (np.isnan(j) and i != 'sqft_living'):
            xcol.remove(i)
        
    return xcol




