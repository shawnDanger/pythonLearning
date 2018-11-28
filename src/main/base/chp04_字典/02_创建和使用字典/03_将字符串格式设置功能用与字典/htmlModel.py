template = '''
<html>
<head><title>{title}</title></head>
<body>
{title}
{text}
</body>
</html>
'''
data = {'title': '标题', 'text': '内容'}
print(template.format_map(data))
