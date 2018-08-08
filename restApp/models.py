from django.db import models
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Stock(models.Model):
	ticker = models.CharField(max_length=10)
	open = models.FloatField()
	close = models.FloatField()
	volume = models.IntegerField()

	def __str__(self):
		return self.ticker

class Snippet(models.Model):
	owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE, default=1)
	highlighted = models.TextField(default='test')
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True, default='')
	code = models.TextField()
	linenos = models.BooleanField(default=False)
	language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
	style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

	def save(self, *args, **kwargs):

		lexer = get_lexer_by_name(self.language)
		linenos = self.linenos and 'table' or False
		options = self.title and {'title': self.title} or {}
		formatter = HtmlFormatter(style=self.style, linenos=linenos,full=True, **options)
		self.highlighted = highlight(self.code, lexer, formatter)
		super(Snippet, self).save(*args, **kwargs)

	class Meta:
		ordering = ('created',)


class Activity(models.Model):
	user = models.ForeignKey('restApp.users', on_delete=models.CASCADE, default=1)
	chat = models.ForeignKey('restApp.chats', on_delete=models.CASCADE, default=1)
	username = models.CharField(max_length=30)
	datetime = models.DateTimeField(auto_now_add=True)
	activity = models.TextField()
	duration = models.IntegerField()
	type = models.IntegerField()
	status = models.IntegerField()

class Administration(models.Model):
	hash = models.CharField(max_length=36)
	name = models.CharField(max_length=100)
	datetime = models.DateTimeField(auto_now_add=False)
	refresh = models.DateTimeField(auto_now_add=True)
	email = models.CharField(max_length=100)
	server = models.CharField(max_length=100)
	department = models.CharField(max_length=100)
	rating = models.IntegerField()
	datetime = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=100)
	country = models.CharField(max_length=150)
	timezone = models.CharField(max_length=5)
	dial = models.CharField(max_length=5)
	telephone = models.CharField(max_length=20)
	message = models.TextField()
	operator = models.BigIntegerField()
	status = models.IntegerField()

class Chats(models.Model):
	hash = models.CharField(max_length=36)
	name = models.TextField()
	datetime = models.DateTimeField(auto_now_add=False)
	refresh = models.DateTimeField(auto_now_add=True)
	email = models.TextField()
	server = models.TextField()
	department = models.TextField()
	rating = models.IntegerField()
	typing = models.IntegerField()
	transfer = models.IntegerField()
	status = models.IntegerField()

class Chatvisitors(models.Model):
	chat = models.ForeignKey('restApp.chats', on_delete=models.CASCADE, default=1)
	visitor = models.CharField(max_length=81)

class Contacts(models.Model):
	datetime = models.DateTimeField(auto_now_add=True)
	telephone = models.CharField(max_length=20)
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=255)

class Countries(models.Model):
	code = models.AutoField(primary_key=True)
	country = models.CharField(max_length=50)
	dial = models.CharField(max_length=10)

class Custom(models.Model):
	request = models.BigIntegerField()
	custom = models.TextField()
	name = models.TextField()
	reference = models.TextField()

class Departements(models.Model):
	name = models.TextField()
	email = models.CharField(max_length=50)
	status = models.IntegerField()

class Devices(models.Model):
	user = models.ForeignKey('restApp.users', on_delete=models.CASCADE, default=1)
	datetime = models.DateTimeField(auto_now_add=True)
	unique = models.TextField()
	device = models.TextField()
	os = models.TextField()
	token = models.TextField()

class Expireddtotp(models.Model):
	datetime = models.DateTimeField(auto_now_add=True)

class Fullcontactperson(models.Model):
	datetime = models.DateTimeField()
	email = models.CharField(max_length=255)
	data =  models.TextField()

class Geolocation(models.Model):
	request = models.BigIntegerField()
	city = models.TextField()
	state = models.TextField()
	country = models.TextField()
	latitude = models.TextField()
	longitude = models.TextField()

class Infusionsofttags(models.Model):
	tag = models.BigIntegerField()
	name = models.TextField()
	description = models.TextField()

class Initiatechat(models.Model):
	request = models.BigIntegerField()
	datetime = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey('restApp.users', on_delete=models.CASCADE, default=1)
	message = models.BigIntegerField()

class Messages(models.Model):
	chat = models.ForeignKey('restApp.chats', on_delete=models.CASCADE, default=1)
	username = models.CharField(max_length=30)
	datetime = models.DateTimeField(auto_now_add=True)
	message = models.TextField()
	align = models.IntegerField()
	status = models.IntegerField()

class Ratings(models.Model):
	chat = models.ForeignKey('restApp.chats', on_delete=models.CASCADE, default=1)
	user = models.ForeignKey('restApp.users', on_delete=models.CASCADE, default=1)
	rating = models.IntegerField()

class Requests(models.Model):
	ipaddress = models.CharField(max_length=100)
	useragent = models.CharField(max_length=200)
	resulution = models.CharField(max_length=20)
	city = models.TextField()
	state = models.TextField()
	country = models.TextField()
	datetime = models.DateTimeField(auto_now_add=False)
	request = models.DateTimeField(auto_now_add=True)
	refresh = models.DateTimeField(auto_now_add=True)
	url = models.TextField()
	title = models.CharField(max_length=150)
	referrer = models.TextField()
	path = models.TextField()
	initiate = models.BigIntegerField()
	status = models.IntegerField()

class Responses(models.Model):
	name = models.TextField()
	datetime = models.DateTimeField()
	type = models.IntegerField()
	category = models.TextField()
	content = models.TextField()
	tags = models.TextField()

class Sessions(models.Model):
	chat = models.ForeignKey('restApp.chats', on_delete=models.CASCADE, default=1)
	user = models.ForeignKey('restApp.users', on_delete=models.CASCADE, default=1)
	requested = models.DateTimeField(auto_now_add=False)
	accepted = models.DateTimeField(auto_now_add=False)
	end = models.DateTimeField(auto_now_add=False)

class Settings(models.Model):
	name = models.AutoField(primary_key=True)
	value = models.TextField()

class Sms(models.Model):
	datetime = models.DateTimeField(auto_now_add=True)
	sid = models.CharField(max_length=35)
	conversation = models.CharField(max_length=36)
	user = models.BigIntegerField()
	body = models.TextField()
	mediaurls = models.TextField()
	status = models.CharField(max_length=20)
	price = models.DecimalField(max_digits=19, decimal_places=2)
	priceunit = models.CharField(max_length=3)

class Smsconversations(models.Model):
	datetime = models.DateTimeField(auto_now_add=False)
	froom = models.CharField(max_length=20)
	to = models.CharField(max_length=20)
	user = models.ForeignKey('restApp.users', on_delete=models.CASCADE, default=1)
	department = models.TextField()
	status = models.IntegerField()

class Totp(models.Model):
	user = models.AutoField(primary_key=True)
	secret = models.CharField(max_length=16)
	backup = models.TextField()

class Typing(models.Model):
	chat = models.ForeignKey('restApp.chats', related_name='chatstype', on_delete=models.CASCADE, default=1)
	user = models.ForeignKey('restApp.users', on_delete=models.CASCADE, default=1)
	status = models.IntegerField()

class Users(models.Model):
	username = models.CharField(max_length=255)
	password = models.TextField()
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	email = models.CharField(max_length=255)
	department = models.TextField()
	image = models.TextField()
	datetime = models.DateTimeField(auto_now_add=False)
	refresh = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)
	disabled = models.IntegerField()
	privilage = models.IntegerField()
	status = models.BigIntegerField()
	custom = models.BigIntegerField()

class Websockets(models.Model):
	timestamp = models.BigIntegerField()
	websocket = models.IntegerField()
	active = models.IntegerField()
