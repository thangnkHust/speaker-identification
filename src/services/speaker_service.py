from src.models import db, Todo
from flask import jsonify, abort, make_response
import os

def register_audio_speaker(name, upload_file):
    name = name.lower()
    file_name = upload_file.filename
    path_save = os.path.join('data/speaker_ident', name)

    if not os.path.exists(path_save):
	    os.makedirs(path_save)
    
    upload_file.save(os.path.join(path_save, file_name))

    return make_response({
        'name': name,
        'file_name': file_name
    })