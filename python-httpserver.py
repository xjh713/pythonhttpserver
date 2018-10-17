from SimpleHTTPServer import SimpleHTTPRequestHandler
import SocketServer
import urllib
import os
      
class MyHandler(SimpleHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
       
    def do_GET(self):
        print "got get request %s" % (self.path)
        #data0 = urllib.splitquery(self.path)[0]
        hql = urllib.splitquery(self.path)[1]
        print "hql===%s" %(hql)
        
        exe_cmd = "hive -e '"+str(hql)+"'"
        print 'cmd===%s' %(exe_cmd)
        #os.system(exe_cmd)
        self.wfile.write('ssss')
          
    #curl -d "aaa" http://127.0.0.1:8090|||curl -d "select * from test;" http://127.0.0.1:8090
    def do_POST(self):
        print "got post!!"
        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len)
               
        hql = post_body
        print "hql===%s" %(hql)
        exe_cmd = "hive -e '"+str(hql)+"'"
        print 'cmd===%s' %(exe_cmd)
        #os.system(exe_cmd)
        lines_d = os.popen(exe_cmd).readlines()
        lines = ''
        for row in lines_d:
            #print row
            lines+=str(row)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(lines)
        
def start_server():
    httpd = SocketServer.TCPServer(("10.198.47.101", 8090), MyHandler)
    print 'Starting httpd...'
    httpd.serve_forever()
    
if __name__ == "__main__":
    start_server()
