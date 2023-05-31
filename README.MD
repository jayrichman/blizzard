#Blizzard Hearthstone Card Data Application
This is a simple Flask web application that retrieves and displays Hearthstone card data from the Blizzard API.

#Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

#Prerequisites
You'll need Python 3 installed on your machine. You can check your Python version using the following command:

```
python3 --version
```
#Setup
First, clone the repository to your local machine.

Next, navigate to the project directory and create a virtual environment with the following command:

```
python3 -m venv blizzard
```
Activate the virtual environment:

```
source blizzard/bin/activate
```
#Environment Variables
You need to set the following environment variables. Make sure to replace "your_client_id" and "your_client_secret" with your actual Client ID and Client Secret.

```
export CLIENT_ID="your_client_id"
export CLIENT_SECRET="your_client_secret"
```
Running the Application
To run the application, set the FLASK_APP environment variable and run the Flask server with the following commands:

```
export FLASK_APP=app.py
flask run
```
This will start a server running at http://localhost:5000.

Now you can navigate to this address in your web browser to see the application in action.