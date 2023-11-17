# Probability OF Disease 
# A test indicating the presence of disease in cats is 95% accurate in terms of both sensitivity and
# specificity. The prevalence of the disease is 3% which means only 3% of known cats have the
# disease. If your cat tests positive (negative) for the disease, what's the probability that your cat has
# (doesn't have) the disease?
# Write a program which takes in the accuracy of a test as well as the percent of a population which
# has the disease and returns a list containing:
# • Firstly, the probability that an individual has the disease given a positive test result.
# • Secondly, the probability that an individual does not have the disease given a negative test
# result.
# Note that:
# • You can assume the sensitivity and specificity are equal to the accuracy
# • You shouldn't use any libraries.

def probability_of_disease(accuracy, prevalence):
    # Write your code here.
    disease_test_inaccuracy = 1 - accuracy # represents the probability of the test giving an incorrect result.
    prob_sick = prevalence
    prob_helthy = 1 - prevalence

    prob_positive = (prob_sick * accuracy) + (prob_helthy * disease_test_inaccuracy)
    prob_negative = (prob_sick * disease_test_inaccuracy) + (prob_helthy * accuracy)

    prob_sick_positive = (prob_sick * accuracy) / prob_positive
    prob_helthy_negative = (prob_helthy * accuracy) / prob_negative

    return [prob_sick_positive * 100, prob_helthy_negative * 100]