#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>

using namespace std;

// A Huffman tree node
struct Node {
    char ch;
    int freq;
    Node *left, *right;
};

// Comparison object to be used to order the heap
struct compare {
    bool operator()(Node* l, Node* r) {
        return l->freq > r->freq;
    }
};

// Utility function to allocate a new tree node
Node* getNode(char ch, int freq, Node* left, Node* right) {
    Node* node = new Node();
    node->ch = ch;
    node->freq = freq;
    node->left = left;
    node->right = right;
    return node;
}

// Traverse the Huffman Tree and store Huffman Codes in a map
void encode(Node* root, string str, unordered_map<char, string> &huffmanCode) {
    if (root == nullptr)
        return;

    // Found a leaf node
    if (!root->left && !root->right) {
        huffmanCode[root->ch] = str;
    }

    encode(root->left, str + "0", huffmanCode);
    encode(root->right, str + "1", huffmanCode);
}

// Traverse the Huffman Tree and decode the encoded string
void decode(Node* root, int &index, string str) {
    if (root == nullptr)
        return;

    // Found a leaf node
    if (!root->left && !root->right) {
        cout << root->ch;
        return;
    }

    index++;

    if (str[index] == '0')
        decode(root->left, index, str);
    else
        decode(root->right, index, str);
}

// Builds Huffman Tree and decode given input text
void buildHuffmanTree(string text) {
    // Count frequency of appearance of each character
    unordered_map<char, int> freq;
    for (char ch : text) {
        freq[ch]++;
    }

    // Create a priority queue to store live nodes of Huffman tree
    priority_queue<Node*, vector<Node*>, compare> pq;

    // Create a leaf node for each character and add it to the priority queue
    for (auto pair : freq) {
        pq.push(getNode(pair.first, pair.second, nullptr, nullptr));
    }

    // Do until there is more than one node in the queue
    while (pq.size() != 1) {
        // Remove the two nodes of highest priority (lowest frequency) from the queue
        Node* left = pq.top(); pq.pop();
        Node* right = pq.top(); pq.pop();

        // Create a new internal node with these two nodes as children and with frequency equal to the sum of the two nodes' frequencies
        int sum = left->freq + right->freq;
        pq.push(getNode('\0', sum, left, right));
    }

    // Root stores pointer to the root of Huffman Tree
    Node* root = pq.top();

    // Traverse the Huffman Tree and store Huffman Codes in a map
    unordered_map<char, string> huffmanCode;
    encode(root, "", huffmanCode);

    // Print the Huffman Codes
    cout << "Huffman Codes are:\n";
    for (auto pair : huffmanCode) {
        cout << pair.first << " " << pair.second << '\n';
    }

    // Print the original string
    cout << "\nOriginal string was:\n" << text << '\n';

    // Print the encoded string
    string str = "";
    for (char ch : text) {
        str += huffmanCode[ch];
    }

    cout << "\nEncoded string is:\n" << str << '\n';

    // Traverse the Huffman Tree again and this time decode the encoded string
    cout << "\nDecoded string is:\n";
    int index = -1;
    while (index < (int)str.size() - 2) {
        decode(root, index, str);
    }
    cout << '\n';
}

int main() {
    string text = "Huffman coding is a data compression algorithm.";
    buildHuffmanTree(text);
    return 0;
}