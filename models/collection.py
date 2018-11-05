from mongoengine import StringField,Document

class User(Document):
    acccountname = StringField()
    username = StringField()
    password = StringField()
    image = StringField()
class Present(Document):
    reciverid = StringField()
    sendername = StringField()
    image = StringField()
    wishing = StringField()
