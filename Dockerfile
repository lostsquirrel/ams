FROM registry.cn-hangzhou.aliyuncs.com/lisong/python-base:0.1.0

ADD ./ /app
EXPOSE 9000

ENTRYPOINT [ "python", "/app/server.py" ]
