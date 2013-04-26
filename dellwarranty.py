#!/usr/bin/python
import sys #module used to receive command line arguments into script and check python version
if sys.version.startswith('2.'):
    print("Script only runs in Python 3 and above.")
    sys.exit(1)
import urllib.request #module used to request Dell webpage
    
def getwarranty(servicetag):
    
    """ (str) -> str
    Returns date as string by downloading html as a string and performing a regex search
    to find the date. 
    >>> getwarranty('2M95GR1')
    '1/16/2013'
    >>> getwarranty('BKTR3G1')
    '4/22/2011'
    >>> getwarranty('GWQN141')
    '12/18/2006'
    """
    
    u = "http://www.dell.com/support/troubleshooting/us/en/555/servicetag/" + servicetag + \
        "#ui-tabs-5"
    f = urllib.request.urlopen(u)
    contents = str(f.read())
    f.close()
    i = 0
    warranty = ""
    while True:
        i = contents.find('TopTwoWarrantyListItem', i)
        if i == -1:
            break
        i = contents.find('>', i + 1)
        i = contents.find('>', i + 1)
        i = contents.find('>', i + 1)
        i = contents.find('>', i + 1)
        j = contents.find('<', i + 1)
        warranty = contents[i+1:j]

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
