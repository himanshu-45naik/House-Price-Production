import logging
from abc import ABC , abstractmethod
import pandas as pd

logging.basicConfig(level=logging.INFO,format="%(asctime)s-%(levelname)s-%(message)s")


class MissingValueHandlingStrategy(ABC):
    @abstractmethod
    def handle(self,df:pd.DataFrame)->pd.DataFrame:
        """Abstract method to handle missing value in the DataFrame

        Args:
            df (pd.DataFrame): Dataframe for which missing values are handled

        Returns:
            pd.DataFrame: The updated dataframe with handled missing values
        """
        pass
    
class DropMissingValues(MissingValueHandlingStrategy):
    def __init__(self,axis=0,thres=None):
        """Initializes the axis and thres based on which data is handled
        
        Args:
        axis(int): 0 to drop rows and 1 to drop columns
        thres : The thresold of Non-NA values based on which rows or column is dropped"""
        
        self.axis = axis
        self.thres = thres
    
    def handle(self, df:pd.DataFrame)->pd.DataFrame:
        """Drops rows or columns with missing values 
        
        Args:
        df : The dataframe for which missing values are handled
        """
        logging.info("Dropping missing values with axis {self.axis}")
        df_cleaned = df.dropna(axis=self.axis,thresh=self.thres)
        logging.info("Missing values dropped")
    
        return df_cleaned
    
class FillingMissingValues(MissingValueHandlingStrategy):
    def __init__(self,method="mean",fill_values=None):
        """Initializesthe FillMissingStrategy with a specific

        Args:
            method (str, optional):The method to fill missing values. Defaults to "mean".
            fill_values (_type_, optional): The constant value for filling missing value. Defaults to None.
        """
        self.method = method
        self.fill_values = fill_values
        
    def handle(self, df:pd.DataFrame)->pd.DataFrame:
        """Filling missing values using specifies method or constant value

        Args:
            df (pd.DataFrame): The data frame for which the values are filled
        Returns:
            pd.DataFrame: The updated dataframe with filled missing values
        """
        
        logging.info(f"Filling missing values using method:{self.method}")
        
        df_cleaned = df.copy()
        if self.method == "mean":
            numeric_columns = df_cleaned.select_dtypes(include="number").columns
            df[numeric_columns] = df[numeric_columns].fillna(
                df[numeric_columns].mean()
            )
        elif self.method == "median":
            numeric_columns = df_cleaned.select_dtypes(include="number")
            df[numeric_columns] = df[numeric_columns].fillna(
                df[numeric_columns].median()
            )
        elif self.method == "mode":
            for column in df_cleaned.columns:
                df_cleaned[column].fillna(df[column].mode().iloc[0])
                
        elif self.method == "constant":
            df_cleaned = df_cleaned.fillna(self.fill_values)
        else:
            logging.warning(f"Unknown Methods '{self.method}'. ")
            
        logging.info("Missing Values filled.")
        
        return df_cleaned
    
    
class MissingValueHandler:
    def ___init__(self,strategy:MissingValueHandlingStrategy):
        """Initializes the strategy for handling data

        Args:
            strategy (MissingValueHandlingStrategy): THe strategy baesed on which data is handled
        """
        
        self._strategy = strategy
        
    def set_strategy(self,strategy:MissingValueHandlingStrategy):
        """Sets strategy based on which data is handled for missing values
        
        Args: 
        strategy (MissingValueHandlingStrategy) : The strategy baesed on which data is handled"""
        
        self._strategy = strategy
        
    def execute_strategy(self,df:pd.DataFrame):
        """Executes the strategy for filling data

        Args:
            df (pd.DataFrame): The dataframe for which the missing values are handled
        """
        
        self._strategy.handle(df)
        

if __name__ == "__main__":
    pass