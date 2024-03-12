package main

import (
	"crypto/tls"
	"fmt"
	"os"
	"time"

	mqtt "github.com/eclipse/paho.mqtt.golang"
)

var broker = "ssl://9b6c1af8442543edbffca7a1864df2e3.s1.eu.hivemq.cloud:8883"
var username = "rnicola"     // Use seu nome de usuário real aqui
var password = "cellarDoor1" // Use sua senha real aqui

var handler mqtt.MessageHandler = func(client mqtt.Client, msg mqtt.Message) {
	fmt.Printf("Received message: %s from topic: %s\n", msg.Payload(), msg.Topic())
}

func main() {
	opts := mqtt.NewClientOptions()
	opts.AddBroker(broker)
	opts.SetClientID("go_mqtt_client")
	opts.SetUsername(username)
	opts.SetPassword(password)
	opts.SetDefaultPublishHandler(handler)
	opts.OnConnect = func(c mqtt.Client) {
		fmt.Println("Connected")
	}
	opts.SetTLSConfig(&tls.Config{InsecureSkipVerify: true, ClientAuth: tls.NoClientCert})

	client := mqtt.NewClient(opts)
	if token := client.Connect(); token.Wait() && token.Error() != nil {
		fmt.Println(token.Error())
		os.Exit(1)
	}

	subTopics := map[string]byte{
		"meuTesteIoT/sensor/radiacao_solar": 0,
		"meuTesteIoT/sensor/temperatura":    0,
	}

	for topic := range subTopics {
		if token := client.Subscribe(topic, 0, nil); token.Wait() && token.Error() != nil {
			fmt.Println(token.Error())
			os.Exit(1)
		}
	}

	fmt.Println("Subscribed to topics")
	time.Sleep(60 * time.Second) // Mantém a conexão aberta por um tempo

	client.Disconnect(250)
	fmt.Println("Disconnected")
}
