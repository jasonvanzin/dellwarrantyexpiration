#!/usr/bin/python
import sys
#module used to receive command line arguments into script
#and check python version
if sys.version.startswith('2.'):
    print("Script only runs in Python 3 and above.")
    sys.exit(1)
import urllib.request #module used to request Dell webpage
import re #module used for regex

    
def getwarranty(servicetag):
    
    """ (str) -> str
    Returns date as string by downloading html as a string and performing a
    regex search to find the date. 
    >>> getwarranty('2M95GR1')
    '4/16/2014'
    >>> getwarranty('BKTR3G1')
    '4/22/2011'
    >>> getwarranty('GWQN141')
    '2/18/2006'
    """
    
    u = "http://www.dell.com/support/troubleshooting/us/en/555/servicetag/" + \
        servicetag + "#ui-tabs-5"
    f = urllib.request.urlopen(u)
    contents = str(f.read())
    f.close()
    warranty = ""
    warrantytuple = re.findall(r'(Warranty with an end date of \S+)(\d+/\d+/\d+)', contents)
    testdates = []
    i = 0
    #while loop gets the date string, converts it into integer tuples in the list testdates
    #so the dates can be compared to find which one is the greatest. Dell's warranty site
    #can have several warranty dates listed.
    while i < len(warrantytuple):
        datesplit = warrantytuple[i][1].split('/')
        testdates.append((int(datesplit[2]), int(datesplit[0]), int(datesplit[1])))
        i += 1
    maxdate = max(testdates)
    warranty = str(maxdate[1]) + '/' + str(maxdate[2]) + '/' + str(maxdate[0])
    return warranty
  
def main():
    args = sys.argv[-1] # Get last word from commandline so it can be checked to see if it's a service tag.
    if not args:
        print('usage: dellwarranty.py [servicetag]')
        sys.exit(1)
    if 'dellwarranty.py' in args:
       print('usage: dellwarranty.py [servicetag]')
       sys.exit(1)
    else:
        servicetag = sys.argv[-1]
        warrantyexpiration = getwarranty(servicetag)
        if warrantyexpiration == "":
            print("Service tag", servicetag, "not found.")
        else:
            print(warrantyexpiration)

if __name__ == '__main__':
    main()
