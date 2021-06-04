import pandas as pd
import os
import json

my_path = 'test_data'
base_path = 'https:/dataset.vn/audios/test/'
positive_data = []
negative_data = []

def get_metadata(json_file):
    with open(json_file, 'r') as file:
        metadata = json.load(file)
    return metadata

def create_abs_path(path):
    return 


for element in os.listdir(my_path):
    files_path = os.listdir(my_path + '/' + element)
    metadata = get_metadata(my_path + '/' + element +  '/' + files_path[6])
    
    extend_metadata = {
        "id": element,
        "breathing-deep": base_path + my_path + '/' + element +  '/' + files_path[0],
        "breathing-shallow": base_path + my_path + '/' + element +  '/' + files_path[1],
        "cough-heavy": base_path + my_path + '/' + element +  '/' + files_path[2],
        "cough-shallow": base_path + my_path + '/' + element +  '/' + files_path[3],
        "counting-fast": base_path + my_path + '/' + element +  '/' + files_path[4],
        "counting-normal": base_path + my_path + '/' + element +  '/' + files_path[5],
        "vowel-a": base_path + my_path + '/' + element +  '/' + files_path[7],
        "vowel-e": base_path + my_path + '/' + element +  '/' + files_path[8],
        "vowel-o": base_path + my_path + '/' + element +  '/' + files_path[9]
    }
    metadata.update(extend_metadata)

    if metadata["test_status"] == 'p':
        metadata["test_status"] = 'POSITIVE'
        positive_data.append(metadata)
    elif metadata["test_status"] == 'n':
        metadata["test_status"] = 'NEGATIVE'
        negative_data.append(metadata)
    else: 
        metadata["covid_status"] = 'NOT-TESTED-YET'

with open(my_path + '_positive'+ '.json', 'w') as file:
    json.dump(positive_data, file)

with open(my_path + '_negative'+ '.json', 'w') as file:
    json.dump(negative_data, file)

df = pd.read_json(my_path + '_negative'+ '.json')
df.to_csv(my_path + '_negative'+ '.csv')

df = pd.read_json(my_path + '_positive'+ '.json')
df.to_csv(my_path + '_positive'+ '.csv')
