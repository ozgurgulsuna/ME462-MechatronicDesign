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
} encoder[8];
    

int main() {
    for(int i=0;i<4;i++){               // we have max of four state machines
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
    const uint PIN_AB_middleLeft = 10;  // middle left wheel pins 

    PIO pio = pio0;
    
    const uint sm_mR = 0; // state machine 0 (sm0) is dedicated for middle right wheel // FOR ILE DONDUR
    const uint sm_mL = 1; // state machine  1 (sm1) is dedicated for middle left wheel

    uint offset = pio_add_program(pio, &quadrature_encoder_program);
    quadrature_encoder_program_init(pio, sm_mR, offset, PIN_AB_middleRight, 0);
    quadrature_encoder_program_init(pio, sm_mL, offset, PIN_AB_middleLeft, 0);

    while (1) {
        // note: thanks to two's complement arithmetic delta will always
        // be correct even when new_value wraps around MAXINT / MININT
        for(int i=0;i<2;i++){
            encoder[i].new_value = quadrature_encoder_get_count(pio, i);
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

        printf("position1 %8d, delta %6d, position2 %8d, delta %6d\n", encoder[0].new_value, encoder[0].delta, encoder[1].new_value, encoder[1].delta);
        sleep_ms(100);
    }
}

