from Project2_Flask import main_functions
import requests
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SelectField


class ReviewSearch(FlaskForm):
    movie_title = StringField("NYT Review Search")
    order_by = SelectField("Order by",
                           choices=[('by-opening-date', 'By Opening Date'),
                                    ('by-publication-date', 'By Publication Date'),
                                    ('by-title', "By Title")])

    critics = RadioField("Filter by Critics Picks?",
                         choices=[('Y', 'Filter by Picks'),
                                  ('', 'No Filter')])


def movie_search(title, order, critic):
    api_key_dict = main_functions.read_from_file("Project2_Flask/JSON_Files/api_keys.json")
    api_key = api_key_dict["my_key"]

    url = "https://api.nytimes.com/svc/movies/v2/reviews/search.json?query=" + title + "&" + "critics-pick=" + critic + "&" + "order=" + order + ";" + "&api-key=" + api_key

    response = requests.get(url).json()
    "https://api.nytimes.com/svc/movies/v2/reviews/search.json?query=godfather&api-key=yourkey"
    main_functions.save_to_file(response, "Project2_Flask/JSON_Files/reviews.json")

    my_articles = main_functions.read_from_file("Project2_Flask/JSON_Files/reviews.json")
    print(url)
    return my_articles
