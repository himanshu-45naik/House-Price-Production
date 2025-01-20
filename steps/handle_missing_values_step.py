import pandas as pd
from zenml import step
from src.handling_missing_values import DropMissingValues, FillingMissingValues, MissingValueHandler

@step

def handle_missing_values(df:pd.DataFrame,strategy:str)->pd.DataFrame:
    """
    Handles missing values for the given dataframe
    """  
    
    if strategy == "drop":
        handler = MissingValueHandler(DropMissingValues(axis=0))
    if strategy in ["mean","mode","median","constant"]:
        handler = MissingValueHandler(FillingMissingValues(method=strategy))
    else:
        raise ValueError(f"Unsupported missing value handling strategy: {strategy}")
    
    
    cleaned_df = handler.handle_missing_values(df)
    return cleaned_df
     