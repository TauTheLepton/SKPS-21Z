#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
// #include <string.h>
// #include <pthread.h>
#include <gpiod.h>

const unsigned int pin_buzzer = 12;
// int koniec = 0;
// pthread_t pid1, pid2;


// //Funkcje drukujące komunikat co pewien czas
// void * drukuj1(void * arg)
// {
//     while(1) {
//         printf("Komunikat z wątku A\n");
//         usleep(1110000);
//     }
// }

// void * drukuj2(void * arg)
// {
//     while(1) {
//         printf("Komunikat z wątku B\n");
//         usleep(723000);
//     }
// }


int main(int argc, char *argv[])
{
    // pthread_create(&pid1,NULL,drukuj1,NULL);
    // pthread_create(&pid2,NULL,drukuj2,NULL);
    // pthread_join(pid1,NULL);
    // pthread_join(pid2,NULL);
    struct gpiod_chip gpio_chip0 = gpio_chip_open();
    struct gpiod_line *buzz;
    buzz = gpiod_chip_get_line(chip, pin_buzzer);
    gpiod_line_request_output(buzz, "example1", 0);
    int intensity;
    // pinMode(pinPWM, PWM_OUTPUT);
    float time = 1000;
    while(1)
    {
        for(intensity=1; intensity<1000; intensity++)
        {
            gpiod_line_set_value(buzz, 1);
            usleep(time*intensity);
            gpiod_line_set_value(buzz, 0);
            usleep(time*(1000-intensity));
        }
    }
    return 0;
}
