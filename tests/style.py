from pyoglml.style import properties
# Test StyleProperty class
p = StyleProperty()
if p.parseValue(''):
	print('StyleProperty.parseValue(self, "") error')
else:
	print('StyleProperty.parseValue(self, value) OK')
# Test FloatProperty class
p = FloatProperty()
if p.parseValue(''):
	print('FloatProperty.parseValue(self, "") error')
elif not p.parseValue('left') or p.value != 'left':
	print('FloatProperty.parseValue(self, "left") error')
elif not p.parseValue('right') or p.value != 'right':
	print('FloatProperty.parseValue(self, "right") error')
elif not p.parseValue('none') or p.value != 'none':
	print('FloatProperty.parseValue(self, "none") error')
else:
	print('FloatProperty.parseValue(self, value) OK')
