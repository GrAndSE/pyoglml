# Declare 

FONTUNITS = (
	'',
	'px',
	'%',
	'em',
	'pt'
)

INTUNITS = (
	'',
	'%',
	'px'
)

POSITIONS = (
	'static',
	'relative',
	'absolute',
	'fixed',
)

FLOATINGS = (
	'none',
	'left',
	'right',
)

HALIGNS = (
	'left',
	'right',
	'center',
)
VALIGNS = (
	'top',
	'bottom',
	'middle',
)

DISPLAY = (
	'none',
	'inline',
	'block',
	'inline',
	'inline-block',
	'list-item',
	'run-in',
	'compact',
	'table',
	'inline-table',
	'table-row-group',
	'table-header-group',
	'table-footer-group',
	'table-row',
	'table-row-group',
	'table-column',
	'table-column-group',
	'table-cell',
	'table-caption',
	'ruby',
	'ruby-base',
	'ruby-text',
	'ruby-base-group',
	'ruby-text-group',
)

class StyleProperty(object):
	'''
	Style property class
	'''

	def __init__(self):
		'''
		Create new StyleProperty instance
		'''
		super(StyleProperty, self).__init__()

	def parseValue(self, value):
		'''
		Parse string value and return True if was succesfully parsed or False
			.value		values string representation
		Returns False any way for this class
		'''
		return False


class AutoIntProperty(StyleProperty):
	'''
	Style property can contains integer value with px or % units or auto
	'''

	def __init__(self):
		super(AutoIntProperty, self).__init__()

	def parseValue(self, value):
		value 		= value.strip().lower()
		if value == 'auto':
			self.value = 'auto'
			return True
		self.value	= int(value)
		for units in INTUNITS:
			if units in value:
				self.units = units
				return True
		return False


class IntProperty(StyleProperty):
	'''
	Style property that can accepts integer value with px or % or none or inherit
	'''

	def __init__(self):
		super(IntProperty, self).__init__()

	def parseValue(self, value):
		value	= value.strip().lower()
		if value == 'none':
			self.value	= 'none'
		elif value == 'inherit':
			self.value	= 'inherit'
		else:
			self.value	= int(value)
			for units in INTUNITS:
				if units in value:
					self.units = units
					return True
			return False
		return True

class NumericalProperty(StyleProperty):
	'''
	Style with numerical value
	'''

	def __init__(self):
		super(NumericalProperty, self).__init__()

	def parseValue(self, value):
		self.value	= float(value)
		return True


class FloatProperty(StyleProperty):
	'''
	Property contains object floating value
	'''

	def __init__(self):
		super(FloatProperty, self).__init__()

	def parseValue(self, value):
		value		= value.strip()
		self.value	= ''
		if value not in FLOATINGS:
			return False
		for floating in FLOATINGS:
			if floating == value:
				self.value	= floating
				return True


class DisplayProperty(StyleProperty):
	'''
	Displaying property
	'''

	def __init__(self):
		super(DisplayProperty, self).__init__()

	def parseValue(self, value):
		value		= value.strip()
		if value not in DISPLAY:
			return False
		for display in DISPLAY:
			if display == value:
				self.value	= display
				return True


class PositionProperty(StyleProperty):
	'''
	Element position property
	'''

	def __init__(self):
		super(PositionProperty, self).__init__()

	def parseValue(self, value):
		value	= value.strip()
		if value not in POSITIONS:
			return False
		for position in POSITIONS:
			if position == value:
				self.value	= position
				return True

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
