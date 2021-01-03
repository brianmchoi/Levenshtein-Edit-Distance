#!/usr/bin/python

#task 4 inspired by
#http://stevehanov.ca/blog/?id=114&fbclid=IwAR0SAVql_pdtYVWc7UQU2grRy9keMbfQ98k2U4vRdkXWgRcMnRrLUyrZy6U
#code NOT directly copied

#similar Trie structure to article
class TrieNode:
  def __init__(self):
    self.word = None
    self.children = {}

  def insert(self, word):
    node = self
    for letter in word:
      if letter not in node.children:
        node.children[letter] = TrieNode()
      node = node.children[letter]
    node.word = word

  def search(self, word, max_cost):
    cur_row = range(len(word) + 1)
    results = []

    #call recursive search function for letter
    for letter in self.children:
      self.search_helper(self.children[letter], letter, word, cur_row, results, max_cost)

    best_value = min(results)
    return best_value

  def search_helper(self, node, letter, word, prev_row, results, max_cost):
    columns = len(word) + 1
    cur_row = [prev_row[0] + 1]

    #my implementation for calculating distance
    for column in range(1, columns):
      if word[column - 1] != letter:
        value = min(cur_row[column - 1] + 1, prev_row[column] + 1, prev_row[column - 1] + 1)
        cur_row.append(value)
      else:
        value = min(cur_row[column - 1] + 1, prev_row[column] + 1, prev_row[column - 1])
        cur_row.append(value)
    
    if node.word != None and cur_row[-1] <= max_cost:
      results.append(cur_row[-1])
    if min(cur_row) <= max_cost:
      for letter in node.children:
        self.search_helper(node.children[letter], letter, word, cur_row, results, max_cost)


def task4(dictionary, raw):
  trie = TrieNode()

  for word in open(dictionary, "r"):
    trie.insert(word.rstrip('\n'))

  distance_list = []

  with open(raw, "r") as file:
    for word in file.readlines():
      distance_list.append(trie.search(word.rstrip('\n'), 20))
  
  return distance_list


if __name__ == '__main__':
  print(task4('dictionary.txt', 'raw.txt'))
	