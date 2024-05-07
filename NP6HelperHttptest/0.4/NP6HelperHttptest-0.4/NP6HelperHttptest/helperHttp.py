"""
	helper to analyze header Http
"""

def content_type(header, mimeType):
	"""
		Function to check if header is not null and if header contains the mimeType wanted
	"""
	return len(header.strip()) == 0 or any(value.strip() == mimeType for value in header.split(';'))


			