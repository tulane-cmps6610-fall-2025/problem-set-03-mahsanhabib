# CMPS 6610 Problem Set 03
## Answers

**Name:** Md. Ahsan Habib


Place all written answers from `problemset-03.md` here for easier grading.




- **1b.**
    - Work of the algorithm (iterate):  $W(n) = W(n-1) + 1 \in O(n)$.
    - Span of the algorithm (iterate): $S(n) = S(n-1) + 1 \in O(n)$.





- **1d.**
    - Work of the algorithm (reduce):  $W(n) = 2W(n/2) + 1 \in O(n)$.
    - Span of the algorithm (reduce): $S(n) = S(n/2) + 1 \in O(\log n)$.




- **1e.**
    - In such case, the recursion would be:  
        $\qquad T(n) = T(n/3) + T(2n/3) + 1$

    - Work:  
        $\qquad W(n) = W(n/3) + W(2n/3) + 1$  
        Let $L(n)$ be the number of leaves as a function of $n$. Each internal node contributes leaves equal to the sum of leaves of its children: $L(n) = L(n/3) + L(2n/3)$. 
        If we guess that it has the form $L(n) = n^c$ for some $c$ (power-law guess), we can plug it into the equation and find the $c$.  
        $\qquad n^c = (n/3)^c + (2n/3)^c$  
        $\qquad \quad = n^c ((1/3)^c + (2/3)^c ) $

        Now we need to solve $(1/3)^c + (2/3)^c = 1`. From this, we can find the $c = 1$ (the equation has the unique solution for this). So $L(n) = n^c = n$, which implies $W(n) = O(n)$.  

    - Span:  
        $\qquad S(n) = \max\{S(n/3), S(2n/3)\} + 1 \\ 
        \qquad \quad \quad= S(2n/3) + 1$  
        The recursion depth $d$ satisfies $(2/3)^d \cdot n \le 1$, hence $d = \log_{3/2} n$.  
        Therefore, $S(n) = O(\log n)$.  

- **2a.**
    - Algorithm for **dedup**:
        - Initialize empty set $seen$ and empty list $result$
        - For each element $e$ in the $A$: 
            - If $e$ not in $seen$:
                - Add $e$ to $seen$
                - Append $e$ to $result$
        - Return $result$
        
    

    - SPARC specification of **dedup** function.  
    $(dedup\, A): \\
        \text{let } \\
            \quad seen = \emptyset, \\
            \quad result = [] \\
        \text{ in} \\
            \quad \text{for each } x \in A:\\
                \quad \quad \text{if } x \notin seen:\\
                    \quad \quad \quad \text{add } x \text{ to } result, \\
                    \quad \quad \quad \text{add } x \text{ to } seen\\
            \quad \text{return } result\\
        \text{end}
    $
    
    **Complexity:** Work $O(n)$ (if we use hash table for $seen$ implementation, it requires $O(1)$ for membership test), however without hash table, it would be quadratice work i.e., $O(n^2)$. \
    Span $O(n)$ as we need to preserve order.

- **2b.**
    - Algorithm for **multi-dedup**:
        - Initialize empty set $seen$ and empty list $result$
        - For each list $A_i$ in $A$:
            - For each element $e$ in the $A_i$: 
                - If $e$ not in $seen$:
                    - Add $e$ to $seen$
                    - Append $e$ to $result$
        - Return $result$

    - SPARC specification of **multi-dedup** function.  
    $(multi\text{-}dedup\, A): \\ 
        \text{let } \\
            \quad seen = \emptyset, \\
            \quad result = [] \\
        \text{ in} \\
            \quad \text{for each list } A_i \in A:\\
                \quad \quad \text{for each } e \in A_i:\\
                    \quad \quad \quad \text{if } e \notin seen:\\
                        \quad \quad \quad \quad \text{add } e \text{ to } result, \\
                        \quad \quad \quad \quad \text{add } e \text{ to } seen\\
            \quad \text{return } result\\
        \text{end}
    $
    
    **Complexity:** Lets say we have $m$ lists and each list has $n$ elements. Then the Work is $O(mn)$ (if we use hash table for $seen$ implementation, it requires $O(1)$ for membership test). \
    Span $O(\log m + \log n)$. As order is not considered, we can parallelize both within a list and across the lists. If we can process each list independently in the parallel, combining $m$ list in a binary-tree fashion takes $\log m$ steps. On the other hand, we can insert all element into a set in parallel where each insertion into a balanced tree set requires $O(\log n)$ span. 

- Compared to 2*a*, it requires more work as there are multiple lists where 2*a* has only a single list. Whereas, in case of span (2*a* preserve the order and 2*b* doesn't), 2*a* requires linear span while 2*b* has logarithmic span due to no dependency of order. 


- **2c.**
    - For 2*a* (single-list dedup, preserve order):
        - *iterate*: No advantegeous as we need to preserve the order.
        - *reduce*: Possible but not advantageous for span when preserving global order. Here, the merge must be sequential to keep first-appearance order.
        - *map/filter/scan*: Not useful to use.

    - For 2*b* (multi-list dedup, order not required):
        - *map*: Useful to turn each list $A_i$ into a local set of uniques in parallel.
        - *reduce*: Useful to union the local sets via a tree reduction (parallel), yielding the global unique set.
        - *iterate*: Useful to flatten the mulitple lists.




- **3b.**
    - Work of the iterative solution:  $W(n) = W(n-1) + 1 \in O(n)$.
    - Span of the iterative solution: $S(n) = S(n-1) + 1 \in O(n)$.



- **3d.**
    - Work: 
        - Map needs $O(n)$ works.
            - $W(n)=n \cdot O(1) \in O(n)$
        - Scan needs $O(n)$ works.
            - $W(n)=2W(n/2)+O(1) \in O(n)$
        - Min finding over the list needs $O(n)$ works.  
            - $W(n)=2W(n/2)+O(1) \in O(n)$.  
        - So, the total work is $O(n)$. 

    - Span: 
        - Map needs $O(1)$ span (parallel).
            - $S(n)=O(1) \in O(1)$
        - Scan needs $O(\log n)$ span (contraction-based).
            - $S(n)=S(n/2)+O(1) \in O(\log n)$
        - Min finding over the list needs $O(\log n)$ span.  
            - $S(n)=S(n/2)+O(1) \in O(\log n)$
        - So, the span is $O(\log n)$. 




- **3f.**

    - Recurrence is : $T(n)=2T(n/2)+O(1)$
    - So, work: $W(n)=2W(n/2)+O(1) \in O(n)$.
    - Span: $S(n)=S(n/2)+O(1) \in O(\log n)$.



