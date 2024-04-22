from pages import Page

class Action:
  def __init__(self, label, gcode):
    self.label = label
    self.gcode = gcode


class TestPage(Page):
  actions = [
    Action("Power on", "POWER_ON"),
    Action("Power off", "POWER_OFF")
  ]

  def __init__(self):
    super().__init__('Test Page')
    self.selection = 0

  def render(self, lcd):
    super().render(lcd)
    # Clear
    lcd.Draw_Rectangle(1, lcd.Color_Bg_Black, 0, 0, lcd.width, lcd.height - 1)
    print(f"testpage render selection={self.selection}")
    x = 0
    y = 10
    line_height = 30

    for i, a in enumerate(self.actions):
      lcd.Draw_String(
        False, False, lcd.DWIN_FONT_STAT, lcd.Color_White,
        lcd.Color_Bg_Black, x + 4, y + 4, a.label)
      if i == self.selection:
        lcd.Draw_Rectangle(
          2, # Xor fill
          lcd.Color_White,
          x, y,
          lcd.width - 1,
          y + line_height - 1
        )
      y += line_height

    self.set_dirty(False)

  def on_encoder_cw(self, pd):
    super().on_encoder_cw(pd)
    self.selection = (self.selection + 1) % len(self.actions)
    self.set_dirty()

  def on_encoder_ccw(self, pd):
    super().on_encoder_ccw(pd)
    self.selection = self.selection - 1
    while self.selection < 0:
      self.selection += len(self.actions)
    self.set_dirty()

  def on_enter(self, pd):
    super().on_enter(pd)
    a = self.actions[self.selection]
    print(f"testpage on_enter selection={self.selection} a={a}")
    if a is not None:
      pd.sendGCode(a.gcode)
      self.selection = 0
      self.set_dirty()
