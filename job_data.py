class JobData:
    def __init__(self, title, company_name, reward, link):
        self.title = title
        self.company_name = company_name
        self.reward = reward
        self.link = link

    def to_list(self):
        return [self.title, self.company_name, self.reward, self.link]
