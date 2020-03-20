from xml.etree.ElementTree import parse

# xml 형태의 annotation 파일을 읽어들여서 imgName, objectName, xmin, ymin, xmax, ymax을 출력해주는 함수 
# 단, 각 출력값은 option을 통해 하나씩 출력
def ReadAnnot(annotName, option):
	# 'annotName'을 불러와서 parsing
	tree = parse(annotName)
	# tree의 가장 상위 계층(<annotation>) 불러오기 
	root = tree.getroot()

	if option == 'imgName':
		# root에서 'filename'이라는 이름을 가진 하위 계층의 text 불러오기
		# annotation/filename 의 text 
		imgName = root.find('filename').text

		return imgName

	if option == 'objectName':
		# annotation/object 를 모두(all) 불러와서 ListObject에 할당 
		ListObject = root.findall('object')

		# object들의 name을 저장할 빈 리스트 생성
		objectName = []

		# ListOjbect에 저장된 object들의 'name'을 불러와서 name에 저장 
		# name을 objectName에 순차적으로 append
		for i in ListObject:
			name = i.find('name').text
			objectName.append(name)

		# 출력 형태는 list
		return objectName

	if option == 'xmin':
		ListObject = root.findall('object')

		xmin = []
		for i in ListObject:
			xminValue = int(i.find('bndbox').find('xmin').text)
			xmin.append(xminValue)

		return xmin


	if option == 'ymin':
		ListObject = root.findall('object')

		ymin = []
		for i in ListObject:
			yminValue = int(i.find('bndbox').find('ymin').text)
			ymin.append(yminValue)

		return ymin


	if option == 'xmax':
		ListObject = root.findall('object')

		xmax = []
		for i in ListObject:
			xmaxValue = int(i.find('bndbox').find('xmax').text)
			xmax.append(xmaxValue)

		return xmax


	if option == 'ymax':
		ListObject = root.findall('object')

		ymax = []
		for i in ListObject:
			ymaxValue = int(i.find('bndbox').find('ymax').text)
			ymax.append(ymaxValue)

		return ymax
