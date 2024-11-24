from rest_framework.throttling import UserRateThrottle

class RoleBasedRateThrottle(UserRateThrottle):
    def get_rate(self):
        if self.scope == 'admin':
            return '1000/min'  # Лимит для админов
        return super().get_rate()
