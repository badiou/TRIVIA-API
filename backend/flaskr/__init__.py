#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


############################################################################################################
#
#                                         FUNCTION FOR QUESTIONS PAGINATION (10 PER PAGE)
#
###########################################################################################################

def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    questions = [question.format() for question in selection]
    current_questions = questions[start:end]
    return current_questions


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)

############################################################################################################
#
#                                         SET CORS TO ALLOW ALL ORIGIN
#
###########################################################################################################

    CORS(app, resources={r"/api/*": {'origins': '*'}})

############################################################################################################
#
#                                        DECORATOR after_request
#
###########################################################################################################

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS')
        return response

############################################################################################################
#
#                                        GET ALL CATEGORIES
#
###########################################################################################################

    @app.route('/categories')
    def get_all_categories():
        categories = Category.query.all()
        categories_object = {}
        for category in categories:
            categories_object[category.id] = category.type
        if len(categories_object) == 0:
            abort(404)
        return jsonify({'success': True,
                       'categories': categories_object})

############################################################################################################
#
#                                         GET ALL QUESTIONS AND PAGINATION (10 PER PAGE)
#
###########################################################################################################

    @app.route('/questions', methods=['GET'])
    def get_questions():
        selection = Question.query.all()
        total_questions = len(selection)
        current_questions = paginate_questions(request, selection)
        categories = Category.query.all()
        categories_object = {}
        for category in categories:
            categories_object[category.id] = category.type
        if len(current_questions) == 0:
            abort(404)
        return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': total_questions,
            'categories': categories_object,
            })

############################################################################################################
#
#                                       DELETE ONE QUESTION BY ID
#
###########################################################################################################

    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        question = Question.query.filter(Question.id
                == question_id).one_or_none()
        if question is None:
            abort(404)
        try:
            question.delete()
            selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, selection)
            return jsonify({
                'success': True,
                'deleted': question_id,
                'questions': current_questions,
                'total_questions': len(Question.query.all()),
                })
        except:
            abort(422)

############################################################################################################
#
#                                         SEARCH OR CREATE NEW QUESTIONS
#
###########################################################################################################

    @app.route('/questions', methods=['POST'])
    def create_question():
        body = request.get_json()
        if body.get('searchTerm'):
            search = body.get('searchTerm')
            selection = \
                Question.query.order_by(Question.id).filter(Question.question.ilike('%{}%'.format(search))).all()
            if len(selection) == 0:
                abort(404)
            paginated = paginate_questions(request, selection)
            return jsonify({'success': True, 'questions': paginated,
                           'total_questions': len(Question.query.all())})
        else:
            new_question = body.get('question')
            new_answer = body.get('answer')
            new_difficulty = body.get('difficulty')
            new_category = body.get('category')
            if new_question is None or new_answer is None \
                or new_difficulty is None or new_category is None:
                abort(422)
            try:
                question = Question(question=new_question,
                                    answer=new_answer,
                                    difficulty=new_difficulty,
                                    category=new_category)
                question.insert()
                selection = Question.query.order_by(Question.id).all()
                current_questions = paginate_questions(request,
                        selection)
                return jsonify({
                    'success': True,
                    'created': question.id,
                    'created_question': question.question,
                    'questions': current_questions,
                    'total_questions': len(Question.query.all()),
                    })
            except:
                abort(422)

############################################################################################################
#
#                                       GET QUESTION BY CATEGORY
#
###########################################################################################################

    @app.route('/categories/<int:category_id>/questions')
    def get_question_by_category(category_id):
        category = Category.query.filter(Category.id
                == category_id).one_or_none()
        if category is None:
            abort(400)
        selection = Question.query.filter_by(category=category.id).all()
        paginated = paginate_questions(request, selection)
        return jsonify({
            'success': True,
            'questions': paginated,
            'total_questions': len(Question.query.all()),
            'current_category': category.type,
            })

############################################################################################################
#
#                                                  PLAY THE QUIZ
#
#
###########################################################################################################

    @app.route('/quizzes', methods=['POST'])
    def play_quizzes():

    # get data from json

        body = request.get_json()
        previous_questions = body.get('previous_questions')
        category = body.get('quiz_category')

        if category is None or previous_questions is None:
            abort(400)
        if category['id'] == 0:  # if the user select all get all questions
            questions = Question.query.all()
        else:

      # if the user select other element in the list get questions for this category

            questions = Question.query.filter_by(category=category['id'
                    ]).all()
        total_questions = len(questions)

        def random_question():
            return random.choice(questions)

      # random.choice helps to select random element in the list

        def verify_if_question_is_used(question):
            isUsed = False
            for q in previous_questions:
                if q == question.id:
                    isUsed = True
            return isUsed

        question = random_question()

        while verify_if_question_is_used(question):

      # Here i have choose a new question. I need to choose question and test if the question is the previous question or not.
      # If the question is on list of previous question, i will choose on the list another question.

            question = random_question()

            if len(previous_questions) == total_questions:
                return jsonify({'success': True})

    # return the question

        return jsonify({'success': True, 'question': question.format()})

############################################################################################################
#
#                                        HANDLER FOR ERROR
#
###########################################################################################################

    @app.errorhandler(404)
    def not_found(error):
        return (jsonify({'success': False, 'error': 404,
                'message': 'Not found'}), 404)

    @app.errorhandler(422)
    def unprocessable(error):
        return (jsonify({'success': False, 'error': 422,
                'message': 'unprocessable'}), 422)

    @app.errorhandler(400)
    def error_client(error):
        return (jsonify({'success': False, 'error': 400,
                'message': 'Bad request'}), 400)

    @app.errorhandler(500)
    def server_error(error):
        return (jsonify({'success': False, 'error': 500,
                'message': 'internal server error'}), 500)

    return app



			