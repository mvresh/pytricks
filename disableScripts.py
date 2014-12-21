def disableScripts ( directoryStart ) :
    os.path.walk( directoryStart, callback, '' )

def callback ( args, directory, files ) :
    print 'Scanning',directory
    for fileName in files:
        if os.path.isfile( os.path.join(directory,fileName) ) :
            if string.lower(os.path.splitext(fileName)[1]) in ['.html','.htm'] :
                disableScriptFromHtml ( os.path.join(directory,fileName) )

def disableScriptFromHtml ( filepath ) :
    print '  Processing',os.path.split(filepath)[1]
    file = open(filepath, 'rb')
    html = file.read()
    file.close()
    regexp = re.compile(r'<script.*?>', re.IGNORECASE)
    html = regexp.sub('<script language="MonthyPythonsScript">',html)
    file = open(filepath, 'w+')
    file.write(html)
    file.close()

if len(sys.argv) > 1 :
    stripscripts( sys.argv[1] )
else:
    print message
    
