# local-recognizer

## Схема дирректорий

> -- tester (базовая дирректория проекта)
> > -- control
> > > -- conversion (сюда сохраняются изображения с боксами)
> > > > -- csv (сюда сохраняются файлы csv)

> > > > -- images (здесь должны быть исходные файлы для обработки)

> > > -- models (дирректория для хранения моделей YOLO)
> > > > -- warlus_1 (в дирректории должны быть файлы модели coco.names, warlus.weights, yolov3.cfg)


## Запуск создания csv файлов
до начала работы в дирректории tester/control/images доолжны находится целевые изображения
```bash
make run
```