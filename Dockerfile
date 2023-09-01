# pull official base image
# 도커에서 제공하는 여러 이미지들 중 파이썬에서 설치된 것을 가져온다.
FROM python:3.9-slim-buster

# set work directory
# 아무것도 없는 가상 컴퓨터에 폴더를 생성하여 작업파일을 수행할 경로
WORKDIR /usr/src/app

# set envionment variable
# 컴파일 과정에서 .py확장자가 자동으로 생성되는 것을 방지하는 코드
ENV PYTHONDONTWRTIEBYTECODE 1
# 파이썬이 버퍼링하지않고 바로 수행되도록 하는 코드
ENV PYTHONBUFFERED 1

# 현재 django 수행 내용을 해당 폴더에 복사
COPY . /usr/src/app/

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
