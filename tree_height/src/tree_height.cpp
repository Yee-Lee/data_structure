#include <algorithm>
#include <iostream>
#include <vector>

#include <queue>
#include <stack>
class Node;

class Node {
public:
    int key;
    Node *parent;
    std::vector<Node *> children;

    Node() {
      this->parent = NULL;
    }

    void setParent(Node *theParent) {
      parent = theParent;
      parent->children.push_back(this);
    }
};


int main_with_large_stack_space() {
  std::ios_base::sync_with_stdio(0);
  int n;
  std::cin >> n;

  std::vector<Node> nodes;
  nodes.resize(n);
  int root_index = 0;
  for (int child_index = 0; child_index < n; child_index++) {
    int parent_index;
    std::cin >> parent_index;
    
    if (parent_index >= 0)
      nodes[child_index].setParent(&nodes[parent_index]);
    else
    {
      root_index = child_index;
    }
    
    nodes[child_index].key = child_index;
  }


// Use DFS
int maxHeight = 0;
std::queue<Node*> s;
s.push(&nodes[root_index]);
while(!s.empty()){
  int size = s.size();
  for(int i=0; i<size; i++){
    Node* nptr = s.front();
    s.pop();
    for( auto cptr : nptr->children){
      s.push(cptr);
    }
  }
  maxHeight++;
  
}

/*
  // Replace this code with a faster implementation
  int maxHeight = 0;
  for (int leaf_index = 0; leaf_index < n; leaf_index++) {
    int height = 0;
    for (Node *v = &nodes[leaf_index]; v != NULL; v = v->parent)
      height++;
    maxHeight = std::max(maxHeight, height);
  }
*/


  std::cout << maxHeight << std::endl;
  return 0;
}

int main ()
{
  return main_with_large_stack_space();
}
