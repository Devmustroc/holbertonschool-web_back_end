#!/usr/bin/python3
""" 8. List all documents in Python """

from pymongo import MongoClient


def list_all(mongo_collection):
    """ lists all documents in a collection """
    documents = []
    for document in mongo_collection.find():
        documents.append(document)
    return documents
