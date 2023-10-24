import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer

def read_clean_data(save_to_csv=False):
    
    """ Loads the data from the processed_data.csv file and preprocesses it. Loads the 
    pollution data from the PM2.5 csv files and preprocesses it. Combines the two 
    datasets, so that the pollution datapoints are moved one day forward. Saves the
    combined dataset to a csv file.

    Args:
        save_to_csv: A boolean indicating whether to save the preprocessed data to a csv file.
    
    Returns:
        data: A pandas dataframe containing the preprocessed data.
        
    """

    data = pd.read_csv('Data\weather_data\processed_data.csv')  # Load the data

    data = data.iloc[296:-2, :].reset_index(drop=True)  # Adjust the data to include the 2003-2022 range

    pollution_data_1 = pd.read_csv('Data\PM2.5\PM2.5_2003_2012.csv') # Load the pollution data
    pollution_data_2 = pd.read_csv('Data\PM2.5\PM2.5_2013_2022.csv')

    pollution_data = pd.concat([pollution_data_1, pollution_data_2], axis=0)    # Combine the two pollution dataframes
    pollution_data = pollution_data.iloc[::-1].reset_index(drop=True)   # Reverse the order of the pollution data
    pollution_data = pollution_data.drop(['Station ID', 'Pollutant'], axis=1)   # Drop the unnecessary columns

    pollution_data.replace(9999, np.NaN, inplace=True)  # Replace the 9999 values with NaN
    pollution_data['P2.5'] = pollution_data.mean(axis=1)    # Calculate the mean of the pollution data (for each day)

    X = data.drop('date', axis=1).iloc[1:, :].reset_index(drop=True)    # Separate the input features and move the data one day forward
    y = pd.DataFrame(pollution_data['P2.5']).iloc[:-1, :]   # Separate the output feature and move the data one day backward
    
    y.fillna(y.mean(), inplace=True)    # Replace the NaN values with the mean of the pollution data
    
    data = pd.concat([X, y], axis=1)    # Combine the input and output features

    if save_to_csv: 
        data.to_csv('Data\weather_data\data.csv', index=False)  # Save the data to a csv file
    return data

    
def load_X_y():
    """ Loads the features X and the output y from the data.csv file.

    Args:
        None
    
    Returns:
        X: A pandas dataframe containing the input features.
        y: A pandas dataframe containing the output feature.
        
    """
    
    data = pd.read_csv('Data\weather_data\data.csv')    # Load the data
    X = data.drop('P2.5', axis=1)   # Separate the input features
    y = pd.DataFrame(data['P2.5'])  # Separate the output feature
    return X, y
    
X, y = load_X_y()


