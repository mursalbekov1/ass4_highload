from locust import HttpUser, task

class LoadTest(HttpUser):
    @task
    def test_api(self):
        self.client.get('/secure-data/')
