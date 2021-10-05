import os
from typing import Optional
from fastapi import FastAPI
from loguru import logger
import logging
from fastapi.middleware.cors import CORSMiddleware
from annhub_python.routes import Router
from annhub_python.core.logging import InterceptHandler


class PyAnn(FastAPI):
    """Creates an application instance

    ** Possible parameters**
    Due to being inherited from FastAPI library. Almost all
    paramters are identical with FastAPI.

    Ref: https://github.com/tiangolo/fastapi
    """

    def __init__(self, *args, **kwargs):
        super(PyAnn, self).__init__(*args, **kwargs)
        self._model_path = None
        self._input_length = None
        self._model_id = None

    def set_model(self, model_path: str) -> None:
        """ Define an absolute path to your model.

        Args:
            model_path (str): [Absolute path to model]

        Raises:
            ValueError: Raised when the path is not provided.
            ValueError: Raised when the path is not an absolute path.
        """

        if not model_path:
            raise ValueError(
                "A model path must be provided."
            )

        elif os.path.exists(model_path):
            message = f"Machine learning model at {self._model_path} not exists!"
            raise FileNotFoundError(message)

        self._model_path = model_path

    def set_input_length(self, input_length: int) -> None:
        """ For each model, the input length must be defined before
        the data input is fed into model.

        Args:
            input_length (int): Input length of an array.

        Raises:
            ValueError: Raise when input length is not provided.
            ValueError: Raise when input length is not a positive number.
        """

        if not input_length:
            raise ValueError(
                "An input length must be provided."
            )
        elif input_length < 0:
            raise ValueError(
                "An input length must be a positive integer number."
            )
        self._input_length = int(input_length)

    def set_model_id(self, model_id: int) -> None:
        """ Model ID is used to specify which model architecture will be used.

        Args:
            model_id (int): Model ID, which was defined by ANSCENTER.
            For ex: Iris model is 5122020,...

        Raises:
            ValueError: Raise when model ID is not provided.
            ValueError: Raise when model ID is not a positive number.
        """
        if not model_id:
            raise ValueError(
                "Model ID must be provided."
            )
        elif model_id < 0:
            raise ValueError(
                "A model id must be a positive integer number."
            )
        self._model_id = int(model_id)

    def get_application(self):
        """ Prepare the main application. Taking responsibility for:
        1. Connect to API router (define api prefix, tags,...)
        2. Setup logging function (logging level, log rotation, retention policy, ...)
        """

        router = Router(self._model_path, self._model_id, self._input_length)
        self.include_router(router, prefix="/api")

        self.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        LOGGING_LEVEL = logging.DEBUG if self.debug else logging.INFO

        logging.basicConfig(
            handlers=[InterceptHandler(level=LOGGING_LEVEL)],
            level=LOGGING_LEVEL
        )

        logger.configure(
            handlers=[{
                        "sink": "logs/annhub-python.log",
                        "level": LOGGING_LEVEL,
                        "rotation": "5 MB"
                    }]
            )

        return self

    def run(
        self,
        host: str = "0.0.0.0",
        port: int = 8080,
        debug: Optional[bool] = None
     ) -> None:
        """ Run the application on a local development server

        Args:
            host (str, optional): [the hostname to listen on].
            Defaults to "0.0.0.0".

            port (int, optional): [the port of the web server].
            Defaults to 8080.

            debug (bool, optional): [if given, enable or disasble debug mode].
            Defaults to False.
        """
        if port:
            port = int(port)

        if debug is not None:
            self.debug = bool(debug)
        else:
            self.debug = False

        if self._model_path is None or self._input_length is None or self._model_id is None:
            raise ValueError(
                "Model path, Model ID, and input length must be provided."
                )

        app = self.get_application()

        import uvicorn

        uvicorn.run(app, host=host, port=port, debug=debug)
