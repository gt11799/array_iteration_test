array_iteration_test
====================

测试了不同的array的迭代方式。
在使用array迭代的时候，把计算复杂度高的量放到内循环还是外循环？
亲自测试了一下，发现其实区别并不是很明显，可能与numpy的批量计算的优化有关。
具体见http://blog.csdn.net/gt11799/article/details/39119045
