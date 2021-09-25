
import pyrebase
from .firebase_workers import get_config_details
from .custom_callbacks import BaseEpochTrack,BaseTrainTrack

class Workspace_Lab():
    def __init__(self):
        super(Workspace_Lab, self).__init__()
        
        self.firebase_init = pyrebase.initialize_app(get_config_details)
        self.logging_database = self.firebase_init.database()
        self.workspace_name = None 
        self.experiment_name = None  
        self.callbacks_type = None 
        
        
    def create_Workspace(self,workspace_name):
        self.workspace_name = workspace_name
        print("Workspace Name : ",workspace_name)
        print("Workspace Created..!")
        
        return workspace_name
        
    def create_experiment(self,experiment_name):
        self.experiment_name = experiment_name
        print("Workspace Name : ",self.workspace_name)
        print("Experiment Name : ",self.experiment_name)        
        return experiment_name
    
    def set_callbacks(self,callbacks_type):
        self.callbacks_type = callbacks_type
        if self.callbacks_type == 'Base_Epochs':
            callback_obj =  BaseEpochTrack(workspace_name=self.workspace_name,experiment_name=self.experiment_name,get_logs=True)
        elif self.callbacks_type == 'Base_Batches':
            callback_obj =  BaseTrainTrack(workspace_name=self.workspace_name,experiment_name=self.experiment_name,get_logs=True)
            
        return callback_obj