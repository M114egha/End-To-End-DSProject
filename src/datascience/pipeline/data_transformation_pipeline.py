from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import  DataTransformation
from src.datascience import logger
from pathlib import Path

STAGE_NAME="Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), 'r') as f:
                line = f.read().strip()
                logger.info(f"Validation status read from file: '{line}'")

                # Split by ':' and extract the value part
                status = line.split(":")[-1].strip().lower()

                if status == "true":
                    config = ConfigurationManager()
                    data_transformation_config = config.get_data_transformation_config()
                    data_transformation = DataTransformation(config=data_transformation_config)
                    data_transformation.train_test_split()
                else:
                    raise Exception("Your data scheme is not valid")


        except Exception as e:
            raise e