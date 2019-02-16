#importando bibioteca para datas
import datetime
currentDate = datetime.date.today()
userInput = input('Please birthday')
birthday = datetime.datetime.strptime(userInput, '%d/m/%Y').date()
print(userInput)
days = birthday - currentDate
print(days.days)