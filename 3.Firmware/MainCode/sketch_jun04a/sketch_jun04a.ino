#include <Servo.h>
#include <SPI.h>


Servo ESC;  // create servo object to control a servo
Servo steer;  // create servo object to control a servo
Servo fservo, bservo, tservo;
Servo pan;

int fon = 45, foff = 120, bon = 160, boff = 50, ton = 40, toff = 110, pan_angle = 50;
int var1, var2, var3;
int dvel, dsteer_angle;
int car_vel = 1500;
int steer_angle = 93;
String buffer, tempo;

void setup() {
 Serial.begin(115200);
 Serial.setTimeout(1);
 pan.attach(9);
 ESC.attach(11);
 steer.attach(10);
 fservo.attach(7);
 bservo.attach(6);
 tservo.attach(5);
 pan.write(pan_angle);
 ESC.write(car_vel);
 steer.write(steer_angle);
 //Serial.print("starting....");
 delay(50);

}
void loop() {

  float  time_beg = millis();
  while (!Serial.available()){
    if((millis() - time_beg) > 500) ESC.write(1500);
    }
  tempo = Serial.readString();
  clearSerial();
  divide_strings(tempo);
  if(tempo[0] == 'V'){  //adjust the car velocity
    if(var1 == 0) ;
    else dvel = var1;
    dsteer_angle = -1*var2/20;
    linear_speed(dvel);
    steering_angle(dsteer_angle);
  }
  else if(tempo[0] == 'D'){ // adjust the differential servos
    diff_servos(var1, var2, var3);
  }
  else if(tempo[0] == 'C'){ // adjust the differential servos
    if(var1 == 0) ;
    else dvel = var1;
    if (var2 == 0) ;
    else dsteer_angle = -1*var2/10.91 + 92.25;
    linear_speed(dvel);
    steering_angle_2(dsteer_angle);
  }
  else if(tempo[0] == 'P'){ // adjust the differential servos
    pan_angle = pan_angle + var1;
    if(pan_angle>100) pan_angle = 100;
    else if(pan_angle<0) pan_angle = 0;
    pan.write(pan_angle);
    Serial.println(pan_angle);
    delay(15);
  }

  

}


void linear_speed(int dvel){
 car_vel = 1500 + dvel;
 if(car_vel > 2000) car_vel =2000;
 if(car_vel < 1000) car_vel = 1000;
 ESC.write(car_vel);
 
 
  
}


void steering_angle(int dsteer_angle){
 steer_angle = steer_angle + dsteer_angle;
 //Serial.println(steer_angle);
 if(steer_angle > 120) steer_angle =120;
 if(steer_angle < 65) steer_angle = 65;
 steer.write(steer_angle);

}

void steering_angle_2(int dsteer_angle){
 steer_angle = dsteer_angle;
 //Serial.println(steer_angle);
 if(steer_angle > 120) steer_angle =120;
 if(steer_angle < 65) steer_angle = 65;
 steer.write(steer_angle);

}


void diff_servos(int front, int back, int takviye){
  if(front == 1) fservo.write(fon);
  else if(front == 0) fservo.write(foff);
  if(back == 1) bservo.write(bon);
  else if(back == 0) bservo.write(boff);
  if(takviye == 1) tservo.write(ton);
  else if(takviye == 0) tservo.write(toff);
  delay(50);
}


void divide_strings(String datas){
  String strs[10];
  int StringCount = 0;

  //buffer = datas.readStringUntil('\n');
  buffer = datas;
  //Serial.println(buffer); //Printing for debugging purpose
  while (buffer.length() > 0)
  {
    int index = buffer.indexOf(' ');
    if (index == -1) // No space found
    {
      strs[StringCount++] = buffer;
      break;
    }
    else
    {
      strs[StringCount++] = buffer.substring(0, index);
      buffer = buffer.substring(index+1);
    }
    }

    var1 = strs[1].toInt();
    var2 = strs[2].toInt();
    //Serial.println(var1);
    //Serial.println(var2);
    //return_value[0] = var1;
    //return_value[1] = var2;
    
    if(StringCount == 3) {
      //return return_value;
    }
    else if(StringCount == 4) {
      var3 = strs[3].toInt();
      //Serial.println(var3);
      //return_value[2] = var3;
      //return return_value;
    }
  

    
  
}

void clearSerial(){
  int temp = Serial.available();
  for(int i = 0; i < temp; i++) Serial.read();
}
