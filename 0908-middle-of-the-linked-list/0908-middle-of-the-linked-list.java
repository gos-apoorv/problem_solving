/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {

    // Slowhead to loop through linkedlist in 1 step
    ListNode slowHead = head;
    // Slowhead to loop through linkedlist in 2 step
    ListNode fastHead = head;

    while(fastHead.next != null && fastHead.next.next != null){
        slowHead = slowHead.next;
        fastHead = fastHead.next.next;
    }

    if(fastHead.next != null){
        slowHead = slowHead.next;
    }

    return slowHead; 
    }
}