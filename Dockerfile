FROM winamd64/python
WORKDIR /Wp-Zadanie
COPY . /Wp-Zadanie
RUN pip install -r requirements.txt
RUN pip install pyinstaller
CMD [ "pyinstaller", "./main.py", "-F" ]
