import requests

params = {'amount': 10,
          'type': 'boolean',
}

response = requests.get(url='https://opentdb.com/api.php', params=params).json()

question_data = response['results']
