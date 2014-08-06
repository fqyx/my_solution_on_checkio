rec=lambda n: n and rec(n//2)+(n&1)
checkio=lambda n,m: rec(n^m)
