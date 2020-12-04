#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;


int main()
{
  //open input file of trees

  ifstream inputFile;
  inputFile.open("input");

  vector<string> fields = {"byr","iyr","eyr","hgt","hcl","ecl","pid"};
  int numberOfValidPassports;
  string data;

  ostringstream ss;
  ss << inputFile.rdbuf();
  data = ss.str();

  for (int i = 0; i < 100;i+=2)
  {
    if (data[i]=='\n' && data[i+1]=='\n')
    {
      //cout<<"$\n$\n";
    }
    else
    {
      //cout << data[i] << data[i+1];
    }
  }
  //cout << "\ndata = \n" << data.substr(0,100) << "\n~~~~~\n";

  vector <vector<vector<string>>> passports;
  vector <string> currentFields;
  int start = 0;
  int end = 0;

    vector<string> currentUnprocessedPassport;

  while(start < data.size())
  {
    string currentLine;
    vector <vector<string>> currentPassport;

    //printf("start = %d, data.size() = %ld", start, data.size());
    end = data.find('\n',start);
    //cout << "\n[ end = " << end << "]\n";
    //cout << "*****[" << data.substr(start, end-start) << "]*****\n";

    currentLine = (data.substr(start, end-start));

    //cout << "\n\nVVVVVVVVVV\n[" << currentLine << "]" << ((currentLine=="") ? " yes":" no") << "\n^^^^^^^^^^\n\n";

    if (currentLine == "")
    {
      //cout << "currentUnprocessedPassport.size() = " << currentUnprocessedPassport.size() << "\n";
      for (int i = 0; i < currentUnprocessedPassport.size(); i++)
      {
        //cout << "test 1\n";
        vector<string> currentPair;
        string currentUnsplitPair;
        int start = 0;
        int end = 0;

        while(start < currentUnprocessedPassport[i].size())
        {
                  //cout << "test 2\n";
          end = currentUnprocessedPassport[i].find(' ',start);


          if (end<0)
          {
            end = currentUnprocessedPassport[i].size()-1;
          }

          currentUnsplitPair = currentUnprocessedPassport[i].substr(start,end-start);

          //cout << currentUnsplitPair << "\n";

          int colonPos = currentUnsplitPair.find(':');
          currentPair.push_back(currentUnsplitPair.substr(0, colonPos));

          //cout << "colonPos = " << colonPos << " > " << currentUnsplitPair << " < " << currentUnsplitPair.size() << "\n";

          currentPair.push_back(currentUnsplitPair.substr(colonPos, currentUnsplitPair.size()-1-colonPos));
          currentPassport.push_back(currentPair);

          //cout << "currentPair[0] = " << currentPair[0] << "\n";

          start = end+1;
        }
        currentUnprocessedPassport.clear();
      }
      passports.push_back(currentPassport);
      //cout << "size = " << passports.size() << "\n";
      currentPassport.clear();
    }
    else
    {
      currentUnprocessedPassport.push_back(currentLine);
    }


    start = end+1;
  }
    /*
  while(start < data.size())
  {
    printf("-----\n1: start: %d, end: %d\n", start, end);
    end = data.substr(start).find("\n\n");
    cout << ">" << data.substr(start, 20) << "<\n";

    cout << "{" << end-start << "}\n";

    cout << "#####[" << data.substr(start,end-start) << "]#####\n";

    printf("2: start: %d, end: %d\n", start, end);
    splitData.push_back(data.substr(start, end-start));
    printf("3: start: %d, end: %d\n", start, end);
    start = end+2;
    printf("4: start: %d, end: %d\n", start, end);

  }*/


  for (int i = 0; i < passports.size(); i++)
  {
    for (int j = 0; j < passports[i].size(); j++)
    {
      for (int k = 0; k < passports[i][j].size(); k++)
      {
        printf("passport %d, field %d, part %d = ",i,j,k);
        cout << passports[i][j][k] << "\n";
      }
    }
  }
}
