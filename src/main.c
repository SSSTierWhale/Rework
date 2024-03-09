/*
** EPITECH PROJECT, 2024
** Uhd in C
** File description:
** main
*/
#include "../include/src.h"
#include "../include/struct.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

items_array_t init_items(void)
{
    static items_t items[] = {
        {"Boruto", 1.363231749397397},
        {"Power of Sage", 2.744466559315083},
        {"Elite Ninjutsu ninja random card", 0.7591290519388293},
        {"Ascension optional pack", 0.18203094526069427},
        {"Elite Genjutsu ninja random card", 0.7591290519388293},
        {"Elite Taijutsu ninja random card", 0.7591290519388293},
        {"Refined stone", 4.57377754218217},
        {"Potential Stone", 2.744466559315083},
        {"Soul jade", 5.03185541542062},
        {"Random Red Exclusive Pack", 0.18203094526069427},
        {"Fire Talisan", 0.06401088184991446},
        {"Blade", 0.06401088184991446},
        {"Hizuren Hat", 0.06401088184991446},
        {"Water Dragon Armor", 0.06401088184991446},
        {"Rare Fire Secrets", 0.06401088184991446},
        {"Hiruzen Garment", 0.06401088184991446},
        {"Shisui Garment", 0.06401088184991446},
        {"Hayate boots", 0.06401088184991446},
        {"Silver Pin", 0.06401088184991446},
        {"Fire Badge", 0.06401088184991446},
        {"Orange Mask", 0.06401088184991446},
        {"Fire Ring", 0.06401088184991446},
        {"Red Comma", 0.06401088184991446},
        {"Gold Rope", 0.06401088184991446},
        {"Nara Medicine", 0.06401088184991446},
        {"Chiyo Garment", 0.06401088184991446},
        {"Random Rank Ss Summon Scroll shard", 3.658621965734173},
        {"Expert Enhancement Stone", 2.5244291529560017},
        {"Enhance Stone Pack", 2.5244291529560017},
        {"SSR Yang/Yin Random Pack", 1.5552643949471403},
        {"24-hour-ninja EXP scroll", 4.57377754218217},
        {"24-hour-ryo chest", 4.57377754218217},
        {"24-hour-ninja soul energy", 5.946010821839711},
        {"24-hour-forbidden scroll chest", 2.744466559315083},
        {"Combine a random rank S summoned beast", 5.488933118630166},
        {"Basic Shape Pill", 4.57377754218217},
        {"8-hour-ninja soul energy", 9.148555254393244},
        {"Advance Enhancement Stone", 2.5244291529560017},
        {"Expert forge stone (1)", 2.744466559315083},
        {"Expert forge stone (2)", 1.3722332796575416},
        {"8-hour-forbidden scroll chest", 5.946010821839711},
        {"Random Rank A Summon Scroll shard", 7.318244101497252},
        {"Advanced forge stone", 2.5614354440254834},
        {"SR Ninjutsu random card", 2.5244291529560017},
        {"SR Genjutsu random card", 2.5244291529560017},
        {"SR Taijutsu random card", 2.5244291529560017},
        {"Basic Enhancement Stone", 2.5244291529560017}
    };
    items_array_t result = {items, sizeof(items) / sizeof(items[0])};
    return result;
}

int main(void)
{
    srand(time(NULL));
    items_array_t items = init_items();
    char input[100];

    do {
        printf("How many summons do you want to do ? (Use 'quit' to leave) ");
        scanf("%s", input);

        if (strcmp(input, "quit") == 0) {
            break;
        }
        int numInvocations = atoi(input);
        if (numInvocations < 1 || numInvocations > 10) {
            printf("Invalid amount of summons\n");
        } else {
            summon(items.items, items.size, numInvocations);
        }
    } while (1);

    return 0;
}