from flask import Flask
import flask
from flask import request
from pymongo import MongoClient
import pymongo
from flask_restful import Resource, Api
import os
import csv
from flask import Response
from datetime import datetime





# Instantiate the app
app = Flask(__name__)
api = Api(app)

#from docker-compose.yml
# client = MongoClient("brevets_mongodb", 27017)
# db = client.brevetsdb

HOSTNAME = "mongodb_host"
DATABASE_NAME = "brevets_db"
COLLECTION_NAME = "brevets"

client = MongoClient(host=HOSTNAME, port=27017)
db = client[DATABASE_NAME][COLLECTION_NAME]

#all values, in json by default
# class allL(Resource):
#     def get(self):

#         #checks the URL and grabs any top value user may have entered (i.e. top = 3)
#         top = request.args.get("top")

#         #if user didn't give us any top, then we are just going to display 20 values
#         #as stated in the default size from calc.html
#         if (top == None): top = 20

#         #grab the items the user inputed
#         #in the case the user submitted a top value, we want to be in ascending order
#         #as stated in the README when there are top values. So pymongo function
#         #ASCENDING will accomplish this
#         #limit the values by user entered top or by 20
#         _items = db.find().sort("openTime", pymongo.ASCENDING).limit(int(top))

#         #set up our list / unpack it some
#         items = [item for item in _items]

#        #collect open and close times from _items and our variables in new() from app.py
#         return {
#             'openTime': [item['openInfo'] for item in items],
#             'closeTime': [item['closeInfo'] for item in items]
#         }

class allL(Resource):
    def get(self):
        top = request.args.get("top", default=20, type=int)
        _items = db.find().limit(top)
        items = [item for item in _items]

        result = {
            'brevets': [
                {
                    'distance': item['distance'],
                    'begin_date': item['begin_date'],
                    'begin_time': item['begin_time'],
                    'controls': [
                        {
                            'km': control['km'],
                            'mi': control['mi'],
                            'location': control['location'],
                            'open': control['open'],
                            'close': control['close']
                        } for control in item.get('controls', [])
                    ]
                } for item in items
            ]
        }

        return result
    
   
class OpenOnly(Resource):
    def get(self):
        top = request.args.get("top", default=20, type=int)
        _items = db.find().limit(top)
        items = [item for item in _items]

        result = {
            'brevets': [
                {
                    'distance': item['distance'],
                    'begin_date': item['begin_date'],
                    'begin_time': item['begin_time'],
                    'controls': [
                        {
                            'km': control['km'],
                            'mi': control['mi'],
                            'location': control['location'],
                            'open': control['open'],
                        } for control in item.get('controls', [])
                    ]
                } for item in items
            ]
        }

        return result

    

class CloseOnly(Resource):
    def get(self):
        top = request.args.get("top", default=20, type=int)
        _items = db.find().limit(top)
        items = [item for item in _items]

        result = {
            'brevets': [
                {
                    'distance': item['distance'],
                    'begin_date': item['begin_date'],
                    'begin_time': item['begin_time'],
                    'controls': [
                        {
                            'km': control['km'],
                            'mi': control['mi'],
                            'location': control['location'],
                            'close': control['close'],
                        } for control in item.get('controls', [])
                    ]
                } for item in items
            ]
        }

        return result



class AllJSON(Resource):
    def get(self):
        top = request.args.get("top", default=20, type=int)
        _items = db.find().limit(top)
        items = [item for item in _items]

        result = {
            'brevets': [
                {
                    'distance': item.get('distance', 0),
                    'begin_date': item.get('begin_date', ''),
                    'begin_time': item.get('begin_time', ''),
                    'controls': [
                        {
                            'km': control.get('km', 0),
                            'mi': control.get('mi', 0),
                            'location': control.get('location', ''),
                            'open': control.get('open', ''),
                            'close': control.get('close', '')
                        } for control in item.get('controls', [])
                    ]
                } for item in items
            ]
        }

        return flask.jsonify(result)

class OpenOnlyJSON(Resource):
    def get(self):
        top = request.args.get("top", type=int)
        _items = db.find()
        items = [item for item in _items]

        # Flatten controls and extract open times
        all_open_times = [control.get('open') for item in items for control in item.get('controls', [])]

        # Sort all open times
        sorted_open_times = sorted(all_open_times)[:top] if top else all_open_times

        result = {
            'brevets': [
                {
                    'distance': item['distance'],
                    'begin_date': item['begin_date'],
                    'begin_time': item['begin_time'],
                    'controls': [
                        {
                            'km': control['km'],
                            'mi': control['mi'],
                            'location': control['location'],
                            'open': control['open'],
                        } for control in sorted(item.get('controls', []), key=lambda x: x.get('open', ''))
                        if top is None or control['open'] in sorted_open_times
                    ]
                } for item in items
            ]
        }

        return flask.jsonify(result)

class CloseOnlyJSON(Resource):
    def get(self):
        top = request.args.get("top", type=int)
        _items = db.find()
        items = [item for item in _items]

        # Flatten controls and extract close times
        all_close_times = [control.get('close') for item in items for control in item.get('controls', [])]

        # Sort all close times
        sorted_close_times = sorted(all_close_times)[:top] if top else all_close_times

        result = {
            'brevets': [
                {
                    'distance': item['distance'],
                    'begin_date': item['begin_date'],
                    'begin_time': item['begin_time'],
                    'controls': [
                        {
                            'km': control['km'],
                            'mi': control['mi'],
                            'location': control['location'],
                            'close': control['close'],
                        } for control in sorted(item.get('controls', []), key=lambda x: x.get('close', ''))
                        if top is None or control['close'] in sorted_close_times
                    ]
                } for item in items
            ]
        }

        return flask.jsonify(result)



class AllCSV(Resource):
    def get(self):
        top = request.args.get("top", default=20, type=int)
        _items = db.find().limit(top)
        items = [item for item in _items]

        # Create a CSV string
        csv_data = "brevets/distance,brevets/begin_date,brevets/begin_time,brevets/controls/0/km,brevets/controls/0/mi,brevets/controls/0/location,brevets/controls/0/open,brevets/controls/0/close\n"

        for item in items:
            distance = item.get('distance', 0)
            begin_date = item.get('begin_date', '')
            begin_time = item.get('begin_time', '')

            for i, control in enumerate(item.get('controls', [])[:top]):
                km = control.get('km', 0)
                mi = control.get('mi', 0)
                location = control.get('location', '')
                open_time = control.get('open', '')
                close_time = control.get('close', '')

                # Append row to CSV data
                csv_data += f"{distance},{begin_date},{begin_time},{km},{mi},{location},{open_time},{close_time}\n"

        # Create a CSV response
        response = Response(csv_data, content_type='text/csv')
        response.headers['Content-Disposition'] = 'attachment; filename=brevets_data.csv'

        return response

class OpenOnlyCSV(Resource):
    def get(self):
        top = request.args.get("top", type=int)
        _items = db.find()
        items = [item for item in _items]

        # Flatten controls and extract open times
        all_open_times = [control.get('open') for item in items for control in item.get('controls', [])]

        # Sort all open times
        sorted_open_times = sorted(all_open_times)[:top] if top else all_open_times

        # Create a CSV string for OpenOnly
        csv_data = "brevets/distance,brevets/begin_date,brevets/begin_time,brevets/controls/0/km,brevets/controls/0/mi,brevets/controls/0/location,brevets/controls/0/open\n" if top is None else "brevets/distance,brevets/begin_date,brevets/begin_time,brevets/controls/0/km,brevets/controls/0/mi,brevets/controls/0/location,brevets/controls/0/open\n"

        for item in items:
            distance = item.get('distance', 0)
            begin_date = item.get('begin_date', '')
            begin_time = item.get('begin_time', '')

            for control in sorted(item.get('controls', []), key=lambda x: x.get('open', '')):
                km = control.get('km', 0)
                mi = control.get('mi', 0)
                location = control.get('location', '')
                open_time = control.get('open', '')

                # Append row to CSV data if top is not specified or if the open time is in the sorted list
                if top is None or open_time in sorted_open_times:
                    if top is None:
                        csv_data += f"{distance},{begin_date},{begin_time},{km},{mi},{location},{open_time}\n"
                    else:
                        csv_data += f"{distance},{begin_date},{begin_time},{km},{mi},{location},{open_time}\n"

        response = Response(csv_data, content_type='text/csv')
        if top:
            response.headers['Content-Disposition'] = f'attachment; filename=top_{top}_open_times_data.csv'
        else:
            response.headers['Content-Disposition'] = 'attachment; filename=open_times_data.csv'

        return response
    

class CloseOnlyCSV(Resource):
    def get(self):
        top = request.args.get("top", type=int)
        _items = db.find()
        items = [item for item in _items]

        # Flatten controls and extract close times
        all_close_times = [control.get('close') for item in items for control in item.get('controls', [])]

        # Sort all close times
        sorted_close_times = sorted(all_close_times)[:top] if top else all_close_times

        # Create a CSV string for CloseOnly
        csv_data = "brevets/distance,brevets/begin_date,brevets/begin_time,brevets/controls/0/km,brevets/controls/0/mi,brevets/controls/0/location,brevets/controls/0/close\n" if top is None else "brevets/distance,brevets/begin_date,brevets/begin_time,brevets/controls/0/km,brevets/controls/0/mi,brevets/controls/0/location,brevets/controls/0/close\n"

        for item in items:
            distance = item.get('distance', 0)
            begin_date = item.get('begin_date', '')
            begin_time = item.get('begin_time', '')

            for control in sorted(item.get('controls', []), key=lambda x: x.get('close', '')):
                km = control.get('km', 0)
                mi = control.get('mi', 0)
                location = control.get('location', '')
                close_time = control.get('close', '')

                # Append row to CSV data if top is not specified or if the close time is in the sorted list
                if top is None or close_time in sorted_close_times:
                    if top is None:
                        csv_data += f"{distance},{begin_date},{begin_time},{km},{mi},{location},{close_time}\n"
                    else:
                        csv_data += f"{distance},{begin_date},{begin_time},{km},{mi},{location},{close_time}\n"

        response = Response(csv_data, content_type='text/csv')
        if top:
            response.headers['Content-Disposition'] = f'attachment; filename=top_{top}_close_times_data.csv'
        else:
            response.headers['Content-Disposition'] = 'attachment; filename=close_times_data.csv'

        return response
    



api.add_resource(allL, '/listAll')
api.add_resource(OpenOnly, '/listOpenOnly')
api.add_resource(CloseOnly, '/listCloseOnly')


api.add_resource(AllJSON, '/listAll/json')
api.add_resource(OpenOnlyJSON, '/listOpenOnly/json')
api.add_resource(CloseOnlyJSON, '/listCloseOnly/json')


api.add_resource(AllCSV, '/listAll/csv')
api.add_resource(OpenOnlyCSV, '/listOpenOnly/csv')
api.add_resource(CloseOnlyCSV, '/listCloseOnly/csv')





# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
