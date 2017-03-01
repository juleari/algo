;; Insertion sort algorithm
(define (insertion-sort xs cmp?)
  (define (insert xs ys x)
    (cond ((null? ys) (append xs (list x)))
          ((cmp? (car ys) x) (insert (append xs (list (car ys))) (cdr ys) x))
          (else               (append xs (list x) ys))))

  (define (helper xs ys)
    (if (null? ys)
        xs
        (helper (insert '() xs (car ys)) (cdr ys))))

  (helper '() xs))
