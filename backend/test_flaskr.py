import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format('postgres','badiou','localhost:5432',self.database_name)
        setup_db(self.app, self.database_path)
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
        self.new_question={
            'question':'Who are you ?',
            'answer':'My name is Badiou OURO-BANG''NA',
            'difficulty':1,
            'category':1
        }
        
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_categories(self):
        res=self.client().get('/categories')
        data=json.loads(res.data) #ici on recupère la données provenant de la response
        self.assertEqual(res.status_code, 200) 
        self.assertEqual(data['success'],True)
        self.assertTrue(data['categories'])  
        self.assertTrue(len(data['categories']))
    

    def test_get_paginate_questions(self):
        res=self.client().get('/questions')
        data=json.loads(res.data) #get data from response
        self.assertEqual(res.status_code, 200) 
        self.assertEqual(data['success'],True)
        self.assertTrue(data['categories'])
        self.assertTrue(data['questions'])    
        self.assertTrue(len(data['questions']))
    
    def test_delete_questions(self):
        res=self.client().delete('/questions/1')
        data=json.loads(res.data)
        question=Question.query.filter(Question.id==1).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True) 
        self.assertEqual(data['deleted'],1)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))
        self.assertEqual(question,None)

    def test_search_question_without_results(self):
        res=self.client().post('/questions',json={'searchTerm':'appleJacks'})
        data=json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'],True) 
        self.assertEqual(data['total_questions'],0) 
        self.assertEqual(len(data['questions']),0)
    
    def test_search_with_result(self):
        res=self.client().post('/questions',json={'searchTerm':'title'})
        data=json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'],True) 
        self.assertEqual(data['total_questions'],2) 
        self.assertEqual(len(data['questions']),2) 

    def test_create_new_question(self):
        res=self.client().post('/questions',json=self.new_question)
        data=json.loads(res.data)
        self.assertEqual(res.status_code, 200) 
        self.assertTrue(data['success'],True) 
        self.assertTrue(data['created'])
        self.assertTrue(len(data['questions']))
    
    def test_404_send_requesting_beyond_the_value_page(self):
        res=self.client().get('/questions?page=1000')
        data=json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'],'Not found')

    def test_404_if_questions_does_not_exist(self):
        res=self.client().delete('/questions/1000')
        data=json.loads(res.data)
        self.assertEqual(res.status_code,404)
        self.assertEqual(data['success'],False)
    
    def test_quizzes_error(self):
        res = self.client().post('/quizzes', json={})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad request')
    
    def test_fail_400_questions_per_category(self):
        res=self.client().get('/categories/100/questions')
        data=json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'], 'Bad request')

    
    def test_quizzes(self):
        response = self.client().post('/quizzes',
                                      json={'previous_questions': [17, 18],
                                            'quiz_category': {'type': 'Art', 'id': '2'}})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])
        self.assertEqual(data['question']['category'], "2")
        self.assertNotEqual(data['question']['id'], 17)
        self.assertNotEqual(data['question']['id'], 18)

# # Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
			
			
			
			
			
			
			
			