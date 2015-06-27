# coding=utf-8
import sublime, sublime_plugin
import locale
from datetime import datetime

class Example3Command(sublime_plugin.TextCommand):
	def run(self, edit):
		stamp = datetime.today().strftime("%Y年%m月%d日%a")
		for r in self.view.sel():
			if r.empty():
				self.view.insert (edit, r.a, unicode(stamp, 'utf-8') )
			else:
				self.view.replace(edit, r,    unicode(stamp, 'utf-8'))