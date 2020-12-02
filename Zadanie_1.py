import json

"""Импортируем в словари значения из файлов .json при этом выполняем проверку входных данных. Если входной файл не импортирован, значит создаем файл error.json"""

values={}
params={}

error_text={
	"error": {
		"message": "Входные файлы некорректны"
		}
	}
try: 
    with open('values.json', 'r', encoding='utf-8') as fh: #открываем файл на чтение
        values = json.load(fh) #загружаем из файла данные в словарь values

except:
    if bool(values)==False:
        with open('error.json', 'w+') as fh: 
            json.dump(error_text, fh, ensure_ascii=False)

try:
    with open('TestcaseStructure2.json', 'r', encoding='utf-8') as fh: #открываем файл на чтение
        params = json.load(fh) #загружаем из файла данные в словарь params
    
except:
    if bool(params)==False:
        with open('error.json', 'w+') as fh:
            json.dump(error_text, fh, ensure_ascii=False)

"""Приводим импортированные данные в вид читаемого списка-словаря и проводим проверку значеий соответствия id.
 Если ID из Values, совпадает с ID из TestCaseStructure, то присваиваем новое значение Value"""


for txt in values['values']:
    for txt2 in params['params']:
        if txt['id'] == txt2['id']:
            txt2['value'] = txt['value']

"""Формируем новый файл StructureWithValues.json"""

with open('StructureWithValues.json', 'w+') as fh: 
        json.dump(params, fh, ensure_ascii=False)

exit()



# P.S. Я не смог разложить файл Testcasestructure в нормальный вид, в файле присутствуют лишние запятые, что приводит к ошибке. Для примера я создал файл TestcaseStructure2.json
# P.P.S Впервые работаю с ипортом JSON в Python, поэтому прошу прощения за подобный код, но я старался =)




