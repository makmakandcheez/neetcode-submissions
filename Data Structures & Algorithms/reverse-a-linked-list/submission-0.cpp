/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseHelper(ListNode* head, ListNode* caller) {
        if (head==nullptr) return caller;
        ListNode* temp = reverseHelper(head->next, head);
        head->next = caller;
        return temp;
    }

    ListNode* reverseList(ListNode* head) {
        return reverseHelper(head, nullptr);
    }
};
