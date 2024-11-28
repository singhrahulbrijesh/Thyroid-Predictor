import pandas as pd
import pickle
from file_operations import file_methods
from data_preprocessing import preprocessing
from data_ingestion import data_loader_prediction
from application_logging import logger

class Prediction:

    def __init__(self):
        self.file_object = open("Prediction_Logs/Prediction_Log.txt", 'a+')
        self.log_writer = logger.App_Logger()

    def predictionFromModel(self):
        try:
            self.log_writer.log(self.file_object, 'Start of Prediction')
            data_getter = data_loader_prediction.Data_Getter_Pred(self.file_object, self.log_writer)
            data = data_getter.get_data()

            preprocessor = preprocessing.Preprocessor(self.file_object, self.log_writer)
            data = preprocessor.dropUnnecessaryColumns(data, ['TSH_measured', 'T3_measured', 'TT4_measured', 'T4U_measured', 'FTI_measured', 'TBG_measured', 'TBG', 'TSH'])

            # Replace '?' values with np.nan
            data = preprocessor.replaceInvalidValuesWithNull(data)

            # Get encoded values for categorical data
            data = preprocessor.encodeCategoricalValuesPrediction(data)

            # Check for null values
            if preprocessor.is_null_present(data):
                data = preprocessor.impute_missing_values(data)

            file_loader = file_methods.File_Operation(self.file_object, self.log_writer)
            kmeans = file_loader.load_model('KMeans')

            # Ensure data is a DataFrame with the same features used during training
            clusters = kmeans.predict(data)
            data['clusters'] = clusters

            result = []  # Initialize blank list for storing predictions
            with open('EncoderPickle/enc.pickle', 'rb') as file:
                encoder = pickle.load(file)

            for i in data['clusters'].unique():
                cluster_data = data[data['clusters'] == i].drop(['clusters'], axis=1)
                model_name = file_loader.find_correct_model_file(i)
                model = file_loader.load_model(model_name)
                predictions = model.predict(cluster_data)
                result.extend(encoder.inverse_transform(predictions))

            result_df = pd.DataFrame(result, columns=['Predictions'])
            result_df.to_csv("Prediction_Output_File/Predictions.csv", header=True)  # Save predictions
            self.log_writer.log(self.file_object, 'End of Prediction')

        except Exception as ex:
            self.log_writer.log(self.file_object, 'Error occurred while running the prediction!! Error:: %s' % ex)
            raise ex

        return "Prediction_Output_File/Predictions.csv"

if __name__ == "__main__":
    try:
        pred = Prediction()
        
        # Ensure directories exist
        import os
        os.makedirs("Prediction_Logs", exist_ok=True)
        os.makedirs("Prediction_Output_File", exist_ok=True)
        
        # Run prediction
        print("Starting prediction...")
        path = pred.predictionFromModel()
        print(f"Prediction completed. Results saved to: {path}")
        
        # Log contents
        with open("Prediction_Logs/Prediction_Log.txt", 'r') as f:
            print("\nLog contents:")
            print(f.read())
        
        # Check predictions
        predictions = pd.read_csv("Prediction_Output_File/Predictions.csv")
        print("\nPrediction Results Summary:")
        print(f"Number of predictions: {len(predictions)}")
        print("\nFirst few predictions:")
        print(predictions.head())
        print("\nValue counts:")
        print(predictions['Predictions'].value_counts())
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
            