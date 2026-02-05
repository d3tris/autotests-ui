# На основе последнего официального образа Ubuntu
FROM ubuntu

# Устанавливаем Python и нужные утилиты
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Создаём отдельное виртуальное окружение и используем его(обходим PEP 668)
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Рабочая директория
WORKDIR /app

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m playwright install --with-deps

# Копируем проект
COPY . /app

# Запускаем автотесты
CMD ["python3", "-m", "pytest", "-m", "regression", "--alluredir=./allure-results"]
