# who_are_you
This repository contains the code associated with the paper: "Who Are You (I Really Wanna Know)? Detecting Audio DeepFakes Through Vocal Tract Reconstruction" that will be presented at USENIX Secuirty 2022. 

Abstract: Generative machine learning models have made convincing voice synthesis a
reality. While such tools can be extremely useful in applications where people
consent to their voices being cloned (e.g., patients losing the ability to
speak, actors not wanting to have to redo dialog, etc), they also allow for the
creation of nonconsensual content known as deepfakes. This malicious audio is
problematic not only because it can convincingly be used to impersonate
arbitrary users, but because detecting deepfakes is challenging and generally
requires knowledge of the specific deepfake generator. In this paper, we develop
a new mechanism for detecting audio deepfakes using techniques from the field of
articulatory phonetics.  Specifically, we apply fluid dynamics to estimate the
arrangement of the human vocal tract during speech generation and show that
deepfakes often model impossible or highly-unlikely anatomical arrangements.
When parameterized to achieve 99.9% precision, our detection
mechanism achieves a recall of 99.5%, correctly identifying all but
one deepfake sample in our dataset. We then discuss the limitations of this
approach, and how deepfake models fail to reproduce all aspects of speech
equally. In so doing, we demonstrate that subtle, but biologically constrained
aspects of how humans generate speech are not captured by current models, and
can therefore act as a powerful tool to detect audio deepfakes.
