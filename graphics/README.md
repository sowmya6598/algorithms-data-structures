# Algorithms in Computer Graphics

In this exercise you will implement functions being frequently used in computer graphics, CAD systems, design software etc.
We deal with a 3D solid which is assumed to be given as an array, say F, of triangles (faces) forming its surface:

F[1....N], where N is a number of faces. In turn, each face F[i] (of the type Face) is a triple of points [x,y,z]  (of the type Point) of 3D space. Additionally we define the Edge structure holding solid/face edges.

The main structures are given below:

```
struct Point {double x, y, z;} 
struct Face {Point v1, v2, v3;} 
struct Edge {Point v1, v2;}
struct Solid {Face F[]; int size;}
```


1. Write the set of functions computing distances between various types of geometric objects (see this [link](http://geomalgorithms.com/algorithms.html) for tips):

```
double dist(Point P, Point P);double dist(Edge E, Point P);double dist(Edge E1, Edge E2);
double dist(Edge E, Face F);double dist(Face P, Point P);double dist(Face f1, Face f2);double dist(Solid S1, Solid S2);
```


2a. Test dist(Face f1, Face f2) for two Faces given below:

```
1.0; 0.0; 0.0
0.0; 1.0; 0.0
0.0; 0.0; 0.0

100.0; 0.0; 0.13
0.0; 100.0; 0.13
-100.0; -100.0; 0.13
```


2b. Test implemented procedures by launching dist(Solid S1, Solid S2) for two solids given in this file (plain text file).

Remark. The file format is following:

![alt text](http://galaxy.agh.edu.pl/~sedziwy/wordpress/wp-content/uploads/solid-1.png)
