# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 03:19:13 2016
@author: yxl
"""
from imagepy.core.util import fileio
from sciapp import Source
from imagepy.core.engine import Simple

class SaveImage(fileio.Writer):
	title = 'Save'

	def load(self, ips):
		self.filt = [i[0] for i in sorted(Source.manager('writer').names())]
		return True

class WindowCapture(fileio.Writer):
	title = 'Save With Mark'
	filt = ['PNG']

	def run(self, ips, imgs, para = None):
		WindowsManager.get().canvas.save_buffer(para['path'])

plgs = [SaveImage, WindowCapture]