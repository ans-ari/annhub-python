import os
from typing import List
from annhub_python.core.errors import PredictException, ModelLoadException, InvalidInputException
from loguru import logger
from annhub_python.ml_lib import annhub as annhub


class MachineLearningModel(object):
    """ Main machine learning model wrapper object.
    Take responsibility of saving model's information,
    Load model into memory, predict.

    """

    def __init__(self, model_path : str, model_id: int, input_length: int) -> None:
        super().__init__()
        self._model_path = model_path
        self._input_length = input_length
        self._model_id = model_id
        self.load()

    def load(self):
        """ Load model into memory

        Raises:
            FileNotFoundError: Raise when the provided model path is not correct.
        """
        if not os.path.exists(self._model_path):
            message = f"Machine learning model at {self._model_path} not exists!"
            logger.error(message)
            raise FileNotFoundError(message)

        self.load_model()
    
    def load_model(self):
        """ Integrate with annhub library to load the model into memory.
        The model is identified by model path and model id.

        Raises:
            ModelLoadException: Raise when an annhub model can not be loaded properly.
        """
        self.model = annhub.ANNHUB(self._model_id)
        self.model.LoadWeightFile(self._model_path)
        if not self.model:
            message = f"Model {self._model_id} could not load!"
            logger.error(message)
            raise ModelLoadException(message)

    def predict(self, data_input: List[float]) -> List[float]:
        """ Predict function of a given model.
        Check the data constraints and feed data input to 
        annhub machine learning model, which has been loaded into memory before.

        Args:
            data_input (List[float]): Received data input from web controller.

        Raises:
            InvalidInputException: Raise when the data input is not meet the predefined size.
            PredictException: Raise when the model can not predict and produce final results.

        Returns:
            List[float]: Model output
        """
        if data_input.__len__() != self._input_length:
            message = f"The model is defined with input size: {self._input_length}, but got size {data_input.__len__()}"
            logger.error(message)
            raise InvalidInputException(message)

        self.model.Predict(data_input)
        output = self.model.GetOutput()
        if not output:
            message = f"Error when predict input:'{data_input}'"
            logger.error(message)
            raise PredictException(message)

        logger.info("Input: {}, Output: {}", data_input, output)
        return output


