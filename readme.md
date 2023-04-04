# Midterm - Spring 2023

1.
    1. **(15)** Write necessary object oriented code in file `Q1.py` so that your code passes test `test_Q1` in `test_Q1.py`.
    2. **(10)** Draw the class diagram of the classes in Question 1.1. Draw your class diagram either using draw.io or manually on a paper. Add your class diagram to the repository as a **picture** file. Do not include the raw drawio file. Name your picture file as `Q1-2` with an appropriate extention (png, jpeg, etc.).
2.
    1. **(20)** Write a recursive function called `subsets_less_than_x(v, x)` in file `Q2.py` such that, given a list of intergers (`v`) and an integer value (`x`), the function returns the list of subsets of `v` that sum up to a value less than `x`. Make sure that your function passes test `test_Q2.py`.
    1. **(10)** Write an analysis of the time complexity of your function in Question 2.1 to file `Q2-2.md`.
3. Use the graph classes `DAG`, `Node` and `Arc` that we developed in the lectures. A modified version of the classes are given in `Q3.py` as a starter code.
    1. **(5)** Explain why, in this code, I chose to define `self._nodes` as a *dictionary* instead of a *list*. Write your answer to file `Q3-1.md`.
    2. **(20)** Implement function `has_path_between_nodes(self, from_node_id: int, to_node_id: int) -> bool` in class `DAG` which is expected to return `True` if there is a path from node with id `from_node_id` to node with id `to_node_id`. Make sure that your code passes tests `test_Q3_1` and `test_Q3_2` in `test_Q3.py`.
4. Answer this question by examining the code in `Q4.py`. Write your answers to file `Q4.md`. In all the answers please add a clear explanation of your answer. An answer will not be graded if it is not supported by a valid explanation.
    1. **(2)** Considering the original code, what happens (and why) if you activate only the commented line indicated as **#Q4.1**
    2. **(2)** Considering the original code, what happens (and why) if you activate only the commented line indicated as **#Q4.2**
    3. **(2)** Considering the original code, what happens (and why) if you activate only the commented line indicated as **#Q4.3**
    4. **(14)** Considering the original code, draw the content of active namespace tables in memory as of the time the execution is at line indicated as **#Q4.4**. Draw the namespace tables on a paper and add the **picture** to the repository. Name your picture file as `Q4-4` with an appropriate extention (png, jpeg, etc.).
