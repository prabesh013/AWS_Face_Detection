import boto3

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_ROOT = BASE_DIR / 'media'


def rekognition(filename):
    client = boto3.client('rekognition')

    with open(MEDIA_ROOT/filename, 'rb') as image:
        response = client.detect_faces(
            Image={
                'Bytes': image.read()
            },
            Attributes=["ALL"]
        )
    return response
