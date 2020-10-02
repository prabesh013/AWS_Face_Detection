def clean(response):
    data = dict()
    # total = len(response['FaceDetails'])
    # data['total'] = total
    count = 0
    for face in response['FaceDetails']:
        people = dict()
        count = count + 1
        people['age'] = f"{face['AgeRange']['Low']}-{face['AgeRange']['High']}"
        people['gender'] = f"{face['Gender']['Value']}"
        people['emotionstate'] = f"{face['Emotions'][0]['Type']} with Confidence {face['Emotions'][0]['Confidence']}"
        people['sunglasses'] = f"{face['Sunglasses']['Value']}"
        people['beard'] = f"{face['Beard']['Value']}"
        data[str(count)] = people
    return data
