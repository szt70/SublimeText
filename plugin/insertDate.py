# coding=utf-8
import sublime, sublime_plugin
import locale
from datetime import datetime

class TodaydateCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		WEEKDAY = ('月','火','水','木','金','土','日')
		stamp = datetime.today().strftime("%Y年%m月%d日") + "(" + WEEKDAY[datetime.today().weekday()] + ")"
		for r in self.view.sel():
			if r.empty():
				self.view.insert (edit, r.a, unicode(stamp, 'utf-8') )
			else:
				self.view.replace(edit, r,    unicode(stamp, 'utf-8'))
