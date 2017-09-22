import requests

url = 'http://api.wunderground.com/api/xx/conditions/q/canada/anjou.json'
result = requests.get(url)
condition_meteo = result.json()

print(condition_meteo['current_observation']['temp_c'])
print(condition_meteo['current_observation']['temp_f'])
print(condition_meteo['current_observation']['weather'])

result.close()