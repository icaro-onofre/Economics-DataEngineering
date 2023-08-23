FROM python:3.9-bullseye
# 2023-08-23

RUN  pip install --upgrade pip && \
                pip install pandas \
                requests \
                boto3 \
                beautifulsoup4 \
                pyarrow \
                python-dotenv \
                pytest --target=/usr/local/lib/python3.9/dist-packages && \
                export PATH=$PATH:/usr/local/lib/python3.9/dist-packages
                
ENV PYTHONPATH=/usr/local/bin/python

 CMD ["python"]


