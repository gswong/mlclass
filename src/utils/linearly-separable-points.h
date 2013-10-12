// Copyright 2013 Gary Wong

#ifndef UTILS_LINEARLY_SEPARABLE_POINTS_H_
#define UTILS_LINEARLY_SEPARABLE_POINTS_H_

class LinearlySeparablePoints {
  public:
    LinearlySeparablePoints(unsigned num_points);
    double x1;
    double y1;
    double x2;
    double y2;
  private:
    LinearlySeparablePoints();
};

#endif  // UTILS_LINEARLY_SEPARABLE_POINTS_H_
