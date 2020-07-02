# Video-resume-shortlisting
Intelligent video interview agent used to predict communication skill and perceived personality traits

The research paper followed:
https://link.springer.com/article/10.1186/s13673-020-0208-3

Work done:
The CNN model is ready and was trained on a small dataset (8 videos with 40 frames each), for communication skills which we annotated ourselves
The model uses a softmax layer to predict a score from 0.1 to 6.0 at present
Separate models need to be trained for separate skill scores
We have assigned scores to each video and have trained the model utilising the same value for all extracted frames
The model can predict scores framewise.

Difficulties faced:
The paper is not very comprehensive on the details of the architecture, a very loose idea is provided. We took help from the same paper published in the previous year.
The details on the utilisation of the softmax layer to obtain the scores isn’t very clear either.
Lack of freely available and professionally annotated datasets.
The paper does not look at videos as a whole but looks at frames separately. There is thus no clear mention of how to deal with the correlation between them and how to predict scores from videos after the model is trained.
Many of the proposed features like communication skills cannot be discerned by just looking at a single frame, because of which the model may not give best results.
The large number of neurons on the dense layer did not allow us to train the model on our devices, it crashed due to low memory, we brought it down to 200 instead of 4096.

Pending work / Scope of Improvement:
The number outputs in the softmax layer can be brought down to maybe 10 instead of 60 as such high precision isn’t required in these cases and that would also require a much higher level of data to train.
The model was trained on a very small dataset. The dataset needs to be augmented and the model needs to be trained again, preferably by professionally annotated videos.
The choice of features needs to be reconsidered. The current set as in the paper is not easily comprehensible but features like confidence, assertiveness, etc maybe a better choice. We’ll need to survey and consider such choices, also keeping in mind that the decided features must be possible to evaluate by just looking at a frame and not the whole video.
Exploring the possibility of analysing audio to judge a candidate’s features like communication skills, confidence, flow of speech, etc
Audio nonverbal cues have been found to be associated with a broad array of social constructs in social psychology and have been successfully used in computational applications for the automated inference of constructs as diverse as dominance, emergent leadership, personality traits, negotiations outcomes, or hirability ratings in face-to-face settings.
Textual Features - 
Textual features help in assessment of GMA(intelligence, cognitive ability) which is important for many hiring decisions. This information is not reflected in personality traits and hence textual features can be useful.
To assess the linguistic usage of the vlogger, we employed several Readability indexes on the transcripts. This was done by using open source implementations of various readability measures in the NLTK-contrib package of the Natural Language Toolkit (NLTK). More specifically, we used 8 measures as features for the Readability representation: ARI, Flesch Reading Ease, FleschKincaid Grade Level, Gunning Fog Index, SMOG Index, Coleman Liau Index, LIX, and RIX.
In addition, we also used two simple statistical features for an overall Text representation: total word count in the transcript, and the amount of unique words within the transcript.
Visual Features -
Open Face
MEI - In order to capture overall movement of the vlogger’s face, a Weighted Motion Energy Image (wMEI) is constructed from the resulting face segmented video. MEI is a grayscale image that shows how much movement happens on each pixel throughout video, with white indicating a lot of movement and black indicating less movement.
By departing from our face segmented video instead of a whole video frame, we minimize the involvement of background in our calculation and thus get a better representation of the subject’s true movement.
