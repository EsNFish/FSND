import json
import random

from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import psycopg2
from sqlalchemy.exc import DBAPIError

from .models import setup_db, Category, Question

QUESTIONS_PER_PAGE = 10


def paginate_questions(request, questions):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in questions]
    current_questions = questions[start:end]

    return current_questions


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    db = setup_db(app)

    # set up CORS
    CORS(app, resources={r"*": {"origins": "*"}})

    # set up access control allow
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE')
        return response

    @app.route('/categories', methods=['GET'])
    def get_categories():
        categories = Category.query.all()
        formatted_categories = {category.id: category.type for category in categories}
        return jsonify({
            'success': True,
            'categories': formatted_categories
        }), 200

    @app.route('/questions', methods=['POST', 'GET'])
    def get_questions():

        if request.method == 'GET':
            questions = Question.query.all()
            formatted_questions = paginate_questions(request, questions)
            categories = Category.query.all()
            formatted_categories = {category.id: category.type for category in categories}

            return jsonify({
                'success': True,
                'questions': formatted_questions,
                'total_questions': len(questions),
                'categories': formatted_categories
            }), 200

        if request.method == 'POST':
            data = request.json

            questions = Question.query.filter(
                func.lower(Question.question).contains(func.lower(data['searchTerm']))).all()

            return jsonify({
                'success': True,
                'questions': [question.format() for question in questions]
            }), 200

    @app.route('/questions/<delete_id>', methods=['DELETE'])
    def delete_question(delete_id):

        effected_lines = 0

        try:
            effected_lines = Question.query.filter(Question.id == delete_id).delete()
            db.session.commit()
        except DBAPIError:
            db.session.rollback()
            db.session.close()
            abort(422)

        if effected_lines == 0:
            db.session.rollback()
            db.session.close()
            abort(404)

        db.session.close()

        return jsonify({
            'success': True
        }), 204

    @app.route('/questions/question', methods=['POST'])
    def handle_question():
        data = request.json
        new_question = Question(answer=data['answer'], question=data['question'], difficulty=data['difficulty'],
                                category=data['category'])
        new_question.insert()
        return jsonify({
            'success': True
        }), 204

    @app.route('/categories/<category>/questions', methods=['GET'])
    def search_by_category(category):

        questions = Question.query.filter(Question.category == category).all()

        return jsonify({
            'success': True,
            'questions': [question.format() for question in questions]
        }), 200

    @app.route('/quizzes', methods=['POST'])
    def play_quiz():

        data = json.loads(request.data)
        previous_questions = data['previous_questions']
        quiz_category = data['quiz_category']

        if quiz_category['id'] == 0:
            questions = Question.query.all()
        else:
            questions = Question.query.filter(Question.category == quiz_category['id']).all()

        formatted_questions = [question.format() for question in questions]
        final_questions = [formatted_question for formatted_question in formatted_questions if
                           formatted_question['id'] not in previous_questions]

        if len(final_questions) == 0:
            return jsonify({
                'success': True
            })

        random_question_index = random.randint(0, len(final_questions) - 1)
        return jsonify({
            'success': True,
            'question': final_questions[random_question_index]
        })

    @app.errorhandler(404)
    def unprocessable_entity(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        })

    @app.errorhandler(422)
    def unprocessable_entity(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable Entity"
        })

    return app
