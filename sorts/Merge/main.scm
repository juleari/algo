;; Merge sort algorithm
(define (merge-sort xs cmp?)
  (define (merge ls rs)
    (cond ((null? ls) rs)
          ((null? rs) ls)
          ((cmp? (car rs) (car ls)) (cons (car rs) (merge ls (cdr rs))))
          (else                     (cons (car ls) (merge (cdr ls) rs)))))

  (if (< (length xs) 2)
      xs
      (merge (merge-sort (left xs) cmp?) (merge-sort (right xs) cmp?))))

(define (take n xs)
  (if (or (zero? n)
          (null? xs))
      '()
      (cons (car xs) (take (- n 1) (cdr xs)))))

(define (drop n xs)
  (if (or (zero? n)
          (null? xs))
      xs
      (drop (- n 1) (cdr xs))))

(define (half-length xs) (ceiling (/ (length xs) 2)))
(define (left  xs) (take (half-length xs) xs))
(define (right xs) (take (half-length xs) (drop (half-length xs) xs)))

(define main merge-sort)
