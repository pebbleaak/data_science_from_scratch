from typing import List

Vector = list[float]

height_wieght_age = [70, 170, 40]

x: Vector = [1, 2, 3, 4] 
y: Vector  = [4, 5, 6, 7] 

z: Vector = [12, 22, 24,55,22]

many_vectors: List[Vector] = [x,y ]


grades = [95, 80, 75, 62]


def add(v: Vector, w: Vector) -> Vector:

    """Adds corresponding elements"""

    assert len(v) == len(w), "vectors must be same length"

    new_vector: Vector = [ v_i + w_i for v_i, w_i in zip(v, w) ]

    return new_vector


assert add([1,2, 3], [4, 5, 6]) == [5, 7, 9]

def subtract(v: Vector, w: Vector) -> Vector:

    """Subtracts corresponding elements"""

    assert len(v) == len(w), "vectors must be same length"

    new_vector: Vector = [ v_i - w_i for v_i, w_i in zip(v, w) ]

    return new_vector


assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]


def vector_sum(vectors: List[Vector]) -> Vector:

    """Sums all corresponding elements"""

    assert vectors, "no vectors provided"

    num_elements = len(vectors[0])

    assert all(len(v) == num_elements for v in vectors)
  
   #x return [sum(vector[i] for vector in vectors) for i in range(num_elements)]
    new_list =  [ vector[0] for vector in vectors  ]

    print(new_list)


    
vector_sum(many_vectors)
