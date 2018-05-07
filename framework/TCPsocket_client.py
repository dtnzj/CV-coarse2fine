

import SocketServer

#定义request handler类，从BaseRequestHandler类继承
class MyTCPHandler(SocketServer.BaseRequestHandler): 
    #复写handle()方法，注意：该方法必须复写，用于处理当前的request
    def handle(self): 
        #self.request是和客户端连接的套接字，可直接使用
        self.data = 'LocationRequest'
        print(self.data)
        self.request.sendall(self.data)



if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    #传入监听地址、端口号和request handler类
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler) 
    #启动监听处理request
    server.serve_forever() 