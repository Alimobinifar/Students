from operator import mod
from model import *


def show_studens():
    students = show_all()
    return students


def inset_student(name,family,phone,address):
    create_student(name,family,phone,address)
    if create_student :
        return True

def remove_student(id):
    delete_student(id)


def update_student_controller(id,name,family,phone,address):
    update_student(id,name,family,phone,address)