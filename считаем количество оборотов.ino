unsigned long rm = 0;
unsigned long now = 0;
unsigned long timeold = 0;


void setup ()
{
  //pinMode (13, OUTPUT); // built-in LED pin set to output
  pinMode (8, INPUT);   // module digital output connected to Arduino pin 8
  Serial.begin(9600);   // initialize serial
}
void loop ()
{
  //Serial.println(rm); // display analog and digital values to serial
  //Serial.println(rm*60.0*1000.0/(millis() - timeold));
  //Serial.println(millis() - timeold);
  String data = String(rm*60.0*1000.0/(millis()));
  //Serial.println(data);
  Serial.println(data + "," +millis() );
  //Serial.println();
  if (digitalRead(8) == HIGH) {
    rm++;
    timeold = millis();
  }
  if(millis() - timeold > 3000){
    timeold = millis();
    rm = 0;
  }
  //timeold = millis();
  delay(50); // wait 100 milliSeconds
}