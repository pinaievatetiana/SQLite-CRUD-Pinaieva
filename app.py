from flask import Flask, render_template, request, redirect, url_for
import database_connector

app = Flask(__name__)

database_connector.create_db_table()

@app.route('/')
def index():
    movies = database_connector.get_all_items()
    return render_template('index.html', movies=movies)

@app.route('/add', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        movie_data = {
            'title': request.form['title'],
            'genre': request.form['genre'],
            'release_year': request.form.get('release_year'),
            'director': request.form.get('director'),
            'rating': request.form.get('rating')
        }
        database_connector.insert_item(movie_data)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_movie(id):
    if request.method == 'POST':
        movie_data = {
            'title': request.form['title'],
            'genre': request.form['genre'],
            'release_year': request.form.get('release_year'),
            'director': request.form.get('director'),
            'rating': request.form.get('rating')
        }
        database_connector.update_item(id, movie_data)
        return redirect(url_for('index'))
    
    movie = database_connector.get_item_by_id(id)
    return render_template('edit.html', movie=movie)

@app.route('/delete/<int:id>')
def delete_movie(id):
    database_connector.delete_item(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)