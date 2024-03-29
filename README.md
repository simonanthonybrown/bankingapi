# Simon Brown Banking API

This is a simple baking API developed to allow a user to access account balance and make transfers between accounts. 

I used FastAPI as it's the framework I'm most familiar with when it comes to building APIs and I've had some experience using it in a passion project. 

For the data management side I knew that future development would likely use a remote relational database service, so I wanted to emulate a SQL-like environment for my local work. This led to me investigating SQLite and SQLAlchemy to handle the data needed for this project. I was able to successfully implement this and use it in both of the path operators I created.

It was a real challenge figuring out how to fit the pieces together and to write code that I knew would work if you simply changed out the SQLite details for the details of a cloud-native database, but I believe I have managed that. 

Future implementations would involve the inclusion of FastAPI's built in OAuth2 for authorizing users before they gain access to any of the API's features. It would also be good to get the time to add the ability to view previous transactions for an account.

The main next step would be to implement some integration testing using Starlette to mock HTTP requests and ensure that the API is returning the exptected responses from those requests.

# Running the API

## Account values to use in this example

This API uses a mocked database using SQLite. There are four mocked bank accounts and their details are listed below:

Account 1: 
Account num = 82041626, sort code = 927837, userid = 'KL9283', starting balance = 11500.23

Account 2:
Account num = 64736641, sort code = 560743, userid = 'SY6627', starting balance = 543.65

Account 3:
Account num = 70231442, sort code = 463782, userid = 'PK2873', starting balance = 8954.92

Account 4:
Account num = 44893061, sort code = 937478, userid = 'WE7112', starting balance = 34534.87

Please use these values while testing the functionality of the API.

## Option 1: Docker local

1. Navigate to the root of the project ./baking_api and use the included Dockerfile to build a docker image: `docker build -t <imagename> .`
2. Once the image is built, run it using: `docker run -d --name <containername> -p 8080:80 <imagename>`
3. Use a browser to navigate to http://127.0.0.0:8080/docs to access the FastAPI interactive docs
4. Test out the path operation functions!

## Option 2: Local environment

1. In the ./banking_api directory, create a virtual environment using: `python -m venv <nameofvenv>`
2. Activate the venv using: `.\<nameofvenv>\scripts\activate`
3. Install the required packages using: `pip install -r requirements.txt`
4. Run the uvicorn server with: `uvicorn app.main:app --host 0.0.0.0 --port 8080`
5. Leave that terminal open and running as it is now handling your uvicorn server
6. Use a browser to navigate to http://127.0.0.0:8080/docs to access the FastAPI interactive docs
7. Test out the path operation functions!
8. Don't forget to CTRL+C out of the Uvicorn terminal when you're done to stop the server running, and enter `deactivate` in your venv terminal to shut down the virtual environment