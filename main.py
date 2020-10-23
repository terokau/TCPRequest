import requests
import socketserver as soc
import xml.etree.ElementTree as ET
import sys

def main():

	settings = ET.parse('conf.xml')
	root = settings.getroot()
	
	for child in root.findall('address'):
		host = child.text

	for child in root.findall('port'):
		port = int(child.text)

	#host = root.find('address').text
	#port = int(root.find('port').text)
	#host = 'localhost'
	#port = 9000
	print('Starting open of server: ' , host, ' : ' , port)

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

		try:
			getResponse = requests.get(self.setUrl)
			return getResponse.text
		except Exception as e:
			print(e)
			return 'Error on Request, '

if __name__ == '__main__':
	main()
