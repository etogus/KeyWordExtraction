Key Terms Extraction.


<p>Extracting keywords can help with determining the meaning of the text.<br/>
In this project extracting of relevant words is done on a collection of news stories by focusing part-of-speech search and TF-IDF methods.</p><br/>

The program does the following:
> 1. Read an XML-file containing stories and headlines.<br/>
> 2. Extract the headers and the text.<br/>
> 3. Tokenize each text.<br/>
> 4. Exclude the tokens that start with ', stopwords, and punctuation marks.<br/>
> 5. Lemmatize the remaining tokens in the story.<br/>
> 6. Count the TF-IDF metric for each word in all stories.<br/>
> 7. Pick the five best scoring words.<br/>
> 8. Print each story's headline and the five most frequent words in descending order.<br/>

Example:<br/>
> New Portuguese skull may be an early relative of Neandertals:<br/>
> skull genus member trait ridge<br/>

> Loneliness May Make Quitting Smoking Even Tougher:<br/>
> loneliness study author wootton treur<br/>
