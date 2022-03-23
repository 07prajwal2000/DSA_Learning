class ListNode{
    constructor(val, next){
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

var addTwoNumbers = function(l1, l2) {
    let dummy = new ListNode();
    let current = dummy;

    let carry = 0;

    while (l1 !== null || l2 !== null || carry !== 0) {
        let v1 = l1 === null ? 0 : l1.val;
        let v2 = l2 === null ? 0 : l2.val;

        let sum = v1 + v2 + carry;

        carry = parseInt(sum / 10);
        sum %= 10;
        current.next = new ListNode(sum);

        current = current.next;
        l1 = l1 === null ? null : l1.next;
        l2 = l2 === null ? null : l2.next;
    }

    return dummy.next;
};

let a = new ListNode(2);
let b = new ListNode(4);
let c = new ListNode(3);

let d = new ListNode(5);
let e = new ListNode(6);
let f = new ListNode(4);
let g = new ListNode(3);


a.next = b;
b.next = c;

d.next = e;
e.next = f;
// f.next = g;

console.log(addTwoNumbers(a, d))