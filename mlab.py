import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds143143.mlab.com:43143/20-11


host = "ds143143.mlab.com"
port = 43143
db_name = "20-11"
user_name = "admin"
password = "admin123"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
