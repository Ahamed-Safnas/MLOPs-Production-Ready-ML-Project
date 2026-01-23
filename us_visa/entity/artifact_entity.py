from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    trained_file_path:str 
    test_file_path:str 

@dataclass
class DataValidationArtifact:
    validation_status:bool #whether data validation is successful or not
    message: str   #dataset has a data drift or not
    drift_report_file_path: str #path to the drift report file

@dataclass
class DataTransformationArtifact:
    transformed_object_file_path:str 
    transformed_train_file_path:str
    transformed_test_file_path:str
