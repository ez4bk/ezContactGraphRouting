from queue import PriorityQueue


class ContactGraph:
    def __init__(self, id, start_time, end_time, sender, receiver, owlt):
        self.id = id
        self.start = start_time
        self.end = end_time
        self.snd = sender
        self.rcv = receiver
        self.owlt = owlt
        self.arrival_time = float("Inf")
        self.visited_nodes = []
        self.predecessor = None
        self.visited = False
        self.next = None


def ReadContactsFromFile(filename):
    contacts = []
    with open(filename, 'r') as f:
        for line in f:
            id, start, end, snd, rcv, owlt = line.strip().split()
            id = int(id)
            start = float(start)
            end = float(end)
            snd = int(snd)
            rcv = int(rcv)
            owlt = float(owlt)
            contacts.append(ContactGraph(id, start, end, snd, rcv, owlt))
    return contacts


def ContactReviewProcedure(contacts, current_contact, final_contact, destination, best_delivery_time, heap):
    for contact in contacts:
        if (contact.snd != current_contact.rcv
                or contact.end < current_contact.arrival_time
                or contact.visited
                or contact.rcv in current_contact.visited_nodes):
            continue

        arrival_time = max(current_contact.arrival_time, contact.start) + contact.owlt

        if arrival_time < contact.arrival_time:
            contact.arrival_time = arrival_time
            contact.predecessor = current_contact
            contact.visited_nodes = current_contact.visited_nodes + [contact.rcv]
            heap.put((contact.arrival_time, contact.id))
            if contact.rcv == destination and contact.arrival_time < best_delivery_time:
                best_delivery_time = contact.arrival_time
                final_contact = contact

    current_contact.visited = True
    return final_contact, best_delivery_time


def ContactSelectionProcedure(contacts, best_delivery_time, heap):
    if heap.empty():
        return None

    while not heap.empty() and contacts[heap.queue[0][1] - 1].visited:
        if contacts[heap.get()[1] - 1].arrival_time > best_delivery_time:
            return None

    current_contact = contacts[heap.get()[1] - 1]

    return current_contact


def ContactGraphRouting(contacts, source, destination, heap):
    final_contact = None
    best_delivery_time = float("Inf")
    current_contact = source

    while True:
        final_contact, best_delivery_time = (
            ContactReviewProcedure(contacts, current_contact, final_contact, destination, best_delivery_time, heap))
        current_contact = ContactSelectionProcedure(contacts, best_delivery_time, heap)
        if current_contact is None:
            break

    return final_contact, best_delivery_time


def DijkstraRouting(src, dst, contacts):
    root_contact = ContactGraph(0, 0, float('inf'), src, src, 0)
    root_contact.arrival_time = 0

    heap = PriorityQueue()

    final_contact, best_delivery_time = ContactGraphRouting(contacts, root_contact, dst, heap)

    node_list = []
    contact_list = []

    contact = final_contact
    while contact.predecessor is not None:
        node_list.append(contact.rcv)
        contact_list.append(contact.id)
        contact = contact.predecessor

    node_list.append(contact.rcv)
    node_list.reverse()
    contact_list.reverse()

    return node_list, contact_list, best_delivery_time


if __name__ == '__main__':
    filename = "ContactList.txt"
    src = 8
    dst = 5
    contacts = ReadContactsFromFile(filename)
    node_list, contact_list, best_delivery_time = DijkstraRouting(src, dst, contacts)
    print(f"The file contains {len(contacts)} contacts.")
    print(f"Shortest path from source node {src} to destination node {dst} is:")
    print("Contact No\tSrc\tDst\tStart\tEnd")
    print("__________\t___\t___\t_____\t___")
    for node, contact in zip(node_list, contact_list):
        print(f"{contact}\t\t\t{contacts[contact - 1].snd}\t{contacts[contact - 1].rcv}\t{contacts[contact - 1].start}\t{contacts[contact - 1].end}")
    print(f"Using this path, the earliest arrival time at node {dst} is: {best_delivery_time}")

