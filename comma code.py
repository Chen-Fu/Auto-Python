#Your function should be able to work with any list value passed to it.
#Be sure to test the case where an empty list [] is passed to your function.


def comma(spam):
    try:
        result = spam[0]
        for i in range(1,len(spam)-1):
            result = result + ', ' + spam[i]
        result = result + ' ,and ' + spam[len(spam)-1]
        return result
    except:
        return[]

spam = ['apples', 'bananas', 'tofu', 'cats']
comma(spam)

