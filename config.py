#coding:utf-8
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class config:
	"""docstring for config"""
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string blabla'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
	FLASKY_MAIL_SENDER = 'Flasky Admin <104938037@qq.com>'
	FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(config):
	"""docstring for DevelopmentConfig"""
	DEBUG = True
	MAIL_SERVER = 'smtp.qq.com'
	MAIL_PORT = 465
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
	'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(config):
	"""docstring for TestingConfig"""
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
	'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(config):
	"""docstring for ProductionConfig"""
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
	'sqlite:///' + os.path.join(basedir, 'data.sqlite')
		
config = {
	'development':DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig

	'default': DevelopmentConfig
}

		