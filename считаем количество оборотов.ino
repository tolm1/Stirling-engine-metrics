unsigned long rm = 0;
unsigned long now = 0;
unsigned long timeold = 0;


void setup ()
{
  pinMode (8, INPUT);   // module digital output connected to Arduino pin 8
  Serial.begin(9600);   // initialize serial
}
void loop ()
{
  String data = String(rm*60.0*1000.0/(millis()));
  Serial.println(data + "," +millis() );
  if (digitalRead(8) == HIGH) {
    rm++;
    timeold = millis();
  }
  if(millis() - timeold > 3000){
    timeold = millis();
    rm = 0;
  }
  delay(50); // wait 50 milliSeconds
}
