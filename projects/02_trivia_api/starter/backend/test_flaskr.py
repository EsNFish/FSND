import json
import unittest
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from flaskr.models import setup_db, Category, Question


def question_builder(question='What', answer='Why', category='random', difficulty=1):
    return {
        'question': question,
        'answer': answer,
        'category': category,
        'difficulty': difficulty
    }


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://test:test@{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.drop_all()
            self.db.create_all()

    def tearDown(self):
        # remove any data between tests
        with self.app.app_context():
            try:
                self.db.session.query(Category).delete()
                self.db.session.query(Question).delete()
                self.db.session.commit()
            except:
                self.db.session.rollback()

            self.db.session.close()
        pass

    def populate_categories(self, categories=None):
        # Set default if no categories are passed in
        if categories is None:
            categories = ['Video Games', 'Music', 'Anime']

        # Add categories to database
        for category in categories:
            self.db.session.add(Category(type=category))
        self.db.session.commit()
        pass

    def populate_questions(self, questions=None):
        if questions is None:
            questions = [
                question_builder(),
                question_builder()
            ]

        for question_data in questions:
            self.db.session.add(Question(question=question_data['question'], answer=question_data['answer'],
                                         category=question_data['category'], difficulty=question_data['difficulty']))
        self.db.session.commit()

        pass

    """
       Tests will follow the following format:
       
           setup: put any data needed into the database
           
           exercise: make the call
           
           assertion: make any assertions
    """

    def test_get_categories__returns_categories_from_database(self):
        with self.app.app_context():
            self.populate_categories()

        res = self.client().get('/categories')

        expected_categories = ['Video Games', 'Music', 'Anime']
        data = json.loads(res.data)
        actual_categories = [category_type for key, category_type in data['categories'].items()]
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(actual_categories, expected_categories)

    def test_get_questions__returns_questions_from_database(self):
        with self.app.app_context():
            self.populate_questions()
            self.populate_categories()

        res = self.client().get('/questions')

        expected_questions = [{'Why', 'random', 'What', 1}, {'Why', 'random', 'What', 1}]
        expected_num_questions = 2
        expected_categories = ['Video Games', 'Music', 'Anime']
        data = json.loads(res.data)
        actual_questions = [{question['question'], question['answer'], question['category'], question['difficulty']} for
                            question in data['questions']]
        actual_num_questions = data['total_questions']
        actual_categories = [category_type for key, category_type in data['categories'].items()]
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(actual_questions, expected_questions)
        self.assertEqual(actual_num_questions, expected_num_questions)
        self.assertEqual(actual_categories, expected_categories)

    def test_get_questions__paginates_to_10_questions(self):
        # create 12 questions
        questions = [
            question_builder(), question_builder(), question_builder(), question_builder(), question_builder(),
            question_builder(), question_builder(), question_builder(), question_builder(), question_builder(),
            question_builder(), question_builder()
        ]

        with self.app.app_context():
            self.populate_questions(questions)
            self.populate_categories()

        expected_num_questions = 10
        expected_total_questions = 12

        res = self.client().get('/questions')
        data = json.loads(res.data)

        actual_num_questions = len(data['questions'])
        actual_total_questions = data['total_questions']

        self.assertEqual(actual_num_questions, expected_num_questions)
        self.assertEqual(actual_total_questions, expected_total_questions)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
