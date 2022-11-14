FROM python:3.9 as builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN python --version && \
    pip install -r requirements.txt

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /usr/local/src/ /usr/local/src/
COPY /src /app/src
ENV PYTHONPATH=/app

CMD ["uvicorn", "src.main:app"]
