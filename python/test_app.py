from app import vectors_collinear
from app import vectors_collinear_list

def test_collinear():
   assert vectors_collinear(1, 2, 2, 4)
   assert vectors_collinear(3, 6, -1, -2)
   assert vectors_collinear(0, 0, 0, 0)

def test_not_collinear():
   assert not vectors_collinear(1, 2, 3, 4)
   assert not vectors_collinear(1, 2, 5, 12)

def test_vectors_collinear_list():
   assert vectors_collinear_list([1, 2], [2, 4])
   assert vectors_collinear_list([3, 6], [-1, -2])
   assert vectors_collinear_list([0, 0], [0, 0])

def test_not_collinear_list():
   assert not vectors_collinear_list([1, 2], [3, 4])
   assert not vectors_collinear_list([1, 2], [8, 44])
