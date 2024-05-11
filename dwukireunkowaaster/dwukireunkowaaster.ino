#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>


 #define CE_PIN  9
 #define CSN_PIN 10


const byte pipe [][6] = {"00006", "00003"};

RF24 radio(CE_PIN, CSN_PIN);
int data;
short int channel = 200;
uint8_t adres[2] = {0, 1};


void setup()
{

  radio.begin();
  radio.setChannel(channel);
  radio.setPALevel(RF24_PA_MAX);
  radio.setDataRate(RF24_250KBPS);
  radio.openWritingPipe(pipe[0]); // zapis
  radio.openReadingPipe(1, pipe[1]); // odczyt

  Serial.begin(9600);

  delay(5000);
Serial.println("start");
}


int odebrane;
void loop()
{

  if(Serial.available()){
    String d =&Serial.readStringUntil('\n')[0];
    data=atoi(&d[0]);
    Serial.println("nadawanie");
    Serial.println(data);
    delay(2);
    radio.stopListening();  
    radio.write( data, sizeof(data) );
    delay(2);
    radio.startListening();
  }
   radio.startListening();
    if ( radio.available() )
    {
      radio.read( odebrane, sizeof(odebrane) );
      Serial.println("odebrano");
      Serial.println(odebrane);
    }
}

