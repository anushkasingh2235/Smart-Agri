import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, 'agri'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agri.settings')

from agri.wsgi import application
