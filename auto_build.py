import sys, os, getopt, subprocess


'''
@abstract execute "cd" command with user's parameter
@parameter directory, new directory to change to 
'''
def changeDir(directory):
    print("project dir %s" % directory)
    os.chdir(directory)
    
'''
@abstract execute "xcodebuild" command to build iOS project
@parameter targetName target to be build with
'''
def xcbuild(targetName, directory="./build/"):
    print("target %s, configuration %s" % (targetName, ""))
    archiveCmd = "xcodebuild -scheme " + targetName + " archive -archivePath " + directory + targetName + ".xcarchive"
    ipaCmd = "xcodebuild -exportArchive -exportFormat ipa" + " -archivePath " + directory + "/" + targetName + ".xcarchive" + " -exportPath " + directory + "/" + targetName + ".ipa"
                
    print("archive cmd %s, ipa cmd %s" % (archiveCmd, ipaCmd))
    
    process = subprocess.Popen(archiveCmd, shell=True)
    process.wait()
    
    process = subprocess.Popen(ipaCmd, shell=True)
    output = process.communicate()
    print output

'''
@abstract execute xcodebuild to auto build iOS project. 
@parameter $1: project path, --target target name, --configuration debug, release or user defined configuration
@example --target=your target name --config=Release -x [project path] [out put path.format]
'''
def main():
    try:
        print("start")
        opts, args = getopt.getopt(sys.argv[1:], "x", ["target=", "config="])
        
        print(opts)
        
        print("change dir")
        #swtich to project directory
        changeDir(args[0])
        
        print("xcodebuild opts %s" % opts)
        #execute xcodebuile
        xcbuild(opts[0][1])
    except getopt.GetoptError as e:
        # usage()
        print("error %s" % e)
        sys.exit(2)


if __name__ == '__main__':
    main()
    
    