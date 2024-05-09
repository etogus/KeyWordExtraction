Key Terms Extraction.


<p>Extracting keywords can help to determine the text meaning. Also, it can help with splitting texts into different categories.<br/>
In this project extracting of relevant words is done on a collection of news stories by focusing part-of-speech search and TF-IDF methods.</p><br/><br/>

The program does the following:
> Read an XML-file containing stories and headlines.<br/>
> Extract the headers and the text.<br/>
> Tokenize each text.<br/>
> Exclude the tokens that start with ', stopwords, and punctuation marks.<br/>
> Lemmatize the remaining tokens in the story.<br/>
> Count the TF-IDF metric for each word in all stories.<br/>
> Pick the five best scoring words.<br/>
> Print each story's headline and the five most frequent words in descending order.<br/>

Example:<br/>
> New Portuguese skull may be an early relative of Neandertals:<br/>
> skull genus member trait ridge<br/>

> Loneliness May Make Quitting Smoking Even Tougher:<br/>
> loneliness study author wootton treur<br/>
