#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

 #define CE_PIN  9
 #define CSN_PIN 10


const byte pipe [][6] = {"00003", "00006"};

RF24 radio(CE_PIN, CSN_PIN);
short int channel = 200;
uint8_t adres[2] = {0, 1};

struct Data{
  float a;
};
Data data;
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
int nadaj=0;
void loop()
{
  if(nadaj==1){
    delay(5);
    radio.stopListening();  
    Serial.println("nadano ");
    Serial.println(data.a);
    radio.write( &data, sizeof(Data) );
    delay(2);
    nadaj=0;
  }

    radio.startListening();
    if ( radio.available() )
    {
      radio.read( &data, sizeof(Data) );
      nadaj=1;
      Serial.println("odebrano ");
      Serial.println(data.a);

    }
  }

