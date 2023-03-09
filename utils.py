import requests

def voice_clone(api_url, name, sentance, voice_path1, voice_path2):
    data = {
        "your_name": name,
        "text": sentance,
    }
    multipart_form_data = {
        'audio1': ('audio1.wav', open(voice_path1, 'rb')),
        'audio2': ('audio2.wav', open(voice_path2, 'rb'))
    }

    response = requests.post(api_url + 'get_audio', files=dict(multipart_form_data), data=data)
    return response.content

def face_animator(api_url, name, image_path, voice_path):
    data = {
        "name": name,
    }

    multipart_form_data = {
        "image": ("image.jpg", open(image_path, 'rb')),
        "audio": ("audio.wav", open(voice_path, 'rb'))
    }

    response = requests.post(api_url + "generate_video", files=dict(multipart_form_data), data=data)
    return response.content
