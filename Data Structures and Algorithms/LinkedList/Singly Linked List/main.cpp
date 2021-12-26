#include <iostream>

using namespace std;

class Node {
public:
    int data;
    Node* next;
};

void print(Node* n) {
    while (n != NULL) {
        cout << n->data << " ";//0x235ed754820
        n = n->next;
    }
}

void push(Node** head_ref, int new_data)
{
    Node* new_node = new Node();// new 0x2cecc604820
    new_node->data = new_data; // head 0x2cecc6043b0
    new_node->next = (*head_ref); //0x319bbffcf8
    (*head_ref) = new_node;
}
void append(Node** head_ref, int new_data)
{

    Node* new_node = new Node();

    Node* last = *head_ref;

    new_node->data = new_data;
    new_node->next = NULL;

    if (*head_ref == NULL)
    {
        *head_ref = new_node;
        return;
    }

    while (last->next != NULL)
        last = last->next;

    last->next = new_node;
}
void insertAfter(Node* head_ref,int new_data){
    if(head_ref == NULL){
        cout << "the given previous node cannot be NULL";
        return;
    }
    Node* new_node = new Node();
    new_node->data = new_data;
    new_node->next = head_ref->next;
    head_ref->next = new_node;


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

    head->next = third->next;
//
//    cout<<"\nAfter Inserted A new Data "<<endl;
//    //push
//    push(&head , 99);
//    print(head);

//    append(&head, 88);
//    cout << "\nAfter Appended " << endl;
//    print(head);

//    insertAfter(third->next,100);
//    puts("\nAfter Inser Data");
//    print(head);



    return 0;
}