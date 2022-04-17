from flask import Flask, request, jsonify, render_template
from mongo.connection import MongoDb
from mongo.vocabulary import Vocabulary
from tools.crawler import get_html, get_audios


def create_app():
    app = Flask(__name__)
    # set up configs
    app.config.from_pyfile('configs/development_config.py')

    mongo_client = MongoDb(
        host=app.config.get('MONGO_HOST'),
        port=app.config.get('MONGO_PORT'),
        username=app.config.get('MONGO_USERNAME'),
        password=app.config.get('MONGO_PASSWORD'),
        database='vocabulary'
    )

    @app.route('/')
    def index():
        return render_template("home.html")

    @app.route('/word', methods=['POST'])
    def save_word():
        db = Vocabulary(mongo_client.db, language='danish')
        db.insert_word(request.get_json())
        return jsonify({'success': 'ok'})

    @app.route('/word', methods=['GET'])
    def search_word():
        db = Vocabulary(mongo_client.db, language='danish')
        word = request.get_json()['word']
        results = db.find_word(word)
        return jsonify({'result': results})

    @app.route('/query/<word>', methods=['GET'])
    def search_and_save(word):
        db = Vocabulary(mongo_client.db, language='danish')
        db.insert_word({"word": word})
        url = f"https://ordnet.dk/ddo/ordbog?query={word}"
        return render_template("play_audio.html", url=url, word=word)

    return app


if __name__ == '__main__':
    create_app().run(
        host='0.0.0.0',
        port='20000'
    )
