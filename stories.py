"""Madlibs Stories."""

class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'echo
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


fairy = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

airplane = Story(
    ['occupation', "adjective","noun","verb","food","clothing"],
""" Janet really loves to travel, so she's a {occupation} at flying on airplanes. She knows exactly what to pack. She never leaves without a {adjective} {noun} to {verb}, some {food} for nibble on if she's hungry trip, and a comfortable {clothing} to wrap herself in when it gets cold."""
)
# {'occupation':"vet", "adjective":"brave","noun":"shell","verb":"run","food":"gummy bears","clothing":"socks"}

vacation = Story(["adjective","descriptor", "noun", "plural_noun","game"], """ A vacation is when you take a trip to some {adjective} place with your {descriptor} family. Usually you go to some place that is near a/an {noun}.  A good vacation place is one where you can ride {plural_noun} or play {game}.""")