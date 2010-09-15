from properties import AutoIntProperty, DisplayProperty, FloatProperty, IntProperty, NumericalProperty, PositionProperty, StyleProperty

class StyleGroup(object):
	'''
	Class provides
	'''

	mapping = {
		'width':			AutoIntProperty,
		'min-width':		IntProperty,
		'max-width':		IntProperty,
		'height':			AutoIntProperty,
		'min-height':		IntProperty,
		'max-height':		IntProperty,
		'font-size':		NumericalProperty,
		'margin-left':		AutoIntProperty,
		'margin-right':		AutoIntProperty,
		'margin-top':		AutoIntProperty,
		'margin-bottom':	AutoIntProperty,
		'padding-left':		AutoIntProperty,
		'padding-right':	AutoIntProperty,
		'padding-top':		AutoIntProperty,
		'padding-bottom':	AutoIntProperty,
		'line-height':		NumericalProperty,
		'float':			FloatProperty,
		'position':			PositionProperty,
		'display':			DisplayProperty,
	}

	def __init__(self, name, content):
		'''
		Create new StyleGroup instance
			.name		style group name
			.content	style descriptions
		'''
		self.name	= name
		self.props	= {}
		# Parse content
		props		= content.split(';')
		for prop in props:
			prop_name, prop_value	= prop.split()

	def getPropertyStyle(self, name):
		name	= name.strip()
		if name in StyleGroup.mapping:
			return StyleGroup.mapping[name]
		return StyleProperty
