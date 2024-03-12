package main

import (
	"bytes"
	"crypto/tls"
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"time"

	mqtt "github.com/eclipse/paho.mqtt.golang"
)

var brokerAddress string = "9b6c1af8442543edbffca7a1864df2e3.s1.eu.hivemq.cloud"
var port = 8883
var topic = "my/test/topic"
var username = "rnicola"
var password = "cellarDoor1"
var apiURL string = "http://localhost:5000/data"

var messagePubHandler mqtt.MessageHandler = func(client mqtt.Client, msg mqtt.Message) {
	fmt.Printf("Received message: %s from topic: %s\n", msg.Payload(), msg.Topic())

	// Constrói os dados a serem enviados
	data := map[string]interface{}{
		"valor": string(msg.Payload()),
	}

	// Envia os dados para a API
	err := postDataToAPI(apiURL, data)
	if err != nil {
		fmt.Println("Failed to post data to API:", err)
		return
	}

	fmt.Println("Data posted to API successfully")
}

var connectHandler mqtt.OnConnectHandler = func(client mqtt.Client) {
	fmt.Println("Connected to MQTT Broker")
	client.Subscribe(topic, 1, nil)
}

func postDataToAPI(url string, data map[string]interface{}) error {
	jsonData, err := json.Marshal(data)
	if err != nil {
		return err
	}

	response, err := http.Post(url, "application/json", bytes.NewBuffer(jsonData))
	if err != nil {
		return err
	}
	defer response.Body.Close()

	// Aqui você pode adicionar qualquer processamento adicional baseado na resposta
	if response.StatusCode != http.StatusCreated {
		return fmt.Errorf("received non-201 status code %d", response.StatusCode)
	}

	return nil
}

func main() {
	opts := mqtt.NewClientOptions()
	opts.AddBroker(fmt.Sprintf("ssl://%s:%d", brokerAddress, port)) // Corrigido para formatar a porta corretamente
	opts.SetClientID("go_mqtt_client")
	opts.SetUsername(username)
	opts.SetPassword(password)
	opts.SetDefaultPublishHandler(messagePubHandler)
	opts.OnConnect = connectHandler

	opts.SetTLSConfig(&tls.Config{InsecureSkipVerify: true})

	client := mqtt.NewClient(opts)
	if token := client.Connect(); token.Wait() && token.Error() != nil {
		fmt.Println(token.Error())
		os.Exit(1)
	}

	// Publicando uma mensagem
	msg := "Hello from Go client"
	token := client.Publish(topic, 0, false, msg)
	token.Wait()

	time.Sleep(30 * time.Second) // Manter o cliente rodando por algum tempo

	client.Disconnect(250)
	fmt.Println("Disconnected from MQTT Broker")
}
