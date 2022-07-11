from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps


from playsound import playsound
playsound("song.mp3", False)

def Temp():
	city = input('Температура в каком городе вас интересует?: ')

	owm = OWM('c6f6ff41de37ed426e602019ba594840')
	mgr = owm.weather_manager()

	observation = mgr.weather_at_place(city)
	w = observation.weather

	temperature = w.temperature('celsius')['temp']
	temperature_max = w.temperature('celsius')['temp_max']
	temperature_min = w.temperature('celsius')['temp_min']

	print('В городе ', city, ' сейчас температура: ', temperature,'C')
	print('Максимальная температура: ', temperature_max,'C')
	print('Минимальная температура: ', temperature_min,'C')
	print('На улицах сейчас: ', w.detailed_status)

Temp()


while True:
	answer_1 = input('Хотите узнать погоду в другом городе?: ')
	if answer_1 == 'Да' or answer_1 == 'да' or answer_1 == 'Yes' or answer_1 == 'yes':
		Temp()
	elif answer_1 == 'Нет' or answer_1 == 'нет' or answer_1 == 'No' or answer_1 == 'no':
		break
	else:
		print('Данный ответ мне не понятен, попробуйте: Да или Нет')

input('Press ENTER to exit')
