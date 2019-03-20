// donner un nom:
int led = 13;

// the setup routine runs once when you press reset:
void setup() {
  // initialiserle pin digital comme output.
  pinMode(led, OUTPUT);
  Serial.begin(115200);
}

// boucle infini:
void loop() {
  digitalWrite(led, HIGH);   // LED on (HIGH avec voltage HIGH)
  Serial.println("Hello Here");
  delay(1000);               // attendre une seconde  
  digitalWrite(led, LOW);    // LED off avec  voltage LOW
  delay(1000);               // attendre une seconde  
}
