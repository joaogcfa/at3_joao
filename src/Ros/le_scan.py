#! /usr/bin/env python
# -- coding:utf-8 --

import rospy
import numpy as np
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import LaserScan

distancia = 0

def scaneou(dado):
	# print("Faixa valida: ", dado.range_min , " - ", dado.range_max )
	# print("Leituras:")
	# print(np.array(dado.ranges).round(decimals=2)[0])
	# #print("Intensities")
	#print(np.array(dado.intensities).round(decimals=2))
	global distancia
	distancia = np.array(dado.ranges).round(decimals=2)[0]
	
v = 0.3
w = np.pi/4

if __name__=="__main_":

	rospy.init_node("le_scan")

	velocidade_saida = rospy.Publisher("/cmd_vel", Twist, queue_size = 3 )
	recebe_scan = rospy.Subscriber("/scan", LaserScan, scaneou)

	while not rospy.is_shutdown():
		while distancia > 0.98:
			velocidade = Twist(Vector3(v, 0, 0), Vector3(0, 0, 0))
			velocidade_saida.publish(velocidade)
		if distancia <= 0.98:
			velocidade = Twist(Vector3(-v, 0, 0), Vector3(0, 0, 0))
			velocidade_saida.publish(velocidade)