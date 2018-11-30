def ce(muffled):
    try:
        if muffled:
            raise Exception('出现异常')
        else:
            raise BaseException('基础异常')
    except (Exception, ValueError, TypeError) as e:
        if muffled:
            print('输出异常')  # 捕捉并处理
            print(e)
        else:
            # raise  # 继续抛出
            raise ValueError from Exception
    except BaseException:
        pass
    except:  # 会捕捉到意外的异常
        print('捕获所有异常')
    else:  # 目前在死循环中有用,如果错误就一直输入,正确就继续
        print('若没发生异常执行')
    finally:  # 可单独和try结合
        print('最终都会执行的代码块,通常用来清理东西,比如关闭文件.')


ce(1)
ce(0)
