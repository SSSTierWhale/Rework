/*
** EPITECH PROJECT, 2024
** Uhd in C
** File description:
** main
*/
#include "../include/src.h"
#include "../include/struct.h"

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

unit_array_t init_units(void)
{
    static unit_t units[] = {
        {"Hidan", 1.0/28},
        {"Kakuzu", 1.0/28},
        {"Jiraya", 1.0/28},
        {"Deidara", 1.0/28},
        {"Kisame", 1.0/28},
        {"Naruto (4-tailed)", 1.0/28},
        {"Tsunade", 1.0/28},
        {"Orochimaru", 1.0/28},
        {"Sasori", 1.0/28},
        {"Sasuke (Juin)", 1.0/28},
        {"Tobi", 1.0/28},
        {"Zetsu", 1.0/28},
        {"Hiruzen Sarutobi", 1.0/28},
        {"Itachi", 1.0/28},
        {"Mei", 1.0/28},
        {"Fourth Raikage A", 1.0/28},
        {"Onoki", 1.0/28},
        {"Konan", 1.0/28},
        {"Danzo", 1.0/28},
        {"[Kazekage] Gaara", 1.0/28},
        {"Hundred Seal Sakura", 1.0/28},
        {"[5th Hokage] Tsunade", 1.0/28},
        {"Asura Path", 1.0/28},
        {"Killer B", 1.0/28},
        {"Sage Kabuto", 1.0/28},
        {"Minato", 1.0/28},
        {"Shisui", 1.0/28},
        {"Pain", 1.0/28},
        {"Choji", 2.0/28},
        {"Shino", 2.0/28},
        {"Shikamaru", 2.0/28},
        {"Kurenai", 2.0/28},
        {"Asuma", 2.0/28},
        {"Naruto (Part II)", 2.0/28},
        {"Temari", 2.0/28},
        {"Hinata", 2.0/28},
        {"Kankuro", 2.0/28},
        {"Kabuto", 2.0/28},
        {"Sasuke (Part II)", 2.0/28},
        {"Lee", 2.0/28},
        {"Tenten", 2.0/28},
        {"Might Guy", 2.0/28},
        {"Kakashi", 2.0/28},
        {"Ino", 2.0/28},
        {"Gaara", 2.0/28},
        {"Kiba", 2.0/28},
        {"Yamato", 2.0/28},
        {"Kimimaro", 2.0/28},
        {"Sakura (Part II)", 2.0/28},
        {"Neji", 2.0/28},
        {"Sai", 2.0/28},
        {"Haku", 2.0/28},
        {"Zabuza", 2.0/28},
        {"Suigetsu", 2.0/28},
        {"Karin", 2.0/28},
        {"Jyugo", 2.0/28},
        {"Sakon & Ukon", 3.0/15},
        {"Tayuya", 3.0/15},
        {"Sasuke (Part I)", 3.0/15},
        {"Shiranui Genma", 3.0/15},
        {"Naruto (Part I)", 3.0/15},
        {"Iruka", 3.0/15},
        {"Hayate", 3.0/15},
        {"Tayuya", 3.0/15},
        {"Kidomaru", 3.0/15},
        {"Yoroi", 3.0/15},
        {"Mizuki", 3.0/15},
        {"Jirobo", 3.0/15},
        {"Kotetsu", 3.0/15},
        {"Sakura (Part I)", 3.0/15},
        {"Shizune", 3.0/15},
        {"Izumo", 3.0/15},
        {"Zaku", 94.0/5},
        {"Kin", 94.0/5},
        {"Dosu", 94.0/5},
        {"Gozu", 94.0/5},
        {"Meto", 94.0/5}
    };
    unit_array_t unit_array = {units, sizeof(units) / sizeof(units[0])};
    return unit_array;
}

int main(void)
{
    srand(time(NULL));
    items_array_t items = init_items();
    unit_array_t units = init_units();
    int choix;

    do {
        printf("\033[1;34m1. Ninja wish summon\n2. Ninja\n3. Summons\n4. Help\n5. Quit\nEnter your choice: \033[0m");
        scanf("%d", &choix);
        switch (choix) {
            case 1: ;
                ninja_wish_summon(items.items, items.size);
                break;
            case 2:
                break;
            case 3:
                unit_wish_summon(units);
                break;
            case 4:
                break;
            case 5:
                break;
            default:
                printf("\033[1;31mInvalid choice. Please enter a number between 1 and 5.\033[0m\n");
        }
    } while (choix != 5);
    return 0;
}
