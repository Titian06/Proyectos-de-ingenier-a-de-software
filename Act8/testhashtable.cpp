/* Filename:  testhashtable.cc
 * Author:    Susan Gauch
 * Date:      2/25/09
 * Purpose:   A test file for a hashtable of words and numbers.
*/

#include <iostream>

#include "hashtable.h"

using namespace std;

int main()
{
const unsigned long HT_SIZE = 500;
HashTable Ht(HT_SIZE);

   Ht.Print("dict.txt");
   Ht.Insert ("Susan", 9);
   Ht.Insert ("John", 6);
   Ht.Insert ("David", 42);
   Ht.Print("dict.txt");
   cout << "David's magic number is: " << Ht.GetData("David") << endl;
}
