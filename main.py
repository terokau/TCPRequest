import requests
import socketserver as soc
import sys

def main():
	host,port = '192.168.1.130',60000
	
	with soc.TCPServer((host,port),TCPHandle) as server:
		server.serve_forever()
		
class TCPHandle(soc.BaseRequestHandler):
	
	def handle(self):
		conn = MyRequest()
		self.data = self.request.recv(2048).strip()
		print('From: ' , format(self.client_address[0]))
		print('Data: ' , self.data)
		self.response = conn.getRequestData(self.data)
		print('Reponse: ' , self.response)
		self.request.sendall(str.encode(self.response))
		
class MyRequest():
	
	
	def getRequestData(self,setUrl):
		self.setUrl = str(setUrl,'utf-8')
		sgetResponse = requests.get(self.setUrl)
		try:
			return sgetResponse.text
		except Exception as e:
			print(e)
			return 'Error on Request, ' 
		
if __name__ == '__main__':
	main()
	
	
