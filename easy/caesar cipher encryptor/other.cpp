// solution if we make our alphabet
#include <string>
#include <vector>
#include <iostream>

char getEncrypted(char letter, int key, std::string alphabet)
{
    int encryptedCode = alphabet.find(letter) + key;
    return alphabet[encryptedCode % 26];       
}


std::string caesarCypherEncryptor(std::string str, int key)
{
    std::vector<char> encryptedLetters;
    key = key % 26;
    std::string alphabet = "abcdefghijklmnopqrstuvwxyz";
    for (int i = 0; i < str.length(); ++i)
    {
        encryptedLetters.push_back(getEncrypted(str[i], key, alphabet));
    }

    return std::string(encryptedLetters.begin(), encryptedLetters.end());
}

int main()
{
    std::string string = "xyz";
    int key = 2;
 
    std::cout << caesarCypherEncryptor(string, key) << std::endl;
}