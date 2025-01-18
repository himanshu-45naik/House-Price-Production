from zenml import Model,pipeline,step
from steps.data_ingestion_step import data_ingestion_step


@pipeline(
    model=Model(
        name="house_prices_predictor"
    )
)

def ml_pipeline():
    """Define end-to-end machine learning pipeline"""
    
    ## Data ingestion step
    raw_data = data_ingestion_step(
        "/home/himanshu/Coding/House_Price/archive.zip"
    )
    
    #filled_data = 