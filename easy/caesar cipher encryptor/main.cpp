#include <string>
#include <vector>
#include <iostream>

char getEncrypted(char letter, int key)
{
    int encryptedLetterCode = letter + key;                                     // increase letter code by key
    return encryptedLetterCode <= 122 ? encryptedLetterCode : 96 + encryptedLetterCode % 122;       // range is 96 - 122 
}


std::string caesarCypherEncryptor(std::string str, int key)
{
    key = key % 26;                                                // key might be greater than alpbhabet's lenght and we can get ot of it that is how we solve it
    std::vector<char> encrypterdLetters;

    for (int i = 0; i < str.length(); ++i)
    {
        encrypterdLetters.push_back(getEncrypted(str[i], key));          // get the encrypted letter and push it to our vector of chars
    }

    return std::string(encrypterdLetters.begin(), encrypterdLetters.end());     // make vector of chars into string to show it
}

int main()
{
    std::string string = "xyz";
    int key = 2;

    std::cout << caesarCypherEncryptor(string, key) << std::endl;
}