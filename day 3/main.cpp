#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

class World
{
  public:
    vector<vector<bool>>trees;
    int worldHeight;
    int worldWidth;
};

class Player
{
public:
  Player(int xPos, int yPos);
  int x;
  int y;
  bool moveTo(int xPos, int yPos, World world);
  int treesHit;
  long treeMultiplier;
};

Player::Player(int xPos, int yPos)
{
  x = xPos;
  y = yPos;
};

bool Player::moveTo(int xPos, int yPos, World world)
{
  x = (xPos % world.worldWidth);
  y = yPos;

  /*for (int i = 0; i < world.trees[y].size(); i++)
  {
    cout << (world.trees[y][i] ? "#" : ".");
  }
  cout << "\n";
  cout << "y = " << y << "\n";*/
  return world.trees[y][x];
};

int main()
{
  //open input file of trees

  ifstream inputFile;
  inputFile.open("input");

  string currentTreeChars;
  vector<bool>currentTreeLine;

  World world1;

  while(getline(inputFile,currentTreeChars))
  {
    currentTreeLine = {};
    for (int i = 0; i < currentTreeChars.size(); i++)
    {
      currentTreeLine.push_back((currentTreeChars[i]=='#'));
    }
    world1.trees.push_back(currentTreeLine);
  }

  world1.worldHeight = world1.trees.size();
  world1.worldWidth = world1.trees[1].size();

  //create player1

  Player player1(0,0);

  while(player1.y < world1.worldHeight-1)
  {
    player1.treesHit += player1.moveTo(player1.x+3, player1.y+1, world1);
    //cout << "player1.x = " << player1.x << ", player1.y = " << player1.y << "\n";
  }

  cout << "The player encountered " << player1.treesHit << " trees\n";


  //part 2



  player1.treeMultiplier = 0;

  int xIncrements [5] = {1,3,5,7,1};
  int yIncrements [5] = {1,1,1,1,2};

  for (int i = 0; i < 5; i++)
  {
    player1.x = 0;
    player1.y = 0;
    player1.treesHit = 0;

    while(player1.y < world1.worldHeight-1)
    {
      player1.treesHit += player1.moveTo(player1.x + xIncrements[i], player1.y + yIncrements[i], world1);
      //cout << "player1.x = " << player1.x << ", player1.y = " << player1.y << "\n";
    }

    cout << fixed << "Current trees hit = " << player1.treesHit << ", tree multiplier is currently " << player1.treeMultiplier << "\n";

    player1.treeMultiplier = ((player1.treeMultiplier==0) ? player1.treesHit : player1.treeMultiplier * player1.treesHit);
  }

  cout << fixed << "Tree multiplier = " << player1.treeMultiplier << "\n";
}
