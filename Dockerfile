FROM python:3.7

# 作業ディレクトリを設定  
WORKDIR /usr/src/app  

ADD requirements.txt /usr/src/app  

# Pipenvをインストール  
RUN apt-get update \
&& pip install --upgrade pip \
&& pip install -r requirements.txt \
&& apt-get install -y python3-dev default-libmysqlclient-dev \
&& pip install mysqlclient


# django-admin startproject tangooo_pro
# cd tangooo_pro
# python manage.py startapp tangooo
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver 0:8000