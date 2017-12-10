import os,sys
# from pathlib import Path

sourceDir = ""
targetDir = ""

localDir = ""

sourceEncodingStr = "gbk"
targetEncodingStr = "UTF-8"

extStr = "_utf8.html"


def convertCoding(filePath, localDir):
	print 'convertCoding, filePath is: ' + filePath
	if filePath.endswith(".html") and filePath.find(extStr) < 0:
		sourceFile = open(filePath)
		sourceStr = sourceFile.read()
		if sourceStr.find(sourceEncodingStr) >= 0:
			# replace "gbk" with UTF-8 for HTML files
			sourceStr = sourceStr.replace(sourceEncodingStr, targetEncodingStr)
			sourceFile.close()

			targetFilePath = ""
			# if targetDir == "":
			# 	targetFilePath = filePath[:filePath.rfind(".html")] + "_utf8.html"
			# else:
			fileName = filePath[filePath.rfind("/")+1:]
			targetFilePath = targetDir + localDir + fileName + extStr

			print 'targetDir is ' + targetDir
			print 'targetFilePath is ' + targetFilePath

			targetFile = open(targetFilePath, "w")
			# change encoding from "gbk" to UTF-8 for HTML files
			try:
				targetFile.write(unicode(sourceStr, sourceEncodingStr).encode(targetEncodingStr))
			except UnicodeDecodeError as e:
				print e
				print 'perhaps not a file encoded in ' + sourceEncodingStr
				# print "UnicodeDecodeError({0}): {1}".format(e.errno, e.strerror)				
			except:
				print "Unexpected error:", sys.exc_info()[0]
				raise
			targetFile.close()
		else:
			print 'not in ' + sourceEncodingStr + " encoding, no need to convert!!!"
	else:
		print 'not an html file!!!'

# folderPath and localDir here should end with "/"
def convertCodingFolder(folderPath, localDir):
	for entry in os.listdir(folderPath):
		path = folderPath + entry
		if os.path.isdir(path):
			convertCodingFolder(path + "/", localDir + entry + "/")
		else:
			convertCoding(path, localDir)


def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def ensureEndDash(file_path):
	if not file_path.endswith("/"):
		file_path = file_path + "/"
	return file_path


# -------------- main --------------
if __name__ == '__main__':

	if len(sys.argv) >= 3:
		sourceDir = sys.argv[1]
		targetDir = sys.argv[2]
		# targetDirPath = Path(targetDir)
		ensure_dir(targetDir)
		sourceDir = ensureEndDash(sourceDir)
		targetDir = ensureEndDash(targetDir)

		print 'argv len 3, argv[1] is ' + sourceDir
	elif len(sys.argv) == 2:
		sourceDir = targetDir = sys.argv[1]
		print 'argv len 2, argv[1] is ' + sourceDir
	else:
		raise NameError('specify sourceDir at least!!!')

	convertCodingFolder(sourceDir, "")

