/**
 * Copyright (c) 2021 pmarques-dev @ github
 *
 * SPDX-License-Identifier: BSD-3-Clause
 */

#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/pio.h"
#include "hardware/timer.h"

#include "quadrature_encoder.pio.h"

//
// ---- quadrature encoder interface example
//
// the PIO program reads phase A/B of a quadrature encoder and increments or
// decrements an internal counter to keep the current absolute step count
// updated. At any point, the main code can query the current count by using
// the quadrature_encoder_*_count functions. The counter is kept in a full
// 32 bit register that just wraps around. Two's complement arithmetic means
// that it can be interpreted as a 32-bit signed or unsigned value, and it will
// work anyway.
//
// As an example, a two wheel robot being controlled at 100Hz, can use two
// state machines to read the two encoders and in the main control loop it can
// simply ask for the current encoder counts to get the absolute step count. It
// can also subtract the values from the last sample to check how many steps
// each wheel as done since the last sample period.
//
// One advantage of this approach is that it requires zero CPU time to keep the
// encoder count updated and because of that it supports very high step rates.
//

struct Encoders{
    int new_value;  // dene     int new_value = 0;
    int delta;
    int old_value;
} encoder[6];
    

int main() {
    for(int i=0;i<6;i++){               // we have max of four state machines
        encoder[i].new_value = 0;
        encoder[i].delta     = 0;
        encoder[i].old_value = 0;
    };
    
    //middleRight.new_value, middleRight.old_value, middleRight.delta = 0;
    //middleLeft.new_value, middleLeft.old_value, middleLeft.delta = 0;
    

    //int new_value, delta, old_value = 0;

    // Base pin to connect the A phase of the encoder.
    // The B phase must be connected to the next pin

    const uint LED_PIN = PICO_DEFAULT_LED_PIN;
    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);
    stdio_init_all();
    
    const uint PIN_AB_middleRight = 12;  // middle right wheel pins 
    const uint PIN_AB_middleLeft = 20;  // middle left wheel pins 
    const uint PIN_AB_frontRight = 16;  // middle right wheel pins 
    const uint PIN_AB_frontLeft = 18;  // middle left wheel pins 
    const uint PIN_AB_rearRight = 2;  // middle right wheel pins 
    const uint PIN_AB_rearLeft = 10;  // middle left wheel pins 

    PIO pio_0 = pio0;
    PIO pio_1 = pio1;
    
    const uint sm_mR = 2; // state machine 0 (sm0) is dedicated for middle right wheel // FOR ILE DONDUR
    const uint sm_mL = 3; // state machine  1 (sm1) is dedicated for middle left wheel
    const uint sm_fR = 0; // state machine 0 (sm0) is dedicated for middle right wheel // FOR ILE DONDUR
    const uint sm_fL = 1; // state machine  1 (sm1) is dedicated for middle left wheel
    const uint sm_rR = 0; // state machine 0 (sm0) is dedicated for middle right wheel // FOR ILE DONDUR
    const uint sm_rL = 1; // state machine  1 (sm1) is dedicated for middle left wheel
    
    uint offset_0 = pio_add_program(pio_0, &quadrature_encoder_program);
    uint offset_1 = pio_add_program(pio_1, &quadrature_encoder_program);
    
    quadrature_encoder_program_init(pio_0, sm_mR, offset_0, PIN_AB_middleRight, 0);
    quadrature_encoder_program_init(pio_0, sm_mL, offset_0, PIN_AB_middleLeft, 0);
    
    quadrature_encoder_program_init(pio_0, sm_fR, offset_0, PIN_AB_frontRight, 0);
    quadrature_encoder_program_init(pio_0, sm_fL, offset_0, PIN_AB_frontLeft, 0);

    quadrature_encoder_program_init(pio_1, sm_rR, offset_1, PIN_AB_rearRight, 0);
    quadrature_encoder_program_init(pio_1, sm_rL, offset_1, PIN_AB_rearLeft, 0);

    while (1) {
        // note: thanks to two's complement arithmetic delta will always
        // be correct even when new_value wraps around MAXINT / MININT
        for(int i=0;i<4;i++){
            encoder[i].new_value = quadrature_encoder_get_count(pio_0, i);
            encoder[i].delta = encoder[i].new_value - encoder[i].old_value;
            encoder[i].old_value = encoder[i].new_value;
        };
        for(int i=4;i<6;i++){
            encoder[i].new_value = quadrature_encoder_get_count(pio_1, i-4);
            encoder[i].delta = encoder[i].new_value - encoder[i].old_value;
            encoder[i].old_value = encoder[i].new_value;
        };        
        if(encoder[0].delta > 0 ){
            gpio_put(LED_PIN, 1);
        }
        else if(encoder[0].delta < 0) {
            gpio_put(LED_PIN,0);
        }
        else{
        }

        printf("fRP %8d,fRS %6d,fLP %8d,fLS %6d,mRP %8d,mRS %6d,mLP %8d,mLS %6d,rRP %8d,rRS %6d,rLP %8d,rLS %6d,\n", encoder[0].new_value, encoder[0].delta, encoder[1].new_value, encoder[1].delta, encoder[2].new_value, encoder[2].delta, encoder[3].new_value, encoder[3].delta, encoder[4].new_value, encoder[4].delta, encoder[5].new_value, encoder[5].delta);
        sleep_ms(250);
    }
}

