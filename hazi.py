import numpy as np

def hardlim (a,b):
  res=0
  for i in range(len(a)):
    res = res + (a[i]*b[i])

  if res < 0:
    res = 0

  return res


def tanit(data, res):
    N, n = data.shape
    lr = 0.001
    w1 = np.random.randn(n, 1)
    w2 = np.random.randn(n, 1)

    E = 1
    eps = 0.0000001
    while E > eps:
        E = 0
        for i in range(N):
            y1 = hardlim(data[i], w1)
            y2 = hardlim(data[i], w2)

            E1 = res[0][i] - y1
            E2 = res[1][i] - y2

            w1 += lr * E1 * data[i].reshape(n,1)
            w2 += lr * E2 * data[i].reshape(n, 1)

            E += E1 ** 2
            E += E2 ** 2
    return np.array([w1, w2])

def hatar(a):
  res = []
  for i in range(len(a)):
    if a[i] < 0.5:
      res.append(0)
    else:
      res.append(1)
  return np.array(res)

def felismer(data, w, res):
    N, n = data.shape
    H = np.array([1,0])

    for i in range(N):
        y1 = hardlim(data[i], w[0])
        y2 = hardlim(data[i], w[1])

        a = hatar(np.array([y1, y2]))
        b = np.array([res[i][0], res[i][1]])

        if np.array_equal(a, b):
            print (data[i])
            if np.array_equal(a,H):
              print("H betu")
            else:
              print("I betu")



def main():
    data = np.array([[1, 0, 1, 1, 1, 1, 1, 0, 1], [0, 1, 0, 0, 1, 0, 0, 1, 0]])
    res = np.array([[1, 0], [0, 1]])

    w = tanit(data, res)

    print("Helyes bemenet")
    felismer(data, w, res)

    print("Hibas bemenet")
    data2 = np.array([[0, 0, 1, 1, 1, 1, 1, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1, 0]])
    felismer(data2, w, res)

main()