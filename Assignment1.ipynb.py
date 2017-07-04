{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Assignment 1\n",
    "\n",
    "This assignment serves the purpose of introducing you to the basics of natural language processing and, more specifically, the natural language processing toolkit, [nltk](http://www.nltk.org/)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Part 1\n",
    "\n",
    "Write code to process the [Brown Corpus](http://www.nltk.org/howto/corpus.html) and answer the questions below . "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1) Write a list, named `nouns`, which contains five nouns that are more common in their plural form than their singular form. (5 points)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from nltk.corpus import brown\n",
    "cat = brown.words()\n",
    "lower = [i.lower() for i in cat]\n",
    "tag = nltk.pos_tag(lower)\n",
    "\n",
    "NN = []\n",
    "for i in tag:\n",
    "    if i[1] == \"NN\":\n",
    "        NN.append(i)\n",
    "NN = set(NN)\n",
    "NNS = []\n",
    "for i in tag:\n",
    "    if i[1] == \"NNS\":\n",
    "        NNS.append(i)\n",
    "NNS = set(NNS)\n",
    "\n",
    "NNcounter = nltk.FreqDist(w for w in NN)\n",
    "NNScounter = nltk.FreqDist(w for w in NNS)\n",
    "\n",
    "NNcounter.most_common(15)\n",
    "NNScounter.most_common(10)\n",
    "\n",
    "nouns = [\"years\",\"eyes\",\"things\",\"children\",\"members\"]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2) Which word has the greatest number of distinct tags? What are they? Assign this word to the variable `g_word` and print its tag. (1 point)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import collections\n",
    "from nltk.corpus import brown\n",
    "cat = brown.words()\n",
    "lower = [i.lower() for i in cat]\n",
    "tag = nltk.pos_tag(lower)\n",
    "\n",
    "L = []\n",
    "for i in tag:\n",
    "    L.append(i)\n",
    "    set(L)\n",
    "count = 0 \n",
    "\n",
    "g_word = max(L[0])\n",
    "print(max(L[1]) )"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3) Write a list, `tag_freq`, containing tags in order of decreasing frequency. (4 points)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from nltk.corpus import brown\n",
    "cat = brown.words()\n",
    "lower = [i.lower() for i in cat]\n",
    "tag = nltk.pos_tag(lower)\n",
    "freq = nltk.FreqDist(w for w in tag)\n",
    "\n",
    "\n",
    "\n",
    "tag_freq = freq.most_common()[::]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Part 2\n",
    "\n",
    "In this part of the assignment, use the `nltk` to find the parts of speech of the sentences below. You should use three taggers to compare the different results: `pos_tag`, `UnigramTagger`, and `BiGramTagger`. Use a multi-line comment to answer the following for each example: (6 points)\n",
    "\n",
    "*Were there any mislabeled tags in any of the word tagger results? Did the three taggers tag words differently? If so, how?* (3 points each)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1. \"The boat is going to sink and I am scared!\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\nYes, the Unigram and Bigram taggers were mostly mostly mislabeled and there was much diveregence in the tagging of the\\nsame word. For example, while the bigram tagger completeley missed most of the words by labelling none, the POS tagger \\nmislabeled \"am\" as the incorrect verd type.\\n'"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# code goes below\n",
    "\n",
    "import nltk.tag, nltk.data\n",
    "import nltk\n",
    "from nltk.corpus import brown\n",
    "\n",
    "example = \"The boat is going to sink and I am scared!\"\n",
    "tokens = nltk.word_tokenize(example)\n",
    "pos_tag = nltk.pos_tag(tokens)\n",
    "brown_tagged_sents = brown.tagged_sents(categories='news')\n",
    "brown_sents = brown.sents(categories='news')\n",
    "unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)\n",
    "uni = unigram_tagger.tag(tokens)\n",
    "bigram_tagger = nltk.BigramTagger(brown_tagged_sents)\n",
    "bi = bigram_tagger.tag(tokens)\n",
    "\n",
    "\"\"\"\n",
    "Yes, the Unigram and Bigram taggers were mostly mostly mislabeled and there was much diveregence in the tagging of the\n",
    "same word. For example, while the bigram tagger completeley missed most of the words by labelling none, the POS tagger \n",
    "mislabeled \"am\" as the incorrect verd type.\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2. \"I had a dream that I found a lost dog and instead of taking it to its rightful owner, I brought it home and kept it.\" "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# code goes below\n",
    "import nltk.tag, nltk.data\n",
    "import nltk\n",
    "from nltk.corpus import brown\n",
    "\n",
    "example = \"I had a dream that I found a lost dog and instead of taking it to its rightful owner, I brought it home and kept it.\"\n",
    "tokens = nltk.word_tokenize(example)\n",
    "pos_tag = nltk.pos_tag(tokens)\n",
    "brown_tagged_sents = brown.tagged_sents(categories='news')\n",
    "brown_sents = brown.sents(categories='news')\n",
    "unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)\n",
    "uni = unigram_tagger.tag(tokens)\n",
    "bigram_tagger = nltk.BigramTagger(brown_tagged_sents)\n",
    "bi = bigram_tagger.tag(tokens)\n",
    "\n",
    "\"\"\"\n",
    "Here again, the bigram tagger failed to label most of the words. Similar to the previous example, \n",
    "the pos_tag and uni_tag taggers were similar for most words in that they identified the correct broad grammar type\n",
    "for e.g. \"am\" is a verb, however, they came to a different conlclusios as to what type of verd \"am\" is in each context.\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3. \"I'm procrastinating my code for this assignment!\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\nanswer to qualitative question goes here!\\n'"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# code goes below\n",
    "example = \"I'm procrastinating my code for this assignment!\"\n",
    "tokens = nltk.word_tokenize(example)\n",
    "pos_tag = nltk.pos_tag(tokens)\n",
    "brown_tagged_sents = brown.tagged_sents(categories='news')\n",
    "brown_sents = brown.sents(categories='news')\n",
    "unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)\n",
    "uni = unigram_tagger.tag(tokens)\n",
    "bigram_tagger = nltk.BigramTagger(brown_tagged_sents)\n",
    "bi = bigram_tagger.tag(tokens)\n",
    "\"\"\"\n",
    "It appears that the unigram and pos_tag taggers diverege most when it comes to personal pronouns. \n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Why do you think different word taggers *would* obtain different tags for the same word? Explain your answer in the markdown cell below. (5 points)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Each taggers uses a different probablistic language model and specifically the Markov assumption is applied differently in each. The unigram taggers takes each word as if it is probablisitically independent from the next while the Bigram model uses conditional probability taking the previous word into consideration. Finally, the POS tagger, to my understanding, computes the probability of the word-tag given the other words and tags in the sentence. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "How do you think stemming words would affect the variance-bias in word tagging? Explain your answer in the markdown cell below. (5 points)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Stemming words would have a varied effect across the tagging schemas via the probability distribution of the word. In the unigram tagger, a stem like \"presum\" (aka, \"presume and other forms of the word). The variance would go down, but the bias would increase. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Part 3 \n",
    "\n",
    "This part will require that you write functions to normalize and stem a given input. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Write a function `normalize()` that takes a string of text as input and returns a list of tokenized words in lower case format. You should not use built-in functions from `nltk` or any other natural language processing modules. (6 points)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def normalize(sentence):\n",
    "    L = []\n",
    "    for word in sentence.split():\n",
    "        L.append(word.lower())\n",
    "    return(L)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Write a function `stem()` that takes a list of normalized words as input and returns **two** lists of the stemmed words -- one using the Lancaster Stemmer, the other using the Porter Stemmer. (5 points)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import nltk\n",
    "def stem(sentence):\n",
    "    lancaster = nltk.LancasterStemmer()\n",
    "    lanc_stem = [lancaster.stem(i) for i in sentence]\n",
    "    porter = nltk.PorterStemmer()\n",
    "    port_stem = [porter.stem(i) for i in sentence]\n",
    "    return lanc_stem, port_stem\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.6.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
