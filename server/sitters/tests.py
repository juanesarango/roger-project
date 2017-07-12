from collections import OrderedDict
import pandas as pd

from django.test import TestCase
from django.urls import reverse

from sitters.models import Review
from import_data import import_reviews_data
from bs4 import BeautifulSoup


class ModelsTestCase(TestCase):

    def test_models_in_bd_match_csv(self):
        start_row = 0
        end_row = 10

        # Populate database
        import_reviews_data(start_row, end_row)

        # Get data from database
        reviews = Review.objects.all()
        db_data = []
        for review in reviews:
            db_data.append(OrderedDict({
                'rating': review.rating,
                'sitter_image': review.sitter.image,
                'end_date': review.end_date.strftime("%Y-%m-%d"),
                'text': review.text,
                'owner_image': review.owner.image,
                'dogs': '|'.join([dog.name for dog in review.dogs.all()]),
                'sitter': review.sitter.name,
                'owner': review.owner.name,
                'start_date': review.start_date.strftime("%Y-%m-%d")
            }))
        db_dataframe = pd.DataFrame(db_data)

        # Get data from csv
        csv_dataframe = pd.read_csv('reviews.csv')[start_row:end_row]

        # Compare both dataframes
        self.assertIs(db_dataframe.equals(csv_dataframe), True)


class ViewTestCase(TestCase):

    def test_route_of_list(self):
        response = self.client.get('/')
        soup = BeautifulSoup(response.content, 'html.parser')
        list_dom = str(soup.find(id='filter-react-app'))
        self.assertEqual(list_dom, '<div id="filter-react-app"></div>')
