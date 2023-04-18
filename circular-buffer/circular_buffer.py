"""Implementation of Circular buffer"""

class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        pass


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        pass


class CircularBuffer:
    """Implementation of Circular buffer"""
    def __init__(self, capacity):
        self.write_index = 0
        self.read_index = 0  # Will always be first position
        self.size = capacity
        self.buffer = []
        for _ in range(self.size):
            self.buffer.append(None)

    def read(self):
        """Pops the last written element"""
        if self.buffer[self.read_index] is None:
            raise BufferEmptyException("Circular buffer is empty")

        ret_val = self.buffer[self.read_index]
        del self.buffer[self.read_index]
        self.write_index -= 1
        self.buffer.append(None)
        return ret_val

    def write(self, data):
        """Pushes the latest element to buffer"""
        if self.write_index >= self.size:
            raise BufferFullException("Circular buffer is full")

        self.buffer[self.write_index] = data
        self.write_index += 1


    def overwrite(self, data):
        """Overwrites the last written element"""
        if self.write_index < self.size:
            self.buffer[self.write_index] = data
            self.write_index += 1
        else:
            del self.buffer[self.read_index]
            self.buffer.append(data)

    def clear(self):
        """Cleans the buffer"""
        for num in range(self.size):
            self.buffer[num] = None
        self.read_index = 0
        self.write_index = 0
