texts = '''mv: cannot move 'Py_Algo/백준/Gold/10986. 나머지 합' to './백준/Gold/10986. 나머지 합': Directory not empty
mv: cannot move 'Py_Algo/백준/Gold/12865. 평범한 배낭' to './백준/Gold/12865. 평범한 배낭': Directory not empty
mv: cannot move 'Py_Algo/백준/Gold/1300. K번째 수' to './백준/Gold/1300. K번째 수': Directory not empty
mv: cannot move 'Py_Algo/백준/Gold/1450. 냅색문제' to './백준/Gold/1450. 냅색문제': Directory not empty
mv: cannot move 'Py_Algo/백준/Gold/14500. 테트로미노' to './백준/Gold/14500. 테트로미노': Directory not empty
mv: cannot move 'Py_Algo/백준/Gold/1644. 소수의 연속합' to './백준/Gold/1644. 소수의 연속합': Directory not empty
mv: cannot move 'Py_Algo/백준/Gold/1717. 집합의 표현' to './백준/Gold/1717. 집합의 표현': Directory not empty
mv: cannot move 'Py_Algo/백준/Gold/17281. ⚾' to './백준/Gold/17281. ⚾': Directory not empty
mv: cannot move 'Py_Algo/백준/Gold/17298. 오큰수' to './백준/Gold/17298. 오큰수': Directory not empty
mv: cannot move 'Py_Algo/백준/Gold/17471. 게리맨더링' to './백준/Gold/17471. 게리맨더링': Directory not empty
mv: cannot move 'Py_Algo/백준/Gold/1766. 문제집' to './백준/Gold/1766. 문제집': Directory not empty
mv: cannot move 'Py_Algo/백준/Gold/1806. 부분합' to './백준/Gold/1806. 부분합': Directory not empty
mv: cannot move 'Py_Algo/백준/Gold/1941. 소문난 칠공주' to './백준/Gold/1941. 소문난 칠공주': Directory not empty
mv: cannot move 'Py_Algo/백준/Gold/2357. 최솟값과 최댓값' to './백준/Gold/2357. 최솟값과 최댓값': Directory not empty
mv: cannot move 'Py_Algo/백준/Gold/2470. 두 용액' to './백준/Gold/2470. 두 용액': Directory not empty
mv: cannot move 'Py_Algo/백준/Gold/25682. 체스판 다시 칠하기 2' to './백준/Gold/25682. 체스판 다시 칠하기 2': Directory not empty
mv: cannot move 'Py_Algo/백준/Gold/7576. 토마토' to './백준/Gold/7576. 토마토': Directory not empt'''

source_dir = "Py_Algo/백준/Gold"
target_dir = "./백준/Gold"

for text in texts.split('\n'):
    text = text.removeprefix(f"mv: cannot move '{source_dir}/").replace("' to '", "@").split('@')[0]
    if texts:
        dir_name = text.split('@')[0]
        print(f'mv {source_dir}/{dir_name}/* {target_dir}/{dir_name}/ &&')
        print(f'rmdir {source_dir}/{dir_name} &&')
    else:
        print(f'mv {source_dir}/* {target_dir}/')