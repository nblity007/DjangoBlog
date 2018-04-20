添加环境变量
	将%PYTHONHOME%\Lib\site-packages\django\bin加入系统环境变量
	
创建项目
	django-admin.py startproject my_blog
	
创建模块
	python manage.py startapp article
	
在项目中添加模块
	在my_blog目录下settings.py的变量INSTALLED_APPS中添加模块名（article）
	
启动django服务器
	python manage.py runserver localhost:9000
	
数据库配置
	settings.py-->DATABASES

在article目录下models.py中添加对象属性

同步数据库
	python manage.py migrate
	python manage.py makemigrations
	python manage.py migrate
	(migrate命令按照app顺序建立或者更新数据库, 将models.py与数据库同步)

进入Django中的交互式shell来进行数据库的增删改查等操作

使用markdown之前，先安装markdown库
	pip instal markdown
使用高亮
	pip install Pygments
	选择高亮的样式，demo地址：http://pygments.org/demo/6734157/?style=monokai
	参数说明-S:样式
		pygmentize -S monokai -f html -a .codehilite > monokai.css
