using namespace std;


struct StringIntPair {
    char key[15];     // 15 bytes
    int numdocs;      // 4 bytes
    long start;       // 4 bytes (posición en posting file)
    // Total: 23 bytes → Ajustar a 24 bytes para alineación
};

// En PostingFile
struct PostingEntry {
    int docid;        // 4 bytes
    double weight;    // 8 bytes (TF-IDF)
    long next;        // 4 bytes
    // Total: 16 bytes (80/16 = 5 registros por lectura)
};