import pickle
import os
import shutil


class File_Operation:
    """
    This class shall be used to save the model after training
    and load the saved model for prediction.
    """
    def __init__(self,file_object,logger_object):
        self.file_object = file_object
        self.logger_object = logger_object
        self.model_directory='models/'

    def save_model(self,model,filename):
        """
        Method Name: save_model
        Description: Save the model file to directory
        Outcome: File gets saved
        On Failure: Raise Exception
        """
        self.logger_object.log(self.file_object, 'Entered the save_model method of the File_Operation class')
        try:
            # Create the directory structure
            path = os.path.join(self.model_directory,filename)
            
            # Ensure the models directory exists
            if not os.path.exists(self.model_directory):
                os.makedirs(self.model_directory)
                
            # If path exists, remove it and its contents
            if os.path.isdir(path):
                shutil.rmtree(path)
            
            # Create new directory
            os.makedirs(path)

            # Save the model
            model_path = os.path.join(path, filename + '.sav')
            with open(model_path, 'wb') as f:
                pickle.dump(model, f, protocol=pickle.HIGHEST_PROTOCOL)

            self.logger_object.log(self.file_object,
                               'Model File '+filename+' saved. Exited the save_model method of the Model_Finder class')
            return 'success'
        except Exception as e:
            self.logger_object.log(self.file_object,
                               'Exception occured in save_model method of the Model_Finder class. Exception message:  ' + str(e))
            self.logger_object.log(self.file_object,
                               'Model File '+filename+' could not be saved. Exited the save_model method of the Model_Finder class')
            raise Exception()

    def load_model(self,filename):
        """
        Method Name: load_model
        Description: load the model file to memory
        Output: The Model file loaded in memory
        On Failure: Raise Exception
        """
        self.logger_object.log(self.file_object, 'Entered the load_model method of the File_Operation class')
        try:
            model_path = os.path.join(self.model_directory, filename, filename + '.sav')
            if not os.path.exists(model_path):
                raise Exception(f"Model file not found at {model_path}")
                
            with open(model_path, 'rb') as f:
                self.logger_object.log(self.file_object,
                                   'Model File ' + filename + ' loaded. Exited the load_model method of the Model_Finder class')
                return pickle.load(f)
        except Exception as e:
            self.logger_object.log(self.file_object,
                               'Exception occured in load_model method of the Model_Finder class. Exception message:  ' + str(e))
            self.logger_object.log(self.file_object,
                               'Model File ' + filename + ' could not be saved. Exited the load_model method of the Model_Finder class')
            raise Exception()

    def find_correct_model_file(self,cluster_number):
        """
        Method Name: find_correct_model_file
        Description: Select the correct model based on cluster number
        Output: The Model file
        On Failure: Raise Exception
        """
        self.logger_object.log(self.file_object, 'Entered the find_correct_model_file method of the File_Operation class')
        try:
            self.cluster_number = cluster_number
            self.folder_name = self.model_directory
            
            # Check if model directory exists
            if not os.path.exists(self.folder_name):
                raise Exception(f"Model directory {self.folder_name} not found")
                
            self.list_of_files = os.listdir(self.folder_name)
            for self.file in self.list_of_files:
                try:
                    if (self.file.index(str(self.cluster_number))!=-1):
                        self.model_name = self.file
                except:
                    continue
            self.model_name = self.model_name.split('.')[0]
            self.logger_object.log(self.file_object,
                               'Exited the find_correct_model_file method of the Model_Finder class.')
            return self.model_name
        except Exception as e:
            self.logger_object.log(self.file_object,
                               'Exception occured in find_correct_model_file method of the Model_Finder class. Exception message:  ' + str(e))
            self.logger_object.log(self.file_object,
                               'Exited the find_correct_model_file method of the Model_Finder class with Failure')
            raise Exception()