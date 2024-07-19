Note Posts App (built on Django)
A simple web app that lets you add notes and post it to the main screen.


**Setup: Clone the project and make sure you are under the main project directory NotePosts_API**

git clone https://github.com/jcode4/NotePosts_API.git


**Create a Virtual Environment: Navigate to the project directory and create a virtual environment (if not already done):**

virtualenv env --no-site-packages

source env/bin/activate  # On Windows, use `env\Scripts\activate`



**Install Dependencies: Install the project dependencies listed in requirements.txt:**

pip install -r requirements.txt



**Configure Settings: Update your project’s settings (e.g., database configuration, secret keys) in settings.py.**



**Apply Migrations: Apply any necessary database migrations:**

The below command will create all the migrations file (database migrations) required to run this App.
python manage.py makemigrations

Now, to apply this migrations run the following command
python manage.py migrate


**Start the server by following command**
python manage.py runserver

Once the server is up and running it should be hosted on http://127.0.0.1:8000/posts/
