import pyrebase
import csv
from utils import get_headers_data
import os
from os.path import exists





def check_file_static():
    path_csv='./static_data/data.csv'
    file_exists = exists(path_csv)
    if file_exists:
        print('FILE EXISTS....')
        #os.remove(path_csv)

    else:
        static_folder_path ='./static_data'
        if os.path.isdir(static_folder_path):
            pass
        else:
            os.mkdir('./static_data')
        print("NOPE, NO CSV")
        pass



print("Hello")

class MyStuffTracker(object):
    """Tracks changes of my stuff in Firebase"""
    _db = pyrebase.initialize_app({
      "apiKey": "AIzaSyDhJxW7n-Q9A-lSIccllUIweKvprRBws-s",
      "authDomain": "mic-proj-golduck.firebaseapp.com",
      "databaseURL": "https://mic-proj-golduck-default-rtdb.firebaseio.com",
      "projectId": "mic-proj-golduck",
      "storageBucket": "mic-proj-golduck.appspot.com",
      "messagingSenderId": "395961098854",
      "appId": "1:395961098854:web:ec6f7d8797f10eff3dc3a7",
      "measurementId": "G-0TVLZMGSCN"

    }).database()

    my_stuff: dict = None  # In my example my data is a list of some dictionaries
    

    @property
    def is_ready(self) -> bool:
        """
        Returns:
            bool: True if my stuff is ready for use
        """
        return self.my_stuff is not None

    def stream_handler(self, message):
        print("Got some update from the Firebase")
        # We only care if something changed

        if message["event"] in ("put", "patch"):
            print("Something changed")
            if message["path"] == "/":
                print("Seems like a fresh data or everything have changed, just grab it!")
                self.my_stuff: dict = message["data"]


            else:
                print("Something updated somewhere, I dont't care I just want the latest snapshot of my stuff")
                # Just get whole-data of my stuff and list (second) item of the pyres (that I expect to be a dict)
                self.my_stuff: dict = list(it.item[1] for it in self._db.child(self.workspace_name).child(self.experiment_name).child(self.track_key).get().pyres)

                ct=list(self._db.child(self.workspace_name).child(self.experiment_name).child(self.track_key).get().pyres[0].item[1].keys())
                for i in ct:
                    print("{} : ".format(i),self.my_stuff[-1][i])
                    if self.my_stuff[-1]['epochs']==1:
                        get_headers_data(workspace_name=self.workspace_name,experiment_name=self.experiment_name,track_key=self.track_key)
                        print("Done CSV")
                    else:
                        pass
                    

                with open('./static_data/data.csv','a') as csv_file:  
                    csv_writer = csv.DictWriter(csv_file, fieldnames=ct)              
                    info = self.my_stuff[-1] 
                    csv_writer.writerow(info)
                    print(info)

    def __init__(self,workspace_name,experiment_name,track_key) -> None:
        """Start tracking my stuff changes in Firebase"""
        super().__init__()
        self.workspace_name = workspace_name
        self.experiment_name = experiment_name
        self.track_key = track_key
        self._db.child(self.workspace_name).child(self.experiment_name).child(self.track_key).stream(self.stream_handler)



