Oct 24 next steps:
 4. Model config & hyperparameters
   - Download a model from the TF2 detection model zoo (https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/2.2.0/training.html?utm_source=chatgpt.com#download-pre-trained-model)
   - edit pipeline config as necessary
   - might need additional editing of dataset

Oct 25 next steps part 2:
Next steps:
 5. Actually training the model
   - According to [official tensorflow documentation](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/2.2.0/training.html?utm_source=chatgpt.com#download-pre-trained-model) the actual training process should be pretty easy. One only needs to get the training script from [tensorflow's github](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/2.2.0/training.html) and run it.
   - Build a dockerfile to run the training
