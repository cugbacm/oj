#!/usr/bin/env python
import pika
import sys

def sendRunID(runID):
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
	channel = connection.channel()
	channel.queue_declare(queue='task_queue', durable=True)
	channel.basic_publish(
		exchange='',
	    routing_key='task_queue',
	    body=runID,
	    properties=pika.BasicProperties(
	    delivery_mode = 2, # make message persistent
	))
	print "send %r" % (runID,)
	connection.close()