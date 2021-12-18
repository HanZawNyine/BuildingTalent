#include <iostream>

using namespace std;

class Node {
public:
    int data;
    Node* next;
};

void print(Node* n) {
    while (n != NULL) {
        cout << n->data << " ";
        n = n->next;
    }
}

void push(Node** head_ref, int new_data)
{
    Node* new_node = new Node();
    new_node->data = new_data;
    new_node->next = (*head_ref);
    (*head_ref) = new_node;
}

int main()
{
    Node* head = NULL;
    Node* second = NULL;
    Node* third = NULL;

    head = new Node();
    second = new Node();
    third = new Node();

    head->data = 1;
    head->next = second;
    second->data = 2;
    second->next = third;
    third->data = 3;
    third->next = NULL;

    print(head);

    cout<<"\nAfter Inserted A new Data "<<endl;
    //push
    push(&head , 99);

    print(head);

    return 0;
}