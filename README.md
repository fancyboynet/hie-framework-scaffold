# hie-framework-scaffold
hie运行框架脚手架

## 安装依赖
    pip install virtualenv
    virtualenv venv 
    . venv/bin/activate
    pip install -r requirements.txt
   
## 注意
暂时不支持python3.x,开发用的是python2.7.11


## 使用

1. 引入FIS

    from fis3 import FIS
    
2. 配置FIS

    app = Flask(__name__)
    FIS(app, static_folder='static', template_folder='templates', debug=True)
    
3. 改用FIS渲染模板

    @app.route('/')
    def index():
        return FIS.render_template('page/index/index.html', title='index')
        
4. 使用蓝图时,注意模板需要带上命名空间

    www = Blueprint('www', __name__)
    @www.route('/')
    def index():
        return FIS.render_template('www:page/index/index.html', title='index')