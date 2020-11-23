from Project2_Flask import app, forms
from flask import request, render_template
import string

@app.route('/', methods=['GET', 'POST'])
def search():
    searchForm = forms.ReviewSearch(request.form)
    if request.method == "POST":
        title = request.form["movie_title"]
        title = title.replace(" ", "+")
        order = request.form["order_by"]
        critic = request.form["critics"]
        search_results = forms.movie_search(title, order, critic)

        return render_template('results.html', result=search_results, title=title, order=order,
                               critic=critic, string=string, form=searchForm)
    return render_template('search.html', form=searchForm)
