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
  int lowerLimit,upperLimit = 0;
  char selectedChar = '\0';
  int selectedCharCount = 0;
  bool charIsValid = false;

  int start = 0;
  int end = 0;

  //get lowerLimit

  cout << "passwordLine = " << passwordLine << "\n";
  end = passwordLine.find('-');
  cout << "test 2, start = " << start << ", end = " << end << "\n";

  lowerLimit = stoi(passwordLine.substr(start, end-start));
  cout << "lower limit = " << lowerLimit << "\n";

  //get upperLimit

  start = end + 1;
  end = passwordLine.find(' ');

  upperLimit = stoi(passwordLine.substr(start, end-start));
  cout << "upper limit = " << upperLimit << "\n";

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

  start = 0;
  end = 0;

  for (int i = 0; i < password.size(); i++)
  {
    cout << "processing [" << password[i] << "]\n";
    if (password[i]==selectedChar) selectedCharCount++;
    cout << "selectedCharCount now " << selectedCharCount << "\n";
  }

  cout << "selectedCharCount = " << selectedCharCount << "\n";

  //if the char occurs at least as much as the lowerLimit and no more
  //than the upperLimit, the password is valid

  if (selectedCharCount >= lowerLimit && selectedCharCount <= upperLimit)
  {
    charIsValid = true;
  }
  return charIsValid;
}
