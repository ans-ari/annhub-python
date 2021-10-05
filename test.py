from annhub_python import PyAnn

pyann = PyAnn()

pyann.set_model("D:\HOC\ANSCENTER\\annhub_python\examples\iris\TrainedModel_c++.ann")

pyann.set_model_id(5122020)

pyann.set_input_length(4)

if __name__ == "__main__":
    pyann.run()