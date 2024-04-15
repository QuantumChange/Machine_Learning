from textblob import TextBlob

oppenhiemer_rw= """I'm still collecting my thoughts after experiencing this film, Cillian Murphy might as well start clearing a space on his mantle for the Best Actor Oscar.

This film is a masterclass in weaving narratives and different time periods while exploring the profound depths of a man whose actions altered the world's trajectory forever, for better or worse. Nolan brings us into the complexities of Oppenheimer, and all the moral conflicts stirring within him.

Murphy's portrayal is so riveting that the long run-time became an afterthought. Robert Downey Jr also offers a great performance and Nolan's push and pull with how he uses sound design throughout is the cherry on top."""


analysis = TextBlob(oppenhiemer_rw)

#Sentiment value
"""Return a tuple of form (polarity, subjectivity, assessments ) where polarity is a float within the range [-1.0, 1.0], subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective, and assessments is a list of polarity and subjectivity scores for the assessed tokens."""

print(analysis.sentiment.polarity)