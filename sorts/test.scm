;; guile -l Insertion/main.scm test.scm <Data/data.scm

;; guile -l main.scm test.scm <data 1>out 2>err
;; где data -- файл с данными
;; [out, err] -- файлы, которые будут созданы, если указаны
;; out -- файл, в который будет осуществляться вывод
;; err -- файл, в который будут выводиться ошибки

(define (array->string xs)
  (apply string-append
         (append (cons "["
                       (map (lambda (s) (string-append (toString s) " ")) xs))
                       (list "]"))))

(define (toString x)
  (cond ((string? x)    x)
        ((number? x)    (number->string x))
        ((list? x)      (array->string x))
        ((procedure? x) "procedure")
        (else "smth")))

(define (get-error-string input output result)
  (string-append "Error:\n  data in:  "
                 (toString input)
                 "\n  expected: "
                 (toString output)
                 "\n recieved: "
                 (toString result)))

(define (get-errors-info results)
  (apply string-append
         (append (list (number->string (length results)) " failed\n")
                 (map (lambda (str) (string-append str "\n")) results))))

(define (get-tests-info tests-length results)
  (string-append "run "
                 (number->string tests-length)
                 " tests:\n"
                 (if (zero? (length results))
                     "tests OK"
                     (get-errors-info results))))

(define (single-test func input output)
  (let ((result (apply func input)))
       (or (equal? result output)
           (get-error-string input output result))))

(define (run-tests func inputs outputs)
  (get-tests-info (length inputs)
                  (filter (lambda (result) (string? result))
                          (map (lambda (input output)
                                       (single-test func input output))
                               inputs
                               outputs))))

(begin
  (eval (read) (interaction-environment))
  (eval (read) (interaction-environment))
  (eval (read) (interaction-environment))
  (eval (read) (interaction-environment))
  (eval (read) (interaction-environment))
  (eval (read) (interaction-environment))
  (define start (get-internal-run-time))
  (define res (run-tests main data-in data-out))
  (display "runTests: ")
  (display (- (get-internal-run-time) start))
  (display " time units")
  (newline)
  (display res)
  (newline))
