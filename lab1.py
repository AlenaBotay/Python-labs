{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b229c302",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Спасённая капитаном Джеком Воробьём, который вытащил её на поверхность и разорвал корсет, она смогла сделать вдох. Пиратский медальон на ней оказывается знакомым капитанy Джеку Воробью. Джентельмен не станет лишать леди приятных иллюзий. По пути Гиббс рассказывает Уиллу легенду о чудесном спасении капитана Джека Воробья от заточения на острове. Я капитан Джек Воробей! Смекаешь?\n"
     ]
    }
   ],
   "source": [
    "s = 'Спасённая Джеком Воробьём, который вытащил её на поверхность и разорвал корсет, она смогла сделать вдох. Пиратский медальон на ней оказывается знакомым Джеку Воробью. Джентельмен не станет лишать леди приятных иллюзий. По пути Гиббс рассказывает Уиллу легенду о чудесном спасении Джека Воробья от заточения на острове. Я Джек Воробей! Смекаешь?'\n",
    "s = s.split(' ')\n",
    "JV = ['Джек', 'Джека', 'Джеку', 'Джеком', 'Джеке']\n",
    "cap = ['капитан', 'капитана', 'капитанy', 'капитаном', 'капитане']    \n",
    "s = [' '] + s \n",
    "text = ''\n",
    "\n",
    "#for i in range(1, len(s)-1):\n",
    "   # print(''.join(s[i]+' '+s[i+1]))\n",
    "#print(len(s))\n",
    "len_str = len(s) - 1\n",
    "i = 1\n",
    "#for i in range(1, len_str):\n",
    "while i < len(s):\n",
    "    #print(s[i])\n",
    "    #print(len(s))\n",
    "    if s[i] in JV and s[i-1] not in cap:\n",
    "        a=[]\n",
    "        b=[]\n",
    "        for j in range(i):\n",
    "            a = a + [s[j]]\n",
    "        for j in range(i,len(s)):    \n",
    "            b = b + [s[j]]\n",
    "        #print(s[i])   \n",
    "        #print([cap[JV.index(s[i])]])\n",
    "        s = a + [cap[JV.index(s[i])]] + b \n",
    "    i+=1  \n",
    "\n",
    "del s[0]\n",
    "text = ' '.join(s)\n",
    "print(text)\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "98d717ef",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
