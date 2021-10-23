from annhub_python import PyAnn

pyann = PyAnn()

pyann.set_model(".\Customer_Churn_TrainedModel_c++.ann")

pyann.set_model_id(5122020)

pyann.set_input_length(30)

if __name__ == "__main__":
    pyann.run()