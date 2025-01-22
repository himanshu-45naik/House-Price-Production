import pandas as pd
from zenml import step
from src.feature_engineering import FeatureEngineer,OneHotEncoding,MinMaxScaling,StandardScaling,LogTransformation


@step 
def feature_engineering(df:pd.DataFrame,strategy:str)->pd.DataFrame:
    """Performs feature engineering on the data.

    Args:
        df (pd.DataFrame): The data onw hich feature engineering is performed.

    Returns:
        pd.DataFrame: The transformed data frame.
    """
    if strategy == "log":
        feature_engineer = FeatureEngineer(LogTransformation)
    elif strategy == "standard":
        feature_engineer = FeatureEngineer(StandardScaling)
    elif strategy == "min-max":
        feature_engineer = FeatureEngineer(MinMaxScaling)
    elif strategy == "onehotencoding":
        feature_engineer = FeatureEngineer(OneHotEncoding)
    else:
        raise ValueError(f"Unsupported feature engineering strategy:{strategy}")

    transformed_data = feature_engineer.apply_transformation
    
    