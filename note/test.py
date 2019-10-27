def consumer(name):
    print('消费者{}准备吃包子。。。'.format(name))
    while True:
        baozi = yield
        print('消费者{}收到包子编号：{}'.format(name, baozi))

c1 = consumer('c1')
c2 = consumer('c2')
c3 = consumer('c3')
c1.__next__()
c2.__next__()
c3.__next__()

for i in range(10):
    print('----生成了第{}批包子----'.format(i))
    c1.send(i)
    c2.send(i)
    c3.send(i)