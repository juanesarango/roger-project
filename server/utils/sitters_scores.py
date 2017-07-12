def get_sitter_rank(stays, rating, score):
    if stays < 10:
        return (rating - score)/10 * stays * rating/5 + score
    else:
        return rating

