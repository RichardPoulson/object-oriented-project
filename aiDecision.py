from abc import ABCMeta, abstractmethod

class aiDecision(metaclass=ABCMeta):
  @abstractmethod
  def search(self, board, max_num_moves):
    pass