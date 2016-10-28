from main import BinaryTree

dataIn = [
    [BinaryTree(10,
        BinaryTree(5,
            BinaryTree(1, None, BinaryTree(4))),
        BinaryTree(35,
            BinaryTree(15),
            BinaryTree(40, BinaryTree(37))))],
    [BinaryTree(100,
        BinaryTree(50,
            BinaryTree(25,
                BinaryTree(10),
                BinaryTree(40,
                    BinaryTree(30, None, BinaryTree(35)))),
            BinaryTree(75,
                BinaryTree(65, BinaryTree(60)),
                BinaryTree(85, BinaryTree(80), BinaryTree(90)))))],
    [BinaryTree(10,
        None,
        BinaryTree(20,
            None,
            BinaryTree(30,
                None,
                BinaryTree(40))))]
]

dataOut = [ 37, 90, 30 ]
