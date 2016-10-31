package linkedlist;

public class Node {
	int data;
	Node next;
	
	public Node() {
		data = 0;
		next = null;
	}
	
	public void printAll(Node head) {
		Node temp = head;
	    while(temp != null) {
	        System.out.println(temp.data);
	        temp = temp.next;
	    }
	}
	
	public Node insertAtTail(Node head,int data) {
		if(head == null) {
	        head = new Node();
	        head.data = data;
	        head.next = null;
	    }
	    else {
	        Node temp = head;
	        while (temp.next != null) {
	            temp = temp.next;
	        }
	        temp.next = new Node();
	        temp.next.data = data;
	        temp.next.next = null;
	    }
	    return head;
	}
	
	public Node insertAtHead(Node head,int data) {
	    if(head == null) {
	        head = new Node();
	        head.data = data;
	        head.next = null;
	    }
	    else {
	        Node temp = new Node();
	        temp.data = data;
	        temp.next = head;
	        head = temp;
	    }
	    return head;
	}
	
	public Node insertAtPosition(Node head, int data, int position) {
	    if(head == null) {
	        head = new Node();
	        head.data = data;
	        head.next = null;
	    }
	    else {
	        Node temp = new Node();
	        temp.data = data;
	        if (position == 0) {
	            temp.next = head;
	            head = temp;
	        }
	        else {
	            Node iterator = head;
	            for (int i = 1; i < position ; i++) {
	                iterator = iterator.next;
	            }
	            temp.next = iterator.next;
	            iterator.next = temp;
	        }
	    }
	    return head;       
	}
	
	public Node delete(Node head, int position) {
	    if(head != null) {
	        if (position == 0) { //At head
	            head = head.next;
	        }
	        else {
	            Node iterator = head;
	            for (int i = 1; i < position ; i++) {
	                iterator = iterator.next;
	            }
	            if (iterator.next.next == null) { //Check the tail
	                iterator.next = null;
	            }
	            else { //In middle
	                iterator.next = iterator.next.next;
	            }
	        }
	    }
	    return head;
	}
	
	public void printReverse(Node head) {
		if(head != null) {
			printReverse(head.next);
			System.out.println(head.data);
		}
	}
	
	Node reversal = null;
	public Node reverseList(Node head) {
	    if(head != null) {
	    	reverseList(head.next);
	        if(reversal == null) {
	        	reversal = new Node();
	        	reversal.data = head.data;
	        	reversal.next = null;
	        }
	        else {
	            Node iterator = reversal;
	            while(iterator.next != null) {
	                iterator = iterator.next;
	            }
	            iterator.next = new Node();
	            iterator.next.data = head.data;
	            iterator.next.next = null;
	        }
	    }
	    head = reversal;
	    return head;
	}
}
