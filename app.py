from flask import Flask
from flask import request
import requests


app = Flask(__name__)

base_url = 'http://demo7835208.mockable.io/'

'''
Status
'''
@app.route('/', methods=['GET'])
def home():
  return { 'msg': 'API OK' }

'''
get all series
'''
@app.route('/series', methods=['GET'])
def get_series():
  resp = requests.get(base_url + 'series')
  return resp.text

'''
get series_id series information
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
'''
@app.route('/series/<series_id>/episode/<episode_id>', methods=['DELETE'])
def save_unwatched_episode(series_id, episode_id):
  if series_id is None or episode_id is None:
    return { 'msg': 'Serie' }
  else:
    return { 'msg': 'Serie: ' + series_id + ' episode: ' + episode_id}
