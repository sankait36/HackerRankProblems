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
	            //Node temp = head;
	            head = head.next;
	            //delete temp;
	        }
	        else {
	            Node iterator = head;
	            for (int i = 1; i < position ; i++) {
	                iterator = iterator.next;
	            }
	            if (iterator.next.next == null) { //Check the tail
	                //Node temp = iterator.next;
	                iterator.next = null;
	                //delete temp;
	            }
	            else { //In middle
	                //Node temp = iterator.next;
	                iterator.next = iterator.next.next;
	                //delete temp;
	            }
	        }
	    }
	    return head;
	}
}
