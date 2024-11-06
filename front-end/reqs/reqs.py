import requests

class Data:
  def __init__(self):
    self.MAINURL = 'http://127.0.0.1:8000'

  def get_count(self):
    res = requests.get(self.MAINURL)
    return res.json()

  def add_one_count(self):
    res = requests.get(self.MAINURL + '/plus')
    return res.json()

  def minus_one_count(self):
    res = requests.get(self.MAINURL + '/minus')
    return res.json()

Data = Data()