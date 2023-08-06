import numpy as np

def gradient_descent(x,y):
    m_curr=0
    b_curr=0
    learning_rate=0.08
    iterations=10000
    n=len(x)
    for i in range(iterations):
        y_pred=(m_curr*x)+b_curr
        cost=(1/n)*(sum([val**2 for val in (y-y_pred)]))
        dm=-(2/n)*sum(x*(y-y_pred))
        db=-(2/n)*sum(y-y_pred)
        m_curr=m_curr-learning_rate*dm
        b_curr=b_curr-learning_rate*db
        print(f"m_curr={m_curr},b_curr={b_curr},cost={cost}")

x=np.array([1,2,3,4,5])
y=np.array([5,7,9,11,13])

gradient_descent(x,y)