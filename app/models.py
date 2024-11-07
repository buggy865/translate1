from django.db import models
from datetime import datetime

class Task(models.Model):
    def __init__(self, name, description, time_required, create_time=None):
        self.name = name 
        self.description = description 
        self.time_required = time_required
        self.create_time = create_time if create_time else datetime.now() 

    def __repr__(self):
        return f"Task(name='{self.name}', description='{self.description}', time_required='{self.time_required}', create_time='{self.create_time}')"

