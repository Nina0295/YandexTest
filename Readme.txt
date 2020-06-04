# Это тестовый проект кандидата на роль автотестера Беловой Нины

Для запуска тестов:
1. Установите chrome webdriver:
- Здесь можно скачать драйвер нужной версии https://chromedriver.chromium.org/downloads
- Здесь можно прочитать инструкцию по установке https://chromedriver.chromium.org/getting-started
2. Создадим папку, где будут храниться наши виртуальные окружения, и перейдем в неё:
- mkdir environments
- cd environments
3. Запустите Selenium окружение из корневой папки:
- Откройте cmd
- Запустите bat file: environments/selenium_env/Scripts/activate.bat
4. Запустите тесты командой pytest -v --tb=line test_search.py

