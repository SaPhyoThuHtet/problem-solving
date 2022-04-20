Medium

'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
'''

Solution:

"""
Uniform Probability ဆိုတာ ဘာလဲဆိုတာ ရှာကြည့်တယ်။

Uniform Probability
====================
In statistics, uniform distribution is a term used to describe a form of probability distribution where every possible outcome has an equal likelihood of happening.
The probability is constant since each variable has equal chances of being the outcome.

Ref: https://corporatefinanceinstitute.com/resources/knowledge/other/uniform-distribution/


ပထမဦးဆုံးကတော့  ဒီproblem ကို မသိဘူး။ မေးခွန်းကိုကော နားမလည်ဘူး။ အရင် အဖြေကို ရှာလိုက်တယ်။ အဖြေကို ဖတ်ကြည့်ရင်း loop invariants ဆိုတဲ့ term အသစ်ကို သိလိုက်တယ်။
enumerate ကိုလည်း သိပ်မသုံးဖူးတော့ ပြန်ပြီးတော့ enumerate ရဲ့ အလုပ်လုပ်ပုံကို ရှာခဲ့တယ်။

"""
