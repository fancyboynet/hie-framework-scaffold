# hie-framework-scaffold
hie运行框架脚手架

## 安装依赖
    pip install virtualenv
    virtualenv venv 
    . venv/bin/activate
    pip install -r requirements.txt
   
## 注意
暂时不支持python3.x,开发用的是python2.7.11


## 目录说明

1. static和templates是Flask默认的放静态资源和模板的目录
2. static-src为开发源码目录,可以为任意名字,每个子目录代表一个子应用
3. blueprints为蓝图文件夹,每一个都代表一个子应用
4. 当然所有目录都是可以改的

```
    static-src
    |-www
    |  |-page
    |  |-widget
    |  |-fis-config.js
    |-m
    
```

## 基本使用
当应用比较简单,不需要使用蓝图时,请运行*app.py*


## 使用蓝图
当应用需要用到蓝图时,请运行*blueprints.py*,同时要注意渲染模板时要带上命名空间

    www = Blueprint('www', __name__)
    @www.route('/')
    def index():
        return FIS.render_template('www:page/index/index.html', title='index')

       