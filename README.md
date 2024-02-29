# FileDownloader

基于flask,主要作用是通过环境变量指定一个路径，通过flask提供指定路径下的文件下载

## 场景

> 适用于需要从一个地方去获取更新文件，但是主机上又不方便SSH或者SFTP文件传输的情况。
>
> 注意：没有开启认证，只能在内网进行文件下载。否则会有安全隐患。

### 使用方法

```
# 通过环境变量指定下载路径
docker run -d -p 5000:5000 -e FLASK_DOWNLOAD_FOLDER=/app/downloads llody/filedownloader:v1

# 将主机目录挂载到容器内提供下载
docker run -d -p 5000:5000 -v /path/to/your/download_directory:/app/downloads -e FLASK_DOWNLOAD_FOLDER=/app/downloads llody/filedownloader:v1


# 下载方式示例
wget -O app.tar http://192.168.1.232:5000/download/app.tar
```

### 主机使用方式

```
# 通过export指定环境变量路径
export FLASK_DOWNLOAD_FOLDER=/path/to/your/download_directory

# 安装flask依赖
pip install -r requirements.txt

# 运行
python3 apprun.py
```
