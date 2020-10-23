import requests
import socketserver as soc
import xml.etree.ElementTree as ET
import sys

def main():

	settings = ET.parse('conf.xml')
	root = settings.getroot()
	allowedHosts = []
	
	host = root.find('address').text
	port = int(root.find('port').text)
	hosts = root.find('hosts')
	for i in hosts.findall('host'):
		print(i.get('address'))
		allowedHosts.append(i.attrib)
	print('Starting open of server: ' , host, ' : ' , port)

	with soc.TCPServer((host,port),TCPHandle) as server:
		server.serve_forever()


class TCPHandle(soc.BaseRequestHandler):

	def handle(self):
		conn = MyRequest()
		getClientAddress = self.client_address[0]
		if(getClientAddress in allowedHosts):
			self.data = self.request.recv(2048).strip()
			print('From: ' , format(self.client_address[0]))
			print('Data: ' , self.data)
			self.response = conn.getRequestData(self.data)
			print('Reponse: ' , self.response)
			self.request.sendall(str.encode(self.response))
		else:
			print("not allowerd from: " + getClientAddress)

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
