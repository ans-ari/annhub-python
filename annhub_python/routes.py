from annhub_python.annhub_python.core.errors import ModelLoadException, PredictException
from annhub_python.core.errors import InvalidInputException
from annhub_python.services.predict import MachineLearningModel
from annhub_python.model.prediction import HealthResponse, MachineLearningReponse
from fastapi.routing import APIRouter
from fastapi import HTTPException
from typing import List


class Router(APIRouter):
    """ Create API route for the model automatically.
    There are two API: predict & health checking for each model.
    
    Args:
        Because of being inherited from FastAPI module, this module
        can use some parameters provided by APIRouter.

        Ref: https://github.com/tiangolo/fastapi/blob/master/fastapi/routing.py#L436
    """

    def __init__(self, model_path, model_id, input_length, *args, **kwargs):
        self.model = MachineLearningModel(model_path, model_id, input_length)
        super(Router, self).__init__(tags=["predictor"], prefix="/v1", *args, **kwargs)
        self.setup()

    def setup(self):
        """ Generate predict API, which has determined model information: model path,
        model id, input length.

        Raises:
            HTTPException: Status code: 404. Raise when data input is empty.
            HTTPException: Status code: 406. Raise when data input is not satisfy input length.
            HTTPException: Status code: 400. Raise when model can not produce output.

        Returns:
            [MachineLearningResponse]: Customizable data output model. 
            At this time, a list of float.
        """
        @self.post(
            "/predict",
            response_model=MachineLearningReponse,
            name="predict:get-prediction"
        )
        async def predict(
            data_input: List[float] = None
        ) -> MachineLearningReponse:
            if not data_input:
                raise HTTPException(status_code=404, detail=f"'data_input' argument invalid!")

            try:
                prediction = self.model.predict(data_input)

            except InvalidInputException as e:
                raise HTTPException(status_code=406, detail=f"{e}")

            except PredictException as e:
                raise HTTPException(status_code=400, detail=f"{e}")

            return MachineLearningReponse(prediction=prediction)


        @self.get(
            "/health",
            response_model=HealthResponse,
            name="health:get-data"
        )
        async def health_check():
            """ Health checking API.
            Check whether the service is alive by produce an sample data input.

            Raises:
                HTTPException: Status code: 404.
                Raise when the model can not be used at this time.

            Returns:
                [HealthReponse]: Customizable health response.
                At this time, a simple boolean to verify if the model is working or not.
            """
            is_health = False
            try:
                input_sample = [0]*self.model._input_length
                self.model.predict(input_sample)
                is_health = True
                return HealthResponse(status=is_health)
            except Exception:
                raise HTTPException(status_code=404, detail="Unhealthy")