import generate
z = generate.load_all()

def tell_a_story(image):
    passage = generate.story(z, image.to_stream())
    return {
        'passage': passage
    }
