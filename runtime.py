from settings import *
from Util.tools import *


def checkAuth(operator):
    '''
    检查操作者权限
    :param operator:
    :return:
    '''
    if operator not in OPERATOR.keys():
        raise UserWarning("操作者不在settings.OPERATOR名单里，无法执行本次操作")
    else:
        return operator


def checkCleanTCR():
    if IS_CLEAN_TCR == 1 :
        cleanTCR()
    else:
        pass


def runTime(operator):
    start = 0
    try:
        checkAuth(operator)
        suite = createSuite()
        createReport(operator, suite)
        end = start + 1
        print(end)
        if end == 1:
            print("case全部执行完毕")
            time.sleep(5)
            checkCleanTCR()

    except:
        raise UserWarning('用例执行失败')


if __name__ == '__main__':
    runTime('Dzreal')
