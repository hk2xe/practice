# Решение квадратного уравнения

Программа для вычисления корней квадратного уравнения вида `ax² + bx + c = 0`.

## 📑

- [Установка](#установка)
- [Использование](#использование)
- [Примеры](#примеры)

Вы можете выбрать один из двух способов:

### Вариант 1: Клонировать репозиторий

```bash
git clone https://github.com/hk2xe/practice.git
cd practice
```

### Вариант 2: Скачать файл напрямую

Скачайте файл по ссылке:

[Скачать](https://objects.githubusercontent.com/github-production-release-asset-2e65be/971907222/d71c830b-f729-47a0-80fc-8b820bc134aa?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=releaseassetproduction%2F20250424%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250424T084850Z&X-Amz-Expires=300&X-Amz-Signature=d7c3f687527473cb2061de01f301298d2a882308826a84943183ce41d8d2ca16&X-Amz-SignedHeaders=host&response-content-disposition=attachment%3B%20filename%3Dmain.py&response-content-type=application%2Foctet-stream)

Затем перейдите в папку с файлом:

```bash
cd путь/к/папке/с/файлом
```

## Использование

Запуск из терминала:

Linux:
```bash
python3 main.py a b c
```
Windows:
```bash
python main.py a b c
```

Где `a`, `b` и `c` — целые числа (коэффициенты уравнения).

## Примеры

Linux:

```bash
python3 main.py 1 -3 2 # Вывод: (1.0, 2.0)
```

Windows:

```bash
python main.py 1 2 1 # Вывод: (-1.0)
```
