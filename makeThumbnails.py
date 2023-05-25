# make thumnails for all images that are new to Git
from git import Repo
from PIL import Image
repo = Repo("c:\\projects\\website")
git = repo.git
s = git.status()
lines = s.splitlines()
newFilesFound = 0
for line in lines:
	if newFilesFound == 0 and "Untracked files" in line:
		newFilesFound = 1
	elif newFilesFound == 1:
		newFilesFound = 2
	elif newFilesFound == 2:
		if (line.endswith(".jpg") or line.endswith(".JPG") or line.endswith(".png") or line.endswith(".PNG")) and "_thumbnail" not in line:
			line = line.lstrip("\t")
			print(line)
			with Image.open(line) as im:
				print(im.size)
				if im.size[0] > im.size[1]:
					if im.size[0] < 600:
						outIm = im;
					else:
						outIm = im.resize((600, int(im.size[1] / ((im.size[0] / 600)))))
				else:
					if im.size[1] < 600:
						outIm = im;
					else:
						outIm = im.resize((int(im.size[0] / ((im.size[1] / 600))), 600))
				fileName = line.split(".")
				outIm.save(fileName[0] + "_thumbnail." + fileName[1])