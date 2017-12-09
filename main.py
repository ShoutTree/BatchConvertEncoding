import os,sys

sourceDir = ""
targetDir = ""

localDir = ""

sourceEncodingStr = "gbk"
targetEncodingStr = "UTF-8"

def convertCoding(filePath, localDir):
	sourceFile = open(filePath)
	sourceStr = source.read()
	# replace "gbk" with UTF-8 for HTML files
	sourceStr.replace(sourceEncodingStr, targetEncodingStr)
	sourceFile.close()

	targetFilePath = ""
	if targetDir == "":
		targetFilePath = filePath[:filePath.rfind(".html")] + "_utf8.html"
	else:
		fileName = filePath[filePath.rfind("/")+1:-1]
		targetFilePath = targetDir + localDir + fileName

	targetFile = open(targetFilePath, "w")
	# change encoding from "gbk" to UTF-8 for HTML files
	targetFile.write(unicode(sourceStr, sourceEncoding).encode(targetEncoding))
	targetFile.close()

# folderPath and localDir here should end with "/"
def convertCodingFolder(folderPath, localDir):
	for entry in os.listdir(folderPath):
		path = folderPath + entry + "/"
		if os.path.isdir(path):
			convertCodingFolder(path, localDir + entry + "/")
		else:
			convertCoding(path, localDir)

# -------------- main --------------
if __name__ == '__main__':

	if len(sys.argv) >= 2:
		sourceDir = sys.argv[1]
		targetDir = sys.argv[2]
	elif len(sys.argv) == 2:
		sourceDir = targetDir = sys.argv[1]
	else:
		raise NameError('specify sourceDir at least!!!')

	convertCodingFolder(sourceDir, "")

