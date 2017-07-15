2017.07.15
1. One liner to rename all files under on directory
It's really helpful when you want to remove some chinese characters from one website.
'xinlang' -> ''
[os.rename(os.path.join(mypath, f), os.path.join(mypath,f.replace(u'meikong', 'mei'))) for f in os.listdir(mypath)]
