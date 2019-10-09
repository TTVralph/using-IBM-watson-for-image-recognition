import io
import os
import sys
import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='jg27XMfTEyZ_TumtVhf70OloEZQmpI1o0hZbvjCLko2N')

url = 'https://vignette.wikia.nocookie.net/fortnite/images/3/3e/Kevin_the_cube.png/revision/latest?cb=20181221204823'
classes_result = visual_recognition.classify(url=url).get_result()
print(json.dumps(classes_result, indent=2))

input("Press ENTER to exit ;)")
