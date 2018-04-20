#include <iostream>
using namespace std;

struct Node {
  int data;
  Node* left;
  Node* right;
};

Node* GetNewNode(int data) {
  Node* newNode = new Node();
  newNode->data = data;
  newNode->left = newNode->right = NULL;
  return newNode;
}

Node* Insert(Node* root, int data){
  if(root == NULL){
    root = GetNewNode(data);
  }
  else if(data <= root->data){
    root->left = Insert(root->left, data);
  }
  else{
    root->right = Insert(root->right, data);
  }
  return root;
}

bool Search(Node* root, int data){
  if (root == NULL){
    return false;
  }
  else if (root->data == data){
    return true;
  }
  else if (data <= root->data){
    return Search(root->left, data);
  }
  else{
    return Search(root->right, data);
  }
}

Node* findMin(Node* root){
  while(root->left != NULL){
    root = root->left;
  }
  return root;
}

void InOrder(Node* root){
  if(root==NULL){
    return;
  }
  InOrder(root->left);
  cout << root->data << " ";
  InOrder(root->right);
}

int main() {
  Node* root = NULL;
  root = Insert(root,15);
	root = Insert(root,10);
	root = Insert(root,20);
	root = Insert(root,25);
	root = Insert(root,8);
	root = Insert(root,12);

  int number;
  cout << "Enter a number to search\n";
  cin >> number;

  if (Search(root, number)==true){
    cout << "Found\n";
  }
  else{
    cout << "Not Found\n";
  }
  cout << "Min : " << findMin(root)->data << endl;

  cout << "Inorder: ";
  InOrder(root);
  cout << "\n";
}
