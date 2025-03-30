#include "stdafx.h"
#include <assert.h>
#include <iostream>
#include <fstream>
#include "hashtable.h"

HashTable::HashTable(const long Size) {
    size = Size * 2; // Tamaño óptimo: 2x entradas esperadas
    collisions = 0;
    hashtable = new StringIntPair[size];
    for (long i = 0; i < size; i++) {
        hashtable[i].key = "";  // Marcador de registro vacío
        hashtable[i].data = -1; // Valor por defecto
    }
}

void HashTable::Insert(const string Key, int Data) {
    long index = Key.length() % size; // Hash simple (ejemplo)
    while (hashtable[index].key != "" && hashtable[index].key != Key) {
        index = (index + 1) % size; // Linear probing
        collisions++;
    }
    hashtable[index].key = Key;
    hashtable[index].data = Data;
}

void HashTable::Print(const string Path) const {
    ofstream file(Path);
    for (long i = 0; i < size; i++) {
        if (hashtable[i].key != "")
            file << hashtable[i].key << ";" << hashtable[i].data << ";" << i << endl;
    }
    file << "Colisiones: " << collisions << endl;
    file.close();
}