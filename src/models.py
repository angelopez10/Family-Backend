from flask_sqlalchemy import SQLAlchemy
import random 

db = SQLAlchemy()

class Family:

    def __init__(self, last_name):
        self.last_name = last_name
        # example list of members
        self._members = [{
            "id": self._generateId(),
            "first_name": "John",
            "lastname": self.last_name
        }]

        # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return random.randint(0, 99999999) #import random 

    def add_member(self, member):
        
        member['id'] = self._generateId
        member['lastname'] = self.last_name
        self.member.append(member)
        return member

    def delete_member(self, id):

        self._members = list(filter(lambda member: member['id']!=id, self._members))
        return True

    def update_member(self, id, member):
        
        _member = self.get_member(id)
        _member.update(member)
        return _member

    def get_member(self, id):
        
        member = list(filter(lambda member: member['id']==id, self._members))
        return member[0]

    def get_all_members(self):
        return self._members