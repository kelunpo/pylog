from typing import Callable, Type

from sequence_options.super_sequence import SuperSequence


def all_distinct(arg_nbr, lst):
  values = {str(x.args[arg_nbr]) if x.args[arg_nbr] is not None else '_' + str(x.id) for x in lst}
  if len(values) == len(lst):
    yield


class SimpleCounter:
  def __init__(self, init_value=0):
    self._count = init_value

  def __str__(self):
    return str(self._count)

  def incr(self, amount=1):
    self._count += amount
    return self


def run_puzzle(problem: Callable, ListType: Type, Answer_List: SuperSequence, additional_answer: Callable = None):
  """ Runs the problem and displays the answer. Takes and displays timing information. """

  inp = None  # needed below at this block level
  from timeit import default_timer as timer
  (start1, end1, start2, end2) = (timer( ), None, None, None)
  for _ in problem(Answer_List):
    end1 = timer( )
    print('\nSolution: ')
    for (index, item) in enumerate(Answer_List):
      print(f'\t{index + 1}. {item}')
    if additional_answer:
      additional_answer(Answer_List)
    inp = input('\nMore? (y, or n)? > ').lower( )
    start2 = timer( )
    if inp != 'y':
      break
  end2 = timer( )
  if inp == 'y':
    print('No more solutions.')
  print(f'\nUsing {ListType.__name__}s, the total compute time was: {round(end1 + end2 - start1 - start2, 3)} sec')
