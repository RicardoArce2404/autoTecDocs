''' Porfavor usar con cuidado, se recomienda usar el script sobre
una copia del archivo a modificar
'''

def length(var):
	c = 0
	for i in var: c += 1
	return c

def pyWrite(text, filename):
	file = open(filename, 'w', encoding = 'utf-8')
	file.writelines(text)
	file.close()
	print('Done')

def pyRead(filename):
	file = open(filename, 'r', encoding = 'utf-8')
	content = file.readlines()
	file.close()
	return content

def getFnName(line):
	line = line[4:]
	fnName = ''
	for i in line:
		if i != '(': fnName += i
		else: break
	return fnName

def getFnInput(line):
	fnInput = ''
	for i in range(length(line)):
		if line[i] == '(' and line[i+1] != ')':
			fnInput = line[i+1:-3]
	return fnInput

filename = input('Nombre de archivo: ')
content = pyRead(filename)
newContent = []

for i in range(length(content)):
	if content[i][:4] == 'def ':
		fnName = getFnName(content[i])
		fnInput = getFnInput(content[i])
		newContent += [f"'''\n"]
		newContent += [f"    Nombre: {fnName}.\n"]
		newContent += [f"    Entrada: {fnInput}.\n"]
		newContent += [f"    Salida: .\n"]
		newContent += [f"    Restricciones: .\n"]
		newContent += [f"'''\n"]
	newContent += [content[i]]

pyWrite(newContent, filename)