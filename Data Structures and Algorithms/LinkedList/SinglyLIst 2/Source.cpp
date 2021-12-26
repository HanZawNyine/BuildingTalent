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
void insertAfter(Node* head_ref, int new_data) {
    if (head_ref == NULL) {
        cout << "the given previous node cannot be NULL";
        return;
    }

    Node* new_node = new Node();
    new_node->data = new_data;
    new_node->next = head_ref->next;
    head_ref->next = new_node;
}

// Delete a node
void deleteNode(Node** head_ref, int key) {
    Node* temp = *head_ref;
    Node* prev = new Node();

    if (temp != NULL && temp->data == key) {
        *head_ref = temp->next;
        printf("delete address : %d\n", temp->next);
        printf("delete data : %d\n", temp->data);
        return;
    }
    // Find the key to be deleted
    while (temp != NULL && temp->data != key) {
        prev = temp;
        temp = temp->next;
    }

    // If the key is not present
    if (temp == NULL) return;

    // Remove the node
    prev->  next = temp->next;
    printf("delete address : %d\n", temp->next);
    printf("delete data : %d\n", temp->data);
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
    puts("\nAfter Delete Data");
    deleteNode(&head, 2);
    print(head);

    //cout << "\nAfter Inserted A new Data " << endl;
    ////push
    //push(&head, 99);
    //print(head);

        /*append(&head, 88);
        cout << "\nAfter Appended " << endl;
        print(head);*/

   /*  insertAfter(head->next,100);
        puts("\nAfter Insert Data");        
        print(head);*/

       
    return 0;
}