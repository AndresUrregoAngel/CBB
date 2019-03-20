/*
 * IoT Button
 */

#include <ESP8266WiFi.h>
int value = 1;
const char* ssid     = "BdeB";  
const char* password = ""; 
 
int BUTTON_PIN= D2;   // D2 pin du ESP8266 12E board
int LED =16;          // D0 pin du ESP8266 12E board
const char* host = "maker.ifttt.com";     //IFTTT channel address
int buttonState = LOW;

void setup() {
  pinMode(BUTTON_PIN, INPUT);
  pinMode(LED,OUTPUT);
  Serial.begin(115200);
  digitalWrite(LED,LOW); // By default Off state
  Serial.println("Button not pressed");
  }

void loop() {
   buttonState = digitalRead(BUTTON_PIN);

    if (buttonState == HIGH) {   
      
       if (value == 1){
      Serial.println("Button Pressed");//button is pulled down to ground via 10k resistor  
         WiFi.disconnect();
        Serial.println("Deconnexion");
       WiFi.begin(ssid, password); // connecting to wifi
       Serial.println("Connexion"); 
int led = HIGH;  
       while (WiFi.status() != WL_CONNECTED) {
        Serial.print(".");
       delay(500);

     //Flash de la LED
    digitalWrite(LED, led);
    led = !led;
  }
  digitalWrite(LED, LOW);//eteindre la LED

       }
       Serial.println("WiFi connecté, Adresse IP: "); 
       Serial.println(WiFi.localIP());
       digitalWrite(LED,HIGH);  // LED turns On
       WiFiClient client;
       const int httpPort = 80;
       if (!client.connect(host, httpPort)) {
        Serial.println("Réseau faible");
       return;
       }
       // On crée notre URI pour le request
       String url = "/trigger/bdeb/with/key/bkYVveqwpz733INwSDuKG9";   //lien pour le trigger de l’event avec key et nom event 
  
       // Envoi du request vers le server
       client.print(String("GET ") + url + " HTTP/1.1\r\n" + "Host: " + host + "\r\n" + "Connection: close\r\n\r\n");  // GET request 
       
       value = 0;
       delay(5000);
       digitalWrite(LED,LOW);  // LED turns Off
       }
    
    else{
    value = 1;
    delay(500);
    }
}
