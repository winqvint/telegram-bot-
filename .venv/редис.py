import redis
import json

red = redis.Redis(
                host = 'localhost',
                port = 6379,

)
dict1 = {'key1': 'value1', 'key2': 'value2'}
red.set('dict1', json.dumps(dict1)) # записываем в кеш строку "value1"
converted_dict = json.loads(red.get('dict1'))
print(type(converted_dict))
print(converted_dict)
red.delete('dict1')
print(red.get('dict1'))