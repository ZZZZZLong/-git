import json

with open('./code/collections_data.json', 'r',encoding='utf-8') as f:
    collections_data = json.load(f)

for collection_id,collection_info in collections_data.items():
    print("="*20)
    print(f"Id:{collection_id}")
    print(collection_info.items())
    for key,value in collection_info.items():
        print(f"{key}: {value}")