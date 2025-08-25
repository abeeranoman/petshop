def main():
    toys = [
        Lazy(),
        Hunter("medium"),
        Guard("large"),
        Guide()
    ]
    for toy in toys:
        toy.talk()

if __name__== "__main__":
    main()
