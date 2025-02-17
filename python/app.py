def vectors_collinear(x1, y1, x2, y2):
   return x1 * y2 == x2 * y1

def vectors_collinear_list(vec1, vec2):
   x1, y1 = vec1
   x2, y2 = vec2
   return x1 * y2 == x2 * y1

collinearity = lambda x1, y1, x2, y2: x1 * y2 == x2 * y1
