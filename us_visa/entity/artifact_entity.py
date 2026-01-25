from dataclasses import dataclass

# artifact_entity.py is used to store the artifact of each component

@dataclass
class DataIngestionArtifact: # to store the artifact of data_ingestion component
    trained_file_path:str 
    test_file_path:str 

@dataclass
class DataValidationArtifact:
    validation_status:bool #whether data validation is successful or not
    message: str   #dataset has a data drift or not
    drift_report_file_path: str #path to the drift report file

@dataclass # dataclass decorator is used to create classes which mainly store data
class DataTransformationArtifact: # to store the artifact of data_transformation component
    transformed_object_file_path:str  # path to the preprocessor object
    transformed_train_file_path:str # path to the transformed train file
    transformed_test_file_path:str


@dataclass
class ClassificationMetricArtifact:
    f1_score:float
    precision_score:float
    recall_score:float



@dataclass
class ModelTrainerArtifact:
    trained_model_file_path:str 
    metric_artifact:ClassificationMetricArtifact


@dataclass
class ModelEvaluationArtifact:
    is_model_accepted:bool
    changed_accuracy:float
    s3_model_path:str 
    trained_model_path:str