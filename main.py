import urllib.request
import time, sys

def notfound(url, line):
    req = urllib.request.Request(url[:-2])
    resp = urllib.request.urlopen(req).read().decode("utf-8")
    found = resp.find("data-context-item-id=")
    vId = resp[found+22:found+33]
    print(vId, line)
    return vId

class YouTubeSongs2video:
    
    def __init__(self, incomeFileData, outputfile, encoding='utf-8'):
        self.incomeFileData = incomeFileData
        self.outputfile = outputfile
        self.encoding = encoding
        self.outputfile = open(outputfile, mode="a")
        

        
    def songsIntoUrl(self):
        with open(self.incomeFileData, encoding=self.encoding) as inputfile:
            for line in inputfile:
                song = line.replace(" ", "+")
                url = "http://youtube.com/results?search_query={}".format(song)
                req = urllib.request.Request(url)
                resp = urllib.request.urlopen(req).read().decode("utf-8")
                found = resp.find("data-context-item-id=")
                vId = resp[found+22:found+33]
                if vId == '__video_id_':
                    vId = notfound(url, line)
                    if vId == '__video_id_':
                        vId = 'error'
                        #break
                
                videoUrl = "http://www.youtube.com/watch?v={}\n".format(vId)
                self.outputfile.write(videoUrl)
                print('Song {} was found at url {}'.format(line, videoUrl))
                #time.sleep(5)
                


def main():
    if len(sys.argv) < 2:
        print("Usage: script.py input.txt output.txt")
    ex = YouTubeSongs2video(sys.argv[1], sys.argv[2])
    ex.songsIntoUrl()

if __name__ == '__main__':
    main()
    
