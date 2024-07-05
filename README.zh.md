# 提瓦特教育出版社官网

该仓库为提瓦特教育出版社官网代码托管仓库，旨在建设标准化的官网设施。

## Overall structure

1. 主页
2. 出版物
3. 通知公告
4. 产品
5. 联系我们/关于我们
6. 登录页面

## 安装

Docker 构建
```bash
    docker build -t teyvatedu .
```
预先准备:
```bash
cd src
mkdir -p /usr/tep/static /usr/tep/templates /usr/tep/sqlite3 /usr/tep/logs
cp -r ./static/* /usr/tep/static
cp -r ./templates/* /usr/tep/templates
cp -r ./sqlite3/* /usr/tep/sqlite3
cp -r ./logs/* /usr/tep/logs
```
运行docker
```bash
    docker run -d -p 80:80 \
    --name teyvatedu \
    -v /usr/tep/static:/app/static \
    -v /usr/tep/templates:/app/templates \
    -v /usr/tep/sqlite3:/app/sqlite3 \
    -v /usr/tep/logs:/app/logs \
    teyvatedu
```


生成环境变量 JWT_SECRET_KEY: 
```bash
tr -dc 'A-Z0-9' < /dev/urandom | head -c 64
```
替换 JWT_SECRET_KEY 为生成的内容.

本地部署命令:
```bash
uvicorn main:app --host=0.0.0.0 --port=8000 --lifespan=on --env-file=.env --log-config=uvicorn_log.yaml
```

## 协议

该项目包含了来自于[Editorial by HTML5 UP](html5up.net)的代码，作者为[@ajlkn], 在该授权协议下 [CC BY 3.0](html5up.net/license). 代码内容有变动。

最后一次修改：2024年7月2日