#Create Student API using Python and Mongo DB (Student, Tutor, Course and timings)s

from werkzeug.wrappers import Request,Response
from flask import Flask, jsonify, request 
from pymongo import MongoClient
from bson.json_util import dumps



def stud():
    client = MongoClient('localhost',27017)
    db = client['studentpro']
    stud = db['stud']
    stud = stud.find()
    return dumps(stud)

def time():
    client = MongoClient('localhost',27017)
    db = client['studentpro']
    time  = db['time']
    time =  time.find()
    return dumps(time)

def tutor():
    client = MongoClient('localhost',27017)
    db = client['studentpro']
    tutor  = db['tutor']
    tutor = tutor .find()
    return dumps(tutor)

def course():
    client = MongoClient('localhost',27017)
    db = client['studentpro']
    course= db['course']
    course = course.find()
    return dumps(course)
