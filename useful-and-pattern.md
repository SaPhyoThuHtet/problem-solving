### Hash Set, Hash Map

- အသုံးဝင်တာ တစ်ခုက Leet Code Questions နှစ်ခု မှာ Hash Set နဲ့ Hash Map ကို built-in hash-set hash-map မသုံးပဲ နဲ့ ရေးခိုင်းတာပါ။  ဒီquestions တွေကတော့ design questions တွေဖြစ်ပါတယ်။ ပထမကတော့ လွယ်တာပေါ့  array နဲ့ ချတယ်။ But Discussion က ခုစာသားလေးကိုတွေ့တော့ သေချာ တွေးပြီးမှပဲ ရေးမယ်လို့ စဥ်းစားမိတယ်။
***
the purpose of this leetcode question is not to pass all the test. it is for understanding how hashset or hashmap works under the hood.

So please do not post any answers using built-in hashset/hashmap, or just use a single array. Ask yourself, are you going to do the same stupid thing if this is the question you are asked in a real interview?
***
အဖြေကိုတော့ ဒီsolution ကနေပဲ ကိုးကားလိုက်ပါတယ်။ https://leetcode.com/problems/design-hashset/discuss/768659/Python-Easy-Multiplicative-Hash-explained

- Hashing ကိုသိထားရင် တခြား design question တွေဖြစ်တဲ့ TinyUrl ဖန်တီးခိုင်းတာမျိုးမှာ အသုံးဝင်တယ်။

### Hashing Knowledge

**Hash Function**

A hash function is any function that can be used to map data of arbitrary size to fixed-size values. The values returned by a hash function are called hash values, hash codes, digests, or simply hashes. The values are usually used to index a fixed-size table called a hash table. (Wiki)

**Hashing**

- Excellent Video to learn hash tabel and hash functions (https://youtu.be/KyUTuwz_b7Q) Keywords: hash table, hash function, open addressing, close addressing, linear probe
- Hashing is the process of transforming any given key or a string of characters into another value. This is usually represented by a shorter, fixed-length value or key that represents and makes it easier to find or employ the original string. The most popular use for hashing is the implementation of hash tables. (https://searchsqlserver.techtarget.com/definition/hashing#:~:text=Hashing%20is%20the%20process%20of,the%20implementation%20of%20hash%20tables.)
- Digital Signature တွေမှာလည်း အသုံးပြုတယ်။ (Look at this video, It is really interesting) https://youtu.be/uw4aTvRDHB4
- Cryptography နဲ့ Encryption Decryption တွေမှာ သုံးတယ်။


### Tree

- Tree တွေက Recursion ပုံစံများတယ်
- Traversal မှာ Depth First Search နဲ့ Breadth First Search Traversal ပုံစံမျိုးတွေပဲ
- Depth First Search ကတော့ Stack နဲ့ အလုပ်လုပ်တယ် အဲ့တော့ Recursion သဘောမျိုးဖြစ်တယ်၊ Breadth First Search ဆို Queue ပုံစံနဲ့ အလုပ်လုပ်တယ်
  အဲ့တော့ Recursion ပုံစံနဲ့ မဟုတ်ဘူး
- နောက်ထပ် Tree ပုံစံကတော့ Binary Search Tree ပဲ။ အဲ့တာဆို သေချာတယ် In order Traversal နဲ့တင် အလုပ် ဖြစ်ပြီ။ In Order Traversal ကို ကိုယ့်ဘာသာ ရေးတဲ့ ပုံစံရှိတယ် သူများတွေ ရေးတဲ့ ပုံစံလည်း ရှိတယ်။ ကိုယ်ဘာသာရေးတာကကျ သဘောတရားကို Intution ဖြစ်တယ် But အားနည်းချက်က Tree ရဲ့ Type ကိုတော့ သိနေမှ ရမယ်။ သူများတွေ ရေးတဲ့ ပုံစံက ဘယ်ကို အရင်သွား ပြီးရင် Null ဖြစ်ပြီ stack မကုန်သေးရင် pop လုပ် ပြီးတော့ right ထည့်။
