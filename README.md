# 🧮 Python Calculator

Простой калькулятор на Python с поддержкой GitHub Actions для автоматического тестирования.

## 📦 Установка

1. Склонируй репозиторий:
```bash
  git clone https://github.com/username/Calculator.git
  cd Calculator
```

2.Создайте виртуальное окружение и установите зависимости:
```python -m venv venv
  source venv/bin/activate   # Для Linux / Mac
  venv\Scripts\activate      # Для Windows
  pip install -r requirements.txt
```

## ▶️ Запуск приложения
```bash
  python calculator_app/main.py
```

## 🧪 Запуск тестов
```bash
  pytest
```

## ⚙️ CI/CD
В проекте настроен GitHub Actions (.github/workflows/python-app.yml), который:

 * Проверяет код линтером flake8
 * Запускает тесты через pytest

## 📂 Структура проекта
```Calculator/
  ├── calculator_app/      # Исходный код калькулятора
  ├── tests/               # Тесты
  ├── requirements.txt     # Зависимости
  ├── README.md            # Документация проекта
  └── .github/workflows/   # GitHub Actions конфиг
```
