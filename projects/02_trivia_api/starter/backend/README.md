<h1>Backend</h1>

<h2>Postgresql Setup:</h2>

Make sure postgresql is installed on your machine. Instructions on how to do this can be found
here: https://www.postgresql.org/

Once installed you can use the `createdb -U test trivia` command to create the db and then `psql trivia < trivia.psql`
command to set up the tables and populate the tables with initial data for the app

By default, the application will default to the following setup for postgresql:

- <strong>Port:</strong> 5432
- <strong>User name:</strong> test
- <strong>User password:</strong> test

These values can be changed by modifying the variable database_path in the model.py file before starting the API

<h2>Starting the API</h2>

If you do not already have a Python environment created, execute the following:

1) `python3 -m venv /path/to/new/virtual/environment` (the path is where you want to save the config files for the new
   virtual environment)
2) `source <venv>/bin/activate` (venv is the path used in the previous step)
3) `pip install requirements.txt` (this file is located in the project directory)

More details can be found here: https://docs.python.org/3/library/venv.html

To start the api execute the following commands while in the backend directory:

1) `FLASK_APP=flaskr`
2) `FLASK_ENV=development`
3) `flask run`

The base path of the API is localhost:5000

To hit the API, you can use curl or any web browser

<h2>Endpoints</h2>

<h3>GET /categories</h3>

- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the
  category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs.

```json
{
  "1": "Science",
  "2": "Art",
  "3": "Geography",
  "4": "History",
  "5": "Entertainment",
  "6": "Sports"
}
```

<h3>GET /questions?page=${integer}</h3>

- Fetches a list of questions and list of categories 10 at a time
- Query Param: page (used to get the specified group of 10 questions)
- Returns: An object with the keys categories, questions, success, and total_questions</br>

```json
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "questions": [
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }
  ],
  "success": true,
  "total_questions": 13
}
```

<h3>POST /questions</h3>

- Fetches a list of questions containing the search term in the question
- Request Body:

```json 
{"searchTerm": "<seacrch term>"} 
```

- Returns: An object with the keys questions and success

```json
{
  "questions": [
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }
  ],
  "success": true
}
```

<h3>POST /questions</h3>

- Posts a new question to the database
- Request Body:

```json
{
  "question": "What is your favorite color?",
  "answer": "Yellow",
  "difficulty": 1,
  "category": "3"
}
```

- Returns: `204 NO CONTENT`

<h3>DELETE /questions/${delete_id}</h3>

- Deletes the question with the id that matches the path param delete_id
- Path param: delete_id - interger
- Returns: `204 NO CONTENT`

<h3>GET /categories/${category}/questions</h3>

- Returns a list of questions of the same category
- Path param: category - int
- Returns:

```json
{
  "questions": [
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    }
  ],
  "success": true
}
```

<h3>POST /quizzes</h3>

- Returns a random question for either all categories or one if specified.
- Request Body:

```json
{
  "previous_questions": [],
  "quiz_category": {
    "type": "Science",
    "id": "1"
  }
}
```

- Returns a question :

```json
{
  "question": {
    "answer": "CPU",
    "category": 1,
    "difficulty": 1,
    "id": 29,
    "question": "wat is brain of computer"
  },
  "success": true
}
```

<h2>Error Codes</h2>
<h3>404</h3>
Error Response:

```json
{
  "success": false,
  "error": 404,
  "message": "resource not found"
}
```

Thrown when:

- User attempts to delete an id that doesn't exist

<h3>422</h3>
Error Response:

```json
{
  "success": false,
  "error": 422,
  "message": "Unprocessable Entity"
}
```

Thrown when:

- The user attempts to delete a question with an id that is too large for an int. Example:
  100000000000000000000
- User sends post request to /questions with a improper body

<h2>Unit Tests</h2>

<h3>Setting up the test database</h3>
By default the unit tests use a database named trivia_test. It also uses a user named test with a password of test to
log into the database. These can be changed in the test_flaskr.py file if desired.

Notes:

- Make sure the database `triva_test` exists. If it does not, you can execute `createdb -U test trivia_test` to create
  the database
- The unit tests will create the tables and populate them with data as needed. No manual action is required of the user.

<h3>Executing the unit tests</h3>
To run the unit tests, execute: `python -m test_flaskr` from the project directory.

<h3>Unit test format</h3>
Each test conforms to the following:

1) Tests use the following naming
   convention: `test_<name of method being tested>__<any special cases>__<what is the expected outcome>`

    - an example test name is : `test_delete_question__id_to_delete_does_not_exist__should_get_404_error`
    - the special case is not necessary, it is mostly used to differentiate edge cases for the same method.
      Example: `test_delete_question__should_delete_question_with_id_passed_in`
2) Follows the structure of setup, exercise and assert

    - setup is where any test data is set up, utils have been provided to help set up the database
    - exercise is where the endpoint beting tested is called
    - assert is where any assertions are made about the results of the exercise
3) Each tests sets up it's own data in the database and clears it afterwards to keep tests consistent every run.

<h3>Resetting test database if something goes wrong</h3>

1) `dropdb -U test test_trivia`
2) `createdb -U test test_trivia`
3) `python -m test_flaskr`