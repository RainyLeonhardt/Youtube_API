# Import necessary tools
from . import db

# Define the database object
class Video(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  views = db.Column(db.Integer)
  author = db.Column(db.String(255))
  video_title = db.Column(db.String(255))

  # Define the initial values for the Video object
  def __init__(self, views, author, video_title):
    # The database will automatically generate a new id, so we don't need to provide an initial value
    # self.views here refers to the 'views' on line 7
    # Use 'self.' to distinguish variables in this models file from the parameters in the __init__ method
    self.views = views  # 'views' is the parameter name on line 12
    self.author = author
    self.video_title = video_title
