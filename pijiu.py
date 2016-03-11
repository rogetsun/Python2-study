# coding:utf-8
__author__ = 'uv2sun'
pj = 0  # 剩余啤酒
pg = 0  # 瓶盖
jp = 0  # 酒瓶
he = 0  # 喝了几瓶


def drink():
    global pj, pg, jp, he

    if (pj > 0):
        pj -= 1
        he += 1
        pg += 1
        jp += 1
        if (pg >= 4):
            # print '瓶盖=%s, 换一瓶酒' % (pg,)
            pj += 1
            pg -= 4
        if (jp >= 2):
            # print '酒瓶=%s, 换一瓶酒' % (jp,)
            pj += 1
            jp -= 2
        # print '一共喝了%s瓶,还剩%s酒瓶,%s瓶盖' % (he, jp, pg)

        return True
    else:
        return False


def while_drink(i):
    global pj, he, jp, pg
    pj = i
    he = 0
    jp = 0
    pg = 0
    while drink():
        # print '我喝'
        pass


for i in range(1, 100):

    while_drink(i)
    print '买%s,喝%s瓶,剩余:%s酒瓶,%s瓶盖' % (i, he, jp, pg)
    if jp == 0 and pg == 0:
        print i
