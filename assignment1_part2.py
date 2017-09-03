#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 1 assignment 1 part 2"""

class Book(object):

    author = ''
    title = ''
    
    def __init__(self, author, title):
        """Book.
        Args:
            author: name of author
            title: name of book
        Attritubtes:
            title (str): title of the book
            author (str): author of the book
        """
            
        self.author = author
        self.title = title
        
    def display(self):
        """format text and display"""
        output = '{}, written by {}.'.format(self.title, self.author)
        return output

Book1 = Book('John Steinback', 'Of Mice and Men')
Book2 = Book('Harper Lee', 'To Kill a Mockingbird', )
print Book1.display()
print Book2.display()
