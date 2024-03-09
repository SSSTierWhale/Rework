/*
** EPITECH PROJECT, 2024
** Uhd in C
** File description:
** struct
*/

#ifndef INCLUDED_STRUCT_H
    #define INCLUDED_STRUCT_H

typedef struct items_s {
    char *name;
    double weight;
} items_t;

typedef struct items_array_s {
    items_t *items;
    int size;
} items_array_t;

#endif
