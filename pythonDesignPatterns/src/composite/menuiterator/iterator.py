from pythonDesignPatterns.src.composite.menuiterator.stack import Stack


class PythonIterator(object):
    """
    This class is used as a facade and abstraction layer on top of
    Python's default iterator iter(). It also proportions a hasNext() method
    """

    def __init__(self, it) -> None:
        super().__init__()
        self.it = iter(it)
        self._hasnext = None

    def __iter__(self):
        """
        This method is called when an iterator is required for a container.
        This method should return a new iterator object that can iterate over all the objects in the container.
        For mappings, it should iterate over the keys of the container.

        Iterator objects also need to implement this method; they are required to return themselves.
        :return: the iterator, wich is itself
        """
        return self

    def __next__(self):
        """
        Return the next item from the container.
        If there are no further items, raise the StopIteration exception
        :return: the next item in the iteration
        """
        if self._hasnext:
            result = self._thenext
        else:
            result = next(self.it)
        self._hasnext = None
        return result

    def getNext(self):
        """
        It returns the next item in the iteration from this iterator
        :raises: StopIteration if there are no more items
        :return: the next item in the iteration
        """
        return self.__next__()

    def hasNext(self):
        """
        Returns if there's a next element in the iteration.
        :return: True if there's a nex element in the iteration, False otherwise
        """
        if self._hasnext is None:
            try:
                self._thenext = next(self.it)
            except StopIteration:
                self._hasnext = False
            else:
                self._hasnext = True
        return self._hasnext


class Iterator(object):
    """
    This class describes the interface for a Iterator class and hierarchy and
    provides a default implementation as well being an adapter to the PythonIterator
    facade to Python default's iter()
    """

    def __init__(self, iterator=None, iterable=None) -> None:
        super().__init__()
        if iterator:
            self.iterator = iterator
        elif iterable:
            self.iterator = PythonIterator(iterable)

    @staticmethod
    def createIterator(iterable):
        """
        Creates an Iterator on top of this iterable structure
        :param iterable: data structure to be iterated
        :return: the whole iterator on top of the provided data structure
        """
        return Iterator(iterable=iterable)

    def getNext(self):
        return next(self.iterator)

    def hasNext(self):
        return self.iterator.hasNext()

    def remove(self):
        return NotImplemented



class CompositeIterator(Iterator):
    def __init__(self, iterator):
        super().__init__(iterator=iterator)
        self.stack = Stack()
        self.stack.push(iterator)

    def getNext(self):
        if self.hasNext():
            iterator = self.stack.peek()
            component = iterator.getNext()
            # Java impl, but can't import Menu here because circular imports aren't allowed
            #if isinstance(component, Menu):
            if component:
                self.stack.push(component.createIterator())

            return component
        else:
            return None

    def hasNext(self):
        if self.stack.isEmpty():
            return False
        else:
            iterator = self.stack.peek()
            if not iterator.hasNext():
                self.stack.pop()
                return self.hasNext()
            else:
                return True

    def remove(self):
        raise NotImplementedError


class NullIterator(Iterator):
    def getNext(self):
        return None

    def hasNext(self):
        return False

    def remove(self):
        raise NotImplementedError

