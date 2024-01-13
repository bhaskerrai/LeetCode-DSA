#  Check if the Sentence Is Pangram

# A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

def checkIfPangram(sentence: str) -> bool:

    sentence = set(sentence)

    return len(sentence) == 26


print(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
print(checkIfPangram("Lleetcode"))