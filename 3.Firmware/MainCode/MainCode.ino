#include <Servo.h>
#include <SPI.h>


Servo ESC;  // create servo object to control a servo
Servo steer;  // create servo object to control a servo
Servo fservo, bservo, tservo;

int fon, foff, bon, boff, ton, toff;
int var1, var2, var3;
int dvel, dsteer_angle;
int car_vel = 0;
int steer_angle = 93;
String buffer, tempo;

void setup() {
 Serial.begin(115200);
 Serial.setTimeout(1);
 ESC.attach(9);
 steer.attach(8);
 fservo.attach(7);
 bservo.attach(6);
 tservo.attach(5);
 ESC.write(car_vel);
 steer.write(steer_angle);
}
void loop() {
  while (!Serial.available());
  tempo = Serial.readString();
  clearSerial();
  //Serial.println(tempo[0]);
  divide_strings(tempo);
  if(tempo[0] == 'V'){
    dvel = 2*var1;
    dsteer_angle = var2;
    //Serial.println(vel);
    //Serial.println(steer_angle);
    linear_speed(dvel);
    steering_angle(dsteer_angle);
  }
  else if(tempo[0] == 'D'){
    diff_servos(var1, var2, var3);
  }
  if (!Serial.available()){
    car_vel = 0;
    //steer_angle = 93;
    ESC.write(car_vel);
    //steer.write(steer_angle);
  }
  

}


void linear_speed(int dvel){
 car_vel = car_vel + dvel;
 if(car_vel > 180) car_vel =180;
 if(car_vel < 0) car_vel = 0;
 ESC.write(car_vel);
 delay(40);
 
  
}


void steering_angle(int dsteer_angle){
 steer_angle = steer_angle + dsteer_angle;
 if(steer_angle > 130) steer_angle =130;
 if(steer_angle < 55) steer_angle = 55;
 steer.write(steer_angle);
 delay(40);
  
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
