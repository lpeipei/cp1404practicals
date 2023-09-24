from flask import Flask, render_template, request, redirect, url_for, session
import wikipedia

app = Flask(__name__)
# Set the secret key. Keep this really secret:
app.secret_key = 'IT@JCUA0Zr98j/3yXa R~XHH!jmN]LWX/,?RT'


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        session['search_term'] = request.form['search']
        return redirect(url_for('results'))
    return render_template("search.html")


@app.route('/results')
def results():
    search_term = session['search_term']
    page = get_page(search_term)
    if page is None:
        return "No results found for the search term."
    else:
        return render_template("results.html", page=page)


def get_page(search_term):
    try:
        page = wikipedia.page(search_term)
    except wikipedia.exceptions.PageError:
        # no such page, return a random one
        page = wikipedia.page(wikipedia.random())
    except wikipedia.exceptions.DisambiguationError:
        # this is a disambiguation page, get the first real page (close enough)
        page_titles = wikipedia.search(search_term)
        # sometimes the next page has the same name (different caps), so don't try the same again
        if page_titles[1].lower() == page_titles[0].lower():
            title = page_titles[2]
        else:
            title = page_titles[1]
        page = get_page(wikipedia.page(title))
    return page


if __name__ == '__main__':
    app.run()
