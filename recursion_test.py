from recursion_max import recursion_max

test_code = '''
def test():
    recursion_max([1, 2, 4, 5, 3, 8, 3, 5])
'''

if __name__=="__main__":
    import timeit
    time_taken=timeit.repeat(stmt=test_code, setup="from recursion_max import recursion_max", repeat=5)
    print(time_taken)
    print(f'Average time {sum(time_taken)/5}')

# 0.23717257499993138