FROM python:alpine3.19
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt && apk add --no-cache curl && adduser -D adenilson
USER adenilson
EXPOSE 8000
HEALTHCHECK --interval=10s --timeout=5s --start-period=30s --retries=3 CMD [ "curl", "-f", "http://localhost:8000/health" ]
COPY . . 
CMD ["fastapi", "dev"]