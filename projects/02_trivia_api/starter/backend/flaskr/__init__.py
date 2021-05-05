from flask import Flask, jsonify, request, abort
from flask_cors import CORS

from .models import setup_db, Category, Question

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, questions):
  page = request.args.get('page', 1, type=int)
  start =  (page - 1) * QUESTIONS_PER_PAGE
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

        if request.method == 'POST':
            data = request.json

            new_question = Question(answer=data['answer'], question=data['question'], difficulty=data['difficulty'], category=data['category'])
            print(new_question)
            new_question.insert()
            return jsonify({
                'success': True
            }), 204

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

    @app.route('/questions/<delete_id>', methods=['DELETE'])
    def delete_question(delete_id):
        try:
            Question.query.filter(Question.id == delete_id).delete()
            db.session.commit()
        except:
            db.session.rollback()
            abort(404)

        db.session.close()

        return jsonify({
            'success': True
        }), 204

    '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''

    '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''

    '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''

    '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
    @app.errorhandler(404)
    def unprocessable_entity(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        })

    return app
