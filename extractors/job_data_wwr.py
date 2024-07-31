class JobDataWWR:
    def __init__(self, title, company, position, region,  link):
        self.title = title
        self.company = company
        self.position = position
        self.region = region
        self.link = link

    def to_list(self):
        return [self.title, self.company, self.position, self.region,  self.link]
