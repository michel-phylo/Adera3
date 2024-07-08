# Adera3
#Project Title: Predicting Cancer Origin Using Copy Number Alterations (CNA) and Copy Number Variation (CNV)

# Overview:
The accurate identification of the primary tumor origin in metastatic cancer cases is crucial for guiding treatment decisions and improving patient outcomes. Copy Number Alterations (CNA) and Copy Number Variation (CNV) have emerged as significant genomic markers for predicting metastatic cancer origins. However, existing models based on CNV or CNA often suffer from low accuracy rates.

Objective:
In this project, we aim to address this challenge using advanced neural network approaches. Our dataset encompasses CNA profiles from twenty distinct cancer types. Our primary goal is to develop robust predictive models capable of accurately determining cancer types based on genomic data.

# Approaches:

# Deep Neural Networks:

We evaluated two deep neural network architectures: a ReLU-based network and a 2D convolutional network. These models were trained to predict cancer types using CNA profiles and locus coordinates.
Shallow Neural Networks:

Additionally, we categorized cancer types based on anatomical and physiological similarities and constructed shallow neural networks. These networks were designed to differentiate between closely related cancer types within the same cluster.
# Results:
Both deep and shallow neural network approaches demonstrated promising results, achieving high prediction accuracies. The deep neural networks, in particular, exhibited a superior accuracy rate of up to 60%, suggesting a potential mathematical relationship between CNV types, genomic locations, and cancer types.

# Conclusion:
Our findings underscore the potential of leveraging CNA/CNV profiles to enhance the identification of cancer origins. By integrating these genomic markers into routine clinical assessments, our approach aims to support pathologists in making more informed decisions and improving diagnostic accuracy using readily available clinical tests.

# Next Steps:
Moving forward, we plan to further refine our models, explore additional datasets to validate our findings, and collaborate with clinical experts to translate our research into practical clinical applications.

# How to explore our models
#Install Required Libraries:
Ensure you have all the necessary libraries installed as specified in the setup.py file.

# Run the Program:
Execute the program using the command adera3.0_run in your terminal.

# Choose Model Options:
Follow the prompts to select the model configurations you wish to evaluate. Press Enter to confirm your choices.

# Compilation and Plotting:
The selected model will compile and generate plots. You can find these plots in the results_Adera3 folder.

# Future Updates:
We are continuously improving our project and plan to introduce real-time prediction features in the future. Stay tuned for updates!


