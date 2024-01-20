## Devopsinfo
- Стек - Django + Postgresql + Traefik
- Для стилей использована библиотека PicoCSS с легкой кастомизацией
## Что сделано на данный момент?
- [x] Приложение запущено в Docker compose под доменом [korneplod.xyz](korneplod.xyz), есть поддержка TLS
- [x] Полностью реализованы все страницы кроме страницы "Навыки"
- [x] Админка поддерживает CRUD-операции над моделями
- [x] Реализовано простенькое Restfull API для подгрузки табличных данных скриптом сразу после предобработки файла с вакансиями
## Что осталось сделать?
- [ ] Нормальный деплой с Gunicorn в режиме продакшена и использование Nginx для обслуживания статики
- [ ] Ускорить парсинг данных с hh.ru
- [ ] Допилить API - пока что с помощью него нельзя загружать изображения с графиками, нельзя удалять и изменять остальные объекты
- [ ] Аутентификация для API
- [ ] Настроить небольшой пайплайн с автодеплоем с помощью GitHub Actions?...