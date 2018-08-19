import musicutil
from ..utils import error

from flask import (Blueprint, g, render_template, request, session, url_for,
                   abort, Response, jsonify, app, redirect)

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/search', methods=['POST', 'GET'])
def api_search():
    resp = redirect('/')

    if request.method == 'POST':
        json_data = request.get_json()
        src_name = json_data.get('source')
        query = json_data.get('query')
        max = json_data.get('max')
        html = json_data.get('html')

        try:
            g.music = musicutil.get_source(src_name)()
            if query:
                if not (max and str(max).isdigit() and 1 <= int(max) <= musicutil.MusicSource.chiasenhac_vn._MAX_SEARCH):
                    max = musicutil.MusicSource.chiasenhac_vn._MAX_SEARCH
                if html:
                    results = g.music.search(query.strip(), max, False)
                    results = {'data': render_template('search/search_items.html', results=results)}
                else:
                    results = g.music.search(query.strip(), max, True)
                resp = jsonify(results)
            else:
                resp = error.api_invalid('search',
                                      '"query" is required parameter')
        except KeyError:
            resp = error.source_not_found('download', src_name)

    return resp


@bp.route('/download', methods=['POST', 'GET'])
def api_download():
    resp = redirect('/')

    if request.method == 'POST':
        json_data = request.get_json()
        src_name = json_data['source'].strip()
        song_url = json_data['url'].strip()
        html = json_data.get('html')
        parent_id = json_data.get('parentId')

        try:
            g.music = musicutil.get_source(src_name)()
            if song_url:
                if html:
                    if parent_id:
                        d_data = g.music.download_details(song_url, False)
                        d_data = {'data': render_template('search/download_item.html', data=d_data, parentId=parent_id)}
                        resp = jsonify(d_data)
                    else:
                        resp = error.api_invalid('download', '"parentId" parameter is required')                        
                else:
                    d_data = g.music.download_details(song_url, True)
                    resp = jsonify(d_data)
            else:
                resp = error.api_invalid('download',
                                      '"url" parameter is required')
        except KeyError:
            resp = error.source_not_found('download', src_name)

    return resp


@bp.route('/song', methods=['POST', 'GET'])
def api_song_details():
    resp = redirect('/')

    if request.method == 'POST':
        json_data = request.get_json()
        src_name = json_data['source'].strip()
        song_url = json_data['url'].strip()
        html = json_data.get('html')

        try:
            g.music = musicutil.get_source(src_name)()
            if song_url:
                if html:
                    song_data = []
                    #Implement when html template is ready
                    # song_data = g.music.song_info(song_url, False)
                    # song_data = {'data': render_template('', data=song_data)}
                else:
                    song_data = g.music.song_info(song_url, True)
                resp = jsonify(song_data)
            else:
                resp = error.api_invalid('song', '"url" parameter is required')
        except KeyError:
            resp = error.api_invalid(
                    'song',
                    'Given music source [{}] not supported yet.'.format(
                        src_name))

    return resp


@bp.errorhandler(500)
def internal_error(err):
    return error.error('500', 'Internal Server Error', errorSource='Server', error="Some unhandled internal error occured.")