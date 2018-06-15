#include <iostream>
#include <queue>
using namespace std;

struct Node {
  int data;
  Node *left, *right;
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
  if(root == NULL) return;
  Node* current = root;
  while(current->left != NULL){
    current = current->left;
  }
  return current;
}

Node* findMax(Node *root){
  // Using iteration
  if(root == NULL) return;
  Node* current = root;
  while(current->right != NULL){
    current = current->right;
  }
  return current;
}

Node* findMax2(Node *root){
  // Using recursion
  if(root == NULL) return;
  else if(root->right == NULL){
    return root;
  }
  return findMax(root->right);
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

void InOrder(Node *root){
  if(root==NULL) return;
  InOrder(root->left);
  cout << root->data << " ";
  InOrder(root->right);
}

bool isIdentical(Node *root1, Node *root2){
  if(root1 == NULL && root2 == NULL){
    return true;
  }
  else if((root1->data == root2->data) &&
          isIdentical(root1->left, root2->left) &&
          isIdentical(root1->right, root2->right)){
            return true;
  }
  else{
    return false;
  }
}

int findHeight(Node *root){
  // Returns no. of edges in longest path from root to a leaf node.
  if(root==NULL) return -1;
  return max(findHeight(root->left),findHeight(root->right))+1;
}

void LevelOrder(Node* root){
  if(root == NULL) return;
  queue<Node*> Q;
  Q.push(root);
  while(!Q.empty()){
    Node* current = Q.front();
    cout << current->data << endl;
    if(current->left != NULL) Q.push(current->left);
    if(current->right != NULL) Q.push(current->right);
    Q.pop();
  }
}

bool isLeaf(Node* root){
  return (root->left == NULL and root->right == NULL);
}

bool isBST(Node *root, Node *l = NULL, Node *r = NULL){
    if (root == NULL) return true;
    if (l != NULL and root->data < l->data) return false;
    if (r != NULL and root->data > r->data) return false;
    return isBST(root->left, l, root) and isBST(root->right, root, r);
}

bool isIdentical(Node *root1, Node* root2){
  if(root1 != root2){
    return false;
  }
  else if((root1->data == root2->data) &&
           isIdentical(root1->left, root2->left) &&
           isIdentical(root1->right, root2->right)){
             return true;
  }

int main() {

  Node *root = NULL;
  root = Insert(root,15);
	root = Insert(root,10);
	root = Insert(root,20);
	root = Insert(root,25);
	root = Insert(root,8);
	root = Insert(root,12);

  Node *root1 = NULL;
  root1 = Insert(root1,15);
	root1 = Insert(root1,10);
	root1 = Insert(root1,20);
	root1 = Insert(root1,25);
	root1 = Insert(root1,8);
	root1 = Insert(root1,12);

  if (isIdentical(root, root1)){
    cout << "Identical";
  }
  else{
    cout << "Not identical";
  }

  // root = Delete(root,25);
  //
  // int number;
  // cout << "Enter a number to search\n";
  // cin >> number;
  //
  // if (Search(root, number)==true){
  //   cout << "Found\n";
  // }
  // else{
  //   cout << "Not Found\n";
  // }
  // cout << "Min : " << findMin(root)->data << endl;
  // cout << "Max : " << findMax(root)->data << endl;
  //
  // if (isBST(root)){
  //   cout << "Is BST" << endl;
  // }
  // else{
  //   cout << "Not a BST" << endl;
  // }
  //
  // cout << "Height of BST : " << findHeight(root) << endl;
  //
  // cout << "Inorder: ";
  // InOrder(root);
  // cout << "\n";
}
