# import logging

class Page(object):
  is_dirty = False

  def __init__(self, name):
    self.name = name

  def set_dirty(self, dirty = True):
    self.is_dirty = dirty

  def render(self, lcd):
    print(f'Page {self.name} render')

  def on_enter(self, pd):
    print(f'Page {self.name} onEnter (status={pd.status})')

  def on_encoder_cw(self, pd):
    print(f'Page {self.name} onEncoderCw (status={pd.status})')

  def on_encoder_ccw(self, pd):
    print(f'Page {self.name} onEncoderCcw (status={pd.status})')
