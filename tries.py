class Node():
    def __init__(self, val=None):
        self.children = {}
        self.value = val
        self.isWord = False

    def __str__(self):
        return f'{self.value}'

class Trie():
    def __init__(self):
        self.root = Node()

    def add(self, word):
        current = self.root

        # Loop through the letters in the input word
        # Traverse through the Trie as far as we possibly can
        i = 0
        while i < len(word):
            if word[i] in current.children: # If this next letter is in the children
                current = current.children[word[i]] # move current to that child node
                i += 1
            else: #The next node for the letter we're adding isn't found
                break

        # If we can no longer traverse through the Trie
        # AND we still have letters left in our word...
        # This means we have to add some more nodes to our Trie
        while i < len(word):
            current.children[word[i]] = Node(word[i]) # Create the node
            current = current.children[word[i]] # increment current to traverse to that newly made node
            i += 1
        # Finished looping - this current node must be a word
        current.isWord = True

    def search(self, word):
        '''Return True if the word is in the Trie, or False otherwise '''
        current = self.root

        # Loop over the input word
        for i in range(len(word)):
            if word[i] in current.children:
                # We found the letter!
                # Traverse our current var to the node
                current = current.children[word[i]]
            else:
                # Uh oh, we didn't find the letter
                return False

        # Check if the next letter is present in the current.children
        # If we get to the end of the word, and all letters are present 
        # Return True if isWord=True, Return False otherwise
        return True if current.isWord else False

    def delete(self, word):
        # Loop over the word
        # Check if each letter is present in the tree
        # If the letter isn't present in the tree - that means the user is trying to ask us
        # to delete a word that doesn't exist!

        # However if it does exist, and we manage to loop through the whole word..
        # That means that the 'current' at that point
        # needs to have it's `isWord` value set to False
        pass

    def __str__(self):
        # Some sort of algorithm here that TRAVERSES the whole tree in a CERTAIN order!
        return f'some proper visualization of the tree!'

my_trie = Trie()
my_trie.add('soup')
print(my_trie.root.children['s'])
print(my_trie.root.children['s'].children['o'])
print(my_trie.root.children['s'].children['o'].children['u'])
print(my_trie.root.children['s'].children['o'].children['u'].children['p'])

# All AI is just nested IF statements