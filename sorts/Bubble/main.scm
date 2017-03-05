;; Bubble sort
(define (bubble-sort xs cmp?)
  (define (helper ss bs xs)
    (if (null? xs)
        ss
        (let ((x (car xs))
              (s (cdr xs)))
             (if (null? s)
                 (helper (cons x ss) '() bs)
                 (let ((y  (car s))
                       (ys (cdr s)))
                      (if (cmp? y x)
                          (helper ss (append bs (list y)) (cons x ys))
                          (helper ss (append bs (list x)) (cons y ys))))))))
  (helper '() '() xs))

(define main bubble-sort)
