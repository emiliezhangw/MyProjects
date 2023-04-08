// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
//const unsigned int N = 26;
const unsigned int N = 17576;
int num = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    node *cursor = table[hash(word)];
    while (cursor != NULL)
    {
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    free(cursor);
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int hash;
    if (strlen(word) > 2)
    {
        hash = (toupper(word[0]) - 'A') * 26 * 26 + (toupper(word[1]) - 'A') * 26 + toupper(word[2]) - 'A';
    }
    else if (strlen(word) > 1)
    {
        hash = (toupper(word[0]) - 'A') * 26 + (toupper(word[1]) - 'A');
    }
    else
    {
        hash = (toupper(word[0]) - 'A') * 26;
    }
    //return (toupper(word[0]) - 'A') * 26 + (toupper(word[1]) - 'A');
    //return toupper(word[0]) - 'A';
    return hash;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    //Open dictionary file
    FILE *file = fopen(dictionary, "r");
    char word[LENGTH + 1];
    if (file == NULL)
    {
        return false;
    }
    //Read strings from file one at a time
    //while (fscanf(file, "%s", word) != EOF)
    while (fscanf(file, "%s", word) == 1)
    {
        //Create a new node for each word
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }
        strcpy(n->word, word);
        //Hash word to obtain a hash value
        //Insert node into hash table at that location
        if (table[hash(word)] == NULL)
        {
            n->next = NULL;
            table[hash(word)] = n;
        }
        else
        {
            n->next = table[hash(word)];
            table[hash(word)] = n;
        }
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *n = table[i];
        while (n != NULL)
        {
            num++;
            n = n->next;
        }
    }
    return num;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *tmp = cursor->next;
            free(cursor);
            cursor = tmp;
        }
    }
    return true;
}
