#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

bool isValid(string passwordLine, string& password);

int main()
{
  //open passwords file

  ifstream inputFile;
  inputFile.open("input");

  vector<string> passwords;
  vector<string> validPasswords;

  //put each password's info into an element of a vector

  string currentLine;

  while(getline(inputFile,currentLine))
  {
    cout << "currentLine = " << currentLine << "\n";
    passwords.push_back(currentLine);
  }

  //check if each password is valid, adding just the password itself
  //to the vector validPasswords if true

  string currentPassword = "";

  for (int i = 0; i < passwords.size(); i++)
  {
    cout << "---------- test 1 ----------\n";
    if (isValid(passwords[i], currentPassword)) validPasswords.push_back(currentPassword);
    cout << currentPassword << " is a password that may or may not be valid\n";
  }

  //print number of valid passwords (i.e. the answer)

  cout << "Number of valid passwords = " << validPasswords.size() << "\n";
}

bool isValid(string passwordLine, string& password)
{
  int pos1,pos2 = 0;

  char selectedChar = '\0';
  int selectedCharCount = 0;
  bool charIsValid = false;

  int start = 0;
  int end = 0;

  //get pos1

  cout << "passwordLine = " << passwordLine << "\n";
  end = passwordLine.find('-');
  cout << "test 2, start = " << start << ", end = " << end << "\n";

  pos1 = stoi(passwordLine.substr(start, end-start));
  cout << "lower limit = " << pos1 << "\n";

  //get pos2

  start = end + 1;
  end = passwordLine.find(' ');

  pos2 = stoi(passwordLine.substr(start, end-start));
  cout << "upper limit = " << pos2 << "\n";

  //get selectedChar

  start = end + 1;

  cout << "start = " << start << ", end = " << end << "\n";

  selectedChar = passwordLine[start];
  cout << "selected char = " << selectedChar << "\n";

  start += 3;

  //get password

  password = passwordLine.substr(start, passwordLine.size()-start+1);
  cout << "password = " << password << "\n";

  //count occurrences of selectedChar in password

  /*
  start = 0;
  end = 0;

  for (int i = 0; i < password.size(); i++)
  {
    cout << "processing [" << password[i] << "]\n";
    if (password[i]==selectedChar) selectedCharCount++;
    cout << "selectedCharCount now " << selectedCharCount << "\n";
  }

  cout << "selectedCharCount = " << selectedCharCount << "\n";

  //if the char occurs at least as much as the pos1 and no more
  //than the pos2, the password is valid

  if (selectedCharCount >= pos1 && selectedCharCount <= pos2)
  {
    charIsValid = true;
  }*/

  //check whether exactly 1 of password[pos1-1] and password[pos2-1]
  //contain selectedChar

  return (password[pos1-1] == selectedChar) ^ (password[pos2-1] == selectedChar);
}
