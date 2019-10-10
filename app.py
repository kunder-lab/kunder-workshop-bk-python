from flask import Flask
from flask import request
from flaskext.mysql import MySQL
import requests
import os


app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = os.environ['MYSQL_DATABASE_USER']
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ['MYSQL_DATABASE_PASSWORD']
app.config['MYSQL_DATABASE_DB'] = os.environ['MYSQL_DATABASE_DB']
app.config['MYSQL_DATABASE_HOST'] = os.environ['MYSQL_DATABASE_HOST']
mysql.init_app(app)


base_url = 'http://demo7835208.mockable.io/'

'''
Status
'''
@app.route('/', methods=['GET'])
def home():
  ''' example connection 
  conn = mysql.connect()
  try:
    cursor = conn.cursor()
  finally:
    conn.close()
  '''
  return { 'msg': 'API OK' }

'''
get all series
TODO
filter by category
'''
@app.route('/series', methods=['GET'])
def get_series():
  resp = requests.get(base_url + 'series')
  return resp.text

'''
get series_id series information
TODO
read from service
'''
@app.route('/series/<series_id>', methods=['GET'])
def get_one_series(series_id):
  if series_id is None:
    return { 'msg': 'Serie' }
  else:
    return { 'msg': 'Serie: ' + series_id }

'''
save episode as watched
body: userId
TODO
connection to db
'''
@app.route('/series/<series_id>/episode/<episode_id>', methods=['POST'])
def save_watched_episode(series_id, episode_id):
  if series_id is None or episode_id is None:
    return { 'msg': 'Serie' }
  else:
    return { 'msg': 'Serie: ' + series_id + ' episode: ' + episode_id}
    

'''
delete episode as watched
body: userId
TODO
connection to db
'''
@app.route('/series/<series_id>/episode/<episode_id>', methods=['DELETE'])
def save_unwatched_episode(series_id, episode_id):
  if series_id is None or episode_id is None:
    return { 'msg': 'Serie' }
  else:
    return { 'msg': 'Serie: ' + series_id + ' episode: ' + episode_id}
