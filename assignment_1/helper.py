from math import atan2, pi, cos, sin


def computeLineThroughTwoPoints(p1, p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    a = (y1-y2)/((y1-y2)**2+(x1-x2)**2)**0.5
    b = (x1-x2)/((y1-y2)**2+(x1-x2)**2)**0.5
    c = -(a*x1+b*y1)
    return a, b, c


def computeDistancePointToLine(q, p1, p2):
    [a, b, c] = computeLineThroughTwoPoints(p1, p2)
    Distance = abs(a*q[0] + b*q[1] + c)  # a^2+b^2=1
    return Distance


def computeDistancePointToPoint(p1, p2):
    distance = ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5
    return distance


def computeDistancePointToSegment(q, p1, p2):
    [a, b, c] = computeLineThroughTwoPoints(p1, p2)
    x1 = (b**2)*q[0]-a*b*q[1]-a*c
    if b == 0:
        y1 = q[1]
    else:
        y1 = -(1/b)*(a*x1+c)

    d1 = computeDistancePointToPoint([x1, y1], p1)
    d2 = computeDistancePointToPoint([x1, y1], p2)
    d3 = computeDistancePointToPoint(p1, p2)

    if d1+d2 > d3:
        if d1 > d2:
            w = 2
            dist = computeDistancePointToPoint(q, p2)
            T = p2
        else:
            w = 1
            dist = computeDistancePointToPoint(q, p1)
            T = p1
    else:
        w = 0
        dist = computeDistancePointToLine(q, p1, p2)
        T = [x1, y1]
    return dist, w, T


def computeDistancePointToPolygon(q, P):
    D = []
    n = len(P)
    D.append(computeDistancePointToSegment(q, P[n-1], P[0]))
    for i in range(n-1):
        D.append(computeDistancePointToSegment(q, P[i], P[i+1]))
    return min(D)

def DirectiontowardAPoint(P,Q):
    theta = atan2(Q[1]-P[1], Q[0]-P[0]) #Any vector A
    Ax = cos(theta)
    Ay = sin(theta)
    if theta < 0:
        theta += 2*pi
    return Ax, Ay, theta