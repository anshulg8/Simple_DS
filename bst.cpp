#include <iostream>
using namespace std;

struct Node {
  int data;
  Node *left;
  Node *right;
};

Node* GetNewNode(int data) {
  Node *newNode = new Node();
  newNode->data = data;
  newNode->left = newNode->right = NULL;
  return newNode;
}

Node* Insert(Node *root, int data){
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

bool Search(Node *root, int data){
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

Node* findMin(Node *root){
  while(root->left != NULL){
    root = root->left;
  }
  return root;
}

Node* findMax(Node *root){
  while(root->right != NULL){
    root = root->right;
  }
  return root;
}

void InOrder(Node *root){
  if(root==NULL){
    return;
  }
  InOrder(root->left);
  cout << root->data << " ";
  InOrder(root->right);
}

// Returns no. of edges in longest path from root to a leaf node.
int findHeight(Node *root){
  if(root==NULL) return -1;
  return max(findHeight(root->left),findHeight(root->right))+1;
}

bool isBST(Node *root, Node *l = NULL, Node *r = NULL){
    if (root == NULL) return true;
    if (l != NULL and root->data < l->data) return false;
    if (r != NULL and root->data > r->data) return false;
    return isBST(root->left, l, root) and isBST(root->right, root, r);
}

Node* Delete(Node *root, int data){
  if(root == NULL) return root;
  else if(data < root->data){
    root->left = Delete(root->left, data);
  }
  else if(data > root->data){
    root->right = Delete(root->right, data);
  }
  // When node to be deleted is found
  else{
    // Case1: No child
    if(root->left == NULL && root->right == NULL){
      delete root;
      root = NULL;
    }
    // Case2: One child
    else if(root->left == NULL){
      Node *temp = root;
      root = root->right;
      delete temp;
    }
    else if (root->right == NULL){
      Node *temp = root;
      root = root->left;
      delete temp;
    }
    // Case3: 2 children
    else{
      Node *temp = findMin(root->right);
      // Node *temp = findMax(root->left);
      root->data = temp->data;
      root->right = Delete(root->right, temp->data);
    }
  }
  return root;
}

int main() {

  Node *root = NULL;
  root = Insert(root,15);
	root = Insert(root,10);
	root = Insert(root,20);
	root = Insert(root,25);
	root = Insert(root,8);
	root = Insert(root,12);

  root = Delete(root,25);

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
  cout << "Max : " << findMax(root)->data << endl;

  if (isBST(root)){
    cout << "Is BST" << endl;
  }
  else{
    cout << "Not a BST" << endl;
  }

  cout << "Height of BST : " << findHeight(root) << endl;

  cout << "Inorder: ";
  InOrder(root);
  cout << "\n";
}
