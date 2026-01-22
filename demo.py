from us_visa.logger import logging
# from us_visa.logger import logger


# # logging.info("hey, welcome to our custom log ")
# logger.info("hey, welcome to our custom log ")

from us_visa.pipline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()

