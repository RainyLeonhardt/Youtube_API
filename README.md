# Youtube_API

![image](https://user-images.githubusercontent.com/55123523/225180845-09b3e178-0583-4b95-b3ba-0b215fcdf686.png)

`main.py`:

- `from Youtube_Downloader_API import create_web_app`: This line imports the `create_web_app` function from the `Youtube_Downloader_API` module. The `create_web_app` function is responsible for setting up and configuring the Flask application, including database connections, registering blueprints, and initializing any necessary resources.

- `app = create_web_app()`: This line calls the `create_web_app` function, which returns a fully configured Flask application instance. This instance is stored in the `app` variable.

- `app.run(host='0.0.0.0', port=8080)`: This line starts the Flask development server, running the web application on all available network interfaces (host='0.0.0.0') and listening on port 8080. By setting the host to '0.0.0.0', the application will be accessible not only on the localhost but also on the external IP address of the machine where it's running.

`home.html`:

This code is an HTML template for a Youtube Video Downloader web application. The template uses [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) for styling and layout.

- **DOCTYPE, html, head, and body tags**: These are standard HTML tags to define the document structure.
- **meta charset**: Specifies the character encoding for the HTML document.
- **link**: Imports the Bootstrap CSS from the CDN for styling the webpage.
- **title**: Sets the title of the webpage to "Youtube Video Downloader."
- **style**: Defines a custom CSS class `center` for centering the text.
- **div with class "center container"**: Creates a centered container for the form.
  - **form**: The form for users to input the Youtube URL and submit it for downloading. It uses the `POST` method to submit the data.
  - **h1**: A heading that welcomes users to the Youtube Video Downloader.
  - **div with form-group and input**: Contains an input field for users to paste the Youtube URL.
  - **button**: A submit button to start the download process.
- **div with class "container"**: A container for displaying the downloaded video information in a table.
  - **table**: A Bootstrap-styled table to display the video title, uploader, and view count.
  - **thead and tbody**: Define the header and body of the table, respectively.
  - **{% for video in videos %}**: A Jinja2 loop that iterates through the `videos` list and creates a table row for each video.
    - **td**: Table cells that display the video title, author, and view count.
  - **{% endfor %}**: Ends the Jinja2 loop.
- **script**: Imports the Bootstrap JavaScript bundle for any necessary interactive elements or features.

`models.py`:

This code defines a `Video` class that represents a video record in the database. The class is a subclass of `db.Model`, which is an SQLAlchemy ORM model.

- **Import necessary tools**: Import the `db` object from the current package.
- **Define the database object**: Define the `Video` class with its properties and methods.
  - **id**: A primary key column of type `Integer`. The database will automatically generate unique IDs for each record.
  - **views**: A column to store the number of views for the video as an integer.
  - **author**: A column to store the author/uploader of the video as a string with a maximum length of 255 characters.
  - **video_title**: A column to store the video title as a string with a maximum length of 255 characters.
  - **__init__**: The constructor method for the `Video` class. It takes `views`, `author`, and `video_title` as input parameters and assigns them to the respective class properties. The `id` property is not included in the constructor, as the database will automatically generate it.

`home.py`:

This code defines the `home` blueprint and the `download_youtube_video` function, which handles both GET and POST requests for the main page of the web application.

- **Import the necessary tools**: Import the required modules and objects, such as Flask, YouTube, the Video model, and the database.
- **Create the home blueprint**: Define a new blueprint called `home` for the main page of the web application.
- **download_youtube_video function**: Define the main function for handling GET and POST requests.
  - **GET request**: If the request method is GET, the function retrieves all video records from the database and renders the `home.html` template with the list of videos.
  - **POST request**: If the request method is POST, the function processes the submitted form.
    - Extract the video URL from the submitted form.
    - Create a new YouTube object using the extracted URL.
    - Get the video's view count, author, and title from the YouTube object.
    - Create a new Video object and add it to the database.
    - Download the video to the server using the highest resolution available.
    - Send the downloaded video as a file attachment to the client, allowing them to choose a storage path.

`__init__.py`:

This code sets up and configures a Flask web application, including the database connection, blueprint registration, and resource initialization.

- **Import the necessary tools**: Import the Flask and SQLAlchemy modules.
- **Create a new SQLAlchemy object**: Define a new SQLAlchemy object called `db` to handle database operations.
- **Define the database name**: Set a constant variable `YOUTUBE_DATABASE` to store the name of the database file.
- **create_web_app function**: Define the main function for creating and configuring the Flask application.
  - **Create a Flask object**: Instantiate a new Flask object called `app`.
  - **Set up the database connection**: Configure the database connection using the `YOUTUBE_DATABASE` constant and the `sqlite` URI.
  - **Initialize the database**: Call the `init_app` method on the `db` object to initialize the database with the Flask app.
  - **Register the blueprint**: Import the `home` blueprint and register it with the Flask app, specifying a URL prefix.
  - **Create the database**: Use a context manager to create all necessary tables in the database.
  - **Return the app object**: When the `create_web_app` function is called elsewhere, return the configured Flask app object to the caller.
