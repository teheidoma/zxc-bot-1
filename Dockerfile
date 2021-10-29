FROM python:3

RUN pip install discord

COPY . .

RUN python PythonApplication1.py
