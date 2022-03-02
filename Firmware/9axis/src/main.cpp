/* 
9axis: sensor BNO055 transmite información en grados de la posición del cuerpo humano
Autor: David Ávila Quezada

*/
//////////////////////////////////////////////////////////////////////////////
// Se incluyen librerias necesarias
#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#include <ESP8266_Tones.h>
#include <Wire.h>
#include <SSD1306Wire.h>
#include <image/images.h>

// se modifica funcionalidad del pin ADC, para medir carga de batería
ADC_MODE(ADC_VCC);

// Se definen variables globales
#define WIFI_SSID "FullAxis"
#define WIFI_PASS "Zk*DsU@77BzJAXNk"
#define UDP_PORT 4210 
#define Buzzer 16
#define SSD_I2c 0x3c
#define BNO055_SAMPLERATE_DELAY_MS (100)
#define ARRAY_DATA_TEMP 4

//Se crean Variables
String id_hw;
String IP;
String MAC;
float volt;
String type_hw = "9ax";
String location = "back";
String Status = "iniciando";
int Stat_in = 1;
int count = 0;
char packet_into [255];

//////////////////////////////////////////////////////////////////////////////
// Instancias de perifericos
// Instancia de la pantalla oled
SSD1306Wire display(SSD_I2c, SDA, SCL);

//Se instancia BNO
Adafruit_BNO055 bno = Adafruit_BNO055(55, 0x29);

//Se instancia Tones
ESP8266_Tones Mytone(Buzzer);

// Se instancia UDP
WiFiUDP UDP;
IPAddress remote_IP(192,168,4,1);
//UDP Buffer
char packetBuffer[UDP_TX_PACKET_MAX_SIZE];

//////////////////////////////////////////////////////////////////////////////
// Funcion de estados

void change_state(String st){
  Stat_in = st.toInt();
  
}

// funciones para display

void logo(){
  display.clear();
  display.drawXbm(0, 0, logo_fullAxis_width, logo_fullAxis_height, logo_fullAxis);
}

void conectando(){
    bool state_pin2 = digitalRead(2);
    if(state_pin2 == LOW){
      display.drawString(50,48,"conectando");
    }else{
      display.drawString(50,48,"conectando .");
    }
   
}

void batt_voltage(){
  volt = float(ESP.getVcc()/1000.0);
  String voltage;
  if(volt >= 3) voltage = "100%";
  if(volt < 3 && volt >= 2.7) voltage = "70%";
  if(volt < 2.7 && volt >= 2.6) voltage = "50%";
  if(volt < 2.6 && volt >= 2.5) voltage = "30%";
  if(volt < 2.5 && volt >= 2.422) voltage = "10%";
  if(volt < 2.422 && volt >= 2.3) voltage = "1%";
  if(volt < 2.3 && volt >= 2.2) voltage = "0%";  
  display.drawString(95, 0, voltage);
}

void error_display(String error){
  display.clear();
  display.setFont(ArialMT_Plain_16);
  display.drawString(10, 10, error);
  Serial.print(error);
  display.setFont(ArialMT_Plain_10);
  display.drawString(10, 40,ESP.getResetReason());
  display.display();
}

void Bno_adquire(){
  // se obtiene un dato
  sensors_event_t event;
  bno.getEvent(&event);
  float i;
  if(location == "back"){
    i = -1.0;
  }else{
    i = 1.0;
  }

  String yaw = String(event.orientation.heading*i);
  String pitch = String(event.orientation.pitch*i);
  String roll = String(event.orientation.roll);
  
  display.drawString(2,12, "Estado: ");
  display.drawString(40,12, Status);
  display.drawString(2,22, "roll: ");
  display.drawString(30,22, yaw);
  display.drawString(2,32, "pitch: ");
  display.drawString(30,32, pitch);
  display.drawString(2,42, "yaw: ");
  display.drawString(30,42, roll);
}

void state(int state){
  String Status_dict[] = {"inicializando","en espera",
                          "calibrando", "midiendo"};
  Status = Status_dict[state];
}

void Wifi_display(){
  display.drawLine(2,11,125,11);
  IP = WiFi.localIP().toString();
  if(WiFi.status() == WL_CONNECTED){
    display.drawCircle(7,5,4);
    display.drawCircle(7,5,2);
    display.drawString(20,0, IP); 
  }else{display.drawString(2,0,"Desconectado");}
}

//////////////////////////////////////////////////////////////////////////////
// funciones para transferencia de datos por wifi
// Envios

void UDP_send(String data){
  char Buff_send[255];
  data.toCharArray(Buff_send,255);
  UDP.beginPacket(remote_IP, UDP_PORT);
  UDP.write(Buff_send);
  UDP.endPacket();
}

void UDP_Data_info(){
  IP = WiFi.localIP().toString();
  MAC = WiFi.softAPmacAddress().c_str();
  String data_temp[ARRAY_DATA_TEMP] = {MAC, IP, id_hw, type_hw};
  String Data;
  
  for (int i=0; i < ARRAY_DATA_TEMP; i++){
    Data.concat(data_temp[i]);
    if(i<ARRAY_DATA_TEMP){
      Data.concat("-");
    }else{
      Data.concat("\r\n");
    }
  }
  UDP_send(Data);
}

void UDP_Data_bno(){
  UDP_send("Roll-pitch-yaw");
}
// Recepciones
void UDP_receiver(){
  int packetSize = UDP.parsePacket();
  char Buff_receive[255];
  if(packetSize){
    int len = UDP.read(packet_into, 255);
    if (len > 0) packet_into[len] = 0;


    //packet_into.toString()
    //UDP.read(packet,255);
    if (packet_into != Buff_receive){
          String(packet_into).toCharArray(Buff_receive, 255);
    }
  }
  display.drawString(64, 40, Buff_receive);
}

//////////////////////////////////////////////////////////////////////////////
// otras funciones de procesos 

void Wifi_connect(){
  unsigned long tiempo = 0;
  int periodo = 50;
  int turn = 0;
  
  while (WiFi.status() != WL_CONNECTED) 
  {
    if(millis() > periodo+tiempo){
      tiempo = millis();
      turn = 1;  
    }else{
      turn = 0;
    }
    if(turn == 0){
      digitalWrite(2, LOW);
      logo();
      conectando();
      display.display();

    }else{
      digitalWrite(2, HIGH);
      logo();
      conectando();
      display.display();

    }
  }
}


void standby(){
  state(Stat_in);
  //UDP_Data_info();
  display.clear();
  batt_voltage();
  Wifi_display();
  Bno_adquire();
  UDP_receiver();
  display.display();
}

//////////////////////////////////////////////////////////////////////////////

void setup() {
  //se solicita id del chip, para identificar equipo
  id_hw = String(ESP.getChipId());

  //Se inicia el display
  display.init();
  display.flipScreenVertically();
  display.clear();
  display.setFont(ArialMT_Plain_10);
  logo();

  // Salidas/Entradas
  pinMode(2, OUTPUT);
      
  // Se inicia Wifi
  WiFi.begin(WIFI_SSID, WIFI_PASS);
  WiFi.mode(WIFI_STA);

  // Se intenta conectar al receptor
  Wifi_connect();
    
  // Se inicia el puerto UDP
  display.clear();
  UDP.begin(UDP_PORT);
  digitalWrite(2, LOW);
  delay(1000);

  //Se inicia BNO055
  if (!bno.begin())
  {
    error_display("ERROR: BNO");
    while (1);
  }

  bno.setExtCrystalUse(true);

}
//////////////////////////////////////////////////////////////////////////////  
void loop() {
  standby();
     
}
