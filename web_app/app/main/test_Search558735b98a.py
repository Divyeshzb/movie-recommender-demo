import unittest
from unittest.mock import patch, MagicMock
from flask import session
from your_application import forms, Movie, current_user, render_template
from your_application.routes import search

class TestSearch558735b98a(unittest.TestCase):

    @patch.object(forms, 'SearchForm')
    @patch.object(session, 'get')
    @patch.object(Movie, 'find_movies')
    @patch.object(render_template, '__call__')
    def test_search_with_search_string(self, mock_render, mock_find_movies, mock_session_get, mock_form):
        mock_form.return_value.search_string.data = "test"
        mock_session_get.return_value = "test"
        mock_find_movies.return_value = ["Movie1", "Movie2"]
        search()
        mock_render.assert_called_with('/main/search_results.html', search_string="test", movies=["Movie1", "Movie2"])

    @patch.object(forms, 'SearchForm')
    @patch.object(session, 'get')
    @patch.object(Movie, 'find_movies')
    @patch.object(render_template, '__call__')
    def test_search_without_search_string(self, mock_render, mock_find_movies, mock_session_get, mock_form):
        mock_form.return_value.search_string.data = None
        mock_session_get.return_value = None
        mock_find_movies.return_value = []
        search()
        mock_render.assert_called_with('/main/search_results.html', search_string=None, movies=[])

if __name__ == '__main__':
    unittest.main()
