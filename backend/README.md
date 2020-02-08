# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## API REFERENCE

Getting starter

Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://localhost:5000; which is set as a proxy in frontend configuration.

## Error Handling
Errors are retourned as JSON objects in the following format:
{
    "success":False
    "error": 400
    "message":"Bad request
}

The API will return four error types when requests fail:
. 400: Bad request
. 500: Internal server error
. 422: Unprocessable
. 404: Not found

## Endpoints
. ## GET/categories

    GENERAL:
        This endpoints returns a list of category object, success value, total number of the categories. 
    
        
    SAMPLE: curl http://localhost:5000/categories

        {
        "categories": 
            {
                "1": "Science",
                "2": "Art",
                "3": "Geography",
                "4": "History",
                "5": "Entertainment",
                "6": "Sports"
            },
        "success": true
        }
. ## GET/questions

    GENERAL:
        This endpoint returns a list of the questions object, sucess value, total number of questions.

        Results are paginated in groups of 10. include a request argument to choose page number, starting from 1.

        SAMPLE: curl http://localhost:5000/questions

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
                "answer": "Maya Angelou",
                "category": 4,
                "difficulty": 2,
                "id": 5,
                "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
                },
                {
                "answer": "Muhammad Ali",
                "category": 4,
                "difficulty": 1,
                "id": 9,
                "question": "What boxer's original name is Cassius Clay?"
                },
                {
                "answer": "Apollo 13",
                "category": 5,
                "difficulty": 4,
                "id": 2,
                "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
                },
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
                },
                {
                "answer": "Brazil",
                "category": 6,
                "difficulty": 3,
                "id": 10,
                "question": "Which is the only team to play in every soccer World Cup tournament?"
                },
                {
                "answer": "Uruguay",
                "category": 6,
                "difficulty": 4,
                "id": 11,
                "question": "Which country won the first ever soccer World Cup in 1930?"
                },
                {
                "answer": "Lake Victoria",
                "category": 3,
                "difficulty": 2,
                "id": 13,
                "question": "What is the largest lake in Africa?"
                },
                {
                "answer": "The Palace of Versailles",
                "category": 3,
                "difficulty": 3,
                "id": 14,
                "question": "In which royal palace would you find the Hall of Mirrors?"
                },
                {
                "answer": "Agra",
                "category": 3,
                "difficulty": 2,
                "id": 15,
                "question": "The Taj Mahal is located in which Indian city?"
                }
            ],
            "success": true,
            "total_questions": 25
            }

. ## DELETE /questions(question_id)

    GENERAL:
        Delete the question of the given ID if it exists. Return the id of the deleted question, success value, total of questions and question list based on current page number to update the frontend

        Results are paginated in groups of 10. include a request argument to choose page number, starting from 1.

        SAMPLE: curl -X DELETE http://localhost:5000/questions/14?page=2

         "deleted": 14,
  "questions": [
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    },
    {
      "answer": "Jackson Pollock",
      "category": 2,
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    },
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    },
    {
      "answer": "Scarab",
      "category": 4,
      "difficulty": 4,
      "id": 23,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    },
    {
      "answer": "DZITRI",
      "category": 3,
      "difficulty": 3,
      "id": 28,
      "question": "Qui a fond\u00e9 la ville de Lom\u00e9 ?"
    },
    {
      "answer": "Coubadja KADER",
      "category": 6,
      "difficulty": 3,
      "id": 30,
      "question": "Quel est le joueur togolais \u00e0 avoir marqu\u00e9 dans une coupe du monde"
    },
    {
      "answer": "Hal Elrod",
      "category": 2,
      "difficulty": 3,
      "id": 31,
      "question": "Qui est l'auteur du livre MIRACLE MORNING"
    }
  ],
  "success": true,
  "total_questions": 24 }

. ## POST/questions

    GENERAL:    
    This endpoint is used to create a new question or to search for a question in relation to the terms contained in the question.
    When the searchTerm parameter is passed from the json, the endpoint performs the search. Otherwise, it is the creation of a new question.
    In the case of the creation of a new question:
    We return the ID of the new question created, the question that was created, the list of questions and the number of questions.

    SAMPLE.....For Search:
    curl -X POST http://localhost:5000/questions -H "Content-Type:application/json" -d "{"searchTerm":"title"}"

                {
        "questions": [
            {
            "answer": "Maya Angelou",
            "category": 4,
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
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
        "total_questions": 25
        }

    SAMPLE.....For create

    curl -X POST http://localhost:5000/questions -H "Content-Type:application/json" -d "{"question":"Who are you ?","answer":"My name is Badiou OURO-BANGNA","difficulty":1,"category":1}"

            {
        "created": 36,
        "created_question": "Who are you ?",
        "questions": [
            {
            "answer": "Apollo 13",
            "category": 5,
            "difficulty": 4,
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
            },
            {
            "answer": "Tom Cruise",
            "category": 5,
            "difficulty": 4,
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
            },
            {
            "answer": "Maya Angelou",
            "category": 4,
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
            },
            {
            "answer": "Edward Scissorhands",
            "category": 5,
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
            },
            {
            "answer": "Muhammad Ali",
            "category": 4,
            "difficulty": 1,
            "id": 9,
            "question": "What boxer's original name is Cassius Clay?"
            },
            {
            "answer": "Brazil",
            "category": 6,
            "difficulty": 3,
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
            },
            {
            "answer": "Uruguay",
            "category": 6,
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
            },
            {
            "answer": "Lake Victoria",
            "category": 3,
            "difficulty": 2,
            "id": 13,
            "question": "What is the largest lake in Africa?"
            },
            {
            "answer": "Agra",
            "category": 3,
            "difficulty": 2,
            "id": 15,
            "question": "The Taj Mahal is located in which Indian city?"
            },
            {
            "answer": "Escher",
            "category": 2,
            "difficulty": 1,
            "id": 16,
            "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
            }
        ],
        "success": true,
        "total_questions": 25
        }

. ## GET categories/id/questions

    GENERAL:    
        Returns the list of questions in the category equal to id. List of questions is paginated (10 per page),

        SAMPLE
        curl http://localhost:5000/categories/1/questions

                {
        "current_category": "Science",
        "questions": [
            {
            "answer": "The Liver",
            "category": 1,
            "difficulty": 4,
            "id": 20,
            "question": "What is the heaviest organ in the human body?"
            },
            {
            "answer": "Alexander Fleming",
            "category": 1,
            "difficulty": 3,
            "id": 21,
            "question": "Who discovered penicillin?"
            },
            {
            "answer": "Blood",
            "category": 1,
            "difficulty": 4,
            "id": 22,
            "question": "Hematology is a branch of medicine involving the study of what?"
            },
            {
            "answer": "My name is Badiou OURO-BANGNA",
            "category": 1,
            "difficulty": 1,
            "id": 36,
            "question": "Who are you ?"
            }
        ],
        "success": true,
        "total_questions": 25
        }

. ## POST /quizzes

    GENERAL: 
      This endpoint retrieves the list of questions in relation to the chosen category. This category is passed in the json. It then returns the questions one by one in a random fashion without choosing the same question more than once.   
        
        SAMPLE
        curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [20, 21],"quiz_category": {"type": "Science", "id": "1"}}'

                  {
            "question": {
              "answer": "My name is Badiou OURO-BANGNA",
              "category": 1,
              "difficulty": 1,
              "id": 36,
              "question": "Who are you ?"
            },
            "success": true
          }
## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```