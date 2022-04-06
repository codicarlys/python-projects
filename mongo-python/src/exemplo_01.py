from http import client
from pymongo import MongoCLient

uri = 'mongodb://root:example@mongo:27017/'

client= MongoCLient(uri)
