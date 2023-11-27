from pymongo import MongoClient

HOSTNAME = "mongodb_host"
DATABASE_NAME = "brevets_db"
COLLECTION_NAME = "brevets"

client = MongoClient(host=HOSTNAME, port=27017)
db = client[DATABASE_NAME][COLLECTION_NAME]


brevet_200 = {
    "distance": 200,
    "begin_date": "01/01/2024",
    "begin_time": "00:00",
    "controls": [
        {
            "km": 0,
            "mi": 0,
            "location": "Starting Point",
            "open": "01/01/2024 00:00",
            "close": "01/01/2024 01:00"
        },
        {
            "km": 100,
            "mi": 62.1,
            "location": None,
            "open": "01/01/2024 02:56",
            "close": "01/01/2024 06:40"
        },
        {
            "km": 150,
            "mi": 93.2,
            "location": "Second Checkpoint",
            "open": "01/01/2024 04:25",
            "close": "01/01/2024 10:00"
        },
        {
            "km": 200,
            "mi": 124.3,
            "location": "Last Checkpoint",
            "open": "01/01/2024 05:53",
            "close": "01/01/2024 13:30"
        }
    ]
}

brevet_1000 = {
    "distance": 1000,
    "begin_date": "01/01/2024",
    "begin_time": "00:00",
    "controls": [
        {
            "km": 0,
            "mi": 0,
            "location": "begin",
            "open": "01/01/2024 00:00",
            "close": "01/01/2024 01:00"
        },
        {
            "km": 1000,
            "mi": 621.4,
            "location": "finish line",
            "open": "01/01/2024 09:05",
            "close": "01/01/2024 03:00"
        }
    ]
}

db.insert_many([brevet_200, brevet_1000])
