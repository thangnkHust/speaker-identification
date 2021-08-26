from flask_restful import Resource, reqparse
from flask import request
from src.services.speaker_service import register_audio_speaker

parser = reqparse.RequestParser()

class SpeakerRegisterList(Resource):
    def post(self):
        name = request.form.get('name')
        upload_file = request.files['file']

        return register_audio_speaker(name, upload_file)

class SpeakerRegister(Resource):
    def get(self):
        pass