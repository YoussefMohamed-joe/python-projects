def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes



start=input("please enter your start: ")
end=input("please enter your end: ")
if (start.isdigit() and end.isdigit()):
    start=int(start)
    end=int(end)
    print(find_primes(start,end))
else:
    print("please enter a valid number")

