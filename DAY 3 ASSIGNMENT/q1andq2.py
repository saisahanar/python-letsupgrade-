{
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": 3
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python_defaultSpec_1595504391187",
   "display_name": "Python 3.8.1 64-bit"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Question 1 :\n",
    "#Find sum of n numbers with help of while loop."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": "15\n"
    }
   ],
   "source": [
    "n=int(input(\"enter n value\"))\n",
    "sum=i=0\n",
    "while i <n:\n",
    "    sum=sum+i\n",
    "    i+=1\n",
    "print(sum)    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": "5 is prime\n"
    }
   ],
   "source": [
    "#Question 2 :\n",
    "#Take an integer and find whether the number is prime or not.\n",
    "n=int(input(\"enter n value\"))\n",
    "if n%2==0:\n",
    "    print(f\"{n} is not prime\")\n",
    "else:\n",
    "    print(f\"{n} is prime\")    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ]
}