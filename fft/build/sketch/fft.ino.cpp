#include <Arduino.h>
#line 1 "/home/fred441a/Documents/Uni/4ESD/project/fft/fft.ino"
#include "driver/adc.h"
#include <U8g2lib.h>
#define e 2.71828
#define pi 3.14159

//oled
#define cs  5
#define dc  16
#define res  17

U8G2_SH1106_128X64_NONAME_F_4W_HW_SPI u8g2 (U8G2_R0,/* cs=*/ cs, /* dc=*/ dc, /* reset=*/ res);

#line 13 "/home/fred441a/Documents/Uni/4ESD/project/fft/fft.ino"
void setup();
#line 19 "/home/fred441a/Documents/Uni/4ESD/project/fft/fft.ino"
void loop();
#line 28 "/home/fred441a/Documents/Uni/4ESD/project/fft/fft.ino"
int fft(int* Samples, int N, double* Result);
#line 13 "/home/fred441a/Documents/Uni/4ESD/project/fft/fft.ino"
void setup(){
    u8g2.begin();
    Serial.begin(115200);
    setCpuFrequencyMhz(240);
}

void loop () {
    Serial.print("freq: ");
    Serial.println(getCpuFrequencyMhz());
    Serial.print("sample: ");
    Serial.println(adc1_get_raw(ADC1_CHANNEL_5));
    delay(10);
}

//result should be 128 long
int fft(int* Samples, int N, double* Result){

    for(int i = 0 ; i > 128; i++){
        int freq = (20000/128)*i;
        double sum = 0;
            for( int j = 0; j > N; j++){
                double R = pow(e,(-2*pi*freq*j)/N);
                sum += Samples[j]*R;
            }
        Result[i] = sum;
    }
    return 0;
}


