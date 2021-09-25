import random
import string
import csv
import pyrebase
from firebase_workers import get_config_details
def random_key_gen(x: int) -> str:
    return "".join(random.choice(string.ascii_letters) for _ in range(x))


def write2csv(headers_list):    
    with open('data.csv','w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=headers_list)
        csv_writer.writeheader()
        print("CSV Success..!")
        return 1
        

def get_headers_data(workspace_name,experiment_name,track_key):
    firebase_init=pyrebase.initialize_app(get_config_details)
    logging_database = firebase_init.database()

    ct=list(logging_database.child(workspace_name).child(experiment_name).child(track_key).get().pyres[0].item[1].keys())
    print("Headers : ",ct)
    make=dict({"data":ct})
    print(make)    
    
    with open('./static_data/data.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(make['data'])
    print("STATIC FILE DONE")
    
    return make
    
    
