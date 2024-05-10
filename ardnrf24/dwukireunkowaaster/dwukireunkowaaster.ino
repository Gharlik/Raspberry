#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

 #define CE_PIN  9
 #define CSN_PIN 10


const byte pipe [][6] = {"00006", "00003"};

RF24 radio(CE_PIN, CSN_PIN);
int data[1];
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
Serial.print("start");
}


unsigned long zapamietanyCzas = 0;
unsigned long roznicaCzasu = 5000UL;
int i=1;
int odebrane[1];
bool odebrano=false;
void loop()
{

  if(millis()-zapamietanyCzas>roznicaCzasu){
    data[0] =i;
    Serial.print("nadawanie");
    Serial.print(data[0]);
    Serial.print("\n");
    delay(2);
    radio.stopListening();  
    radio.write( data, sizeof(data) );
    delay(2);
    zapamietanyCzas = millis();
    radio.startListening();

//     while(odebrano==false){
//       radio.startListening();
//       if ( radio.available() )
//       {
//         radio.read( odebrane, sizeof(odebrane) );
//         Serial.print("odebrano");
//         Serial.print(odebrane[0]);
//         Serial.print("\n");
//         if(odebrane==data+1){
//           odebrano=true;
//         }else{
//           delay(2);
//           Serial.print("nadawanie");
//           Serial.print(data[0]);
//           Serial.print("\n");
//           radio.stopListening();  
//           radio.write( data, sizeof(data) );
// delay(2);
//         }
//       }
//     }


    i++;
  }
   radio.startListening();
    if ( radio.available() )
    {
      radio.read( odebrane, sizeof(odebrane) );
      Serial.print("odebrano");
      Serial.print(odebrane[0]);
      Serial.print("\n");
    }
}

