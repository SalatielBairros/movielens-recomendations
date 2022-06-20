class InvalidRecommendationModelException(Exception):
    def __init__(self, detail_message):
        self.message = "Invalid model"
        self.detail_message = detail_message
        self.full_message = f"{self.message}: {self.detail_message}"