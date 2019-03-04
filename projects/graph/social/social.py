from random import randrange
from collections import deque
from names import get_full_name


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

        num_friends = avgFriendships * numUsers
        for _ in range(num_friends):
            num1 = randrange(len(ids))
            num2 = num1
            while num1 == num2:
                num2 = randrange(len(ids))

            self.addFriendship(ids[num1], ids[num2])

        print(self.users)
        print(self.friendships)

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


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
