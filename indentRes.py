import sys
import pprint
import json

def kriti(Child,z):
	for C in M['children']:
		if 'type' in C :
			if C['type'] == 'item' and C['selected'] == 1:
				return (z+"\n-->"+C['name'])
				#print(C['name'])
				z=kriti(C['children'],z)
			else:
				return ''	
		else:
			return ''		

json_file="foodyo_output.json"
try:
	with open(json_file) as x:
		data = json.load(x)
		check = ''
		#data = json.dump(x)
		#pprint.pprint(type(data))
		#pprint.pprint(data['body']['Recommendations']['menu'])
		for R in data['body']['Recommendations']:
			pprint.pprint(R['RestaurantName'])
			for M in R['menu']:
				if M['type'] == "sectionheader":
					check = kriti(M['children'],check)
					#pprint.pprint(len(M['children']))
		print(check)			
					


except:
	print("Unexpected Error: ",sys.exc_info()[0])
	raise

#class ReadFile:
#	def __init__(self):
#		self.json_file="foodyo_output.json"
#
#	def readF(self):
#		try:
#			with open(self.json_file) as x:
#				data = json.load(x)
#				#data = json.dump(x)
#				pprint.pprint(type(data))
#		except:
#			print("Unexpected Error: ",sys.exc_info()[0])
#			raise
#
#if __name__ == '__main__':
#	F=ReadFile()
#	F.readF()					