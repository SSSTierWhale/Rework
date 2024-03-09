/*
** EPITECH PROJECT, 2024
** Uhd in C
** File description:
** ninja_wish
*/
#include "../include/src.h"
#include "../include/struct.h"

void summon(items_t *items, int numItems, int numSummons)
{
    int i;
    char summons[10][100] = {0};
    double totalWeight = 0;

    for (i = 0; i < numItems; i++) {
        totalWeight += items[i].weight;
    }
    for (i = 0; i < numSummons; i++) {
        double randomNum = (double)rand() * totalWeight / RAND_MAX;
        double currentWeight = 0;
        for (int j = 0; j < numItems; j++) {
            currentWeight += items[j].weight;
            if (randomNum < currentWeight) {
                sprintf(summons[i], "Ninja Wish: Summoned %s", items[j].name);
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

void ninja_wish_summon(items_t *items, int size)
{
    char input[100];
    printf("\033[1;34mHow many summons do you want to do ? \033[0m");
    scanf("%s", input);
    int numInvocations = atoi(input);
    if (numInvocations < 1 || numInvocations > 10) {
        printf("\033[1;31mInvalid amount of summons\033[0m\n");
    } else {
        printf("\033[1;32m");
        summon(items, size, numInvocations);
        printf("\033[0m");
    }
}
