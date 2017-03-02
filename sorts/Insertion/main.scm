;; Insertion sort algorithm
(define (insertion-sort xs cmp?)
  (define (insert xs ys x)
    (cond ((null? ys)        (cons x xs))
          ((cmp? (lst ys) x) (insert (cons (lst ys) xs) (heads ys) x))
          (else              (append ys (list x) xs))))

  (define (helper xs ys)
    (if (null? ys)
        xs
        (helper (insert '() xs (car ys)) (cdr ys))))

  (helper '() xs))

(define (lst xs)
  (if (null? (cdr xs))
      (car xs)
      (lst (cdr xs))))

(define (heads xs)
  (define (helper x xs)
    (if (null? xs)
        '()
        (cons x (helper (car xs) (cdr xs)))))
  (helper (car xs) (cdr xs)))

(define main insertion-sort)
