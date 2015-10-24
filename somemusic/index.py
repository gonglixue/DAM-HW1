from flask import Flask
from flask.ext.script import Manager
from flask import render_template
import os
import smtplib
from email.mime.text import MIMEText
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
import sys
import urllib
import urllib.request
from bs4 import BeautifulSoup

app = Flask(__name__)
manager = Manager(app)
app.config['SECRET_KEY'] = 'My Music Website'

class MessageForm(Form):
	message = StringField('You can leave your suggestions or just say hello to me',validators=[Required()])
	submit = SubmitField('Submit')

@app.route('/')
def homePage():
	return render_template('index.html')

@app.route('/popular/<int:id>')
def temp(id):
	if id<10:
		fp=open(os.getcwd()+'/static/popular/'+'00%s'%id+'.txt') 
	else:
		fp=open(os.getcwd()+'/static/popular/'+'0%s'%id+'.txt')
	description = fp.readlines()  
	fp.close()
	# separate the singer from first line
	str = description[0]
	tuple = str.partition('|')
	singer_name = tuple[2]	
	
	# use singer_name as the key word to search in baidu
	url = "http://music.baidu.com/search?key=" + urllib.parse.quote(singer_name)
	page = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(page)
	name = list(range(5))
	link = list(range(5))
	image = list(range(5))
	i=0
	for item in soup.find_all(class_="group-item"):
		img_src = item.img
		info = item.find(class_ = 'cover')
		image[i] = img_src['src']
		name[i] = img_src['alt']
		link[i] = "http://music.baidu.com" + info['href']
		i=i+1
		if(i==5):
			break
		
	return render_template('popsong2.html',num=id,title=description[0],detail=description[1],name=name,link=link,image=image)
	
@app.route('/popular/')
def popular():
	return render_template('popular.html')

@app.route('/violin/')
def violin():
	return render_template('violin.html')
	
# @app.route('/popular/<int:num>')
# def popsong(num):
	# return render_template('popsong.html',num=num)

@app.route('/violin/<int:id>')
def violinsong(id):
	if id<10:
		fp=open(os.getcwd()+'/static/violin/'+'00%s'%id+'.txt') 
	else:
		fp=open(os.getcwd()+'/static/violin/'+'0%s'%id+'.txt')
	description = fp.readlines()    
	return render_template('violinsong.html',num=id,title=description[0],detail=description[1])
	

mail_host = "smtp.sina.com"
mail_user = "XXX@sina.com"  # e-mail address
mail_pass = ""	#  password _(:з」∠)_ 
@app.route('/message/',methods=['GET','POST'])
def send():
	form = MessageForm()
	result = ''
	if form.validate_on_submit():
		message = form.message.data
		form.message.data=''
		me = message + "<" + mail_user + ">"
		msg = MIMEText(message,_subtype='plain',_charset='GBK') 
		msg['Subject'] = 'SomeMu'
		msg['From'] = me
		msg['To'] = '724351282@qq.com'
		
		server = smtplib.SMTP()
		server.connect(mail_host)
		server.login(mail_user,mail_pass)
		server.sendmail(me, msg['To'],msg.as_string())
		server.close()	
		result = "Thank you for your visit! I'll improve my website according to your sincere suggestions. Have fun :)"
	return render_template('message.html',form = form,result=result)

	
	
if __name__ == '__main__' :
	#app.run(host='10.110.34.102',port=5000)
	app.debug = True
	#app.run()
	app.run(host='0.0.0.0')
