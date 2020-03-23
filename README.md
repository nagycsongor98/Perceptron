# Perceptron

Egy perceptronnak H és I betűk megtanítása és felismerése 3x3-as pixelű kép esetén
A háló megtanulja a betűket és felismeri öket, hiányos pixelű betűt is felismer.

Helyes bemenetek:
  1 0 1
  1 1 1 
  1 0 1
  - H betűt ismer fel
  
  0 1 0
  0 1 0 
  0 1 0
  - I betűt ismer fel

Hibás bemenet:
  0 0 1
  1 1 1 
  1 0 1
  - H betűt ismer fel

  0 0 0
  0 1 0 
  0 1 0
  - I betűt ismer fel
