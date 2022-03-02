/*
Receptor FullAxis
Autor: David Ávila Quezada

*/
//////////////////////////////////////////////////////////////////////////////

// Se incluyen librerias necesarias
#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

// Se definen variables globales
#define AP_SSID "FullAxis"
#define AP_PASS "Zk*DsU@77BzJAXNk"
#define UDP_PORT 4210
int incomingByte = 0; // for incoming serial data

IPAddress remote_IP(192, 168, 4, 100);

// Se instancia UDP
WiFiUDP UDP;
IPAddress local_IP(192, 168, 4, 1);
IPAddress gateway(192, 168, 4, 1);
IPAddress subnet(255, 255, 255, 0);

// UDP Buffer
char packetBuffer[UDP_TX_PACKET_MAX_SIZE];
// Se crean Variables
int inByte = 0;
//////////////////////////////////////////////////////////////////////////////
// funciones para transferencia de datos por wifi

void UDP_receiver()
{
  char packet[255];
  int packetSize = UDP.parsePacket();
  if (packetSize)
  {
    UDP.read(packet, 255);
    Serial.println(packet);
  }
}

// Envios

void UDP_send(String data)
{
  char Buff_send[255];
  data.toCharArray(Buff_send, 255);
  UDP.beginPacket(remote_IP, UDP_PORT);
  UDP.write(Buff_send);
  UDP.endPacket();
}

//////////////////////////////////////////////////////////////////////////////
void setup()
{

  // Setup LED pin
  pinMode(2, OUTPUT);
    digitalWrite(2, LOW);

  // Setup serial port
  Serial.begin(115200);

  // Begin Access Point
  WiFi.softAPConfig(local_IP, gateway, subnet);
  WiFi.softAP(AP_SSID, AP_PASS, 1, 1);
  Serial.println(WiFi.localIP());

  // Begin listening to UDP port
  UDP.begin(UDP_PORT);
}

void loop()
{
    digitalWrite(2, HIGH);

  // send data only when you receive data:
  if (Serial.available() > 0)
  {
    inByte =Serial.read();
    if(inByte == 51){
            UDP_receiver();
    }
  }
}

/*
 if(Serial.available()>0){
   byte coming = Serial.read();
   //incoming[index++] = coming;
   if(coming != 10){
   Serial.print("imprimo: ");
   Serial.println(coming, HEX);
   }
   //UDP_send(coming);


   //UDP.parsePacket();
   //UDP.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE);


 }
 // Receive packet
 //UDP.parsePacket();
 //UDP.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE);
 //if (packetBuffer[0]){
 //  digitalWrite(2, HIGH);
   //Serial.println(packetBuffer);
//  } else {
//   digitalWrite(2, LOW);
// }

} */