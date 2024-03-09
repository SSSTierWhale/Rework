/*
** EPITECH PROJECT, 2024
** Uhd in C
** File description:
** ninja_wish
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "../include/struct.h"

void summon(items_t *items, int numItems)
{
    int i;
    char summons[10][100] = {0};
    double totalWeight = 0;

    for (i = 0; i < numItems; i++) {
        totalWeight += items[i].weight;
    }

    for (i = 0; i < 10; i++) {
        double currentWeight = 0;
        for (int j = 0; j < numItems; j++) {
            double randomNum = (double)rand() * totalWeight / RAND_MAX;
            currentWeight += items[j].weight;
            if (randomNum < currentWeight) {
                sprintf(summons[i], "Ninja Wish: Summoned %s", items[j].name);
                break;
            }
        }
    }
    for (i = 0; i < 10; i++) {
        if (strlen(summons[i]) > 0) {
            printf("%s\n", summons[i]);
        }
    }
}
