using namespace std;

class HashTable {
public:
    HashTable(const long Size); 
    ~HashTable();
    void Insert(const string Key, int Data);
    int GetData(const string Key);
    void Print(const string Path) const;
    long GetCollisions() const;

private:
    struct StringIntPair {
        string key;
        int data;
    };
    StringIntPair *hashtable;
    long size;
    long collisions;
};

class PostingFile { 
public:
    PostingFile(const long Size);
    void Insert(int DocID, float Weight);
    void Print(const string Path) const;

private:
    struct PostingEntry {
        int docid;
        float weight;
    };
    PostingEntry *postingfile;
    long size;
};
