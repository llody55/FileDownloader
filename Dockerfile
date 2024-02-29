# 指定基础镜像
FROM python:3.8-slim

# 设置工作目录
WORKDIR /app

# 安装依赖
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# 复制应用代码
COPY . /app

# 暴露端口
EXPOSE 5000

# 环境变量可以在这里设置，或者在运行容器时通过命令行参数传递
# ENV FLASK_DOWNLOAD_FOLDER /app/downloads

# 设置启动命令
CMD ["python3", "apprun.py"]
