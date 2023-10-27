# Użyj oficjalnego obrazu Pythona 3.x
FROM winamd64/python

# Ustaw katalog roboczy w kontenerze
WORKDIR /app

# Skopiuj pliki źródłowe projektu do kontenera
COPY . /app

# Zainstaluj zależności
RUN pip install -r requirements.txt

# Komenda, która zostanie wykonana po uruchomieniu kontenera
CMD [ "python", "main.py" ]
