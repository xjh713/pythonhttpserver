# pythonhttpserver
python 原生态调用server服务，接收http传递的参数并且处理返回结果

1.代码中提供了post与get两种方式来发起请求，但是传递参数时候,get的如果值里有空格会错误,使用post传递参数，即使参数值里有空格也无妨

2.接收参数值时:
  get:hql = urllib.splitquery(self.path)[1],这样接收url传递格式如此:curl http://127.0.0.1:8090?aaa   
  其中的aaa就是参数值,没有必要使用key-val格式了,如果非要用，可以这样ak=av&bk=bv 最后接收到的还是整个传递过来的ak=av&bk=bv值，还需要拆分开
  
  post:接收如下
       content_len = int(self.headers.getheader('content-length', 0))
       post_body = self.rfile.read(content_len)
       请求方式:curl -d "aaa" http://127.0.0.1:8090  接收也是整个接收,如果有多个参数值还需要拆分
