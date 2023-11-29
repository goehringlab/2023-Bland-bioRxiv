FROM python:3.11.6
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN pip install -e .
CMD ["/bin/bash"]