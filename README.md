# Курс API веб-сервисов от dvmn.org 
# Урок 2. Посчитайте клики по ссылкам
`main.py` запрашивает у пользователя url. Если введеный url в формате коротких ссылок bit.ly, то выведется кол-во кликов по ссылке за всё время. В другом случае попытается сократить ссылку посредствои API bit.ly. Если сократить ссылку невозможно, будет выведен текст с ошибкой.
## Переменные окружения .env
`BITLY_ACCESS_TOKEN` - токен сервиса bit.ly
## Установка
1. Клоинруйте проект командой и перейдите в директорию проекта
 ```bash
git clone https://github.com/d3rr0m/dvmn_api_2.git
```
```bash
cd dvmn_api_2
```
2. Установите виртуальное окружение.
```bash
python -m venv venv
```
3. Активируйте только что созданное виртуальное окружение.
```bash
$ source venv/bin/activate
```
либо
```bash
venv\Scripts\activate.bat
```
4. Установите необходимые пакеты
```bash
pip install -r requirements.txt
```
## Запуск
```bash
python main.py
```
