### Общее для запусков и редактирования:
- в ./data/user_data.py вписать секрет в 'secret' (заменить "*" секретом)
- установить зависимости pip install -r requirements.txt
### Для локального запуска через соленоид
- установить [docker](https://docs.docker.com/engine/install/) и [docker compose](https://docs.docker.com/compose/install/)
- закомментировать в conftest.py
```
browser = webdriver.Chrome(options=options)
```
- раскоментировать в conftest.py
```
browser = webdriver.Remote(
    command_executor="http://selenoid:4444/wd/hub",
    desired_capabilities=capabilities)
```
- запуск docker compose up -d
### Для локального запуска тестов по отдельности через интерфейс IDE
- установить [хромдрайвер](https://chromedriver.chromium.org/getting-started)
- раскомментировать в conftest.py
```
browser = webdriver.Chrome(options=options)
```
- закоментировать в conftest.py
``` 
browser = webdriver.Remote(
    command_executor="http://selenoid:4444/wd/hub",
    desired_capabilities=capabilities) 
```
### Selenoid web UI
В ходе выполнения тестов будет доступен веб интерфейс селеноида. По умолчанию он находится в 0.0.0.0:80 В веб интерфейсе можно:

- Посмотреть как выполняются тесты в контейнерах
- Посмотреть сохраненные видео с тестами
- Посмотреть загруженность и распараллеливание тестов
### Allure
После выполнения тестов, в логах ui_tests отобразится строка с адресом allure репорта Для просмотра логов в терминале нужно ввести: ``` docker logs ui_tests -f ```
