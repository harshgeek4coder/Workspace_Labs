from statistics import mean
import csv
import tensorflow as tf
from tensorflow import keras
from .utils import random_key_gen,write2csv
from .firebase_workers import write_logs_to_firedb_callbacks





    
class BaseEpochTrack(keras.callbacks.Callback):
    def __init__(self,workspace_name,experiment_name,get_logs : bool = False):
        super(BaseEpochTrack,self).__init__()

        self.start_track_time = None
        self.stop_track_time = None
        self.get_logs = get_logs
        
        self.workspace_name = workspace_name 
        self.experiment_name = experiment_name
        
        self.refer_key = random_key_gen(5)
        
        self.track_time_list = []
        self.bool_list = []
        self.set_val = 0
        
        print("WorkSpace Created Successfully.!")
        print("Your Unique Tracking Key : {}".format(self.refer_key))
        
    def on_epoch_begin(self, epoch: int, logs: dict = None):
        keys = list(logs.keys())
        
        self.start_track_time = tf.timestamp()      
        
        

    def on_epoch_end(self, epoch: int, logs: dict = None):
        keys = list(logs.keys())
        
        self.stop_track_time = tf.timestamp()
        
        total_time = float(self.stop_track_time - self.start_track_time)
        
        self.track_time_list.append(total_time)
        
        
        data = logs
        
        data['epochs']=epoch + 1  
        data['time_stamp'] = total_time
        data['avg_time'] = round(mean(self.track_time_list),2)
        data['track_key'] = self.refer_key
        data['workspace_name'] = self.workspace_name
        data['experiment_name'] = self.experiment_name
        
        headers = list(data.keys())
        headers_list = sorted(headers)
        print(headers_list)
        
        
        if self.set_val == 0:
            print(self.set_val)
            self.set_val = write2csv(headers_list)
            print(self.set_val)
        else:
            pass    
        
        write_logs_to_firedb_callbacks(data,workspace_name=self.workspace_name,experiment_name=self.experiment_name,track_key=self.refer_key )
        
        if self.get_logs==True:
            print(data)
            
        self.track_time_list = []
        


class BaseTrainTrack(tf.keras.callbacks.Callback):
    def __init__(self,workspace_name,experiment_name,round_time: int = 2,get_logs: bool = False,
    ):
        super(BaseTrainTrack, self).__init__()
        
        self.start_time = None
        self.end_time = None
        
        self.workspace_name = workspace_name 
        self.experiment_name = experiment_name
        
        self.times = list()
        self.round_time = round_time
        self.print_logs = get_logs
        self.set_val = 0
        self.epochs_x = 0

        self.refer_key = random_key_gen(7)
        print(f"Use this ID to monitor training for this session: {self.refer_key}")

        

    def on_train_batch_begin(self, batch: int, logs: dict = None):

        self.start_time = tf.timestamp()

    def on_train_batch_end(self, batch: int, logs: dict = None):
        
        self.end_time = tf.timestamp()

        # Use Python built in functions to allow using in @tf.function see
        # https://github.com/tensorflow/tensorflow/issues/27491#issuecomment-890887810
        time = float(self.end_time - self.start_time)
        self.times.append(time)

        # Since we have similar logging code use the fact that if first argument of and is False Python doesn't
        # execute the second argument
        data = logs
        data["batch"] = batch + 1
        self.epochs_x +=1
        data["epochs"] = self.epochs_x 
        data["avg_time"] = round(mean(self.times), self.round_time)

        
        
        headers = list(data.keys())
        headers_list = sorted(headers)
        print(headers_list)
        
        if self.set_val == 0:
            print(self.set_val)
            self.set_val = write2csv(headers_list)
            print(self.set_val)
        else:
            pass    
        
        write_logs_to_firedb_callbacks(data,workspace_name=self.workspace_name,experiment_name=self.experiment_name,track_key=self.refer_key )
        

        data["time"] = self.times
        if self.print_logs:
            print(data)

        self.times = list()
