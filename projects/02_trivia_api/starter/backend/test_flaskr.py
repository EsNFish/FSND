import json
import unittest
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from flaskr.models import setup_db, Category


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
        actual_categories = [category['type'] for category in data['categories']]
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(actual_categories, expected_categories)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
