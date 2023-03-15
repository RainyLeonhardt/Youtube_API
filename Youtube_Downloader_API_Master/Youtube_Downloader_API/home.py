# Import the necessary tools
from flask import Blueprint, render_template, request, send_file
from pytube import YouTube
from .models import Video
from . import db

# Create the home blueprint
home = Blueprint('home', __name__)

# [] is a list data type, a list can store multiple data items
@home.route('/', methods=["GET", "POST"])
def download_youtube_video():
  # Accessing the page is a GET request
  # Submitting the form is a POST request
  if request.method == "POST":
    # Extract the URL input by the user on the front-end webpage
    video_url = request.form.get("downloadUrl")

    # Create a new YouTube object using the extracted URL
    youtube_video_object = YouTube(video_url)

    # Use the object's functions to get the video's view count, author, and title
    views = youtube_video_object.views
    author = youtube_video_object.author
    video_title = youtube_video_object.title

    # Write to the database
    new_video = Video(views, author, video_title)
    db.session.add(new_video)
    db.session.commit()

    # Download the video to the server
    get_video = youtube_video_object.streams.get_highest_resolution()

    # Let the client download and choose the storage path
    return send_file(get_video.download(), as_attachment=True)

  # If it's not a POST request, it's a GET request
  else:
    # Read from the database
    videos = Video.query.all()
    # Send the data retrieved from the database to the front-end for display
    return render_template("home.html", videos=videos)