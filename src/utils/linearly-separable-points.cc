// Copyright 2013 Gary Wong

#include "utils/linearly-separable-points.h"
#include <cstdlib>
#include <ctime>

LinearlySeparablePoints::LinearlySeparablePoints(unsigned num_points) {
  srandom(time(NULL));
  x1 = 2*static_cast<double>(random())/RAND_MAX-1;
  y1 = 2*static_cast<double>(random())/RAND_MAX-1;
  x2 = 2*static_cast<double>(random())/RAND_MAX-1;
  y2 = 2*static_cast<double>(random())/RAND_MAX-1;
}
