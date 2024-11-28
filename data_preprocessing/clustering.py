import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from kneed import KneeLocator
from file_operations import file_methods
import numpy as np

class KMeansClustering:
    def __init__(self, file_object, logger_object):
        self.file_object = file_object
        self.logger_object = logger_object

    def elbow_plot(self,data):
        self.logger_object.log(self.file_object, 'Entered the elbow_plot method of the KMeansClustering class')
        wcss=[]
        try:
            # Convert DataFrame to numpy array if it's a DataFrame
            X = data.values if hasattr(data, 'values') else data
            
            for i in range(1,11):
                kmeans = KMeans(n_clusters=i, 
                              init='k-means++',
                              random_state=42,
                              n_init=10)  # Added n_init parameter
                kmeans.fit(X)
                wcss.append(kmeans.inertia_)
            
            plt.plot(range(1,11),wcss)
            plt.title('The Elbow Method')
            plt.xlabel('Number of clusters')
            plt.ylabel('WCSS')
            plt.savefig('preprocessing_data/K-Means_Elbow.PNG')
            
            self.kn = KneeLocator(range(1, 11), wcss, curve='convex', direction='decreasing')
            self.logger_object.log(self.file_object, 'The optimum number of clusters is: '+str(self.kn.knee))
            return self.kn.knee

        except Exception as e:
            self.logger_object.log(self.file_object,'Exception in elbow_plot: ' + str(e))
            raise Exception()

    def create_clusters(self,data,number_of_clusters):
        self.logger_object.log(self.file_object, 'Entered the create_clusters method')
        try:
            # Convert DataFrame to numpy array if it's a DataFrame
            X = data.values if hasattr(data, 'values') else data
            
            self.kmeans = KMeans(n_clusters=number_of_clusters, 
                                init='k-means++',
                                random_state=42,
                                n_init=10)  # Added n_init parameter
            
            self.y_kmeans = self.kmeans.fit_predict(X)

            self.file_op = file_methods.File_Operation(self.file_object,self.logger_object)
            self.save_model = self.file_op.save_model(self.kmeans, 'KMeans')

            if hasattr(data, 'copy'):
                self.data = data.copy()
                self.data['Cluster'] = self.y_kmeans
            else:
                self.data = np.column_stack((data, self.y_kmeans))
                
            self.logger_object.log(self.file_object, f'Successfully created {number_of_clusters} clusters')
            return self.data
            
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception in create_clusters: ' + str(e))
            raise Exception()