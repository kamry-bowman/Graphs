from random import randrange
from collections import deque
from names import get_full_name


def combinations(n, k):
    total = 1
    for i in range(1, k + 1):
        total *= (n + 1 - i) / i
    return int(total)


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        for _ in range(numUsers):
            self.addUser(get_full_name())

        ids = [id for id in self.users.keys()]

        num_friendships = (avgFriendships * numUsers) // 2
        original_possibilities = combinations(numUsers, 2) - 1
        remaining_possibilities = original_possibilities
        picked = []

        while len(picked) < num_friendships:
            candidate = randrange(remaining_possibilities)
            drop = len(picked)

            for i in range(len(picked)):
                if candidate >= picked[i]:
                    candidate += 1
                else:
                    drop = i
                    break

            picked.insert(drop, candidate)
            remaining_possibilities -= 1

        for pointer in picked:
            segment = len(ids) - 1
            while pointer > segment:
                pointer = pointer - segment
                segment -= 1

            first_id_index = len(ids) - 1 - segment
            second_id_index = first_id_index + pointer

            self.addFriendship(ids[first_id_index], ids[second_id_index])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set

        queue = deque()
        visited[userID] = []
        for friend_id in self.friendships[userID]:
            queue.appendleft((userID, friend_id))

        while queue:
            v1, v2 = queue.pop()
            if visited.get(v2) is None:
                # if not, add to visited dict, using tuple and visited dict to construct friendship path
                visited[v2] = visited[v1] + [v1]

                # if not, add all friends edges to queue in the form of a tuple (currentID, friendID)
                for friend_id in self.friendships[v2]:
                    queue.appendleft((v2, friend_id))

        for key in visited:
            visited[key].append(key)

        return visited

    def stats(self):
        total_friends = 0

        avg_degs = 0

        for id in self.users:
            user = self.users[id]
            network = self.getAllSocialPaths(id)
            degs = 0
            for friend in network:
                degs += len(network[friend])
            avg_degs += degs / len(network)
            total_friends += len(network)

            # print(f'{user.name} has {len(network)} friends in extended network')

        print(
            f'Average user has {total_friends / len(self.users)} in extended network')
        print(
            f'Average user has average {avg_degs / len(self.users)} degrees of separation')


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(1000, 5)
    print(sg.friendships)
    sg.stats()
    # connections = sg.getAllSocialPaths(1)
    # print(connections)
