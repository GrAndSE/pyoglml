from const import DISPLAY, FONTUNITS, FLOATINGS, HALIGNS, INTUNITS, POSITIONS

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
	Style property that can accepts integer value with px or % or none or 
	inherit
	'''

	def __init__(self):
		super(IntProperty, self).__init__()

	def parseValue(self, value):
		value	= value.strip().lower()
		if value == 'none' or value == 'inherit':
			self.value	= value
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

class HorisontalAlignProperty(StyleProperty):
	'''
	Property used for any align property
	'''

	def __init__(self):
		'''
		Create new property instance
		'''
		super(HorisontalAlignProperty, self).__init__()

	def parseValue(self, value):
		'''
		Parse value
		'''
		value = value.strip().lower()
		if value not in HALIGNS:
			return False
		self.value = value

class FontSizeProperty(StyleProperty):
	'''
	Class used for parsing font size property
	'''

	def __init__(self):
		'''
		Create new property instance
		'''
		super(FontSizeProperty, self).__init__()

	def parseValue(self, value):
		'''
		Parse font-size value
		'''
		value = value.strip().lower()
		self.value = int(value)
		for units in FONTUNITS:
			if units in value:
				self.units = units
				return True

