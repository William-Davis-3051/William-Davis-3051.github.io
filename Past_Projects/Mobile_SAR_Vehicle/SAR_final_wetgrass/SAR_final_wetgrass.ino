int RelaySAR = 11;
int count; 
int RelayWheel = 10      ;
void setup() {
  // Set RelayPin as an output pin
  Serial.begin(9600);
  pinMode(RelayWheel, OUTPUT);
  pinMode(RelaySAR, OUTPUT);
  digitalWrite(RelayWheel, LOW);
  digitalWrite(RelaySAR, LOW);
}
 
void loop() {
  // Let's turn on the relay...
  digitalWrite(RelayWheel, HIGH);
  digitalWrite(RelaySAR, HIGH);
  Serial.println("starting");
  delay(15000);
  //Pausing to get everything out of the way
  digitalWrite(RelayWheel, LOW);
  Serial.println("running");
  delay(11250);
  //run for 11.25 seconds
  Serial.println("stopping");
  //digitalWrite(RelayPin, LOW);
  
  for (int i = 0; i <= 45; i++) {
    count = count + 1;
    digitalWrite(RelayWheel, HIGH);
    delay(500);
    //stabilizing
    digitalWrite(RelaySAR, LOW);
    Serial.println("taking the picture");
    delay(1500);
    //move car to next position
    digitalWrite(RelaySAR, HIGH); 
    digitalWrite(RelayWheel, LOW);
    Serial.println(count);
    delay(1525);
  }
  
  digitalWrite(RelayWheel, LOW);
  digitalWrite(RelaySAR, HIGH);
  Serial.println("Going after the delay");
  delay(11000);
  digitalWrite(RelayWheel, HIGH);
}
