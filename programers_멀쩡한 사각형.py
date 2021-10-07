def Euclidean(a, b):        #유클리드 호제법 : 두 수의 최대 공약수는 '두 수를 나눈 나머지'와 '나누는 수' 의
    while b != 0:           #               최대 공약수와 같다. 고로 나머지가 0일 경우 '나누는 수'가 최대 공약수.
        r = a % b
        a = b
        b = r
    return a

def solution(w,h):
    answer = 1
    e = Euclidean(w,h)        #1x2 직사각형의 버리는 사각형 수 = (w/(최대공약수) + h/(최대공약수) - 1)* (최대공약수)
    answer = (w*h) - (w+h-e)  #-> (w+h-(최대공약수))
    return answer