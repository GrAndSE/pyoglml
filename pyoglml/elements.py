from pyoglml.style import default_style

class OGLMLElement(object):
	'''
	Base class for any element
	'''

	def __init__(self, id="", className="", parent=None, style=None):
		self.id			= id
		self.className	= className
		self.parent		= parent
		if style is None:
			style = default_style
