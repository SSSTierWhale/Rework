/*
** EPITECH PROJECT, 2024
** Rework
** File description:
** summons
*/
#include "../include/src.h"
#include "../include/struct.h"

void unit_summon(unit_t *units, int numUnits, int numSummons)
{
    int i;
    char summons[10][100] = {0};
    double totalDropRate = 0;

    for (i = 0; i < numUnits; i++) {
        totalDropRate += units[i].drop_rate;
    }
    for (i = 0; i < numSummons; i++) {
        double randomNum = (double)rand() * totalDropRate / RAND_MAX;
        double currentDropRate = 0;
        for (int j = 0; j < numUnits; j++) {
            currentDropRate += units[j].drop_rate;
            if (randomNum < currentDropRate) {
                sprintf(summons[i], "Unit Summon: Summoned %s", units[j].name);
                break;
            }
        }
    }
    for (i = 0; i < numSummons; i++) {
        if (strlen(summons[i]) > 0) {
            printf("%s\n", summons[i]);
        }
    }
}

void unit_wish_summon(unit_array_t unit_array)
{
    char input[100];
    printf("\033[1;34mHow many summons do you want to do ? \033[0m");
    scanf("%s", input);
    int numInvocations = atoi(input);
    if (numInvocations < 1 || numInvocations > 10) {
        printf("\033[1;31mInvalid amount of summons\033[0m\n");
    } else {
        printf("\033[1;32m");
        unit_summon(unit_array.units, unit_array.size, numInvocations);
        printf("\033[0m");
    }
}
