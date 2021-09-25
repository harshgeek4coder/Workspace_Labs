import pyrebase

def get_my_db_configs():
    my_config = {
      "apiKey": "AIzaSyDhJxW7n-Q9A-lSIccllUIweKvprRBws-s",
      "authDomain": "mic-proj-golduck.firebaseapp.com",
      "databaseURL": "https://mic-proj-golduck-default-rtdb.firebaseio.com",
      "projectId": "mic-proj-golduck",
      "storageBucket": "mic-proj-golduck.appspot.com",
      "messagingSenderId": "395961098854",
      "appId": "1:395961098854:web:ec6f7d8797f10eff3dc3a7",
      "measurementId": "G-0TVLZMGSCN"
    };
    
    return my_config
    
    
get_config_details = get_my_db_configs()

admin_config = {
  
  "apiKey": "AIzaSyDhJxW7n-Q9A-lSIccllUIweKvprRBws-s",
  "authDomain": "mic-proj-golduck.firebaseapp.com",
  "databaseURL": "https://mic-proj-golduck-default-rtdb.firebaseio.com",
  "storageBucket" : "mic-proj-golduck.appspot.com",
  "serviceAccount": "configs\mic-proj-golduck-firebase-adminsdk-g8hyo-dfd98e2d68.json"
}

#firebase_admin = pyrebase.initialize_app(admin_config)
firebase_init = pyrebase.initialize_app(get_config_details)
#storage_admin = firebase_admin.storage()
storage = firebase_init.storage()


def write_logs_to_firedb_callbacks(data,workspace_name,experiment_name,track_key):
    firebase_init=pyrebase.initialize_app(get_config_details)
    logging_database = firebase_init.database()        
    
    logging_database.child(workspace_name).child(experiment_name).child(track_key).push(data)
    storage = firebase_init.storage()
    storage.child('./data.csv').put('data.csv')
    
               
    print("Pushed..")



